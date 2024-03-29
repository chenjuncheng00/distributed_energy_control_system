import math
import datetime
from equipment import Lithium_Bromide_Heat
from triple_supply_function import triple_supply_heat_function as tshf, lithium_bromide_heat_function as lbhf
from centrifugal_heat_pump_heat_function import centrifugal_heat_pump_cost_heat as chpch
from air_source_heat_pump_heat_function import air_source_heat_pump_cost_heat as ashpch
from natural_gas_boiler_funtion import natural_gas_boiler_in_out_hot_water as ngbiohw, natural_gas_boiler_heat_cost as ngbhc, natural_gas_boiler_heat_funtion as ngbhf, natural_gas_boiler_heat_result as ngbhr
from energy_storage_equipment_heat_function import energy_storage_equipment_heat_function as esehf, energy_storage_equipment_heat_result as esehr, \
     energy_storage_equipment_heat_storage_residual_read as esehsrr, energy_storage_equipment_heat_storage_residual_write as esehsrw, energy_storage_equipment_heat_cost as esehc
from two_stage_heat_pump_function import two_stage_heat_pump_function as tshpf

def heating_season_function(heat_load, hot_water_load, electricity_load, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water,
                            chph1, chph2, chph3, chph4, ashph1, ashph2, ashph3, ashph4, eseh1, eseh2, eseh3, ngb_hot_water, environment_temperature,
                            heating_water_temperature, ashp_heat_source_water_temperature, gc):

    """采暖季计算"""

    print("正在进行采暖季计算.........")

    # 母管制系统，采暖季计算
    # 离心式热泵制热功率之和
    chph_heating_power_rated_sum = chph1.heating_power_rated + chph2.heating_power_rated + chph3.heating_power_rated + chph4.heating_power_rated
    # 天然气采暖锅炉制热功率之和
    # ngbh_heating_power_rated_sum = ngbh1.heating_power_rated + ngbh2.heating_power_rated 
    # 制热设备额定制热量之和
    eq_heating_power_rated_sum = chph_heating_power_rated_sum
    # 生活热水总流量
    hot_water_flow_total = hot_water_load * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
    # 生活热水泵启动数量，向上取整，每个泵额定流量44t/h
    hw_wp_num = math.ceil(hot_water_flow_total / 44)
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
    if eq_heating_power_rated_sum <= heat_load:
        ice1_load_ratio_min = 1
        ice2_load_ratio_min = 1
    else:
        ice1_load_ratio_min = 0
        ice2_load_ratio_min = 0
    # 列表，储存能源站向外供热供电量
    station_electricity_out_all = []
    station_heat_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存溴化锂供热热量
    lb_heat_load_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存4台设备计算出的负荷率结果
    chph1_load_ratio_result = []
    chph2_load_ratio_result = []
    chph3_load_ratio_result = []
    chph4_load_ratio_result = []
    # 列表，储存4个风冷螺杆式热泵计算出的负荷率结果
    ashph1_load_ratio_result = []
    ashph2_load_ratio_result = []
    ashph3_load_ratio_result = []
    ashph4_load_ratio_result = []
    # 列表，储存2台天然气采暖锅炉设备计算出的负荷率结果
    # ngbh1_load_ratio_result = []
    # ngbh2_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_heating_season == True:
        # 溴化锂1、2的生活热水负荷最大值
        lb1_hot_water_max = gc.lb1_hot_water_max
        lb2_hot_water_max = gc.lb2_hot_water_max
        # 溴化锂设备生活热水计算步长
        lb1_hot_water_step = gc.lb1_hot_water_step
        lb2_hot_water_step = gc.lb2_hot_water_step
        # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
        if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
        elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
        else:  # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
            lb_hot_water_max = hot_water_load
    else:
        lb1_hot_water_max = 0
        lb_hot_water_max = 0
        # 步长不能为0，否则无限循环
        lb1_hot_water_step = gc.project_load_error
        lb2_hot_water_step = gc.project_load_error

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
    # 从热负荷角度计算的内燃机启动数量最大值
    ice_num_max_heat_2 = math.ceil(heat_load / gc.lb1_heat_max)
    # 如果恰好整除，则向上加1
    if ice_num_max_heat_2 == int(ice_num_max_heat_2):
        ice_num_max_heat_1 = ice_num_max_heat_2 + 1
    else:
        ice_num_max_heat_1 = ice_num_max_heat_2
    # 最大数量不可以超过2
    if ice_num_max_heat_1 > 2:
        ice_num_max_heat = 2
    else:
        ice_num_max_heat = ice_num_max_heat_1
    # 两个结果取小值
    ice_num_max_a = min(ice_num_max_heat, ice_num_max_elec)

    # 内燃机启动数量初始值
    if heat_load - min(gc.lb1_heat_max, gc.lb2_heat_max) > eq_heating_power_rated_sum and heat_load - gc.lb1_heat_max - gc.lb2_heat_max <= eq_heating_power_rated_sum:
        ice_num_a = 2
    elif heat_load > eq_heating_power_rated_sum and heat_load - min(gc.lb1_heat_max, gc.lb2_heat_max) <= eq_heating_power_rated_sum:
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

    # 根据当前所处的用电时间段，判断蓄热装置是进行蓄热还是供热
    # 读取目前水罐剩余的蓄热量
    eseh1_heat_stock = esehsrr()[0]
    eseh2_heat_stock = esehsrr()[1]
    eseh3_heat_stock = esehsrr()[2]
    eseh_heat_stock_sum = eseh1_heat_stock + eseh2_heat_stock + eseh3_heat_stock
    # 3个水罐的额定蓄热量总和
    eseh_heating_storage_rated_sum = eseh1.heating_storage_rated + eseh2.heating_storage_rated + eseh3.heating_storage_rated
    # 因为计算周期是1小时，因此蓄热量(kWh)可以直接用于热负荷(kW)的计算，两者数值相同
    if hour_state == 1:
        # 供热状态(正值)
        if eseh_heat_stock_sum * gc.hour_num_of_calculations >= heat_load:
            # 如果蓄热水罐剩余量大于等于热负荷需求量，则蓄热水罐提供的热负荷等于热负荷需求量
            heat_load_eseh = heat_load
        else:
            heat_load_eseh = eseh_heat_stock_sum * gc.hour_num_of_calculations
    else:
        # 蓄热状态(负值)
        # 如果制热设备总功率减去热负荷需求量大于0，则表示可以有设备蓄热
        if eq_heating_power_rated_sum - heat_load > 0:
            if eq_heating_power_rated_sum - heat_load >= eseh_heating_storage_rated_sum * gc.hour_num_of_calculations:
                heat_load_eseh = -eseh_heating_storage_rated_sum * gc.hour_num_of_calculations
            else:
                heat_load_eseh = -(eq_heating_power_rated_sum - heat_load)
        else:
            heat_load_eseh = 0

    # 蓄热装置负荷为0，或处于蓄热状态，但蓄热设备已满，时不进行蓄热装置计算
    if heat_load_eseh == 0 or (heat_load_eseh < 0 and abs(eseh_heating_storage_rated_sum - eseh_heat_stock_sum) * gc.hour_num_of_calculations < gc.project_load_error):
        eseh1_load_ratio = 0
        eseh2_load_ratio = 0
        eseh3_load_ratio = 0
        eseh_heat_load_out = 0
        eseh_power_consumption_total = 0
        eseh_water_supply_total = 0
        # 单独计算补水成本
        cost_eseh_water_supply = eseh_water_supply_total * gc.water_price
    else:
        # 蓄热设备的使用优先级最高，先计算蓄热设备
        ans_eseh_a = esehf(heat_load_eseh, eseh1, eseh2, eseh3, gc)  # 所有的可能解
        ans_eseh = esehr(ans_eseh_a, eseh1, eseh2, eseh3)  # 选出蓄能设备最优解
        # 蓄热设备计算结果
        eseh1_load_ratio = ans_eseh[0]
        eseh2_load_ratio = ans_eseh[1]
        eseh3_load_ratio = ans_eseh[2]
        eseh_heat_load_out = ans_eseh[3]
        eseh_power_consumption_total = ans_eseh[4]
        eseh_water_supply_total = ans_eseh[5]
        # 单独计算补水成本
        cost_eseh_water_supply = eseh_water_supply_total * gc.water_price
    # 对计算出的蓄热装置负荷率进行修正（蓄能的情况变成负值）
    if hour_state == 1:
        # 供热状态(正值)
        eseh_heat_load_out = eseh_heat_load_out
    else:
        # 蓄热状态（负值）
        eseh_heat_load_out = - eseh_heat_load_out
    # 根据蓄热设备的情况对需要其他设备提供的热负荷进行修正
    heat_load -= eseh_heat_load_out

    # 内燃机启动数量，可以是0，可以是1，也可以是2
    while ice_num <= ice_num_max:
        # 重置内燃机、天然气采暖锅炉设备负荷率
        if ice_num >= 1:
            ice1_load_ratio = 1
        else:
            ice1_load_ratio = 0
        if ice_num >= 2:
            ice2_load_ratio = 1
        else:
            ice2_load_ratio = 0
        # 天然气锅炉负荷率默认值
        # ngbh1_load_ratio = ngbh1.load_min
        # ngbh2_load_ratio = ngbh2.load_min
        # 离心式热泵负荷率默认值
        chph1_load_ratio = chph1.load_min
        chph2_load_ratio = chph2.load_min
        chph3_load_ratio = chph3.load_min
        chph4_load_ratio = chph4.load_min
        # 风冷螺杆式热泵负荷率默认值
        ashph1_load_ratio = ashph1.load_min
        ashph2_load_ratio = ashph2.load_min
        ashph3_load_ratio = ashph3.load_min
        ashph4_load_ratio = ashph4.load_min
        # 2台内燃机系统的负荷率
        ice_load_ratio_result_all = [0, 0]
        # 列表，储存设备计算出的负荷率结果
        # ngbh_load_ratio_result_all = [0, 0]
        chph_load_ratio_result_all = [0, 0, 0, 0]
        ashph_load_ratio_result_all = [0, 0, 0, 0]
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
            # 天然气生活热水锅炉需要补充的生活热水
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 双级热泵耗电量、补水量、制热量默认值
            chph_heat_out_total = 0
            tshp_power_consumption_total = 0
            tshp_water_supply_total = 0
            # # 天然气采暖锅炉天然气耗量、耗电总功率，制热总功率、补水量默认值
            # ngbh_nature_gas_consumption_total = 0
            # ngbh_power_consumption_total = 0
            # ngbh_heat_out_total = 0
            # ngbh_water_supply_total = 0
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
                # 内燃机+溴化锂+天然气采暖锅炉运行状态计算
                # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                if ice1_load_ratio < ice1.load_min:
                    ice1_load_ratio = 0
                # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                if ice2_load_ratio < ice2.load_min:
                    ice2_load_ratio = 0
                # 计算三联供系统热出力
                global ts_heat_out_total
                ts_heat_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                # 三联供系统的电出力
                # 计算三联供系统电出力
                ts_electricity_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                # 天然气采暖锅炉需要补充的热负荷
                # heat_load_natural_gas_boiler = heat_load - ts_heat_out_total
                # 离心式热泵需要补充的热负荷
                heat_load_chph_1 = min(heat_load - ts_heat_out_total, chph_heating_power_rated_sum)
                heat_load_chph = max(heat_load_chph_1, 0)
                # 如果此时只有内燃机，且内燃机负荷率和设定的热负荷相差很小，则跳出循环
                if heat_load_chph >= 0 and abs(heat_load_chph) <= gc.project_load_error:
                    # 双级热泵不进行计算
                    tshp_calculate = False
                    # 离心式热泵和风冷热泵负荷率为0
                    chph1_load_ratio = 0
                    chph2_load_ratio = 0
                    chph3_load_ratio = 0
                    chph4_load_ratio = 0
                    ashph1_load_ratio = 0
                    ashph2_load_ratio = 0
                    ashph3_load_ratio = 0
                    ashph4_load_ratio = 0
                    # 双级热泵输入输出为0
                    chph_heat_out_total = 0
                    tshp_power_consumption_total = 0
                    tshp_water_supply_total = 0
                    # # 天然气采暖锅炉不进行计算
                    # ngbh_calculate = False
                    # # 天然气采暖锅炉负荷率都设置为0
                    # ngbh1_load_ratio = 0
                    # ngbh2_load_ratio = 0
                    # # 天然气采暖锅炉的输入输出量
                    # ngbh_nature_gas_consumption_total = 0
                    # ngbh_power_consumption_total = 0
                    # ngbh_heat_out_total = 0
                    # ngbh_water_supply_total = 0
                else:
                    # 双级热泵进行计算
                    tshp_calculate = True
                    # # 天然气采暖锅炉进行计算
                    # ngbh_calculate = True
                if heat_load_chph >= 0 and tshp_calculate == True:
                    # 计算双级热泵的运行策略
                    ans_tshp = tshpf(heat_load_chph, chph1, chph2, chph3, chph4, ashph1, ashph2, ashph3, ashph4,
                                     environment_temperature, heating_water_temperature, ashp_heat_source_water_temperature, gc)
                    # 读取计算结果
                    chph_heat_out_total = ans_tshp[1]
                    tshp_power_consumption_total = ans_tshp[2]
                    tshp_water_supply_total = ans_tshp[3]
                    chph1_load_ratio = ans_tshp[4]
                    chph2_load_ratio = ans_tshp[5]
                    chph3_load_ratio = ans_tshp[6]
                    chph4_load_ratio = ans_tshp[7]
                    ashph1_load_ratio = ans_tshp[8]
                    ashph2_load_ratio = ans_tshp[9]
                    ashph3_load_ratio = ans_tshp[10]
                    ashph4_load_ratio = ans_tshp[11]
                    # 计算天然气采暖锅炉的运行策略
                    # ans_ngbh = ngbhf(heat_load_natural_gas_boiler, ngbh1, ngbh2, gc)
                    # 读取此时的天然气采暖锅炉最优计算结果天然气消耗量
                    # ngbh_nature_gas_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[3]
                    # 读取此时的天然气采暖锅炉最优计算结果耗电功率
                    # ngbh_power_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[4]
                    # 读取此时的天然气采暖锅炉最优计算结果的供热功率
                    # ngbh_heat_out_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[2]
                    # 天然气采暖锅炉补水总量
                    # ngbh_water_supply_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[5]
                    # 此时2台设备的负荷率
                    # ngbh1_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[0]
                    # ngbh2_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[1]
                # 此时整个能源站的向外供电功率
                station_electricity_out_total = ts_electricity_out_total - tshp_power_consumption_total - hw_wp_power_consumption - eseh_power_consumption_total
                # 此时能源站供热总功率
                station_heat_out_total = ts_heat_out_total + chph_heat_out_total + eseh_heat_load_out
                # 如果仅有溴化锂供热，且制热量大于热负荷需求量，则内燃机负荷往下减
                if heat_load_chph <= 0 and station_heat_out_total > heat_load and ts_heat_out_total > 0:
                    # 减小内燃机设备1、2负荷率
                    if ice_num >= 1:
                        ice1_load_ratio -= ice1_step / 100
                    else:
                        ice1_load_ratio = 0
                    if ice_num >= 2:
                        ice2_load_ratio -= ice2_step / 100
                    else:
                        ice2_load_ratio = 0
                # 如果能源站向外供电量大于电负荷需求量，则内燃机负荷往下减
                elif station_electricity_out_total > electricity_load and ts_heat_out_total > 0 + gc.project_load_error:
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
                    # 存储此时的能源站向外供热供电量
                    station_electricity_out_all.append(station_electricity_out_total)
                    station_heat_out_all.append(station_heat_out_total)
                    # 储存此时的内燃机负荷率
                    ice_load_ratio_result_all[0] = ice1_load_ratio
                    ice_load_ratio_result_all[1] = ice2_load_ratio
                    ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                    ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                    # 储存此时的离心式热泵和风冷螺杆式热泵负荷率
                    chph_load_ratio_result_all[0] = chph1_load_ratio
                    chph_load_ratio_result_all[1] = chph2_load_ratio
                    chph_load_ratio_result_all[2] = chph3_load_ratio
                    chph_load_ratio_result_all[3] = chph4_load_ratio
                    chph1_load_ratio_result.append(chph_load_ratio_result_all[0])
                    chph2_load_ratio_result.append(chph_load_ratio_result_all[1])
                    chph3_load_ratio_result.append(chph_load_ratio_result_all[2])
                    chph4_load_ratio_result.append(chph_load_ratio_result_all[3])
                    ashph_load_ratio_result_all[0] = ashph1_load_ratio
                    ashph_load_ratio_result_all[1] = ashph2_load_ratio
                    ashph_load_ratio_result_all[2] = ashph3_load_ratio
                    ashph_load_ratio_result_all[3] = ashph4_load_ratio
                    ashph1_load_ratio_result.append(ashph_load_ratio_result_all[0])
                    ashph2_load_ratio_result.append(ashph_load_ratio_result_all[1])
                    ashph3_load_ratio_result.append(ashph_load_ratio_result_all[2])
                    ashph4_load_ratio_result.append(ashph_load_ratio_result_all[3])
                    # 储存此时天然气采暖锅炉的负荷率
                    # ngbh_load_ratio_result_all[0] = ngbh1_load_ratio
                    # ngbh_load_ratio_result_all[1] = ngbh2_load_ratio
                    # ngbh1_load_ratio_result.append(ngbh_load_ratio_result_all[0])
                    # ngbh2_load_ratio_result.append(ngbh_load_ratio_result_all[1])
                    # 储存溴化锂和天然气锅炉供热水量，溴化锂制热量
                    lb_hot_water_result.append(lb_hot_water_total)
                    ngb_hw_hot_water_result.append(ngb_hot_water_load)
                    lb_heat_load_result.append(ts_heat_out_total)
                    # 计算此时的能源站运行成本和收入
                    # 供电收入或者买电成本（大于0是收入，小于0是成本）
                    if station_electricity_out_total > 0:
                        income_electricity = station_electricity_out_total * gc.sale_electricity_price
                    else:
                        cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                    # 供热收入（用热负荷计算，能源站供热量比热负荷多的部分不计算）
                    income_heat = station_heat_out_total * gc.heating_price
                    # 生活热水收入
                    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                    income_hot_water = hot_water_load_total * gc.hot_water_price
                    # 三联供系统总成本（天然气+补水）
                    cost_ts = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                    # 双级热泵补水总成本
                    cost_tshp_water_supply = tshp_water_supply_total * gc.water_price
                    # 天然气采暖锅炉天然气总成本
                    # cost_ngbh_nature_gas = ngbh_nature_gas_consumption_total * gc.natural_gas_price
                    # 天然气采暖锅炉补水总成本
                    # cost_ngbh_water_supply = ngbh_water_supply_total * gc.water_price
                    # 天然气热水锅炉天然气成本
                    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                    # 天然气热水锅炉补水成本计算
                    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                    # 总收入成本利润
                    income_total = income_heat + income_electricity + income_hot_water
                    cost_total = cost_electricity + cost_tshp_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply + cost_eseh_water_supply
                    profits_total = income_total - cost_total
                    income.append(income_total)
                    cost.append(cost_total)
                    profits.append(profits_total)
                    # 如果内燃机1负荷率已经等于0，则跳出循环
                    if ice1_load_ratio == 0:
                        break
                    elif heat_load_chph <= 0 and tshp_calculate == False:
                        break
                    # 修改内燃机1、2负荷率
                    else:
                        # 减小内燃机设备1、2负荷率
                        if ice_num >= 1:
                            ice1_load_ratio -= ice1_step / 100
                        else:
                            ice1_load_ratio = 0
                        if ice_num >= 2:
                            ice2_load_ratio -= ice2_step / 100
                        else:
                            ice2_load_ratio = 0

                # 如果溴化锂（三联供系统）外供采暖负荷小于0 ，则跳出循环
                if ice_num >= 1 and ts_heat_out_total < 0 + gc.project_load_error:
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
    esehsrw(hour_state, eseh1, eseh2, eseh3, eseh1_load_ratio, eseh2_load_ratio, eseh3_load_ratio, eseh1_heat_stock, eseh2_heat_stock, eseh3_heat_stock, gc)

    # 返回计算结果
    return profits, income, cost, station_heat_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, lb_heat_load_result, lb_hot_water_result, ngb_hw_hot_water_result, chph1_load_ratio_result, chph2_load_ratio_result, chph3_load_ratio_result, chph4_load_ratio_result, ashph1_load_ratio_result, ashph2_load_ratio_result, ashph3_load_ratio_result, ashph4_load_ratio_result, eseh1_load_ratio, eseh2_load_ratio, eseh3_load_ratio, eseh_heat_load_out


