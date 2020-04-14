import math
import datetime
from equipment import Centrifugal_Chiller, Internal_Combustion_Engine, Water_Pump, Natural_Gas_Boiler_hot_water, Energy_Storage_Equipment_Cold
from centrifugal_chiller_function import centrifugal_chiller_function as ccf, centrifugal_chiller_result as ccr
from triple_supply_function import triple_supply_cold_function as tscf
from natural_gas_boiler_funtion import natural_gas_boiler_in_out_hot_water as ngbiohw
from energy_storage_equipment_cold_function import energy_storage_equipment_cold_function as esecf, energy_storage_equipment_cold_result as esecr, energy_storage_equipment_cold_storage_residual_write as esecsrw, energy_storage_equipment_cold_storage_residual_read as esecsrr

def cooling_season_function(cold_load, hot_water_load, electricity_load, gc):
    """制冷季计算"""

    print("正在进行制冷季计算.........")

    # 实例化两个内燃机对象
    ice1 = Internal_Combustion_Engine(792, gc, 0.5)
    ice2 = Internal_Combustion_Engine(792, gc, 0.5)
    # 实例化4个离心式冷水机的各种水泵（离心式热泵的制冷工况采用离心式冷水机的计算模型）
    cc_wp = False
    cc1_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc2_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc3_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc4_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc1_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc2_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc3_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc4_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    # 实例化4个离心式冷水机类（离心式热泵的制冷工况采用离心式冷水机的计算模型）
    cc1 = Centrifugal_Chiller(3164, 0.2, False, cc1_wp_chilled_water, cc1_wp_cooling_water, gc)
    cc2 = Centrifugal_Chiller(3164, 0.2, False, cc2_wp_chilled_water, cc2_wp_cooling_water, gc)
    cc3 = Centrifugal_Chiller(3164, 0.2, False, cc3_wp_chilled_water, cc3_wp_cooling_water, gc)
    cc4 = Centrifugal_Chiller(3164, 0.2, False, cc4_wp_chilled_water, cc4_wp_cooling_water, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个冷却水泵，2个冷冻水泵，2个生活热水水泵
    lb1_wp_cooling_water = Water_Pump(335, False, gc)
    lb2_wp_cooling_water = Water_Pump(335, False, gc)
    lb1_wp_chilled_water = Water_Pump(170, False, gc)
    lb2_wp_chilled_water = Water_Pump(170, False, gc)
    # 实例化1组3个蓄冷水罐的循环水泵（水泵3用1备）
    esec1_wp_chilled_water = Water_Pump(50, False, gc)
    esec2_wp_chilled_water = Water_Pump(50, False, gc)
    esec3_wp_chilled_water = Water_Pump(50, False, gc)
    # 实例化3个蓄冷水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    esec1 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec1_wp_chilled_water, gc)
    esec2 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec2_wp_chilled_water, gc)
    esec3 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec3_wp_chilled_water, gc)

    # 如果是母管制系统
    if gc.header_system == True:
        lb1_wp_hot_water = Water_Pump(44, False, gc)
        lb2_wp_hot_water = Water_Pump(44, False, gc)
        # 实例化天然气生活热水锅炉用到的水泵
        ngb_wp_hot_water = Water_Pump(44, False, gc)
    else:
        lb1_wp_hot_water = Water_Pump(44, False, gc)
        lb2_wp_hot_water = Water_Pump(44, False, gc)
        # 实例化天然气生活热水锅炉用到的水泵
        ngb_wp_hot_water = Water_Pump(170, False, gc)

    # 实例化生活热水锅炉
    ngb_hot_water = Natural_Gas_Boiler_hot_water(2800, 0.2, ngb_wp_hot_water, gc)

    # 如果是母管制系统
    if gc.header_system == True:
        ans_csc = cooling_season_header_system(cold_load, hot_water_load, electricity_load, ice1, ice2, cc1, cc2, cc3, cc4, esec1, esec2, esec3, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water, ngb_hot_water, gc)
    else:
        ans_csc = cooling_season_unit_system(cold_load, hot_water_load, electricity_load, ice1, ice2, cc1, cc2, cc3, cc4, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water, ngb_hot_water, gc)

    # 读取计算结果
    profits = ans_csc[0]
    income = ans_csc[1]
    cost = ans_csc[2]
    station_cold_out_all = ans_csc[3]
    station_electricity_out_all = ans_csc[4]
    ice1_load_ratio_result = ans_csc[5]
    ice2_load_ratio_result = ans_csc[6]
    cc1_load_ratio_result = ans_csc[7]
    cc2_load_ratio_result = ans_csc[8]
    cc3_load_ratio_result = ans_csc[9]
    cc4_load_ratio_result = ans_csc[10]
    lb_cold_load_result = ans_csc[11]
    lb_hot_water_result = ans_csc[12]
    ngb_hw_hot_water_result = ans_csc[13]
    esec1_load_ratio = ans_csc[14]
    esec2_load_ratio = ans_csc[15]
    esec3_load_ratio = ans_csc[16]
    esec_cold_load_out = ans_csc[17]

    #返回计算结果
    return profits, income, cost, station_cold_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, lb_cold_load_result, lb_hot_water_result, ngb_hw_hot_water_result, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec_cold_load_out


