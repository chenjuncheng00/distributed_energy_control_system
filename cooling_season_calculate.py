import math
import datetime
from equipment import Lithium_Bromide_Cold
from centrifugal_chiller_function import centrifugal_chiller_function as ccf, centrifugal_chiller_result as ccr, centrifugal_chiller_cost as ccc
from triple_supply_function import triple_supply_cold_function as tscf, lithium_bromide_cold_function as lbcf
from natural_gas_boiler_funtion import natural_gas_boiler_in_out_hot_water as ngbiohw, natural_gas_boiler_heat_cost as ngbhc
from energy_storage_equipment_cold_function import energy_storage_equipment_cold_function as esecf, energy_storage_equipment_cold_result as esecr, \
     energy_storage_equipment_cold_storage_residual_write as esecsrw, energy_storage_equipment_cold_storage_residual_read as esecsrr, energy_storage_equipment_cold_cost as esecc
from air_source_heat_pump_cold_function import air_source_heat_pump_function_cold as ashpfc, air_source_heat_pump_result_cold as ashprc, air_source_heat_pump_cost_cold as ashpcc
import write_to_database as wtd

def cooling_season_function(cold_load, hot_water_load, electricity_load, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water,
                            lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, cc1, cc2, cc3, cc4,
                            ashpc1, ashpc2, ashpc3, ashpc4, esec1, esec2, esec3, ngb_hot_water, gc):
    """制冷季计算"""

    print("正在进行制冷季计算.........")

    # 母管制系统，制冷季计算

    # 离心式冷水机制冷总功率
    cc_cooling_power_rated_sum = cc1.cooling_power_rated + cc2.cooling_power_rated + cc3.cooling_power_rated + cc4.cooling_power_rated
    # 空气源热泵制冷总功率
    ashpc_cooling_power_rated_sum = ashpc1.cooling_power_rated + ashpc2.cooling_power_rated + ashpc3.cooling_power_rated + ashpc4.cooling_power_rated
    # 制冷设备的总制冷功率（不包括溴化锂）
    eq_cooling_power_rated_sum = cc_cooling_power_rated_sum + ashpc_cooling_power_rated_sum

    # 生活热水总流量
    hot_water_flow_total = hot_water_load * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
    # 生活热水泵启动数量，向上取整，每个泵额定流量44t/h
    hw_wp_num = math.ceil(hot_water_flow_total / 270)
    # 每个水泵生活热水流量
    if hot_water_flow_total > 0:
        hot_water_flow = hot_water_flow_total / hw_wp_num
    else:
        hot_water_flow = 0
    # 生活热水泵耗电计算（定频泵，频率始终为50Hz）
    hw_wp_power_consumption = hw_wp_num * lb1_wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
    # 内燃机设备负荷率调节步长，百分之几
    ice1_step = 5
    ice2_step = 5
    # 迭代计算中内燃机负荷率可以循环到的最小值
    if eq_cooling_power_rated_sum <= cold_load:
        ice1_load_ratio_min = 1
    else:
        ice1_load_ratio_min = 0
    # 列表，储存能源站向外供冷供电量
    station_electricity_out_all = []
    station_cold_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存溴化锂供冷量
    lb_cold_load_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存4台设备计算出的负荷率结果
    cc1_load_ratio_result = []
    cc2_load_ratio_result = []
    cc3_load_ratio_result = []
    cc4_load_ratio_result = []
    # 列表，储存4个空气源热泵计算出的负荷率结果
    ashpc1_load_ratio_result = []
    ashpc2_load_ratio_result = []
    ashpc3_load_ratio_result = []
    ashpc4_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_cooling_season == True:  # 制冷季溴化锂设备参与供生活热水
        # 溴化锂1、2的生活热水负荷最大值
        lb1_hot_water_max = gc.lb1_hot_water_max
        lb2_hot_water_max = gc.lb2_hot_water_max
        # 溴化锂设备生活热水计算步长
        lb1_hot_water_step = gc.lb1_hot_water_step
        # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
        if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (
                lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
        elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (
                lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
        else:  # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
            lb_hot_water_max = hot_water_load
    else:  # 制冷季溴化锂设备不参与供生活热水
        lb1_hot_water_max = 0
        lb_hot_water_max = 0
        # 步长不能为0，否则无限循环
        lb1_hot_water_step = gc.project_load_error

    # 允许启动的内燃机数量最大值
    # 从电负荷角度计算的内燃机启动数量最大值
    ice_num_max_elec_2 = math.ceil(electricity_load / ice1.electricity_power_rated)
    # 如果恰好整除，则向上加1
    if ice_num_max_elec_2 == int(ice_num_max_elec_2):
        ice_num_max_elec_1 = ice_num_max_elec_2 + 1
    else:
        ice_num_max_elec_1 = ice_num_max_elec_2
    # 最大数量不可以超过2
    if ice_num_max_elec_1 > 2:
        ice_num_max_elec = 2
    else:
        ice_num_max_elec = ice_num_max_elec_1
    # 从冷负荷角度计算的内燃机启动数量最大值
    ice_num_max_cold_2 = math.ceil(cold_load / gc.lb1_cold_max)
    # 如果恰好整除，则向上加1
    if ice_num_max_cold_2 == int(ice_num_max_cold_2):
        ice_num_max_cold_1 = ice_num_max_cold_2 + 1
    else:
        ice_num_max_cold_1 = ice_num_max_cold_2
    # 最大数量不可以超过2
    if ice_num_max_cold_1 > 2:
        ice_num_max_cold = 2
    else:
        ice_num_max_cold = ice_num_max_cold_1
    # 两个结果取小值
    ice_num_max_a = min(ice_num_max_cold, ice_num_max_elec)

    # 内燃机启动数量初始值
    if cold_load - min(gc.lb1_cold_max, gc.lb2_cold_max) > eq_cooling_power_rated_sum and cold_load - gc.lb1_cold_max - gc.lb2_cold_max <= eq_cooling_power_rated_sum:
        ice_num_a = 2
    elif cold_load > eq_cooling_power_rated_sum and cold_load - min(gc.lb1_cold_max, gc.lb2_cold_max) <= eq_cooling_power_rated_sum:
        ice_num_a = 1
    else:
        ice_num_a = 0

    # 根据目前所处的用电时间段，重新修正内燃机可以启动的最大数量和内燃机启动数量初始值
    now = datetime.datetime.now()  # 获取当前的时间
    now_hour = now.hour  # 当前的小时
    # 根据预设的非谷电时间段列表，判断目前处于什么时间段
    hour_state = 0  # 用于判断目前是否处于非谷电时间段的判断因子，0表示处于谷电时间段，1表示不处于谷电时间段
    for h in gc.hour_ese_out:
        if now_hour == h:
            hour_state = 1
            break
        else:
            hour_state = 0

    # 如果当前的小时在非谷电时间段，则采用前面计算出的内燃机启动数量，否则为0
    if hour_state == 1:
        ice_num_max = ice_num_max_a
        ice_num = ice_num_a
    else:
        ice_num_max = 0
        ice_num = 0

    # 根据当前所处的用电时间段，判断蓄冷装置是进行蓄冷还是供冷
    # 读取目前水罐剩余的蓄冷量（单位为kWh）
    esec1_cold_stock = esecsrr()[0]
    esec2_cold_stock = esecsrr()[1]
    esec3_cold_stock = esecsrr()[2]
    esec_cold_stock_sum = esec1_cold_stock + esec2_cold_stock + esec3_cold_stock
    # 3个水罐的额定蓄冷量总和（单位为kWh）
    esec_cooling_storage_rated_sum = esec1.cooling_storage_rated + esec2.cooling_storage_rated + esec3.cooling_storage_rated
    # 需要根据每小时计算几次的不同，蓄冷量(kWh)和冷负荷(kW)的计算需要进行换算
    # 在供冷状态判断水罐内剩余的量是否够供冷时，需要考虑每小时计算几次；在蓄冷状态判断水罐内剩余的量是否够蓄冷时，需要考虑每小时计算几次
    # 但传入蓄冷水罐计算函数的功率值(kW)，不考虑每小时计算几次，全部按照默认1小时计算1次考虑，最后在写入水罐消耗或者增加了多少能量(kWh)时，再考虑每小时计算机次
    if hour_state == 1:
        # 供冷状态(正值)
        if esec_cold_stock_sum * gc.hour_num_of_calculations >= cold_load : # 两边都转换成kW值（考虑每小时计算几次）
            # 如果蓄冷水罐剩余量大于等于冷负荷需求量，则蓄冷水罐提供的冷负荷等于冷负荷需求量
            cold_load_esec = cold_load
        else:
            cold_load_esec = esec_cold_stock_sum * gc.hour_num_of_calculations # 两边都转换成kW值
    else:
        # 蓄冷状态(负值)
        # 如果制冷设备总功率减去冷负荷需求量大于0，则表示可以有设备蓄冷
        if eq_cooling_power_rated_sum - cold_load > 0: # 此处单位均为功率值kW，不需要考虑每小时计算几次的问题
            if (eq_cooling_power_rated_sum - cold_load) >= esec_cooling_storage_rated_sum * gc.hour_num_of_calculations: # 两边都转换成kW值（考虑每小时计算几次）
                cold_load_esec = -esec_cooling_storage_rated_sum * gc.hour_num_of_calculations # 两边都转换成kW值
            else:
                cold_load_esec = -(eq_cooling_power_rated_sum - cold_load)
        else:
            cold_load_esec = 0

    # 蓄冷装置负荷为0时，或处于蓄冷状态，但蓄冷设备已满，不进行蓄冷装置计算（两边都转换成kW值）
    if cold_load_esec == 0 or (cold_load_esec < 0 and abs(esec_cooling_storage_rated_sum - esec_cold_stock_sum) * gc.hour_num_of_calculations < gc.project_load_error):
        esec1_load_ratio = 0
        esec2_load_ratio = 0
        esec3_load_ratio = 0
        esec_cold_load_out = 0
        esec_power_consumption_total = 0
        esec_water_supply_total = 0
        # 单独计算补水成本
        cost_esec_water_supply = esec_water_supply_total * gc.water_price
    else:
        # 蓄冷设备的使用优先级最高，先计算蓄冷设备
        ans_esec_a = esecf(cold_load_esec, esec1, esec2, esec3, gc)  # 所有的可能解
        ans_esec = esecr(ans_esec_a, esec1, esec2, esec3)  # 选出蓄能设备最优解
        # 蓄冷设备计算结果
        esec1_load_ratio = ans_esec[0]
        esec2_load_ratio = ans_esec[1]
        esec3_load_ratio = ans_esec[2]
        esec_cold_load_out = ans_esec[3]
        esec_power_consumption_total = ans_esec[4]
        esec_water_supply_total = ans_esec[5]
        # 单独计算补水成本
        cost_esec_water_supply = esec_water_supply_total * gc.water_price
    # 对计算出的蓄冷装置负荷率进行修正（蓄能的情况变成负值）
    if hour_state == 1:
        # 供冷状态(正值)
        esec_cold_load_out = esec_cold_load_out
    else:
        # 蓄冷状态（负值）
        esec_cold_load_out = - esec_cold_load_out
    # 根据蓄冷设备的情况对需要其他设备提供的冷负荷进行修正
    cold_load -= esec_cold_load_out

    # 内燃机启动数量，可以是0，可以是1，也可以是2
    while ice_num <= ice_num_max:
        # 重置内燃机、冷水机设备负荷率
        if ice_num >= 1:
            ice1_load_ratio = 1
        else:
            ice1_load_ratio = 0
        if ice_num >= 2:
            ice2_load_ratio = 1
        else:
            ice2_load_ratio = 0
        cc1_load_ratio = cc1.load_min
        cc2_load_ratio = cc2.load_min
        cc3_load_ratio = cc3.load_min
        cc4_load_ratio = cc4.load_min
        ashpc1_load_ratio = ashpc1.load_min
        ashpc2_load_ratio = ashpc2.load_min
        ashpc3_load_ratio = ashpc3.load_min
        ashpc4_load_ratio = ashpc4.load_min
        # 2台内燃机系统的负荷率
        ice_load_ratio_result_all = [0, 0]
        # 列表，储存4台设备计算出的负荷率结果
        cc_load_ratio_result_all = [0, 0, 0, 0]
        # 列表，储存4台设备计算出的负荷率结果
        ashpc_load_ratio_result_all = [0, 0, 0, 0]
        # 溴化锂设备制备生活热水总量的初始值
        lb1_hot_water = 0
        lb2_hot_water = 0
        # 溴化锂设备生活热水总产量初始值
        lb_hot_water_total = 0
        # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num0_calculate = 0
        # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num1_calculate = 0
        # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num2_calculate = 0
        while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
            # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 0:
                ice_num0_calculate += 1
            # 天然气生活热水锅炉需要补充的生活热水量
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 离心式冷水机耗电总功率，制冷总功率、补水量默认值
            cc_power_consumption_total = 0
            cc_cold_out_total = 0
            cc_water_supply_total = 0
            # 空气源热泵耗电总功率，制冷总功率、补水量默认值
            ashpc_power_consumption_total = 0
            ashpc_cold_out_total = 0
            ashpc_water_supply_total = 0
            # 电收入成本默认值
            income_electricity = 0
            cost_electricity = 0
            # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 0 and ice_num0_calculate > 1:
                break
            # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 1 and ice_num1_calculate > 1:
                break
            # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 2 and ice_num2_calculate > 1:
                break
            # 改变内燃机负荷率
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
                if ice_num == 1 and ice1_load_ratio == 0 and ice2_load_ratio == 0:
                    ice_num1_calculate += 1
                # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
                if ice_num == 2 and ice1_load_ratio == 0 and ice2_load_ratio == 0:
                    ice_num2_calculate += 1
                # 内燃机+溴化锂+离心式冷水机运行状态计算
                # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                if ice1_load_ratio < ice1.load_min + gc.load_ratio_error_coefficient:
                    ice1_load_ratio = 0
                # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                if ice2_load_ratio < ice2.load_min + gc.load_ratio_error_coefficient:
                    ice2_load_ratio = 0
                # 计算三联供系统冷出力
                global ts_cold_out_total
                ts_cold_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water,
                                         lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                # 三联供系统的电出力
                # 计算三联供系统电出力
                ts_electricity_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water,
                                                lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                # 离心式冷水机需要补充的冷负荷
                cold_load_cc_1 = min(cold_load - ts_cold_out_total, cc_cooling_power_rated_sum)
                cold_load_cc = max(cold_load_cc_1, 0)
                # 空气源热泵需要补充的冷负荷
                cold_load_ashpc_1 = min(cold_load - ts_cold_out_total - cold_load_cc, ashpc_cooling_power_rated_sum)
                cold_load_ashpc = max(cold_load_ashpc_1, 0)
                # 如果此时只有内燃机，且内燃机负荷率和设定的冷负荷相差很小，则跳出循环
                if cold_load_cc >= 0 and abs(cold_load_cc) <= gc.project_load_error:
                    # 离心式冷水机不进行计算
                    cc_calculate = False
                    # 离心式冷水机负荷率都设置为0
                    cc1_load_ratio = 0
                    cc2_load_ratio = 0
                    cc3_load_ratio = 0
                    cc4_load_ratio = 0
                    # 离心式冷水机的输入输出量
                    cc_power_consumption_total = 0
                    cc_cold_out_total = 0
                    cc_water_supply_total = 0
                else:
                    # 离心式冷水机进行计算
                    cc_calculate = True
                if cold_load_cc >= 0 and cc_calculate == True:
                    # 计算离心式冷水机的运行策略
                    ans_cc = ccf(cold_load_cc, cc1, cc2, cc3, cc4, gc)
                    # 读取此时的冷水机最优计算结果耗电功率
                    cc_power_consumption_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[5]
                    # 读取此时的冷水机最优计算结果的供冷功率
                    cc_cold_out_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[4]
                    # 冷水机补水总量
                    cc_water_supply_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[6]
                    # 此时4台设备的负荷率
                    cc1_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[0]
                    cc2_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[1]
                    cc3_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[2]
                    cc4_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[3]
                # 判断空气源热泵是否需要计算
                if cold_load_ashpc >= 0 and abs(cold_load_ashpc) <= gc.project_load_error:
                    # 风冷螺杆热泵不进行计算
                    ashpc_calculate = False
                    # 风冷螺杆热泵负荷率都设置为0
                    ashpc1_load_ratio = 0
                    ashpc2_load_ratio = 0
                    ashpc3_load_ratio = 0
                    ashpc4_load_ratio = 0
                    # 风冷螺杆热泵的输入输出量
                    ashpc_power_consumption_total = 0
                    ashpc_cold_out_total = 0
                    ashpc_water_supply_total = 0
                else:
                    # 风冷螺杆热泵进行计算
                    ashpc_calculate = True
                if cold_load_ashpc >= 0 and ashpc_calculate == True:
                    # 计算风冷螺杆热泵的运行策略
                    ans_ashpc = ashpfc(cold_load_ashpc, ashpc1, ashpc2, ashpc3, ashpc4, gc)
                    # 读取此时的冷水机最优计算结果耗电功率
                    ashpc_power_consumption_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[5]
                    # 读取此时的冷水机最优计算结果的供冷功率
                    ashpc_cold_out_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[4]
                    # 补水总量
                    ashpc_water_supply_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[6]
                    # 此时4台设备的负荷率
                    ashpc1_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[0]
                    ashpc2_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[1]
                    ashpc3_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[2]
                    ashpc4_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[3]
                # 此时整个能源站的向外供电功率
                station_electricity_out_total = ts_electricity_out_total - cc_power_consumption_total - ashpc_power_consumption_total \
                                                - hw_wp_power_consumption - esec_power_consumption_total
                # 此时能源站供冷总功率
                station_cold_out_total = ts_cold_out_total + cc_cold_out_total + esec_cold_load_out + ashpc_cold_out_total
                # 如果仅有溴化锂供冷，且制冷量大于冷负荷需求量，则内燃机负荷往下减，内燃机1、2同时下降
                if cold_load_cc + cold_load_ashpc <= 0 and station_cold_out_total > cold_load and ts_cold_out_total > 0:
                    # 减小内燃机设备1、2负荷率
                    if ice_num >= 1:
                        ice1_load_ratio -= ice1_step / 100
                    else:
                        ice1_load_ratio = 0
                    if ice_num >= 2:
                        ice2_load_ratio -= ice2_step / 100
                    else:
                        ice2_load_ratio = 0
                # 如果能源站向外供电量大于电负荷需求量，则内燃机负荷往下减，内燃机1、2同时下降
                elif station_electricity_out_total > electricity_load and ts_cold_out_total > 0 + gc.project_load_error:
                    # 减小内燃机设备1、2负荷率
                    if ice_num >= 1:
                        ice1_load_ratio -= ice1_step / 100
                    else:
                        ice1_load_ratio = 0
                    if ice_num >= 2:
                        ice2_load_ratio -= ice2_step / 100
                    else:
                        ice2_load_ratio = 0
                # 程序跳出条件
                else:
                    # 存储此时的能源站向外供冷供电量
                    station_electricity_out_all.append(station_electricity_out_total)
                    station_cold_out_all.append(station_cold_out_total)
                    # 储存此时的内燃机负荷率
                    ice_load_ratio_result_all[0] = ice1_load_ratio
                    ice_load_ratio_result_all[1] = ice2_load_ratio
                    ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                    ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                    # 储存此时离心式冷水机的负荷率
                    cc_load_ratio_result_all[0] = cc1_load_ratio
                    cc_load_ratio_result_all[1] = cc2_load_ratio
                    cc_load_ratio_result_all[2] = cc3_load_ratio
                    cc_load_ratio_result_all[3] = cc4_load_ratio
                    cc1_load_ratio_result.append(cc_load_ratio_result_all[0])
                    cc2_load_ratio_result.append(cc_load_ratio_result_all[1])
                    cc3_load_ratio_result.append(cc_load_ratio_result_all[2])
                    cc4_load_ratio_result.append(cc_load_ratio_result_all[3])
                    # 储存此时空气源热泵负荷率
                    ashpc_load_ratio_result_all[0] = ashpc1_load_ratio
                    ashpc_load_ratio_result_all[1] = ashpc2_load_ratio
                    ashpc_load_ratio_result_all[2] = ashpc3_load_ratio
                    ashpc_load_ratio_result_all[3] = ashpc4_load_ratio
                    ashpc1_load_ratio_result.append(ashpc_load_ratio_result_all[0])
                    ashpc2_load_ratio_result.append(ashpc_load_ratio_result_all[1])
                    ashpc3_load_ratio_result.append(ashpc_load_ratio_result_all[2])
                    ashpc4_load_ratio_result.append(ashpc_load_ratio_result_all[3])
                    # 储存溴化锂和天然气锅炉供热水量，溴化锂制冷量
                    lb_hot_water_result.append(lb_hot_water_total)
                    ngb_hw_hot_water_result.append(ngb_hot_water_load)
                    lb_cold_load_result.append(ts_cold_out_total)
                    # 计算此时的能源站运行成本和收入
                    # 供电收入或者买电成本（大于0是收入，小于0是成本）
                    if station_electricity_out_total > 0:
                        income_electricity = station_electricity_out_total * gc.sale_electricity_price
                    else:
                        cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                    # 供冷收入（用冷负荷计算，能源站供冷量比冷负荷多的部分不计算）
                    income_cold = station_cold_out_total * gc.cooling_price
                    # 生活热水收入
                    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                    income_hot_water = hot_water_load_total * gc.hot_water_price
                    # 三联供系统总成本（天然气+补水）
                    cost_ts = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water,
                                   lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                    # 冷水机补水总成本
                    cost_cc_water_supply = cc_water_supply_total * gc.water_price
                    # 风冷热泵补水总成本
                    cost_ashpc_water_supply = ashpc_water_supply_total * gc.water_price
                    # 天然气热水锅炉天然气成本
                    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                    # 天然气热水锅炉补水成本计算
                    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                    # 总收入成本利润
                    income_total = income_cold + income_electricity + income_hot_water
                    cost_total = cost_electricity + cost_cc_water_supply + cost_ashpc_water_supply + cost_ts + cost_ngb_hw_nature_gas \
                                 + cost_ngb_hw_water_supply + cost_esec_water_supply
                    profits_total = income_total - cost_total
                    income.append(income_total)
                    cost.append(cost_total)
                    profits.append(profits_total)
                    # 如果内燃机1负荷率已经等于0，则跳出循环
                    if ice1_load_ratio == 0:
                        break
                    elif cold_load_cc <= 0 and cc_calculate == False:
                        break
                    # 修改内燃机1、2负荷率
                    else:
                        if ice_num >= 1:
                            ice1_load_ratio -= ice1_step / 100
                        else:
                            ice1_load_ratio = 0
                        if ice_num >= 2:
                            ice2_load_ratio -= ice2_step / 100
                        else:
                            ice2_load_ratio = 0

                # 如果溴化锂（三联供系统）外供制冷负荷小于0 ，则跳出循环
                if ice_num >= 1 and ts_cold_out_total < 0 + gc.project_load_error:
                    break
            # 溴化锂1、2制备的生活热水量增加
            if ice_num == 0:
                lb1_hot_water = 0
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 0
                ice2_load_ratio = 0
            elif ice_num == 1:
                lb1_hot_water += lb1_hot_water_step
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 1
                ice2_load_ratio = 0
            elif ice_num == 2:
                lb1_hot_water += lb1_hot_water_step
                lb2_hot_water = lb1_hot_water
                # 重置内燃机负荷率
                ice1_load_ratio = 1
                ice2_load_ratio = 1
            else:
                lb1_hot_water = 0
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 0
                ice2_load_ratio = 0
            # 溴化锂设备的总生活热水产量
            lb_hot_water_total = lb1_hot_water + lb2_hot_water
        # 内燃机数量+1
        ice_num += 1

    # 在txt文件中修改蓄能水罐剩余的蓄冷量数据
    esecsrw(hour_state, esec1, esec2, esec3, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec1_cold_stock, esec2_cold_stock, esec3_cold_stock, gc)

    #返回计算结果
    return profits, income, cost, station_cold_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, \
           cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, lb_cold_load_result, \
           lb_hot_water_result, ngb_hw_hot_water_result, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec_cold_load_out, \
           ashpc1_load_ratio_result, ashpc2_load_ratio_result, ashpc3_load_ratio_result, ashpc4_load_ratio_result


def print_cooling_season(ans, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water,
                         lb2_wp_hot_water, cc1, cc2, cc3, cc4, ashpc1, ashpc2, ashpc3, ashpc4, esec1, esec2, esec3, ngb_hot_water, gc, syncbase):
    """将制冷季计算结果打印出来"""
    # 能源站总利润最大值
    profitis_max = max(ans[0])
    # 能源站成本最小值
    cost_min = min(ans[2])
    # 记录列表索引
    # 利润最大索引
    profitis_max_index = ans[0].index(profitis_max)
    # 成本最小索引
    cost_min_index = ans[2].index(cost_min)
    # 采用的索引（利润最大的结果）
    cooling_season_index = profitis_max_index

    # 读取对应索引下的参数
    station_profitis_max = ans[0][cooling_season_index]
    station_cost_min = ans[2][cooling_season_index]
    station_cold_out_all = ans[3][cooling_season_index]
    station_electricity_out_all = ans[4][cooling_season_index]
    ice1_load_ratio = ans[5][cooling_season_index]
    ice2_load_ratio = ans[6][cooling_season_index]
    cc1_load_ratio = ans[7][cooling_season_index]
    cc2_load_ratio = ans[8][cooling_season_index]
    cc3_load_ratio = ans[9][cooling_season_index]
    cc4_load_ratio = ans[10][cooling_season_index]
    # 溴化锂制冷量，制生活热水量
    lb_cold_load = ans[11][cooling_season_index]
    lb_hot_water = ans[12][cooling_season_index]
    # 天然气锅炉制生活热水量
    ngb_hw_hot_water = ans[13][cooling_season_index]
    # 蓄能水罐水泵负荷率
    esec1_load_ratio = ans[14]
    esec2_load_ratio = ans[15]
    esec3_load_ratio = ans[16]
    # 蓄能水罐制冷量
    esec_cold_load_out = ans[17]
    # 风冷热泵负荷率
    ashpc1_load_ratio = ans[18][cooling_season_index]
    ashpc2_load_ratio = ans[19][cooling_season_index]
    ashpc3_load_ratio = ans[20][cooling_season_index]
    ashpc4_load_ratio = ans[21][cooling_season_index]

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(
        station_cost_min) + "\n" + "能源站供冷功率为： " + str(station_cold_out_all) + "\n" + "蓄能装置冷负荷功率为： " + str(
        esec_cold_load_out) + "\n" + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(
        ice1_load_ratio) + "\n" + "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "离心式冷水机1负荷率为： " + str(
        cc1_load_ratio) + "\n" + "离心式冷水机2负荷率为： " + str(cc2_load_ratio) + "\n" + "离心式冷水机3负荷率为： " + str(
        cc3_load_ratio) + "\n" + "离心式冷水机4负荷率为： " + str(cc4_load_ratio) + "\n" + "风冷螺杆热泵1负荷率为： " + str(
        ashpc1_load_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(ashpc2_load_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(
        ashpc3_load_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(ashpc4_load_ratio) + "\n" + "溴化锂设备供冷功率为： " + str(
        lb_cold_load) + "\n" + "溴化锂供生活热水功率为： " + str(lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(
        ngb_hw_hot_water) + "\n" + "蓄能水罐水泵1负荷率： " + str(esec1_load_ratio) + "\n" + "蓄能水罐水泵2负荷率： " + str(
        esec2_load_ratio) + "\n" + "蓄能水罐水泵3负荷率： " + str(esec3_load_ratio) + "\n")

    # 向数据库写入计算结果
    # 内燃机1和溴化锂1
    if ice1_load_ratio > 0:
        # 内燃机1
        ice1_electrical_efficiency = ice1.electricity_power_efficiency(ice1_load_ratio)
        ice1_residual_heat_efficiency = ice1.residual_heat_efficiency(ice1_load_ratio)
        ice1_electrical_power = ice1.electricity_power_rated * ice1_load_ratio
        ice1_total_heat_input = ice1.total_heat_input(ice1_load_ratio, ice1_electrical_efficiency)
        ice1_residual_heat_power = ice1.residual_heat_power(ice1_total_heat_input, ice1_residual_heat_efficiency)
        ice1_natural_gas_consumption = ice1.natural_gas_consumption(ice1_total_heat_input)
        ice1_power_consumption = ice1.auxiliary_equipment_power_consumption(ice1_load_ratio)
        ice1_electrical_income = ice1_electrical_power * gc.sale_electricity_price
        ice1_electrical_cost = ice1_natural_gas_consumption * gc.natural_gas_price + ice1_power_consumption * gc.buy_electricity_price
        wtd.write_to_database_ice1(syncbase, True, False, False, 0, 0, 0, ice1_electrical_efficiency,
                                   ice1_residual_heat_efficiency, ice1_electrical_power, ice1_residual_heat_power,
                                   ice1_natural_gas_consumption, ice1_power_consumption, ice1_electrical_income, ice1_electrical_cost)
        # 溴化锂1
        lb1_cold = Lithium_Bromide_Cold(ice1_residual_heat_power, lb1_wp_chilled_water, lb1_wp_cooling_water, lb1_wp_hot_water, gc)
        lb1_cold_heat_out = lb_cold_load * (ice1_load_ratio/(ice1_load_ratio + ice2_load_ratio))
        lb1_wp_heat_chilled_water_frequency = lbcf(0, ice1_load_ratio, lb1_cold, gc)[5]
        lb1_wp_cooling_water_frequency = lbcf(0, ice1_load_ratio, lb1_cold, gc)[6]
        lb1_power_consumption = lbcf(0, ice1_load_ratio, lb1_cold, gc)[1]
        lb1_chilled_heat_water_flow = lbcf(0, ice1_load_ratio, lb1_cold, gc)[3]
        lb1_cooling_water_flow = lbcf(0, ice1_load_ratio, lb1_cold, gc)[4]
        lb1_wp_chilled_heat_water_power_consumption = lb1_wp_chilled_water.pump_performance_data(lb1_chilled_heat_water_flow, lb1_wp_heat_chilled_water_frequency)[1]
        lb1_wp_cooling_water_power_consumption = lb1_wp_cooling_water.pump_performance_data(lb1_cooling_water_flow, lb1_wp_cooling_water_frequency)[1]
        lb1_fan_power_consumption = 20
        lb1_cold_cop = lb1_cold.cooling_cop(ice1_load_ratio)
        lb1_heat_cop = 0
        lb1_hot_water_cop = 0
        lb1_hot_water_out = 0
        lb1_cold_cost = lb1_power_consumption * gc.buy_electricity_price + lbcf(0, ice1_load_ratio, lb1_cold, gc)[2] * gc.water_price
        lb1_heat_cost = 0
        lb1_hot_water_cost = 0
        lb1_wp_hot_water_power_consumption = 0
        lb1_hot_water_flow = 0
        lb1_cold_income = lb1_cold_heat_out * gc.cooling_price
        lb1_heat_income = 0
        lb1_hot_water_income = 0
        # 内燃机运行状态
        ice1_start_state = True
        ice1_stop_state = False
        ice1_fault_state = False
        # 溴化锂运行状态
        lb1_cold_state = True
        lb1_heat_state = False
        lb1_hot_water_state = False
        lb1_stop_state = False
        lb1_fault_state = False
        # 写入数据库
        wtd.write_to_database_lb1(syncbase, True, False, lb1_wp_heat_chilled_water_frequency, lb1_wp_cooling_water_frequency,
                          lb1_cold_heat_out, lb1_power_consumption, lb1_chilled_heat_water_flow, lb1_cooling_water_flow,
                          lb1_wp_chilled_heat_water_power_consumption, lb1_wp_cooling_water_power_consumption, lb1_fan_power_consumption,
                          lb1_cold_cop, lb1_heat_cop, lb1_hot_water_cop, lb1_hot_water_out, lb1_cold_cost, lb1_heat_cost,
                          lb1_hot_water_cost, lb1_wp_hot_water_power_consumption, lb1_hot_water_flow, lb1_cold_income, lb1_heat_income, lb1_hot_water_income)

    else:
        ice1_electrical_efficiency = 0
        ice1_electrical_power = 0
        ice1_electrical_income = 0
        ice1_electrical_cost = 0
        ice1_natural_gas_consumption = 0
        ice1_power_consumption = 0
        lb1_cold_cop = 0
        lb1_heat_cop = 0
        lb1_hot_water_cop = 0
        lb1_cold_heat_out = 0
        lb1_hot_water_out = 0
        lb1_power_consumption = 0
        lb1_cold_cost = 0
        lb1_heat_cost = 0
        lb1_hot_water_cost = 0
        lb1_cold_income = 0
        lb1_heat_income = 0
        lb1_hot_water_income = 0
        lb1_chilled_heat_water_flow = 0
        lb1_hot_water_flow = 0
        # 1#内燃机运行状态
        ice1_start_state = False
        ice1_stop_state = True
        ice1_fault_state = False
        # 1#溴化锂运行状态
        lb1_cold_state = False
        lb1_heat_state = False
        lb1_hot_water_state = False
        lb1_stop_state = True
        lb1_fault_state = False
        # 写入数据库
        wtd.write_to_database_ice1(syncbase, False, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        wtd.write_to_database_lb1(syncbase, False, True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 内燃机2
    if ice2_load_ratio > 0:
        ice2_electrical_efficiency = ice2.electricity_power_efficiency(ice2_load_ratio)
        ice2_residual_heat_efficiency = ice2.residual_heat_efficiency(ice2_load_ratio)
        ice2_electrical_power = ice2.electricity_power_rated * ice2_load_ratio
        ice2_total_heat_input = ice2.total_heat_input(ice2_load_ratio, ice2_electrical_efficiency)
        ice2_residual_heat_power = ice2.residual_heat_power(ice2_total_heat_input, ice2_residual_heat_efficiency)
        ice2_natural_gas_consumption = ice2.natural_gas_consumption(ice2_total_heat_input)
        ice2_power_consumption = ice2.auxiliary_equipment_power_consumption(ice2_load_ratio)
        ice2_electrical_income = ice2_electrical_power * gc.sale_electricity_price
        ice2_electrical_cost = ice2_natural_gas_consumption * gc.natural_gas_price + ice2_power_consumption * gc.buy_electricity_price
        wtd.write_to_database_ice2(syncbase, True, False, False, 0, 0, 0, ice2_electrical_efficiency,
                                   ice2_residual_heat_efficiency, ice2_electrical_power, ice2_residual_heat_power,
                                   ice2_natural_gas_consumption, ice2_power_consumption, ice2_electrical_income, ice2_electrical_cost)
        # 溴化锂2
        lb2_cold = Lithium_Bromide_Cold(ice2_residual_heat_power, lb2_wp_chilled_water, lb2_wp_cooling_water, lb2_wp_hot_water, gc)
        lb2_cold_heat_out = lb_cold_load * (ice2_load_ratio / (ice1_load_ratio + ice2_load_ratio))
        lb2_wp_heat_chilled_water_frequency = lbcf(0, ice2_load_ratio, lb2_cold, gc)[5]
        lb2_wp_cooling_water_frequency = lbcf(0, ice2_load_ratio, lb2_cold, gc)[6]
        lb2_power_consumption = lbcf(0, ice2_load_ratio, lb2_cold, gc)[1]
        lb2_chilled_heat_water_flow = lbcf(0, ice2_load_ratio, lb2_cold, gc)[3]
        lb2_cooling_water_flow = lbcf(0, ice2_load_ratio, lb2_cold, gc)[4]
        lb2_wp_chilled_heat_water_power_consumption = lb2_wp_chilled_water.pump_performance_data(lb2_chilled_heat_water_flow, lb2_wp_heat_chilled_water_frequency)[1]
        lb2_wp_cooling_water_power_consumption = lb2_wp_cooling_water.pump_performance_data(lb2_cooling_water_flow, lb2_wp_cooling_water_frequency)[1]
        lb2_fan_power_consumption = 20
        lb2_cold_cop = lb2_cold.cooling_cop(ice2_load_ratio)
        lb2_heat_cop = 0
        lb2_hot_water_cop = 0
        lb2_hot_water_out = 0
        lb2_cold_cost = lb2_power_consumption * gc.buy_electricity_price + lbcf(0, ice2_load_ratio, lb2_cold, gc)[2] * gc.water_price
        lb2_heat_cost = 0
        lb2_hot_water_cost = 0
        lb2_wp_hot_water_power_consumption = 0
        lb2_hot_water_flow = 0
        lb2_cold_income = lb2_cold_heat_out * gc.cooling_price
        lb2_heat_income = 0
        lb2_hot_water_income = 0
        # 2#内燃机运行状态
        ice2_start_state = True
        ice2_stop_state = False
        ice2_fault_state = False
        # 2#溴化锂运行状态
        lb2_cold_state = True
        lb2_heat_state = False
        lb2_hot_water_state = False
        lb2_stop_state = False
        lb2_fault_state = False
        # 写入数据库
        wtd.write_to_database_lb2(syncbase, True, False, lb2_wp_heat_chilled_water_frequency, lb2_wp_cooling_water_frequency,
                                  lb2_cold_heat_out, lb2_power_consumption, lb2_chilled_heat_water_flow, lb2_cooling_water_flow,
                                  lb2_wp_chilled_heat_water_power_consumption, lb2_wp_cooling_water_power_consumption,
                                  lb2_fan_power_consumption, lb2_cold_cop, lb2_heat_cop, lb2_hot_water_cop, lb2_hot_water_out, lb2_cold_cost,
                                  lb2_heat_cost, lb2_hot_water_cost, lb2_wp_hot_water_power_consumption, lb2_hot_water_flow,
                                  lb2_cold_income, lb2_heat_income, lb2_hot_water_income)

    else:
        ice2_electrical_efficiency = 0
        ice2_electrical_power = 0
        ice2_electrical_income = 0
        ice2_electrical_cost = 0
        ice2_natural_gas_consumption = 0
        ice2_power_consumption = 0
        lb2_cold_cop = 0
        lb2_heat_cop = 0
        lb2_hot_water_cop = 0
        lb2_cold_heat_out = 0
        lb2_hot_water_out = 0
        lb2_power_consumption = 0
        lb2_cold_cost = 0
        lb2_heat_cost = 0
        lb2_hot_water_cost = 0
        lb2_cold_income = 0
        lb2_heat_income = 0
        lb2_hot_water_income = 0
        lb2_chilled_heat_water_flow = 0
        lb2_hot_water_flow = 0
        # 内燃机运行状态
        ice2_start_state = False
        ice2_stop_state = True
        ice2_fault_state = False
        # 溴化锂运行状态
        lb2_cold_state = False
        lb2_heat_state = False
        lb2_hot_water_state = False
        lb2_stop_state = True
        lb2_fault_state = False
        # 写入数据库
        wtd.write_to_database_ice2(syncbase, False, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        wtd.write_to_database_lb2(syncbase, False, True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 离心式冷水机1
    if cc1_load_ratio > 0:
        cc1_power_consumption_total = ccc(cc1, gc, cc1_load_ratio)[1] # 设备本体+辅机总耗电
        cc1_chilled_water_temperature = gc.chilled_water_temperature
        cc1_cooling_water_temperature = cc1.cooling_water_temperature(cc1_load_ratio)
        cc1_wp_chilled_water_frequency = ccc(cc1, gc, cc1_load_ratio)[6]
        cc1_wp_cooling_water_frequency = ccc(cc1, gc, cc1_load_ratio)[7]
        cc1_cold_out = cc1.cooling_power_rated * cc1_load_ratio
        cc1_power_consumption = ccc(cc1, gc, cc1_load_ratio)[3] # 仅设备本体耗电
        cc1_chilled_water_flow = ccc(cc1, gc, cc1_load_ratio)[4]
        cc1_cooling_water_flow = ccc(cc1, gc, cc1_load_ratio)[5]
        cc1_wp_chilled_water_power_consumption = cc1.wp_chilled_water.pump_performance_data(cc1_chilled_water_flow, cc1_wp_chilled_water_frequency)[1]
        cc1_wp_cooling_water_power_consumption = cc1.wp_cooling_water.pump_performance_data(cc1_cooling_water_flow, cc1_wp_cooling_water_frequency)[1]
        cc1_cooling_tower_power_consumption = 20
        cc1_cop = cc1.centrifugal_chiller_cop(cc1_load_ratio, cc1_chilled_water_temperature, cc1_cooling_water_temperature)
        cc1_income = cc1_cold_out * gc.cooling_price
        cc1_cost = ccc(cc1, gc, cc1_load_ratio)[0]
        # #1离心式冷水机运行状态
        cc1_cold_state = True
        cc1_stop_state = False
        cc1_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc1(syncbase, False, False, True, cc1_wp_chilled_water_frequency, cc1_wp_cooling_water_frequency,
                          cc1_cold_out, cc1_power_consumption, cc1_chilled_water_flow, cc1_cooling_water_flow, cc1_wp_chilled_water_power_consumption,
                          cc1_wp_cooling_water_power_consumption, cc1_cooling_tower_power_consumption, cc1_cop, cc1_income, cc1_cost)
    else:
        cc1_cop = 0
        cc1_power_consumption_total = 0
        cc1_income = 0
        cc1_cost = 0
        cc1_cold_out = 0
        cc1_chilled_water_flow = 0
        # #1离心式冷水机运行状态
        cc1_cold_state = False
        cc1_stop_state = True
        cc1_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc1(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 离心式冷水机2
    if cc2_load_ratio > 0:
        cc2_power_consumption_total = ccc(cc2, gc, cc2_load_ratio)[1]  # 设备本体+辅机总耗电
        cc2_chilled_water_temperature = gc.chilled_water_temperature
        cc2_cooling_water_temperature = cc2.cooling_water_temperature(cc2_load_ratio)
        cc2_wp_chilled_water_frequency = ccc(cc2, gc, cc2_load_ratio)[6]
        cc2_wp_cooling_water_frequency = ccc(cc2, gc, cc2_load_ratio)[7]
        cc2_cold_out = cc2.cooling_power_rated * cc2_load_ratio
        cc2_power_consumption = ccc(cc2, gc, cc2_load_ratio)[3] # 仅设备本体耗电
        cc2_chilled_water_flow = ccc(cc2, gc, cc2_load_ratio)[4]
        cc2_cooling_water_flow = ccc(cc2, gc, cc2_load_ratio)[5]
        cc2_wp_chilled_water_power_consumption = cc2.wp_chilled_water.pump_performance_data(cc2_chilled_water_flow, cc2_wp_chilled_water_frequency)[1]
        cc2_wp_cooling_water_power_consumption = cc2.wp_cooling_water.pump_performance_data(cc2_cooling_water_flow, cc2_wp_cooling_water_frequency)[1]
        cc2_cooling_tower_power_consumption = 20
        cc2_cop = cc2.centrifugal_chiller_cop(cc2_load_ratio, cc2_chilled_water_temperature, cc2_cooling_water_temperature)
        cc2_income = cc2_cold_out * gc.cooling_price
        cc2_cost = ccc(cc2, gc, cc2_load_ratio)[0]
        # #2离心式冷水机运行状态
        cc2_cold_state = True
        cc2_stop_state = False
        cc2_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc2(syncbase, False, False, True, cc2_wp_chilled_water_frequency,
                                  cc2_wp_cooling_water_frequency,
                                  cc2_cold_out, cc2_power_consumption, cc2_chilled_water_flow,
                                  cc2_cooling_water_flow, cc2_wp_chilled_water_power_consumption,
                                  cc2_wp_cooling_water_power_consumption, cc2_cooling_tower_power_consumption,
                                  cc2_cop, cc2_income, cc2_cost)
    else:
        cc2_cop = 0
        cc2_power_consumption_total = 0
        cc2_income = 0
        cc2_cost = 0
        cc2_cold_out = 0
        cc2_chilled_water_flow = 0
        # #2离心式冷水机运行状态
        cc2_cold_state = False
        cc2_stop_state = True
        cc2_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc2(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 离心式冷水机3（离心式热泵1制冷）
    if cc3_load_ratio > 0:
        cc3_power_consumption_total = ccc(cc3, gc, cc3_load_ratio)[1]  # 设备本体+辅机总耗电
        cc3_chilled_water_temperature = gc.chilled_water_temperature
        cc3_cooling_water_temperature = cc3.cooling_water_temperature(cc3_load_ratio)
        cc3_wp_chilled_water_frequency = ccc(cc3, gc, cc3_load_ratio)[6]
        cc3_wp_cooling_water_frequency = ccc(cc3, gc, cc3_load_ratio)[7]
        cc3_cold_out = cc3.cooling_power_rated * cc3_load_ratio
        cc3_power_consumption = ccc(cc3, gc, cc3_load_ratio)[3] # 仅设备本体耗电
        cc3_chilled_water_flow = ccc(cc3, gc, cc3_load_ratio)[4]
        cc3_cooling_water_flow = ccc(cc3, gc, cc3_load_ratio)[5]
        cc3_wp_chilled_water_power_consumption = cc3.wp_chilled_water.pump_performance_data(cc3_chilled_water_flow, cc3_wp_chilled_water_frequency)[1]
        cc3_wp_cooling_water_power_consumption = cc3.wp_cooling_water.pump_performance_data(cc3_cooling_water_flow, cc3_wp_cooling_water_frequency)[1]
        cc3_cooling_tower_power_consumption = 20
        cc3_cop = cc3.centrifugal_chiller_cop(cc3_load_ratio, cc3_chilled_water_temperature, cc3_cooling_water_temperature)
        cc3_income = cc3_cold_out * gc.cooling_price
        cc3_cost = ccc(cc3, gc, cc3_load_ratio)[0]
        # #3离心式冷水机运行状态(#1离心式热泵制冷)
        chp1_cold_state = True
        chp1_heat_state = False
        chp1_stop_state = False
        chp1_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc3(syncbase, False, False, True, cc3_wp_chilled_water_frequency,
                                  cc3_wp_cooling_water_frequency,
                                  cc3_cold_out, cc3_power_consumption, cc3_chilled_water_flow,
                                  cc3_cooling_water_flow, cc3_wp_chilled_water_power_consumption,
                                  cc3_wp_cooling_water_power_consumption, cc3_cooling_tower_power_consumption,
                                  cc3_cop, cc3_income, cc3_cost)
    else:
        cc3_cop = 0
        cc3_power_consumption_total = 0
        cc3_income = 0
        cc3_cost = 0
        cc3_cold_out = 0
        cc3_chilled_water_flow = 0
        # #3离心式冷水机运行状态(#1离心式热泵制冷)
        chp1_cold_state = False
        chp1_heat_state = False
        chp1_stop_state = True
        chp1_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc3(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 离心式冷水机4（离心式热泵2制冷）
    if cc4_load_ratio > 0:
        cc4_power_consumption_total = ccc(cc4, gc, cc4_load_ratio)[1]  # 设备本体+辅机总耗电
        cc4_chilled_water_temperature = gc.chilled_water_temperature
        cc4_cooling_water_temperature = cc4.cooling_water_temperature(cc4_load_ratio)
        cc4_wp_chilled_water_frequency = ccc(cc4, gc, cc4_load_ratio)[6]
        cc4_wp_cooling_water_frequency = ccc(cc4, gc, cc4_load_ratio)[7]
        cc4_cold_out = cc4.cooling_power_rated * cc4_load_ratio
        cc4_power_consumption = ccc(cc4, gc, cc4_load_ratio)[3] # 仅设备本体耗电
        cc4_chilled_water_flow = ccc(cc4, gc, cc4_load_ratio)[4]
        cc4_cooling_water_flow = ccc(cc4, gc, cc4_load_ratio)[5]
        cc4_wp_chilled_water_power_consumption = cc4.wp_chilled_water.pump_performance_data(cc4_chilled_water_flow, cc4_wp_chilled_water_frequency)[1]
        cc4_wp_cooling_water_power_consumption = cc4.wp_cooling_water.pump_performance_data(cc4_cooling_water_flow, cc4_wp_cooling_water_frequency)[1]
        cc4_cooling_tower_power_consumption = 20
        cc4_cop = cc4.centrifugal_chiller_cop(cc4_load_ratio, cc4_chilled_water_temperature, cc4_cooling_water_temperature)
        cc4_income = cc4_cold_out * gc.cooling_price
        cc4_cost = ccc(cc4, gc, cc4_load_ratio)[0]
        # #4离心式冷水机运行状态(#2离心式热泵制冷)
        chp2_cold_state = True
        chp2_heat_state = False
        chp2_stop_state = False
        chp2_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc4(syncbase, False, False, True, cc4_wp_chilled_water_frequency,
                                  cc4_wp_cooling_water_frequency,
                                  cc4_cold_out, cc4_power_consumption, cc4_chilled_water_flow,
                                  cc4_cooling_water_flow, cc4_wp_chilled_water_power_consumption,
                                  cc4_wp_cooling_water_power_consumption, cc4_cooling_tower_power_consumption,
                                  cc4_cop, cc4_income, cc4_cost)
    else:
        cc4_cop = 0
        cc4_power_consumption_total = 0
        cc4_income = 0
        cc4_cost = 0
        cc4_cold_out = 0
        cc4_chilled_water_flow = 0
        # #4离心式冷水机运行状态(#2离心式热泵制冷)
        chp2_cold_state = False
        chp2_heat_state = False
        chp2_stop_state = True
        chp2_fault_state = False
        # 写入数据库
        wtd.write_to_database_cc4(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 空气源热泵1
    if ashpc1_load_ratio > 0:
        ashp1_power_consumption_total = ashpcc(ashpc1, gc, ashpc1_load_ratio)[1]  # 设备本体+辅机总耗电
        environment_temperature = gc.environment_temperature
        ashp1_chilled_water_temperature = gc.chilled_water_temperature
        ashp1_wp_water_frequency = ashpcc(ashpc1, gc, ashpc1_load_ratio)[5]
        ashp1_cold_out = ashpc1.cooling_power_rated * ashpc1_load_ratio
        ashp1_power_consumption = ashpcc(ashpc1, gc, ashpc1_load_ratio)[3] # 仅设备本体耗电
        ashp1_chilled_heat_water_flow = ashpcc(ashpc1, gc, ashpc1_load_ratio)[4]
        ashp1_wp_power_consumption = ashpc1.wp_chilled_water.pump_performance_data(ashp1_chilled_heat_water_flow, ashp1_wp_water_frequency)[1]
        ashp1_fan_power_consumption = 20
        ashp1_cold_cop = ashpc1.air_source_heat_pump_cold_cop(ashpc1_load_ratio, ashp1_chilled_water_temperature, environment_temperature)
        ashp1_heat_cop = 0
        ashp1_cold_income = ashp1_cold_out * gc.cooling_price
        ashp1_cold_cost = ashpcc(ashpc1, gc, ashpc1_load_ratio)[0]
        ashp1_heat_cost = 0
        # #1空气源热泵运行状态
        ashp1_cold_state =True
        ashp1_heat_state = False
        ashp1_stop_state = False
        ashp1_fault_state = False
        wtd.write_to_database_ashp1(syncbase, False, False, True, ashp1_wp_water_frequency,
                                    ashp1_cold_out, ashp1_power_consumption, ashp1_chilled_heat_water_flow,
                                    ashp1_wp_power_consumption, ashp1_fan_power_consumption, ashp1_cold_cop, ashp1_heat_cop, ashp1_cold_income,
                                    ashp1_cold_cost, ashp1_heat_cost)
    else:
        ashp1_cold_cop = 0
        ashp1_heat_cop = 0
        ashp1_power_consumption_total = 0
        ashp1_cold_income = 0
        ashp1_cold_cost = 0
        ashp1_heat_cost = 0
        ashp1_cold_out = 0
        ashp1_chilled_heat_water_flow = 0
        # #1空气源热泵运行状态
        ashp1_cold_state = False
        ashp1_heat_state = False
        ashp1_stop_state = True
        ashp1_fault_state = False
        # 写入数据库
        wtd.write_to_database_ashp1(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 空气源热泵2
    if ashpc2_load_ratio > 0:
        ashp2_power_consumption_total = ashpcc(ashpc2, gc, ashpc2_load_ratio)[1]  # 设备本体+辅机总耗电
        environment_temperature = gc.environment_temperature
        ashp2_chilled_water_temperature = gc.chilled_water_temperature
        ashp2_wp_water_frequency = ashpcc(ashpc2, gc, ashpc2_load_ratio)[5]
        ashp2_cold_out = ashpc2.cooling_power_rated * ashpc2_load_ratio
        ashp2_power_consumption = ashpcc(ashpc2, gc, ashpc2_load_ratio)[3] # 仅设备本体耗电
        ashp2_chilled_heat_water_flow = ashpcc(ashpc2, gc, ashpc2_load_ratio)[4]
        ashp2_wp_power_consumption = ashpc2.wp_chilled_water.pump_performance_data(ashp2_chilled_heat_water_flow, ashp2_wp_water_frequency)[1]
        ashp2_fan_power_consumption = 20
        ashp2_cold_cop = ashpc2.air_source_heat_pump_cold_cop(ashpc2_load_ratio, ashp2_chilled_water_temperature, environment_temperature)
        ashp2_heat_cop = 0
        ashp2_cold_income = ashp2_cold_out * gc.cooling_price
        ashp2_cold_cost = ashpcc(ashpc2, gc, ashpc2_load_ratio)[0]
        ashp2_heat_cost = 0
        # #2空气源热泵运行状态
        ashp2_cold_state = True
        ashp2_heat_state = False
        ashp2_stop_state = False
        ashp2_fault_state = False
        wtd.write_to_database_ashp2(syncbase, False, False, True, ashp2_wp_water_frequency,
                                    ashp2_cold_out, ashp2_power_consumption, ashp2_chilled_heat_water_flow,
                                    ashp2_wp_power_consumption, ashp2_fan_power_consumption, ashp2_cold_cop,
                                    ashp2_heat_cop, ashp2_cold_income, ashp2_cold_cost, ashp2_heat_cost)
    else:
        ashp2_cold_cop = 0
        ashp2_heat_cop = 0
        ashp2_power_consumption_total = 0
        ashp2_cold_income = 0
        ashp2_cold_cost = 0
        ashp2_heat_cost = 0
        ashp2_cold_out = 0
        ashp2_chilled_heat_water_flow = 0
        # #2空气源热泵运行状态
        ashp2_cold_state = False
        ashp2_heat_state = False
        ashp2_stop_state = True
        ashp2_fault_state = False
        # 写入数据库
        wtd.write_to_database_ashp2(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 空气源热泵3
    if ashpc3_load_ratio > 0:
        ashp3_power_consumption_total = ashpcc(ashpc3, gc, ashpc3_load_ratio)[1]  # 设备本体+辅机总耗电
        environment_temperature = gc.environment_temperature
        ashp3_chilled_water_temperature = gc.chilled_water_temperature
        ashp3_wp_water_frequency = ashpcc(ashpc3, gc, ashpc3_load_ratio)[5]
        ashp3_cold_out = ashpc3.cooling_power_rated * ashpc3_load_ratio
        ashp3_power_consumption = ashpcc(ashpc3, gc, ashpc3_load_ratio)[3] # 仅设备本体耗电
        ashp3_chilled_heat_water_flow = ashpcc(ashpc3, gc, ashpc3_load_ratio)[4]
        ashp3_wp_power_consumption = ashpc3.wp_chilled_water.pump_performance_data(ashp3_chilled_heat_water_flow, ashp3_wp_water_frequency)[1]
        ashp3_fan_power_consumption = 20
        ashp3_cold_cop = ashpc3.air_source_heat_pump_cold_cop(ashpc3_load_ratio, ashp3_chilled_water_temperature, environment_temperature)
        ashp3_heat_cop = 0
        ashp3_cold_income = ashp3_cold_out * gc.cooling_price
        ashp3_cold_cost = ashpcc(ashpc3, gc, ashpc3_load_ratio)[0]
        ashp3_heat_cost = 0
        # #3空气源热泵运行状态
        ashp3_cold_state = True
        ashp3_heat_state = False
        ashp3_stop_state = False
        ashp3_fault_state = False
        wtd.write_to_database_ashp3(syncbase, False, False, True, ashp3_wp_water_frequency,
                                    ashp3_cold_out, ashp3_power_consumption, ashp3_chilled_heat_water_flow,
                                    ashp3_wp_power_consumption, ashp3_fan_power_consumption, ashp3_cold_cop, ashp3_heat_cop,
                                    ashp3_cold_income, ashp3_cold_cost, ashp3_heat_cost)
    else:
        ashp3_cold_cop = 0
        ashp3_heat_cop = 0
        ashp3_power_consumption_total = 0
        ashp3_cold_income = 0
        ashp3_cold_cost = 0
        ashp3_heat_cost = 0
        ashp3_cold_out = 0
        ashp3_chilled_heat_water_flow = 0
        # #3空气源热泵运行状态
        ashp3_cold_state = False
        ashp3_heat_state = False
        ashp3_stop_state = True
        ashp3_fault_state = False
        # 写入数据库
        wtd.write_to_database_ashp3(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 空气源热泵4
    if ashpc4_load_ratio > 0:
        ashp4_power_consumption_total = ashpcc(ashpc4, gc, ashpc4_load_ratio)[1]  # 设备本体+辅机总耗电
        environment_temperature = gc.environment_temperature
        ashp4_chilled_water_temperature = gc.chilled_water_temperature
        ashp4_wp_water_frequency = ashpcc(ashpc4, gc, ashpc4_load_ratio)[5]
        ashp4_cold_out = ashpc4.cooling_power_rated * ashpc4_load_ratio
        ashp4_power_consumption = ashpcc(ashpc4, gc, ashpc4_load_ratio)[3] # 仅设备本体耗电
        ashp4_chilled_heat_water_flow = ashpcc(ashpc4, gc, ashpc4_load_ratio)[4]
        ashp4_wp_power_consumption = ashpc4.wp_chilled_water.pump_performance_data(ashp4_chilled_heat_water_flow, ashp4_wp_water_frequency)[1]
        ashp4_fan_power_consumption = 20
        ashp4_cold_cop = ashpc4.air_source_heat_pump_cold_cop(ashpc4_load_ratio, ashp4_chilled_water_temperature, environment_temperature)
        ashp4_heat_cop = 0
        ashp4_cold_income = ashp4_cold_out * gc.cooling_price
        ashp4_cold_cost = ashpcc(ashpc4, gc, ashpc4_load_ratio)[0]
        ashp4_heat_cost = 0
        # #4空气源热泵运行状态
        ashp4_cold_state = True
        ashp4_heat_state = False
        ashp4_stop_state = False
        ashp4_fault_state = False
        wtd.write_to_database_ashp4(syncbase, False, False, True, ashp4_wp_water_frequency,
                                    ashp4_cold_out, ashp4_power_consumption, ashp4_chilled_heat_water_flow,
                                    ashp4_wp_power_consumption, ashp4_fan_power_consumption, ashp4_cold_cop,
                                    ashp4_heat_cop, ashp4_cold_income, ashp4_cold_cost, ashp4_heat_cost)
    else:
        ashp4_cold_cop = 0
        ashp4_heat_cop = 0
        ashp4_power_consumption_total = 0
        ashp4_cold_income = 0
        ashp4_cold_cost = 0
        ashp4_heat_cost = 0
        ashp4_cold_out = 0
        ashp4_chilled_heat_water_flow = 0
        # #4空气源热泵运行状态
        ashp4_cold_state = False
        ashp4_heat_state = False
        ashp4_stop_state = True
        ashp4_fault_state = False
        # 写入数据库
        wtd.write_to_database_ashp4(syncbase, True, True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 蓄冷水罐
    if esec_cold_load_out != 0:
        ese_cold_heat_out = esec_cold_load_out
        ese_residual_storage_energy =  esecsrr()[0] + esecsrr()[1] + esecsrr()[2]
        ese_cost = esecc(esec1, gc, esec1_load_ratio)[0] + esecc(esec2, gc, esec2_load_ratio)[0] + esecc(esec3, gc, esec3_load_ratio)[0]
        if esec_cold_load_out > 0:
            ese_proportion_in = 0
            ese_proportion_out = esec_cold_load_out / station_cold_out_all
            # 蓄冷蓄热水罐运行状态
            ese_cold_out_state = True
            ese_heat_out_state = False
            ese_cold_in_state = False
            ese_heat_in_state = False
            ese_stop_state = False
            ese_fault_state = False
        else:
            ese_proportion_in = abs(esec_cold_load_out /(station_cold_out_all - esec_cold_load_out))
            ese_proportion_out = 0
            # 蓄冷蓄热水罐运行状态
            ese_cold_out_state = False
            ese_heat_out_state = False
            ese_cold_in_state = True
            ese_heat_in_state = False
            ese_stop_state = False
            ese_fault_state = False
            # 写入数据库
        wtd.write_to_database_ese(syncbase, ese_cold_heat_out, ese_residual_storage_energy, ese_cost, ese_proportion_in, ese_proportion_out)
    else:
        ese_cold_heat_out = 0
        ese_residual_storage_energy = esecsrr()[0] + esecsrr()[1] + esecsrr()[2]
        # 蓄冷蓄热水罐运行状态
        ese_cold_out_state = False
        ese_heat_out_state = False
        ese_cold_in_state = False
        ese_heat_in_state = False
        ese_stop_state = True
        ese_fault_state = False
        # 写入数据库
        wtd.write_to_database_ese(syncbase, 0, ese_residual_storage_energy, 0, 0, 0)

    # 蓄能水罐水泵1
    if esec1_load_ratio > 0:
        ese1_wp_water_frequency = esecc(esec1, gc, esec1_load_ratio)[4]
        ese1_chilled_heat_water_flow = esecc(esec1, gc, esec1_load_ratio)[3]
        ese1_wp_power_consumption = esec1.wp_chilled_water.pump_performance_data(ese1_chilled_heat_water_flow, ese1_wp_water_frequency)[1]
        # 写入数据库
        wtd.write_to_database_ese1(syncbase, False, False, True, ese1_wp_water_frequency,
                           ese1_chilled_heat_water_flow, ese1_wp_power_consumption)
    else:
        ese1_wp_power_consumption = 0
        ese1_chilled_heat_water_flow = 0
        # 写入数据库
        wtd.write_to_database_ese1(syncbase, True, True, False, 0, 0, 0)

    # 蓄能水罐水泵2
    if esec2_load_ratio > 0:
        ese2_wp_water_frequency = esecc(esec2, gc, esec2_load_ratio)[4]
        ese2_chilled_heat_water_flow = esecc(esec2, gc, esec2_load_ratio)[3]
        ese2_wp_power_consumption = esec2.wp_chilled_water.pump_performance_data(ese2_chilled_heat_water_flow, ese2_wp_water_frequency)[1]
        # 写入数据库
        wtd.write_to_database_ese2(syncbase, False, False, True, ese2_wp_water_frequency,
                                   ese2_chilled_heat_water_flow, ese2_wp_power_consumption)
    else:
        ese2_wp_power_consumption = 0
        ese2_chilled_heat_water_flow = 0
        # 写入数据库
        wtd.write_to_database_ese2(syncbase, True, True, False, 0, 0, 0)

    # 蓄能水罐水泵3
    if esec3_load_ratio > 0:
        ese3_wp_water_frequency = esecc(esec3, gc, esec3_load_ratio)[4]
        ese3_chilled_heat_water_flow = esecc(esec3, gc, esec3_load_ratio)[3]
        ese3_wp_power_consumption = esec3.wp_chilled_water.pump_performance_data(ese3_chilled_heat_water_flow, ese3_wp_water_frequency)[1]
        # 写入数据库
        wtd.write_to_database_ese3(syncbase, False, False, True, ese3_wp_water_frequency,
                                   ese3_chilled_heat_water_flow, ese3_wp_power_consumption)
    else:
        ese3_wp_power_consumption = 0
        ese3_chilled_heat_water_flow = 0
        # 写入数据库
        wtd.write_to_database_ese3(syncbase, True, True, False, 0, 0, 0)

    # 天然气生活热水锅炉
    if ngb_hw_hot_water > 0:
        ngb3_wp_hot_water_frequency = 50
        ngb3_hot_water_out = ngb_hw_hot_water
        ngb3_load_ratio = ngb3_hot_water_out/ngb_hot_water.heating_power_rated
        ngb3_power_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[0]
        ngb3_hot_water_flow = ngb_hw_hot_water * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
        ngb3_wp_hot_water_power_consumption = ngb_hot_water.wp_hot_water.pump_performance_data(ngb3_hot_water_flow, ngb3_wp_hot_water_frequency)[1]
        ngb3_efficiency = ngb_hot_water.boiler_efficiency(ngb3_load_ratio)
        ngb3_natural_gas_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[1]
        ngb3_income = ngb3_hot_water_out * gc.hot_water_price
        ngb3_cost = ngb3_natural_gas_consumption * gc.natural_gas_price + ngb3_natural_gas_consumption * gc.buy_electricity_price
        # 天然气热水锅炉运行状态
        ngb_hot_water_state = True
        ngb_stop_state = False
        ngb_fault_state = False
        # 写入数据库
        wtd.write_to_database_ngb3(syncbase, True, False, ngb3_wp_hot_water_frequency,
                               ngb3_hot_water_out, ngb3_power_consumption, ngb3_hot_water_flow,
                               ngb3_wp_hot_water_power_consumption,
                               ngb3_efficiency, ngb3_income, ngb3_cost, ngb3_natural_gas_consumption)
    else:
        ngb3_efficiency = 0
        ngb3_natural_gas_consumption = 0
        ngb3_power_consumption = 0
        ngb3_income = 0
        ngb3_cost = 0
        ngb3_hot_water_out = 0
        ngb3_hot_water_flow = 0
        # 天然气热水锅炉运行状态
        ngb_hot_water_state = False
        ngb_stop_state = True
        ngb_fault_state = False
        # 写入数据库
        wtd.write_to_database_ngb3(syncbase, False, True, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 写入系统共用数据结果
    cost_total = station_cost_min
    profit_total = station_profitis_max
    income_total = cost_total + profit_total
    electricity_out_total = station_electricity_out_all
    cold_heat_out_total = station_cold_out_all
    hot_water_out_total = lb_hot_water + ngb_hw_hot_water
    natural_gas_consume_total = ice1_natural_gas_consumption + ice2_natural_gas_consumption + ngb3_natural_gas_consumption
    electricity_consume_total = ice1_power_consumption + ice2_power_consumption + lb1_power_consumption + lb2_power_consumption + cc1_power_consumption_total \
                                + cc2_power_consumption_total + cc3_power_consumption_total + cc4_power_consumption_total + ashp1_power_consumption_total \
                                + ashp2_power_consumption_total + ashp3_power_consumption_total + ashp4_power_consumption_total + ese1_wp_power_consumption\
                                + ese2_wp_power_consumption + ese3_wp_power_consumption + ngb3_power_consumption
    if (ice1_natural_gas_consumption + ice2_natural_gas_consumption) > 0:
        comprehensive_energy_utilization = (ice1_electrical_power + ice2_electrical_power + lb1_cold_heat_out + lb2_cold_heat_out) * 3600 \
                                           / ((ice1_natural_gas_consumption + ice2_natural_gas_consumption) * gc.natural_gas_calorific_value)
    else:
        comprehensive_energy_utilization = 0
    eq_power_consumption_total = cc1_power_consumption_total + cc2_power_consumption_total + cc3_power_consumption_total + cc4_power_consumption_total \
                                 + ashp1_power_consumption_total + ashp2_power_consumption_total + ashp3_power_consumption_total \
                                 + ashp4_power_consumption_total + ese1_wp_power_consumption + ese2_wp_power_consumption + ese3_wp_power_consumption
    if eq_power_consumption_total > 0:
        cop_real_time = (cold_heat_out_total - lb_cold_load)/eq_power_consumption_total
    else:
        cop_real_time = 0
    reduction_in_carbon_emissions = 0
    reduction_in_sulfide_emissions = 0
    reduction_in_nitride_emissions = 0
    reduction_in_dust_emissions = 0
    proportion_of_renewable_energy_power = 0
    wtd.write_to_database_system_utility(syncbase, cost_total, income_total, profit_total, electricity_out_total, cold_heat_out_total, hot_water_out_total,
                                         natural_gas_consume_total, electricity_consume_total, comprehensive_energy_utilization, proportion_of_renewable_energy_power,
                                         cop_real_time, reduction_in_carbon_emissions, reduction_in_sulfide_emissions, reduction_in_nitride_emissions, reduction_in_dust_emissions)

    # 写入能源站冷热电的输入输出功率数据
    photovoltaic_electricity_out_total = 0
    wind_electricity_out_total = 0
    accumulator_electricity_out_total = 0
    electricity_generation_total = ice1_electrical_power + ice2_electrical_power + photovoltaic_electricity_out_total + wind_electricity_out_total + accumulator_electricity_out_total
    ice_electricity_out_total = ice1_electrical_power + ice2_electrical_power
    buy_electricity_total = electricity_consume_total - electricity_generation_total
    lb_cold_out_total = lb1_cold_heat_out + lb2_cold_heat_out
    lb_heat_out_total = 0
    lb_hot_water_out_total = lb1_hot_water_out + lb2_hot_water_out
    ngb_hot_water_out_total = ngb3_hot_water_out
    cc_cold_out_total = cc1_cold_out + cc2_cold_out
    chp_cold_out_total = cc3_cold_out + cc4_cold_out
    chp_heat_out_total = 0
    ashp_cold_out_total = ashp1_cold_out + ashp2_cold_out + ashp3_cold_out + ashp4_cold_out
    ese_cold_out_total = ese_cold_heat_out
    ese_heat_out_total = 0
    cold_out_total = lb_cold_out_total + cc_cold_out_total + chp_cold_out_total + ashp_cold_out_total + ese_cold_out_total
    heat_out_total = lb_heat_out_total + chp_heat_out_total + ese_heat_out_total
    # 写入数据库
    wtd.write_to_database_station_in_out(syncbase, cold_out_total, heat_out_total, electricity_generation_total, lb_cold_out_total, lb_heat_out_total, lb_hot_water_out_total,
                                     cc_cold_out_total, chp_cold_out_total, chp_heat_out_total, ashp_cold_out_total, ese_cold_out_total, ese_heat_out_total,
                                     ice_electricity_out_total, photovoltaic_electricity_out_total, wind_electricity_out_total, accumulator_electricity_out_total,
                                     buy_electricity_total, ngb_hot_water_out_total)

    # 写入能源站冷热电的收入成本数据
    ice_income_total = ice1_electrical_income + ice2_electrical_income
    lb_cold_income_total = lb1_cold_income + lb2_cold_income
    lb_heat_income_total = lb1_heat_income + lb2_heat_income
    lb_hot_water_income_total = lb1_hot_water_income + lb2_hot_water_income
    cc_cold_income_total = cc1_income + cc2_income
    chp_cold_income_total = cc3_income + cc4_income
    chp_heat_income_total = 0
    ashp_cold_income_total = ashp1_cold_income + ashp2_cold_income + ashp3_cold_income + ashp4_cold_income
    ngb_hot_water_income_total = ngb3_income
    photovoltaic_income_total = photovoltaic_electricity_out_total * gc.sale_electricity_price
    wind_income_total = wind_electricity_out_total * gc.sale_electricity_price
    ice_cost_total = ice1_electrical_cost + ice2_electrical_cost
    lb_cold_cost_total = lb1_cold_cost + lb2_cold_cost
    lb_heat_cost_total = lb1_heat_cost + lb2_heat_cost
    lb_hot_water_cost_total = lb1_hot_water_cost + lb2_hot_water_cost
    cc_cold_cost_total = cc1_cost + cc2_cost
    chp_cold_cost_total = cc3_cost + cc4_cost
    chp_heat_cost_total = 0
    ashp_cold_cost_total = ashp1_cold_cost + ashp2_cold_cost + ashp3_cold_cost + ashp4_cold_cost
    ashp_heat_cost_total = ashp1_heat_cost + ashp2_heat_cost + ashp3_heat_cost + ashp4_heat_cost
    ngb_hot_water_cost_total = ngb3_cost
    # 写入数据库
    wtd.write_to_database_income_cost(syncbase, ice_income_total, lb_cold_income_total, lb_heat_income_total, lb_hot_water_income_total, cc_cold_income_total,
                                  chp_cold_income_total, chp_heat_income_total, ashp_cold_income_total, ngb_hot_water_income_total,
                                  photovoltaic_income_total, wind_income_total, ice_cost_total, lb_cold_cost_total, lb_heat_cost_total,
                                  lb_hot_water_cost_total, cc_cold_cost_total, chp_cold_cost_total, chp_heat_cost_total,
                                  ashp_cold_cost_total, ashp_heat_cost_total, ngb_hot_water_cost_total)

    # 写入设备效率数据
    ice_electrical_efficiency = max(ice1_electrical_efficiency, ice2_electrical_efficiency)
    lb_cold_efficiency = max(lb1_cold_cop, lb2_cold_cop)
    lb_heat_efficiency = max(lb1_heat_cop, lb2_heat_cop)
    lb_hot_water_efficiency = max(lb1_hot_water_cop, lb2_hot_water_cop)
    cc_cold_cop = max(cc1_cop, cc2_cop)
    chp_cold_cop = max(cc3_cop, cc4_cop)
    chp_heat_cop = 0
    ashp_cold_cop = max(ashp1_cold_cop, ashp2_cold_cop, ashp3_cold_cop, ashp4_cold_cop)
    ashp_heat_cop = max(ashp1_heat_cop, ashp2_heat_cop, ashp3_heat_cop, ashp4_heat_cop)
    ngb_hot_water_efficiency = ngb3_efficiency
    photovoltaic_electrical_efficiency = 0
    wind_electrical_efficiency = 0
    # 写入数据库
    wtd.write_to_database_equipment_efficiency(syncbase, ice_electrical_efficiency, lb_cold_efficiency, lb_heat_efficiency, lb_hot_water_efficiency,
                                           cc_cold_cop, chp_cold_cop, chp_heat_cop, ashp_cold_cop, ashp_heat_cop,
                                           ngb_hot_water_efficiency, photovoltaic_electrical_efficiency, wind_electrical_efficiency)

    # 写入设备冷冻水出水温度和冷水生活热水总流量数据
    chilled_water_supply_flow_total = lb1_chilled_heat_water_flow + lb2_chilled_heat_water_flow + cc1_chilled_water_flow \
                                      + cc2_chilled_water_flow + cc3_chilled_water_flow + cc4_chilled_water_flow \
                                      + ashp1_chilled_heat_water_flow + ashp2_chilled_heat_water_flow + ashp3_chilled_heat_water_flow + ashp4_chilled_heat_water_flow \
                                      + ese1_chilled_heat_water_flow + ese2_chilled_heat_water_flow + ese3_chilled_heat_water_flow
    chilled_water_supply_temperature = gc.chilled_water_temperature
    chilled_water_return_temperature = gc.chilled_water_temperature + gc.chilled_water_temperature_difference_rated
    heat_water_supply_flow_total = 0
    heat_water_supply_temperature = 0
    heat_water_return_temperature = 0
    hot_water_supply_flow_total = lb1_hot_water_flow + lb2_hot_water_flow + ngb3_hot_water_flow
    hot_water_supply_temperature = gc.hot_water_temperature
    hot_water_return_temperature = gc.hot_water_temperature - gc.hot_water_temperature_difference_rated
    if lb1_cold_heat_out > 0:
        lb1_heat_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        lb1_heat_chilled_water_supply_temperature = 0
    if lb1_hot_water_out > 0:
        lb1_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        lb1_hot_water_supply_temperature = 0
    if lb2_cold_heat_out > 0:
        lb2_heat_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        lb2_heat_chilled_water_supply_temperature = 0
    if lb2_hot_water_out > 0:
        lb2_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        lb2_hot_water_supply_temperature = 0
    if ngb3_hot_water_out > 0:
        ngb3_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        ngb3_hot_water_supply_temperature = 0
    if cc1_cold_out > 0:
        cc1_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        cc1_chilled_water_supply_temperature = 0
    if cc2_cold_out > 0:
        cc2_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        cc2_chilled_water_supply_temperature = 0
    if cc3_cold_out > 0:
        cc3_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        cc3_chilled_water_supply_temperature = 0
    if cc4_cold_out > 0:
        cc4_chilled_water_supply_temperature = gc.chilled_water_temperature
    else:
        cc4_chilled_water_supply_temperature = 0
    chp1_heat_water_supply_temperature = 0
    chp2_heat_water_supply_temperature = 0
    if ashp1_cold_out > 0:
        ashp1_water_supply_temperature = gc.chilled_water_temperature
    else:
        ashp1_water_supply_temperature = 0
    if ashp2_cold_out > 0:
        ashp2_water_supply_temperature = gc.chilled_water_temperature
    else:
        ashp2_water_supply_temperature = 0
    if ashp3_cold_out > 0:
        ashp3_water_supply_temperature = gc.chilled_water_temperature
    else:
        ashp3_water_supply_temperature = 0
    if ashp4_cold_out > 0:
        ashp4_water_supply_temperature = gc.chilled_water_temperature
    else:
        ashp4_water_supply_temperature = 0
    if ese_cold_out_total > 0:
        ese_water_supply_temperature = gc.chilled_water_temperature
    else:
        ese_water_supply_temperature = 0
    # 写入数据库
    wtd.write_to_database_temperature_flow(syncbase, chilled_water_supply_flow_total, chilled_water_supply_temperature, chilled_water_return_temperature,
                                       heat_water_supply_flow_total, heat_water_supply_temperature, heat_water_return_temperature,
                                       hot_water_supply_flow_total, hot_water_supply_temperature, hot_water_return_temperature,
                                       lb1_heat_chilled_water_supply_temperature, lb1_hot_water_supply_temperature, lb2_heat_chilled_water_supply_temperature,
                                       lb2_hot_water_supply_temperature, ngb3_hot_water_supply_temperature, cc1_chilled_water_supply_temperature,
                                       cc2_chilled_water_supply_temperature, cc3_chilled_water_supply_temperature, cc4_chilled_water_supply_temperature,
                                       chp1_heat_water_supply_temperature, chp2_heat_water_supply_temperature, ashp1_water_supply_temperature,
                                       ashp2_water_supply_temperature, ashp3_water_supply_temperature, ashp4_water_supply_temperature, ese_water_supply_temperature)

    # 写入设备运行状态
    photovoltaic_start_state = False
    photovoltaic_stop_state = True
    photovoltaic_fault_state = False
    wind_start_state = False
    wind_stop_state = True
    wind_fault_state = False
    cdz_start_state = False
    cdz_stop_state = True
    cdz_fault_state = False
    accumulator_electricity_out_state = False
    accumulator_electricity_in_state = False
    accumulator_stop_state = True
    accumulator_fault_state = False
    lamp_start_state = False
    lamp_stop_state = True
    lamp_fault_state = False
    # 写入数据库
    wtd.write_to_database_equipment_state(syncbase, ice1_start_state, ice1_stop_state, ice1_fault_state, ice2_start_state, ice2_stop_state, ice2_fault_state,
                                      lb1_cold_state, lb1_heat_state, lb1_hot_water_state, lb1_stop_state, lb1_fault_state, lb2_cold_state,
                                      lb2_heat_state, lb2_hot_water_state, lb2_stop_state, lb2_fault_state, cc1_cold_state, cc1_stop_state, cc1_fault_state,
                                      cc2_cold_state, cc2_stop_state, cc2_fault_state, chp1_cold_state, chp1_heat_state, chp1_stop_state, chp1_fault_state,
                                      chp2_cold_state, chp2_heat_state, chp2_stop_state, chp2_fault_state, ashp1_cold_state, ashp1_heat_state, ashp1_stop_state,
                                      ashp1_fault_state, ashp2_cold_state, ashp2_heat_state, ashp2_stop_state, ashp2_fault_state, ashp3_cold_state,
                                      ashp3_heat_state, ashp3_stop_state, ashp3_fault_state, ashp4_cold_state, ashp4_heat_state, ashp4_stop_state, ashp4_fault_state,
                                      ese_cold_out_state, ese_heat_out_state, ese_cold_in_state, ese_heat_in_state, ese_stop_state, ese_fault_state,
                                      ngb_hot_water_state, ngb_stop_state, ngb_fault_state, photovoltaic_start_state, photovoltaic_stop_state, photovoltaic_fault_state,
                                      wind_start_state, wind_stop_state, wind_fault_state, cdz_start_state, cdz_stop_state, cdz_fault_state,
                                      accumulator_electricity_out_state, accumulator_electricity_in_state, accumulator_stop_state, accumulator_fault_state,
                                      lamp_start_state, lamp_stop_state, lamp_fault_state)