def print_heating_season(ans, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, chph1, chph2,
                         ashph1, ashph2, ashph3, ashph4, eseh1, eseh2, eseh3, ngb_hot_water, environment_temperature,
                         heating_water_temperature, ashp_heat_source_water_temperature, gc):
    """将制热季计算结果打印出来"""
    try:
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
        heating_season_index = profitis_max_index
        # 读取对应索引下的参数
        station_profitis_max = ans[0][heating_season_index]
        station_cost_min = ans[2][heating_season_index]
        station_heat_out_all = ans[3][heating_season_index]
        station_electricity_out_all = ans[4][heating_season_index]
        ice1_load_ratio = ans[5][heating_season_index]
        ice2_load_ratio = ans[6][heating_season_index]
        # ngbh1_load_ratio = ans[7][heating_season_index]
        # ngbh2_load_ratio = ans[8][heating_season_index]
        # 溴化锂制热量，制生活热水量
        lb_heat_load = ans[7][heating_season_index]
        lb_hot_water = ans[8][heating_season_index]
        # 天然气锅炉制生活热水量
        ngb_hw_hot_water = ans[9][heating_season_index]
        # 离心式热泵和风冷螺杆式热泵计算结果
        chph1_load_ratio = ans[10][heating_season_index]
        chph2_load_ratio = ans[11][heating_season_index]
        chph3_load_ratio = ans[12][heating_season_index]
        chph4_load_ratio = ans[13][heating_season_index]
        ashph1_load_ratio = ans[14][heating_season_index]
        ashph2_load_ratio = ans[15][heating_season_index]
        ashph3_load_ratio = ans[16][heating_season_index]
        ashph4_load_ratio = ans[17][heating_season_index]
        # 蓄能水罐水泵负荷率
        eseh1_load_ratio = ans[18]
        eseh2_load_ratio = ans[19]
        eseh3_load_ratio = ans[20]
        # 蓄能水罐制热量
        eseh_heat_load_out = ans[21]
    except:
        # 读取对应索引下的参数
        station_profitis_max = 0
        station_cost_min = 0
        station_heat_out_all = 0
        station_electricity_out_all = 0
        ice1_load_ratio = 0
        ice2_load_ratio = 0
        # ngbh1_load_ratio = 0
        # ngbh2_load_ratio = 0
        # 溴化锂制热量，制生活热水量
        lb_heat_load = 0
        lb_hot_water = 0
        # 天然气锅炉制生活热水量
        ngb_hw_hot_water = 0
        # 离心式热泵和风冷螺杆式热泵计算结果
        chph1_load_ratio = 0
        chph2_load_ratio = 0
        chph3_load_ratio = 0
        chph4_load_ratio = 0
        ashph1_load_ratio = 0
        ashph2_load_ratio = 0
        ashph3_load_ratio = 0
        ashph4_load_ratio = 0
        # 蓄能水罐水泵负荷率
        eseh1_load_ratio = 0
        eseh2_load_ratio = 0
        eseh3_load_ratio = 0
        # 蓄能水罐制热量
        eseh_heat_load_out = 0

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(
        station_cost_min) + "\n" + "能源站供热功率为： " + str(station_heat_out_all) + "\n" + "蓄能装置热负荷功率为： " + str(
        eseh_heat_load_out) + "\n" + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(
        ice1_load_ratio) + "\n" + "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "\n" + "溴化锂设备供热功率为： " + str(
        lb_heat_load) + "\n" + "溴化锂供生活热水功率为： " + str(lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(
        ngb_hw_hot_water) + "\n" + "离心式热泵1负荷率为： " + str(chph1_load_ratio) + "\n" + "离心式热泵2负荷率为： " + str(
        chph2_load_ratio) + "\n" + "离心式热泵3负荷率为： " + str(chph3_load_ratio) + "\n" + "离心式热泵4负荷率为： " + str(
        chph4_load_ratio) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashph1_load_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(
        ashph2_load_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashph3_load_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(
        ashph4_load_ratio) + "\n" + "蓄能水罐水泵1负荷率： " + str(eseh1_load_ratio) + "\n" + "蓄能水罐水泵2负荷率： " + str(
        eseh2_load_ratio) + "\n" + "蓄能水罐水泵3负荷率： " + str(eseh3_load_ratio) + "\n")


    # # 向数据库写入计算结果
    # # 内燃机1和溴化锂1
    # if ice1_load_ratio > 0:
    #     # 内燃机1
    #     ice1_electrical_efficiency = ice1.electricity_power_efficiency(ice1_load_ratio)
    #     ice1_residual_heat_efficiency = ice1.residual_heat_efficiency(ice1_load_ratio)
    #     ice1_electrical_power = ice1.electricity_power_rated * ice1_load_ratio
    #     ice1_total_heat_input = ice1.total_heat_input(ice1_load_ratio, ice1_electrical_efficiency)
    #     ice1_residual_heat_power = ice1.residual_heat_power(ice1_total_heat_input, ice1_residual_heat_efficiency)
    #     ice1_natural_gas_consumption = ice1.natural_gas_consumption(ice1_total_heat_input)
    #     ice1_power_consumption = ice1.auxiliary_equipment_power_consumption(ice1_load_ratio)
    #     ice1_electrical_income = ice1_electrical_power * gc.sale_electricity_price
    #     ice1_electrical_cost = ice1_natural_gas_consumption * gc.natural_gas_price + ice1_power_consumption * gc.buy_electricity_price
    #     # 写入数据库
    #
    #     # 溴化锂1
    #     lb1_heat = Lithium_Bromide_Heat(ice1_residual_heat_power, lb1_wp_heating_water, lb1_wp_hot_water, 0.5, gc)
    #     lb1_cold_heat_out = lb_heat_load * (ice1_load_ratio / (ice1_load_ratio + ice2_load_ratio))
    #     lb1_wp_heat_chilled_water_frequency = lbhf(0, ice1_load_ratio, lb1_heat, gc)[4]
    #     lb1_wp_cooling_water_frequency = 0
    #     lb1_power_consumption = lbhf(0, ice1_load_ratio, lb1_heat, gc)[1]
    #     lb1_chilled_heat_water_flow = lbhf(0, ice1_load_ratio, lb1_heat, gc)[3]
    #     lb1_cooling_water_flow = 0
    #     lb1_wp_chilled_heat_water_power_consumption = lb1_wp_heating_water.pump_performance_data(lb1_chilled_heat_water_flow, lb1_wp_heat_chilled_water_frequency)[1]
    #     lb1_wp_cooling_water_power_consumption = 0
    #     lb1_fan_power_consumption = 0
    #     lb1_cold_cop = 0
    #     lb1_heat_cop = lb1_heat.heating_cop(ice1_load_ratio)
    #     lb1_hot_water_cop = 0
    #     lb1_hot_water_out = 0
    #     lb1_cold_cost = 0
    #     lb1_heat_cost = lb1_power_consumption * gc.buy_electricity_price + lbhf(0, ice1_load_ratio, lb1_heat, gc)[2] * gc.water_price
    #     lb1_hot_water_cost = 0
    #     lb1_wp_hot_water_power_consumption = 0
    #     lb1_hot_water_flow = 0
    #     lb1_cold_income = 0
    #     lb1_heat_income = lb1_cold_heat_out * gc.heating_price
    #     lb1_hot_water_income = 0
    #     # 内燃机运行状态
    #     ice1_start_state = True
    #     ice1_stop_state = False
    #     ice1_fault_state = False
    #     # 溴化锂运行状态
    #     lb1_cold_state = False
    #     lb1_heat_state = True
    #     lb1_hot_water_state = False
    #     lb1_stop_state = False
    #     lb1_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ice1_electrical_efficiency = 0
    #     ice1_electrical_power = 0
    #     ice1_electrical_income = 0
    #     ice1_electrical_cost = 0
    #     ice1_natural_gas_consumption = 0
    #     ice1_power_consumption = 0
    #     lb1_cold_cop = 0
    #     lb1_heat_cop = 0
    #     lb1_hot_water_cop = 0
    #     lb1_cold_heat_out = 0
    #     lb1_hot_water_out = 0
    #     lb1_power_consumption = 0
    #     lb1_cold_cost = 0
    #     lb1_heat_cost = 0
    #     lb1_hot_water_cost = 0
    #     lb1_cold_income = 0
    #     lb1_heat_income = 0
    #     lb1_hot_water_income = 0
    #     lb1_chilled_heat_water_flow = 0
    #     lb1_hot_water_flow = 0
    #     # 1#内燃机运行状态
    #     ice1_start_state = False
    #     ice1_stop_state = True
    #     ice1_fault_state = False
    #     # 1#溴化锂运行状态
    #     lb1_cold_state = False
    #     lb1_heat_state = False
    #     lb1_hot_water_state = False
    #     lb1_stop_state = True
    #     lb1_fault_state = False
    #     # 写入数据库
    #
    #
    # # 内燃机2
    # if ice2_load_ratio > 0:
    #     ice2_electrical_efficiency = ice2.electricity_power_efficiency(ice2_load_ratio)
    #     ice2_residual_heat_efficiency = ice2.residual_heat_efficiency(ice2_load_ratio)
    #     ice2_electrical_power = ice2.electricity_power_rated * ice2_load_ratio
    #     ice2_total_heat_input = ice2.total_heat_input(ice2_load_ratio, ice2_electrical_efficiency)
    #     ice2_residual_heat_power = ice2.residual_heat_power(ice2_total_heat_input, ice2_residual_heat_efficiency)
    #     ice2_natural_gas_consumption = ice2.natural_gas_consumption(ice2_total_heat_input)
    #     ice2_power_consumption = ice2.auxiliary_equipment_power_consumption(ice2_load_ratio)
    #     ice2_electrical_income = ice2_electrical_power * gc.sale_electricity_price
    #     ice2_electrical_cost = ice2_natural_gas_consumption * gc.natural_gas_price + ice2_power_consumption * gc.buy_electricity_price
    #     # 写入数据库
    #
    #     # 溴化锂2
    #     lb2_heat = Lithium_Bromide_Heat(ice2_residual_heat_power, lb2_wp_heating_water, lb2_wp_hot_water, 0.5, gc)
    #     lb2_cold_heat_out = lb_heat_load * (ice2_load_ratio / (ice1_load_ratio + ice2_load_ratio))
    #     lb2_wp_heat_chilled_water_frequency = lbhf(0, ice2_load_ratio, lb2_heat, gc)[4]
    #     lb2_wp_cooling_water_frequency = 0
    #     lb2_power_consumption = lbhf(0, ice2_load_ratio, lb2_heat, gc)[1]
    #     lb2_chilled_heat_water_flow = lbhf(0, ice2_load_ratio, lb2_heat, gc)[3]
    #     lb2_cooling_water_flow = 0
    #     lb2_wp_chilled_heat_water_power_consumption = lb2_wp_heating_water.pump_performance_data(lb2_chilled_heat_water_flow, lb2_wp_heat_chilled_water_frequency)[1]
    #     lb2_wp_cooling_water_power_consumption = 0
    #     lb2_fan_power_consumption = 0
    #     lb2_cold_cop = 0
    #     lb2_heat_cop = lb2_heat.heating_cop(ice2_load_ratio)
    #     lb2_hot_water_cop = 0
    #     lb2_hot_water_out = 0
    #     lb2_cold_cost = 0
    #     lb2_heat_cost = lb2_power_consumption * gc.buy_electricity_price + lbhf(0, ice2_load_ratio, lb2_heat, gc)[2] * gc.water_price
    #     lb2_hot_water_cost = 0
    #     lb2_wp_hot_water_power_consumption = 0
    #     lb2_hot_water_flow = 0
    #     lb2_cold_income = 0
    #     lb2_heat_income = lb2_cold_heat_out * gc.heating_price
    #     lb2_hot_water_income = 0
    #     # 2#内燃机运行状态
    #     ice2_start_state = True
    #     ice2_stop_state = False
    #     ice2_fault_state = False
    #     # 2#溴化锂运行状态
    #     lb2_cold_state = False
    #     lb2_heat_state = True
    #     lb2_hot_water_state = False
    #     lb2_stop_state = False
    #     lb2_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ice2_electrical_efficiency = 0
    #     ice2_electrical_power = 0
    #     ice2_electrical_income = 0
    #     ice2_electrical_cost = 0
    #     ice2_natural_gas_consumption = 0
    #     ice2_power_consumption = 0
    #     lb2_cold_cop = 0
    #     lb2_heat_cop = 0
    #     lb2_hot_water_cop = 0
    #     lb2_cold_heat_out = 0
    #     lb2_hot_water_out = 0
    #     lb2_power_consumption = 0
    #     lb2_cold_cost = 0
    #     lb2_heat_cost = 0
    #     lb2_hot_water_cost = 0
    #     lb2_cold_income = 0
    #     lb2_heat_income = 0
    #     lb2_hot_water_income = 0
    #     lb2_chilled_heat_water_flow = 0
    #     lb2_hot_water_flow = 0
    #     # 内燃机运行状态
    #     ice2_start_state = False
    #     ice2_stop_state = True
    #     ice2_fault_state = False
    #     # 溴化锂运行状态
    #     lb2_cold_state = False
    #     lb2_heat_state = False
    #     lb2_hot_water_state = False
    #     lb2_stop_state = True
    #     lb2_fault_state = False
    #     # 写入数据库
    #
    #
    # # 离心式热泵1（制热）
    # if chph1_load_ratio > 0:
    #     chp1_power_consumption_total = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[1] # 设备本体+辅机总耗电
    #     chph1_heat_source_water_temperature = chph1.heat_source_water_temperature(chph1_load_ratio)
    #     chp1_wp_heat_water_frequency = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[6]
    #     chp1_wp_source_water_frequency = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[7]
    #     chp1_heat_out = chph1.heating_power_rated * chph1_load_ratio
    #     chp1_power_consumption = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[3] # 仅设备本身耗电
    #     chp1_heat_water_flow = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[4]
    #     chp1_source_water_flow = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[5]
    #     chp1_wp_heat_water_power_consumption = chph1.wp_heating_water.pump_performance_data(chp1_heat_water_flow, chp1_wp_heat_water_frequency)[1]
    #     chp1_wp_source_water_power_consumption = chph1.wp_heat_source_water.pump_performance_data(chp1_source_water_flow, chp1_wp_source_water_frequency)[1]
    #     chp1_cop = chph1.centrifugal_heat_pump_cop(chph1_load_ratio, heating_water_temperature, chph1_heat_source_water_temperature)
    #     chp1_income = chp1_heat_out * gc.heating_price
    #     chp1_cost = chpch(chph1, gc, chph1_load_ratio, heating_water_temperature)[0]
    #     # #1离心式热泵制热
    #     chp1_cold_state = False
    #     chp1_heat_state = True
    #     chp1_stop_state = False
    #     chp1_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     chp1_cop = 0
    #     chp1_heat_out = 0
    #     chp1_power_consumption_total = 0
    #     chp1_income = 0
    #     chp1_cost = 0
    #     chp1_heat_water_flow = 0
    #     # #1离心式热泵制热
    #     chp1_cold_state = False
    #     chp1_heat_state = False
    #     chp1_stop_state = True
    #     chp1_fault_state = False
    #     # 写入数据库
    #
    #
    # # 离心式热泵2（制热）
    # if chph2_load_ratio > 0:
    #     chp2_power_consumption_total = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[1]  # 设备本体+辅机总耗电
    #     chph2_heat_source_water_temperature = chph2.heat_source_water_temperature(chph2_load_ratio)
    #     chp2_wp_heat_water_frequency = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[6]
    #     chp2_wp_source_water_frequency = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[7]
    #     chp2_heat_out = chph2.heating_power_rated * chph2_load_ratio
    #     chp2_power_consumption = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[3] # 仅设备本身耗电
    #     chp2_heat_water_flow = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[4]
    #     chp2_source_water_flow = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[5]
    #     chp2_wp_heat_water_power_consumption = chph2.wp_heating_water.pump_performance_data(chp2_heat_water_flow, chp2_wp_heat_water_frequency)[1]
    #     chp2_wp_source_water_power_consumption = chph2.wp_heat_source_water.pump_performance_data(chp2_source_water_flow, chp2_wp_source_water_frequency)[1]
    #     chp2_cop = chph2.centrifugal_heat_pump_cop(chph2_load_ratio, heating_water_temperature, chph2_heat_source_water_temperature)
    #     chp2_income = chp2_heat_out * gc.heating_price
    #     chp2_cost = chpch(chph2, gc, chph2_load_ratio, heating_water_temperature)[0]
    #     # #2离心式热泵制热
    #     chp2_cold_state = False
    #     chp2_heat_state = True
    #     chp2_stop_state = False
    #     chp2_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     chp2_cop = 0
    #     chp2_heat_out = 0
    #     chp2_power_consumption_total = 0
    #     chp2_income = 0
    #     chp2_cost = 0
    #     chp2_heat_water_flow = 0
    #     # #2离心式热泵制热
    #     chp2_cold_state = False
    #     chp2_heat_state = False
    #     chp2_stop_state = True
    #     chp2_fault_state = False
    #     # 写入数据库
    #
    #
    # # 空气源热泵1（制热）
    # if ashph1_load_ratio > 0:
    #     ashp1_power_consumption_total = ashpch(ashph1, gc, ashph1_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[1]  # 设备本体+辅机总耗电
    #     ashp1_wp_water_frequency = ashpch(ashph1, gc, ashph1_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[5]
    #     ashp1_heat_out = ashph1.heating_power_rated * ashph1_load_ratio
    #     ashp1_power_consumption = ashpch(ashph1, gc, ashph1_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[3] # 仅设备本身耗电
    #     ashp1_chilled_heat_water_flow = ashpch(ashph1, gc, ashph1_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[4]
    #     ashp1_wp_power_consumption = ashph1.wp_heating_water.pump_performance_data(ashp1_chilled_heat_water_flow, ashp1_wp_water_frequency)[1]
    #     ashp1_fan_power_consumption = 20
    #     ashp1_cold_cop = 0
    #     ashp1_heat_cop = ashph1.air_source_heat_pump_heat_cop(chph1_load_ratio, ashp_heat_source_water_temperature, environment_temperature)
    #     ashp1_cold_income = 0
    #     ashp1_cold_cost = 0
    #     ashp1_heat_cost = ashpch(ashph1, gc, ashph1_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[0]
    #     # #1空气源热泵运行状态
    #     ashp1_cold_state = False
    #     ashp1_heat_state = True
    #     ashp1_stop_state = False
    #     ashp1_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ashp1_cold_cop = 0
    #     ashp1_heat_cop = 0
    #     ashp1_power_consumption_total = 0
    #     ashp1_cold_income = 0
    #     ashp1_cold_cost = 0
    #     ashp1_heat_cost = 0
    #     ashp1_chilled_heat_water_flow = 0
    #     ashp1_heat_out = 0
    #     # #1空气源热泵运行状态
    #     ashp1_cold_state = False
    #     ashp1_heat_state = False
    #     ashp1_stop_state = True
    #     ashp1_fault_state = False
    #     # 写入数据库
    #
    #
    # # 空气源热泵2（制热）
    # if ashph2_load_ratio > 0:
    #     ashp2_power_consumption_total = ashpch(ashph2, gc, ashph2_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[1]  # 设备本体+辅机总耗电
    #     ashp2_wp_water_frequency = ashpch(ashph2, gc, ashph2_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[5]
    #     ashp2_heat_out = ashph2.heating_power_rated * ashph2_load_ratio
    #     ashp2_power_consumption = ashpch(ashph2, gc, ashph2_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[3] # 仅设备本身耗电
    #     ashp2_chilled_heat_water_flow = ashpch(ashph2, gc, ashph2_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[4]
    #     ashp2_wp_power_consumption = ashph2.wp_heating_water.pump_performance_data(ashp2_chilled_heat_water_flow, ashp2_wp_water_frequency)[1]
    #     ashp2_fan_power_consumption = 20
    #     ashp2_cold_cop = 0
    #     ashp2_heat_cop = ashph2.air_source_heat_pump_heat_cop(chph1_load_ratio, ashp_heat_source_water_temperature, environment_temperature)
    #     ashp2_cold_income = 0
    #     ashp2_cold_cost = 0
    #     ashp2_heat_cost = ashpch(ashph2, gc, ashph2_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[0]
    #     # #2空气源热泵运行状态
    #     ashp2_cold_state = False
    #     ashp2_heat_state = True
    #     ashp2_stop_state = False
    #     ashp2_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ashp2_cold_cop = 0
    #     ashp2_heat_cop = 0
    #     ashp2_power_consumption_total = 0
    #     ashp2_cold_income = 0
    #     ashp2_cold_cost = 0
    #     ashp2_heat_cost = 0
    #     ashp2_chilled_heat_water_flow = 0
    #     ashp2_heat_out = 0
    #     # #2空气源热泵运行状态
    #     ashp2_cold_state = False
    #     ashp2_heat_state = False
    #     ashp2_stop_state = True
    #     ashp2_fault_state = False
    #     # 写入数据库
    #
    #
    # # 空气源热泵3（制热）
    # if ashph3_load_ratio > 0:
    #     ashp3_power_consumption_total = ashpch(ashph3, gc, ashph3_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[1]  # 设备本体+辅机总耗电
    #     ashp3_wp_water_frequency = ashpch(ashph3, gc, ashph3_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[5]
    #     ashp3_heat_out = ashph3.heating_power_rated * ashph3_load_ratio
    #     ashp3_power_consumption = ashpch(ashph3, gc, ashph3_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[3] # 仅设备本身耗电
    #     ashp3_chilled_heat_water_flow = ashpch(ashph3, gc, ashph3_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[4]
    #     ashp3_wp_power_consumption = ashph3.wp_heating_water.pump_performance_data(ashp3_chilled_heat_water_flow, ashp3_wp_water_frequency)[1]
    #     ashp3_fan_power_consumption = 20
    #     ashp3_cold_cop = 0
    #     ashp3_heat_cop = ashph3.air_source_heat_pump_heat_cop(chph1_load_ratio, ashp_heat_source_water_temperature, environment_temperature)
    #     ashp3_cold_income = 0
    #     ashp3_cold_cost = 0
    #     ashp3_heat_cost = ashpch(ashph3, gc, ashph3_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[0]
    #     # #3空气源热泵运行状态
    #     ashp3_cold_state = False
    #     ashp3_heat_state = True
    #     ashp3_stop_state = False
    #     ashp3_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ashp3_cold_cop = 0
    #     ashp3_heat_cop = 0
    #     ashp3_power_consumption_total = 0
    #     ashp3_cold_income = 0
    #     ashp3_cold_cost = 0
    #     ashp3_heat_cost = 0
    #     ashp3_chilled_heat_water_flow = 0
    #     ashp3_heat_out = 0
    #     # #3空气源热泵运行状态
    #     ashp3_cold_state = False
    #     ashp3_heat_state = False
    #     ashp3_stop_state = True
    #     ashp3_fault_state = False
    #     # 写入数据库
    #
    #
    # # 空气源热泵4（制热）
    # if ashph4_load_ratio > 0:
    #     ashp4_power_consumption_total = ashpch(ashph4, gc, ashph4_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[1]  # 设备本体+辅机总耗电
    #     ashp4_wp_water_frequency = ashpch(ashph4, gc, ashph4_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[5]
    #     ashp4_heat_out = ashph4.heating_power_rated * ashph4_load_ratio
    #     ashp4_power_consumption = ashpch(ashph4, gc, ashph4_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[3] # 仅设备本身耗电
    #     ashp4_chilled_heat_water_flow = ashpch(ashph4, gc, ashph4_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[4]
    #     ashp4_wp_power_consumption = ashph4.wp_heating_water.pump_performance_data(ashp4_chilled_heat_water_flow, ashp4_wp_water_frequency)[1]
    #     ashp4_fan_power_consumption = 20
    #     ashp4_cold_cop = 0
    #     ashp4_heat_cop = ashph4.air_source_heat_pump_heat_cop(chph1_load_ratio, ashp_heat_source_water_temperature, environment_temperature)
    #     ashp4_cold_income = 0
    #     ashp4_cold_cost = 0
    #     ashp4_heat_cost = ashpch(ashph4, gc, ashph4_load_ratio, environment_temperature, ashp_heat_source_water_temperature)[0]
    #     # #4空气源热泵运行状态
    #     ashp4_cold_state = False
    #     ashp4_heat_state = True
    #     ashp4_stop_state = False
    #     ashp4_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ashp4_cold_cop = 0
    #     ashp4_heat_cop = 0
    #     ashp4_power_consumption_total = 0
    #     ashp4_cold_income = 0
    #     ashp4_cold_cost = 0
    #     ashp4_heat_cost = 0
    #     ashp4_chilled_heat_water_flow = 0
    #     ashp4_heat_out = 0
    #     # #4空气源热泵运行状态
    #     ashp4_cold_state = False
    #     ashp4_heat_state = False
    #     ashp4_stop_state = True
    #     ashp4_fault_state = False
    #     # 写入数据库
    #
    #
    # # 蓄冷水罐
    # if eseh_heat_load_out != 0:
    #     ese_cold_heat_out = eseh_heat_load_out
    #     ese_residual_storage_energy = esehsrr()[0] + esehsrr()[1] + esehsrr()[2]
    #     ese_cost = esehc(eseh1, gc, eseh1_load_ratio)[0] + esehc(eseh2, gc, eseh2_load_ratio)[0] + \
    #                esehc(eseh3, gc, eseh3_load_ratio)[0]
    #     if eseh_heat_load_out > 0:
    #         ese_proportion_in = 0
    #         ese_proportion_out = eseh_heat_load_out / station_heat_out_all
    #         # 蓄冷蓄热水罐运行状态
    #         ese_cold_out_state = False
    #         ese_heat_out_state = True
    #         ese_cold_in_state = False
    #         ese_heat_in_state = False
    #         ese_stop_state = False
    #         ese_fault_state = False
    #     else:
    #         ese_proportion_in = abs(eseh_heat_load_out / (station_heat_out_all - eseh_heat_load_out))
    #         ese_proportion_out = 0
    #         # 蓄冷蓄热水罐运行状态
    #         ese_cold_out_state = False
    #         ese_heat_out_state = False
    #         ese_cold_in_state = False
    #         ese_heat_in_state = True
    #         ese_stop_state = False
    #         ese_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ese_cold_heat_out = 0
    #     ese_residual_storage_energy = esehsrr()[0] + esehsrr()[1] + esehsrr()[2]
    #     # 蓄冷蓄热水罐运行状态
    #     ese_cold_out_state = False
    #     ese_heat_out_state = False
    #     ese_cold_in_state = False
    #     ese_heat_in_state = False
    #     ese_stop_state = True
    #     ese_fault_state = False
    #     # 写入数据库
    #
    #
    # # 蓄能水罐水泵1
    # if eseh1_load_ratio > 0:
    #     ese1_wp_water_frequency = esehc(eseh1, gc, eseh1_load_ratio)[4]
    #     ese1_chilled_heat_water_flow = esehc(eseh1, gc, eseh1_load_ratio)[3]
    #     ese1_wp_power_consumption = eseh1.wp_chilled_water.pump_performance_data(ese1_chilled_heat_water_flow, ese1_wp_water_frequency)[1]
    #     # 写入数据库
    #
    # else:
    #     ese1_wp_power_consumption = 0
    #     ese1_chilled_heat_water_flow = 0
    #     # 写入数据库
    #
    #
    # # 蓄能水罐水泵2
    # if eseh2_load_ratio > 0:
    #     ese2_wp_water_frequency = esehc(eseh2, gc, eseh2_load_ratio)[4]
    #     ese2_chilled_heat_water_flow = esehc(eseh2, gc, eseh2_load_ratio)[3]
    #     ese2_wp_power_consumption = eseh2.wp_chilled_water.pump_performance_data(ese2_chilled_heat_water_flow, ese2_wp_water_frequency)[1]
    #     # 写入数据库
    #
    # else:
    #     ese2_wp_power_consumption = 0
    #     ese2_chilled_heat_water_flow = 0
    #     # 写入数据库
    #
    #
    # # 蓄能水罐水泵3
    # if eseh3_load_ratio > 0:
    #     ese3_wp_water_frequency = esehc(eseh3, gc, eseh3_load_ratio)[4]
    #     ese3_chilled_heat_water_flow = esehc(eseh3, gc, eseh3_load_ratio)[3]
    #     ese3_wp_power_consumption = eseh3.wp_chilled_water.pump_performance_data(ese3_chilled_heat_water_flow, ese3_wp_water_frequency)[1]
    #     # 写入数据库
    #
    # else:
    #     ese3_wp_power_consumption = 0
    #     ese3_chilled_heat_water_flow = 0
    #     # 写入数据库
    #
    #
    # # 天然气生活热水锅炉
    # if ngb_hw_hot_water > 0:
    #     ngb3_wp_hot_water_frequency = 50
    #     ngb3_hot_water_out = ngb_hw_hot_water
    #     ngb3_load_ratio = ngb3_hot_water_out / ngb_hot_water.heating_power_rated
    #     ngb3_power_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[0]
    #     ngb3_hot_water_flow = ngb_hw_hot_water * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
    #     ngb3_wp_hot_water_power_consumption = ngb_hot_water.wp_hot_water.pump_performance_data(ngb3_hot_water_flow, ngb3_wp_hot_water_frequency)[1]
    #     ngb3_efficiency = ngb_hot_water.boiler_efficiency(ngb3_load_ratio)
    #     ngb3_natural_gas_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[1]
    #     ngb3_income = ngb3_hot_water_out * gc.hot_water_price
    #     ngb3_cost = ngb3_natural_gas_consumption * gc.natural_gas_price + ngb3_natural_gas_consumption * gc.buy_electricity_price
    #     # 天然气热水锅炉运行状态
    #     ngb_hot_water_state = True
    #     ngb_stop_state = False
    #     ngb_fault_state = False
    #     # 写入数据库
    #
    # else:
    #     ngb3_efficiency = 0
    #     ngb3_hot_water_out = 0
    #     ngb3_natural_gas_consumption = 0
    #     ngb3_power_consumption = 0
    #     ngb3_income = 0
    #     ngb3_cost = 0
    #     ngb3_hot_water_flow = 0
    #     # 天然气热水锅炉运行状态
    #     ngb_hot_water_state = False
    #     ngb_stop_state = True
    #     ngb_fault_state = False
    #     # 写入数据库
    #
    #
    # # 写入系统共用数据结果
    # cost_total = station_cost_min
    # profit_total = station_profitis_max
    # income_total = cost_total + profit_total
    # electricity_out_total = station_electricity_out_all
    # cold_heat_out_total = station_heat_out_all
    # hot_water_out_total = lb_hot_water + ngb_hw_hot_water
    # natural_gas_consume_total = ice1_natural_gas_consumption + ice2_natural_gas_consumption + ngb3_natural_gas_consumption
    # electricity_consume_total = ice1_power_consumption + ice2_power_consumption + lb1_power_consumption + lb2_power_consumption +chp1_power_consumption_total \
    #                             + chp2_power_consumption_total + ashp1_power_consumption_total + ashp2_power_consumption_total + ashp3_power_consumption_total \
    #                             + ashp4_power_consumption_total + ese1_wp_power_consumption + ese2_wp_power_consumption + ese3_wp_power_consumption + ngb3_power_consumption
    # if (ice1_natural_gas_consumption + ice2_natural_gas_consumption) > 0:
    #     comprehensive_energy_utilization = (ice1_electrical_power + ice2_electrical_power + lb1_cold_heat_out + lb2_cold_heat_out) * 3600 \
    #                                        / ((ice1_natural_gas_consumption + ice2_natural_gas_consumption) * gc.natural_gas_calorific_value)
    # else:
    #     comprehensive_energy_utilization = 0
    # eq_power_consumption_total = chp1_power_consumption_total + chp2_power_consumption_total + ashp1_power_consumption_total \
    #                              + ashp2_power_consumption_total + ashp3_power_consumption_total + ashp4_power_consumption_total \
    #                              + ese1_wp_power_consumption + ese2_wp_power_consumption + ese3_wp_power_consumption
    # if eq_power_consumption_total > 0:
    #     cop_real_time = (cold_heat_out_total - lb_heat_load) / eq_power_consumption_total
    # else:
    #     cop_real_time = 0
    # reduction_in_carbon_emissions = 0
    # reduction_in_sulfide_emissions = 0
    # reduction_in_nitride_emissions = 0
    # reduction_in_dust_emissions = 0
    # proportion_of_renewable_energy_power = 0
    # # 写入数据库
    #
    # # 写入能源站冷热电的输入输出功率数据
    # photovoltaic_electricity_out_total = 0
    # wind_electricity_out_total = 0
    # accumulator_electricity_out_total = 0
    # electricity_generation_total = ice1_electrical_power + ice2_electrical_power + photovoltaic_electricity_out_total + wind_electricity_out_total + accumulator_electricity_out_total
    # ice_electricity_out_total = ice1_electrical_power + ice2_electrical_power
    # buy_electricity_total = electricity_consume_total - electricity_generation_total
    # lb_cold_out_total = 0
    # lb_heat_out_total = lb1_cold_heat_out + lb2_cold_heat_out
    # lb_hot_water_out_total = lb1_hot_water_out + lb2_hot_water_out
    # ngb_hot_water_out_total = ngb3_hot_water_out
    # cc_cold_out_total = 0
    # chp_cold_out_total = 0
    # chp_heat_out_total = chp1_heat_out + chp2_heat_out
    # ashp_cold_out_total = 0
    # ese_cold_out_total = 0
    # ese_heat_out_total = ese_cold_heat_out
    # cold_out_total = lb_cold_out_total + cc_cold_out_total + chp_cold_out_total + ashp_cold_out_total + ese_cold_out_total
    # heat_out_total = lb_heat_out_total + chp_heat_out_total + ese_heat_out_total
    # # 写入数据库
    #
    #
    # # 写入能源站冷热电的收入成本数据
    # ice_income_total = ice1_electrical_income + ice2_electrical_income
    # lb_cold_income_total = lb1_cold_income + lb2_cold_income
    # lb_heat_income_total = lb1_heat_income + lb2_heat_income
    # lb_hot_water_income_total = lb1_hot_water_income + lb2_hot_water_income
    # cc_cold_income_total = 0
    # chp_cold_income_total = 0
    # chp_heat_income_total = chp1_income + chp2_income
    # ashp_cold_income_total = ashp1_cold_income + ashp2_cold_income + ashp3_cold_income + ashp4_cold_income
    # ngb_hot_water_income_total = ngb3_income
    # photovoltaic_income_total = photovoltaic_electricity_out_total * gc.sale_electricity_price
    # wind_income_total = wind_electricity_out_total * gc.sale_electricity_price
    # ice_cost_total = ice1_electrical_cost + ice2_electrical_cost
    # lb_cold_cost_total = lb1_cold_cost + lb2_cold_cost
    # lb_heat_cost_total = lb1_heat_cost + lb2_heat_cost
    # lb_hot_water_cost_total = lb1_hot_water_cost + lb2_hot_water_cost
    # cc_cold_cost_total = 0
    # chp_cold_cost_total = 0
    # chp_heat_cost_total = chp1_cost + chp2_cost
    # ashp_cold_cost_total = ashp1_cold_cost + ashp2_cold_cost + ashp3_cold_cost + ashp4_cold_cost
    # ashp_heat_cost_total = ashp1_heat_cost + ashp2_heat_cost + ashp3_heat_cost + ashp4_heat_cost
    # ngb_hot_water_cost_total = ngb3_cost
    # # 写入数据库
    #
    #
    # # 写入设备效率数据
    # ice_electrical_efficiency = max(ice1_electrical_efficiency, ice2_electrical_efficiency)
    # lb_cold_efficiency = max(lb1_cold_cop, lb2_cold_cop)
    # lb_heat_efficiency = max(lb1_heat_cop, lb2_heat_cop)
    # lb_hot_water_efficiency = max(lb1_hot_water_cop, lb2_hot_water_cop)
    # cc_cold_cop = 0
    # chp_cold_cop = 0
    # chp_heat_cop = max(chp1_cop, chp2_cop)
    # ashp_cold_cop = max(ashp1_cold_cop, ashp2_cold_cop, ashp3_cold_cop, ashp4_cold_cop)
    # ashp_heat_cop = max(ashp1_heat_cop, ashp2_heat_cop, ashp3_heat_cop, ashp4_heat_cop)
    # ngb_hot_water_efficiency = ngb3_efficiency
    # photovoltaic_electrical_efficiency = 0
    # wind_electrical_efficiency = 0
    # # 写入数据库
    #
    #
    # # 写入设备冷冻水出水温度和冷水生活热水总流量数据
    # chilled_water_supply_flow_total = 0
    # chilled_water_supply_temperature = 0
    # chilled_water_return_temperature = 0
    # heat_water_supply_flow_total = lb1_chilled_heat_water_flow + lb2_chilled_heat_water_flow + chp1_heat_water_flow + chp2_heat_water_flow \
    #                                + ese1_chilled_heat_water_flow + ese2_chilled_heat_water_flow + ese3_chilled_heat_water_flow
    # heat_water_supply_temperature = heating_water_temperature
    # heat_water_return_temperature = heating_water_temperature - gc.heating_water_temperature_difference_rated
    # hot_water_supply_flow_total = lb1_hot_water_flow + lb2_hot_water_flow + ngb3_hot_water_flow
    # hot_water_supply_temperature = gc.hot_water_temperature
    # hot_water_return_temperature = gc.hot_water_temperature - gc.hot_water_temperature_difference_rated
    # if lb1_cold_heat_out > 0:
    #     lb1_heat_chilled_water_supply_temperature = heating_water_temperature
    # else:
    #     lb1_heat_chilled_water_supply_temperature = 0
    # if lb1_hot_water_out > 0:
    #     lb1_hot_water_supply_temperature = gc.hot_water_temperature
    # else:
    #     lb1_hot_water_supply_temperature = 0
    # if lb2_cold_heat_out > 0:
    #     lb2_heat_chilled_water_supply_temperature = heating_water_temperature
    # else:
    #     lb2_heat_chilled_water_supply_temperature = 0
    # if lb2_hot_water_out > 0:
    #     lb2_hot_water_supply_temperature = gc.hot_water_temperature
    # else:
    #     lb2_hot_water_supply_temperature = 0
    # if ngb3_hot_water_out > 0:
    #     ngb3_hot_water_supply_temperature = gc.hot_water_temperature
    # else:
    #     ngb3_hot_water_supply_temperature = 0
    # cc1_chilled_water_supply_temperature = 0
    # cc2_chilled_water_supply_temperature = 0
    # cc3_chilled_water_supply_temperature = 0
    # cc4_chilled_water_supply_temperature = 0
    # if chp1_heat_out > 0:
    #     chp1_heat_water_supply_temperature = heating_water_temperature
    # else:
    #     chp1_heat_water_supply_temperature = 0
    # if chp2_heat_out > 0:
    #     chp2_heat_water_supply_temperature = heating_water_temperature
    # else:
    #     chp2_heat_water_supply_temperature = 0
    # if ashp1_heat_out > 0:
    #     ashp1_water_supply_temperature = ashp_heat_source_water_temperature
    # else:
    #     ashp1_water_supply_temperature = 0
    # if ashp2_heat_out > 0:
    #     ashp2_water_supply_temperature = ashp_heat_source_water_temperature
    # else:
    #     ashp2_water_supply_temperature = 0
    # if ashp3_heat_out > 0:
    #     ashp3_water_supply_temperature = ashp_heat_source_water_temperature
    # else:
    #     ashp3_water_supply_temperature = 0
    # if ashp4_heat_out > 0:
    #     ashp4_water_supply_temperature = ashp_heat_source_water_temperature
    # else:
    #     ashp4_water_supply_temperature = 0
    # if ese_heat_out_total > 0:
    #     ese_water_supply_temperature = heating_water_temperature
    # else:
    #     ese_water_supply_temperature = 0
    # # 写入数据库
    #
    #
    # # 写入设备运行状态
    # cc1_cold_state = False
    # cc1_stop_state = True
    # cc1_fault_state = False
    # cc2_cold_state = False
    # cc2_stop_state = True
    # cc2_fault_state = False
    # photovoltaic_start_state = False
    # photovoltaic_stop_state = True
    # photovoltaic_fault_state = False
    # wind_start_state = False
    # wind_stop_state = True
    # wind_fault_state = False
    # cdz_start_state = False
    # cdz_stop_state = True
    # cdz_fault_state = False
    # accumulator_electricity_out_state = False
    # accumulator_electricity_in_state = False
    # accumulator_stop_state = True
    # accumulator_fault_state = False
    # lamp_start_state = False
    # lamp_stop_state = True
    # lamp_fault_state = False
    # # 写入数据库