def cooling_season_header_system(cold_load, hot_water_load, electricity_load, ice1, ice2, cc1, cc2, cc3, cc4, esec1, esec2, esec3, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """母管制系统，制冷季计算"""
    # 制冷设备的总制冷功率（不包括溴化锂）
    eq_cooling_power_rated_sum = cc1.cooling_power_rated + cc2.cooling_power_rated + cc3.cooling_power_rated + cc4.cooling_power_rated
    # 生活热水总流量
    hot_water_flow_total = hot_water_load * 3600/gc.hot_water_temperature_difference_rated/4.2/1000
    # 生活热水泵启动数量，向上取整，每个泵额定流量44t/h
    hw_wp_num = math.ceil(hot_water_flow_total/44)
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
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_cooling_season == True:# 制冷季溴化锂设备参与供生活热水
        # 溴化锂1、2的生活热水负荷最大值
        lb1_hot_water_max = gc.lb1_hot_water_max
        lb2_hot_water_max = gc.lb2_hot_water_max
        # 溴化锂设备生活热水计算步长
        lb1_hot_water_step = gc.lb1_hot_water_step
        # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
        if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
        elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
        else:  # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
            lb_hot_water_max = hot_water_load
    else:# 制冷季溴化锂设备不参与供生活热水
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
    if cold_load - min(gc.lb1_cold_max, gc.lb2_cold_max) > eq_cooling_power_rated_sum and cold_load - gc.lb1_cold_max- gc.lb2_cold_max <= eq_cooling_power_rated_sum:
        ice_num_a = 2
    elif cold_load > eq_cooling_power_rated_sum and cold_load - min(gc.lb1_cold_max, gc.lb2_cold_max) <= eq_cooling_power_rated_sum:
        ice_num_a = 1
    else:
        ice_num_a = 0

    # 根据目前所处的用电时间段，重新修正内燃机可以启动的最大数量和内燃机启动数量初始值
    now = datetime.datetime.now() # 获取当前的时间
    now_hour = now.hour # 当前的小时
    # 根据预设的非谷电时间段列表，判断目前处于什么时间段
    hour_state = 0 #用于判断目前是否处于非谷电时间段的判断因子，0表示处于谷电时间段，1表示不处于谷电时间段
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
    # 读取目前水罐剩余的蓄冷量
    esec1_cold_stock = esecsrr()[0]
    esec2_cold_stock = esecsrr()[1]
    esec3_cold_stock = esecsrr()[2]
    esec_cold_stock_sum = esec1_cold_stock + esec2_cold_stock +esec3_cold_stock
    # 3个水罐的额定蓄冷量总和
    esec_cooling_storage_rated_sum = esec1.cooling_storage_rated + esec2.cooling_storage_rated + esec3.cooling_storage_rated
    # 因为计算周期是1小时，因此蓄冷量(kWh)可以直接用于冷负荷(kW)的计算，两者数值相同
    if hour_state == 1:
        # 供冷状态(正值)
        if esec_cold_stock_sum >= cold_load:
            # 如果蓄冷水罐剩余量大于等于冷负荷需求量，则蓄冷水罐提供的冷负荷等于冷负荷需求量
            cold_load_esec = cold_load
        else:
            cold_load_esec = esec_cold_stock_sum
    else:
        # 蓄冷状态(负值)
        # 如果制冷设备总功率减去冷负荷需求量大于0，则表示可以有设备蓄冷
        if eq_cooling_power_rated_sum - cold_load > 0:
            if eq_cooling_power_rated_sum - cold_load >= esec_cooling_storage_rated_sum:
                cold_load_esec = -esec_cooling_storage_rated_sum
            else:
                cold_load_esec = -(eq_cooling_power_rated_sum - cold_load)
        else:
            cold_load_esec = 0

    # 蓄冷装置负荷为0时不进行蓄冷装置计算
    if cold_load_esec == 0:
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
        ans_esec_a = esecf(cold_load_esec, esec1, esec2, esec3, gc) # 所有的可能解
        ans_esec = esecr(ans_esec_a, esec1, esec2, esec3) # 选出蓄能设备最优解
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
        # 2台内燃机系统的负荷率
        ice_load_ratio_result_all = [0, 0]
        # 列表，储存4台设备计算出的负荷率结果
        cc_load_ratio_result_all = [0, 0, 0, 0]
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
                ts_cold_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                # 三联供系统的电出力
                # 计算三联供系统电出力
                ts_electricity_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                # 离心式冷水机需要补充的冷负荷
                cold_load_centrifugal_chiller = cold_load - ts_cold_out_total
                # 如果此时只有内燃机，且内燃机负荷率和设定的冷负荷相差很小，则跳出循环
                if cold_load_centrifugal_chiller >= 0 and abs(cold_load_centrifugal_chiller) <= gc.project_load_error:
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
                if cold_load_centrifugal_chiller >= 0 and cc_calculate == True:
                    # 计算离心式冷水机的运行策略
                    ans_cc = ccf(cold_load_centrifugal_chiller, cc1, cc2, cc3, cc4, gc)
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
                # 此时整个能源站的向外供电功率
                station_electricity_out_total = ts_electricity_out_total - cc_power_consumption_total - hw_wp_power_consumption - esec_power_consumption_total
                # 此时能源站供冷总功率
                station_cold_out_total = ts_cold_out_total + cc_cold_out_total + esec_cold_load_out
                # 如果仅有溴化锂供冷，且制冷量大于冷负荷需求量，则内燃机负荷往下减，内燃机1、2同时下降
                if cold_load_centrifugal_chiller <= 0 and station_cold_out_total > cold_load and ts_cold_out_total > 0:
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
                    income_cold = cold_load * gc.cooling_price
                    # 生活热水收入
                    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                    income_hot_water = hot_water_load_total * gc.hot_water_price
                    # 三联供系统总成本（天然气+补水）
                    cost_ts = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2,lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water,lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                    # 冷水机补水总成本
                    cost_cc_water_supply = cc_water_supply_total * gc.water_price
                    # 天然气热水锅炉天然气成本
                    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                    # 天然气热水锅炉补水成本计算
                    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                    # 总收入成本利润
                    income_total = income_cold + income_electricity + income_hot_water
                    cost_total = cost_electricity + cost_cc_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply + cost_esec_water_supply
                    profits_total = income_total - cost_total
                    income.append(income_total)
                    cost.append(cost_total)
                    profits.append(profits_total)
                    # 如果内燃机1负荷率已经等于0，则跳出循环
                    if ice1_load_ratio == 0:
                        break
                    elif cold_load_centrifugal_chiller <= 0 and cc_calculate == False:
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
            if ice_num == 0 :
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
    esecsrw(hour_state, esec1, esec2, esec3, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec1_cold_stock, esec2_cold_stock, esec3_cold_stock)

    # 返回计算结果
    return profits, income, cost, station_cold_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, lb_cold_load_result, lb_hot_water_result, ngb_hw_hot_water_result, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec_cold_load_out


def cooling_season_unit_system(cold_load, hot_water_load, electricity_load, ice1, ice2, cc1, cc2, cc3, cc4, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """单元制系统，制冷季计算"""
    # 设备负荷率调节步长，百分之几
    ice1_step = 5
    ice2_step = 5
    # 迭代计算中内燃机负荷率可以循环到的最小值
    if cc1.cooling_power_rated + cc2.cooling_power_rated + cc3.cooling_power_rated + cc4.cooling_power_rated <= cold_load:
        ice1_load_ratio_min = 1
        ice2_load_ratio_min = 1
    else:
        ice1_load_ratio_min = 0
        ice2_load_ratio_min = 0
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
    # 列表，储存4台离心式冷水机组设备计算出的负荷率结果
    cc1_load_ratio_result = []
    cc2_load_ratio_result = []
    cc3_load_ratio_result = []
    cc4_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_cooling_season == True:
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
        lb2_hot_water_max = 0
        lb_hot_water_max = 0
        # 步长不能为0，否则无限循环
        lb1_hot_water_step = gc.project_load_error
        lb2_hot_water_step = gc.project_load_error

    # 溴化锂设备制备生活热水总量的初始值
    lb1_hot_water = 0
    lb2_hot_water = 0
    # 溴化锂设备生活热水总产量初始值
    lb_hot_water_total = 0

    while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
        while lb2_hot_water <= lb2_hot_water_max and lb2_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
            # 天然气生活热水锅炉需要补充的生活热水量
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，辅机设备耗电量
            ngb_hw_power_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[0]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 重置内燃机、冷水机设备负荷率
            ice1_load_ratio = 1
            ice2_load_ratio = 1
            cc1_load_ratio = cc1.load_min
            cc2_load_ratio = cc2.load_min
            cc3_load_ratio = cc3.load_min
            cc4_load_ratio = cc4.load_min
            # 2台内燃机系统的负荷率
            ice_load_ratio_result_all = [0, 0]
            # 列表，储存4台设备计算出的负荷率结果
            cc_load_ratio_result_all = [0, 0, 0, 0]
            # 离心式冷水机耗电总功率，制冷总功率、补水量默认值
            cc_power_consumption_total = 0
            cc_cold_out_total = 0
            cc_water_supply_total = 0
            # 电收入成本默认值
            income_electricity = 0
            cost_electricity = 0
            # 改变内燃机负荷率
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                while ice2_load_ratio >= ice2_load_ratio_min and ice2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                    # 内燃机+溴化锂+离心式冷水机运行状态计算
                    # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                    if ice1_load_ratio < ice1.load_min:
                        ice1_load_ratio = 0
                    # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                    if ice2_load_ratio < ice2.load_min:
                        ice2_load_ratio = 0
                    # 计算三联供系统冷出力
                    ts_cold_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                    # 三联供系统的电出力
                    # 计算三联供系统电出力
                    ts_electricity_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                    # 离心式冷水机需要补充的冷负荷
                    cold_load_centrifugal_chiller = cold_load - ts_cold_out_total
                    # 如果此时只有内燃机，且内燃机负荷率和设定的冷负荷相差很小，则跳出循环
                    if cold_load_centrifugal_chiller >= 0 and abs(cold_load_centrifugal_chiller) <= gc.project_load_error:
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
                    if cold_load_centrifugal_chiller >= 0 and cc_calculate == True:
                        # 计算离心式冷水机的运行策略
                        ans_cc = ccf(cold_load_centrifugal_chiller, cc1, cc2, cc3, cc4, gc)
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
                    # 此时整个能源站的向外供电功率
                    station_electricity_out_total = ts_electricity_out_total - cc_power_consumption_total - ngb_hw_power_consumption
                    # 此时能源站供冷总功率
                    station_cold_out_total = ts_cold_out_total + cc_cold_out_total
                    # 如果仅有溴化锂供冷，且制冷量大于冷负荷需求量，则内燃机负荷往下减
                    if cold_load_centrifugal_chiller <= 0 and station_cold_out_total > cold_load and ts_cold_out_total > 0:
                        # 减小内燃机设备2负荷率
                        ice2_load_ratio -= ice2_step / 100
                    # 如果能源站向外供电量大于电负荷需求量，则内燃机负荷往下减
                    elif station_electricity_out_total > electricity_load and ts_cold_out_total > 0 + gc.project_load_error:
                        # 减小内燃机设备2负荷率
                        ice2_load_ratio -= ice2_step / 100
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
                        # （用冷负荷计算，能源站供冷量比冷负荷多的部分不计算）
                        income_cold = cold_load * gc.cooling_price
                        # 生活热水收入
                        hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                        income_hot_water = hot_water_load_total * gc.hot_water_price
                        # 三联供系统总成本（天然气+补水）
                        cost_ts = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                        # 冷水机补水总成本
                        cost_cc_water_supply = cc_water_supply_total * gc.water_price
                        # 天然气热水锅炉天然气成本
                        cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                        # 天然气热水锅炉补水成本计算
                        cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                        # 总收入成本利润
                        income_total = income_cold + income_electricity + income_hot_water
                        cost_total = cost_electricity + cost_cc_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
                        profits_total = income_total - cost_total
                        income.append(income_total)
                        cost.append(cost_total)
                        profits.append(profits_total)
                        # 如果内燃机2负荷率已经等于0，则跳出循环
                        if ice2_load_ratio == 0:
                            break
                        elif cold_load_centrifugal_chiller <= 0 and cc_calculate == False:
                            break
                        # 修改内燃机2负荷率
                        else:
                            ice2_load_ratio -= ice2_step / 100
                # 下降内燃机设备1负荷率，内燃机2负荷率重置
                ice1_load_ratio -= ice1_step / 100
                ice2_load_ratio = 1
            # 溴化锂2制备的生活热水量增加
            lb2_hot_water += lb2_hot_water_step
            # 溴化锂设备的总生活热水产量
            lb_hot_water_total = lb1_hot_water + lb2_hot_water
        # 溴化锂1制备的生活热水量增加，设备2重置回默认值
        lb1_hot_water += lb1_hot_water_step
        lb2_hot_water = 0
        # 溴化锂设备的总生活热水产量
        lb_hot_water_total = lb1_hot_water + lb2_hot_water

    # 返回计算结果
    return profits, income, cost, station_cold_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, lb_cold_load_result, lb_hot_water_result, ngb_hw_hot_water_result


def print_cooling_season(ans):
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

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(station_cost_min) + "\n"  + "能源站供冷功率为： " + str(station_cold_out_all) + "\n" + "蓄能装置冷负荷功率为： " + str(esec_cold_load_out) + "\n" + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(ice1_load_ratio) + "\n" + "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "离心式冷水机1负荷率为： " + str(cc1_load_ratio) + "\n" + "离心式冷水机2负荷率为： " + str(cc2_load_ratio) + "\n" + "离心式冷水机3负荷率为： " + str(cc3_load_ratio) + "\n" + "离心式冷水机4负荷率为： " + str(cc4_load_ratio) + "\n" + "溴化锂设备供冷功率为： " + str(lb_cold_load) + "\n" + "溴化锂供生活热水功率为： " + str(lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(ngb_hw_hot_water) + "\n" + "蓄能水罐水泵1负荷率： " + str(esec1_load_ratio) + "\n" + "蓄能水罐水泵2负荷率： " + str(esec2_load_ratio) + "\n" + "蓄能水罐水泵3负荷率： " + str(esec3_load_ratio) + "\n")


def test_csc_header_system(cold_load, hot_water_load, gc):
    """指定负荷率，测试母管制系统制冷季计算"""
    # 实例化两个内燃机对象
    ice1 = Internal_Combustion_Engine(792, gc, 0.5)
    ice2 = Internal_Combustion_Engine(792, gc, 0.5)
    # 实例化4个离心式冷水机的各种水泵
    cc_wp = False
    cc1_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc2_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc3_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc4_wp_chilled_water = Water_Pump(600, cc_wp, gc)
    cc1_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc2_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc3_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    cc4_wp_cooling_water = Water_Pump(710, cc_wp, gc)
    # 实例化4个离心式冷水机类
    cc1 = Centrifugal_Chiller(3164, 0.2, False, cc1_wp_chilled_water, cc1_wp_cooling_water, gc)
    cc2 = Centrifugal_Chiller(3164, 0.2, False, cc2_wp_chilled_water, cc2_wp_cooling_water, gc)
    cc3 = Centrifugal_Chiller(3164, 0.2, False, cc3_wp_chilled_water, cc3_wp_cooling_water, gc)
    cc4 = Centrifugal_Chiller(3164, 0.2, False, cc4_wp_chilled_water, cc4_wp_cooling_water, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个冷却水泵，2个冷冻水泵，2个生活热水水泵
    lb1_wp_cooling_water = Water_Pump(335, False, gc)
    lb2_wp_cooling_water = Water_Pump(335, False, gc)
    lb1_wp_chilled_water = Water_Pump(170, False, gc)
    lb2_wp_chilled_water = Water_Pump(170, False, gc)
    # 如果是母管制系统
    lb1_wp_hot_water = Water_Pump(44, False, gc)
    lb2_wp_hot_water = Water_Pump(44, False, gc)
    # 实例化天然气生活热水锅炉用到的水泵
    ngb_wp_hot_water = Water_Pump(44, False, gc)
    # 实例化1组3个蓄冷水罐的循环水泵（水泵3用1备）
    esec1_wp_chilled_water = Water_Pump(50, False, gc)
    esec2_wp_chilled_water = Water_Pump(50, False, gc)
    esec3_wp_chilled_water = Water_Pump(50, False, gc)
    # 实例化3个蓄冷水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    esec1 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec1_wp_chilled_water, gc)
    esec2 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec2_wp_chilled_water, gc)
    esec3 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec3_wp_chilled_water, gc)

    # 实例化生活热水锅炉
    ngb_hot_water = Natural_Gas_Boiler_hot_water(2800, 0.2, ngb_wp_hot_water, gc)

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

    # 设定内燃机负荷率，内燃机制备生活热水功率
    ice1_load_ratio = 0.5
    ice2_load_ratio = 0.5
    lb1_hot_water = 0
    lb2_hot_water = 0
    lb_hot_water_total = lb1_hot_water + lb2_hot_water
    # 计算三联供系统冷出力
    ts_cold_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
    # 三联供系统的电出力
    # 计算三联供系统电出力
    ts_electricity_out_total = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
    # 离心式冷水机需要补充的冷负荷
    cold_load_centrifugal_chiller = cold_load - ts_cold_out_total
    # 计算离心式冷水机的运行策略
    ans_cc = ccf(cold_load_centrifugal_chiller, cc1, cc2, cc3, cc4, gc)
    # 读取此时的冷水机最优计算结果耗电功率
    cc_power_consumption_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[5]
    # 冷水机补水总量
    cc_water_supply_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[6]
    # 此时整个能源站的向外供电功率
    station_electricity_out_total = ts_electricity_out_total - cc_power_consumption_total - hw_wp_power_consumption

    # 天然气生活热水锅炉需要补充的生活热水量
    ngb_hot_water_load = hot_water_load - lb_hot_water_total
    # 天然气热水锅炉天然气消耗量
    ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
    # 天然气生活热水锅炉，补水量计算
    ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]

    # 供电收入或者买电成本（大于0是收入，小于0是成本）
    if station_electricity_out_total > 0:
        income_electricity = station_electricity_out_total * gc.sale_electricity_price
        cost_electricity = 0
    else:
        cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
        income_electricity = 0
    # 供冷收入（用冷负荷计算，能源站供冷量比冷负荷多的部分不计算）
    income_cold = cold_load * gc.cooling_price
    # 生活热水收入
    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
    income_hot_water = hot_water_load_total * gc.hot_water_price
    # 三联供系统总成本（天然气+补水）
    cost_ts = tscf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
    # 冷水机补水总成本
    cost_cc_water_supply = cc_water_supply_total * gc.water_price
    # 天然气热水锅炉天然气成本
    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
    # 天然气热水锅炉补水成本计算
    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
    # 总收入成本利润
    income_total = income_cold + income_electricity + income_hot_water
    cost_total = cost_electricity + cost_cc_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
    profits_total = income_total - cost_total

    print(income_total, cost_total, profits_total)

#test_csc_header_system()