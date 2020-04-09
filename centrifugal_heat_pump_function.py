import math
from equipment import Centrifugal_Heat_Pump, Water_Pump
from global_constant import Global_Constant

def centrifugal_heat_pump_function_heat(heat_load, chp1, chp2, chp3, chp4, gc):
    """离心式热泵制热负荷计算函数"""
    # 制热，制热，制热
    # 离心式热泵组与水泵的布置方式，header_system（母管制）
    if gc.header_system == True:
        ans = centrifugal_heat_pump_header_system_heat(heat_load, chp1, chp2, chp3, chp4, gc)
    else:
        ans = centrifugal_heat_pump_unit_system_heat(heat_load, chp1, chp2, chp3, chp4, gc)

    # 读取计算结果
    cost = ans[0]
    chp1_load_ratio_result = ans[1]
    chp2_load_ratio_result = ans[2]
    chp3_load_ratio_result = ans[3]
    chp4_load_ratio_result = ans[4]
    total_power_consumption = ans[5]
    total_water_supply = ans[6]

    # 返回计算结果
    return cost, chp1_load_ratio_result, chp2_load_ratio_result, chp3_load_ratio_result, chp4_load_ratio_result, total_power_consumption, total_water_supply


def centrifugal_heat_pump_header_system_heat(heat_load, chp1, chp2, chp3, chp4, gc):
    """不同管道布置方式的离心式热泵计算"""
    # 母管制系统计算（水泵与离心式热泵组不是一对一布置）
    # 获取4台离心式热泵是否为变频，根据是否为变频，设置不同的计算步长
    # 离心式热泵1
    if chp1.frequency_scaling == True:
        chp1_step = 1
    else:
        chp1_step = 10
    # 离心式热泵2
    if chp2.frequency_scaling == True:
        chp2_step = 1
    else:
        chp2_step = 10
    # 离心式热泵3
    if chp3.frequency_scaling == True:
        chp3_step = 1
    else:
        chp3_step = 10
    # 离心式热泵4
    if chp4.frequency_scaling == True:
        chp4_step = 1
    else:
        chp4_step = 10

    # 列表，储存4台设备计算出的负荷率结果
    chp_load_ratio_result_all = [0, 0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台离心式热泵的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台离心式热泵的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    chp1_load_ratio_result = []
    chp2_load_ratio_result = []
    chp3_load_ratio_result = []
    chp4_load_ratio_result = []

    # 确定需要几台设备，向上取整（离心式热泵可以启动的最大数量）
    chp_num_max_2 = math.ceil(heat_load / chp1.heating_power_rated)
    # 如果恰好整除，则向上加1
    if chp_num_max_2 ==int(chp_num_max_2):
        chp_num_max_1 = chp_num_max_2 + 1
    else:
        chp_num_max_1 = chp_num_max_2
    # 最大数量不可以超过4
    if chp_num_max_1 > 4:
        chp_num_max = 4
    else:
        chp_num_max = chp_num_max_1

    # 离心式热泵启动数量初始值
    chp_num = 1

    while chp_num <= chp_num_max:
        # 初始化设备1、2、3、4的负荷率
        if chp_num >= 1:
            chp1_load_ratio = chp1.load_min
        else:
            chp1_load_ratio = 0
        if chp_num >= 2:
            chp2_load_ratio = chp2.load_min
        else:
            chp2_load_ratio = 0
        if chp_num >= 3:
            chp3_load_ratio = chp3.load_min
        else:
            chp3_load_ratio = 0
        if chp_num >= 4:
            chp4_load_ratio = chp4.load_min
        else:
            chp4_load_ratio = 0
        # 计算离心式热泵设备
        while chp1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算4个设备的制热出力
            chp1_heat_out_now = chp1_load_ratio * chp1.heating_power_rated
            chp2_heat_out_now = chp2_load_ratio * chp2.heating_power_rated
            chp3_heat_out_now = chp3_load_ratio * chp3.heating_power_rated
            chp4_heat_out_now = chp4_load_ratio * chp4.heating_power_rated
            chp_heat_out_now_sum = chp1_heat_out_now + chp2_heat_out_now + chp3_heat_out_now + chp4_heat_out_now
            print(chp_num, chp1_heat_out_now, chp2_heat_out_now, chp3_heat_out_now, chp4_heat_out_now)
            if chp_heat_out_now_sum < heat_load:
                # 增加设备1、2、3、4负荷率
                if chp_num >= 1:
                    chp1_load_ratio += chp1_step / 100
                else:
                    chp1_load_ratio = 0
                if chp_num >= 2:
                    chp2_load_ratio += chp2_step / 100
                else:
                    chp2_load_ratio = 0
                if chp_num >= 3:
                    chp3_load_ratio += chp3_step / 100
                else:
                    chp3_load_ratio = 0
                if chp_num >= 4:
                    chp4_load_ratio += chp4_step / 100
                else:
                    chp4_load_ratio = 0
            else:
                # 保存4个设备的负荷率
                chp_load_ratio_result_all[0] = chp1_load_ratio
                chp_load_ratio_result_all[1] = chp2_load_ratio
                chp_load_ratio_result_all[2] = chp3_load_ratio
                chp_load_ratio_result_all[3] = chp4_load_ratio
                chp1_load_ratio_result.append(chp_load_ratio_result_all[0])
                chp2_load_ratio_result.append(chp_load_ratio_result_all[1])
                chp3_load_ratio_result.append(chp_load_ratio_result_all[2])
                chp4_load_ratio_result.append(chp_load_ratio_result_all[3])
                # 计算4个设备本体的总耗电功率（仅设备本体耗电）
                chp1_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[3]
                chp2_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[3]
                chp3_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[3]
                chp4_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[3]
                # 计算4个设备的采暖水流量、低温热源水流量
                # 采暖水和低温热源水总流量
                heating_water_flow_total = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[4]
                heat_source_water_flow_total = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[5]
                # 每个水泵的流量为总流量均分（后期可细化流量分配比例）
                chp1_heating_water_flow = heating_water_flow_total / chp_num
                chp2_heating_water_flow = heating_water_flow_total / chp_num
                chp3_heating_water_flow = heating_water_flow_total / chp_num
                chp4_heating_water_flow = heating_water_flow_total / chp_num
                chp1_heat_source_water_flow = heat_source_water_flow_total / chp_num
                chp2_heat_source_water_flow = heat_source_water_flow_total / chp_num
                chp3_heat_source_water_flow = heat_source_water_flow_total / chp_num
                chp4_heat_source_water_flow = heat_source_water_flow_total / chp_num
                # 辅助设备耗电功率
                chp1_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chp1, gc, chp1_heating_water_flow, chp1_heat_source_water_flow)[0]
                chp2_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chp2, gc, chp2_heating_water_flow, chp2_heat_source_water_flow)[0]
                chp3_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chp3, gc, chp3_heating_water_flow, chp3_heat_source_water_flow)[0]
                chp4_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chp4, gc, chp4_heating_water_flow, chp4_heat_source_water_flow)[0]
                # 耗电量总计
                chp_power_consumption_total = chp1_centrifugal_heat_pump_power_consumption + chp2_centrifugal_heat_pump_power_consumption + chp3_centrifugal_heat_pump_power_consumption + chp4_centrifugal_heat_pump_power_consumption + chp1_auxiliary_equipment_power_consumption + chp2_auxiliary_equipment_power_consumption + chp3_auxiliary_equipment_power_consumption + chp4_auxiliary_equipment_power_consumption
                total_power_consumption.append(chp_power_consumption_total)
                # 计算4个设备的总补水量
                chp1_water_supply = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[2]
                chp2_water_supply = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[2]
                chp3_water_supply = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[2]
                chp4_water_supply = centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[2]
                chp_water_supply_total = chp1_water_supply + chp2_water_supply + chp3_water_supply + chp4_water_supply
                total_water_supply.append(chp_water_supply_total)
                # 计算4个设备的成本
                chp_cost_total = chp_power_consumption_total * gc.buy_electricity_price + chp_water_supply_total * gc.water_price
                cost.append(chp_cost_total)
                break
        # 增加离心式热泵数量
        chp_num += 1

    # 返回计算结果
    return cost, chp1_load_ratio_result, chp2_load_ratio_result, chp3_load_ratio_result, chp4_load_ratio_result, total_power_consumption, total_water_supply


def centrifugal_heat_pump_unit_system_heat(heat_load, chp1, chp2, chp3, chp4, gc):
    """不同管道布置方式的离心式热泵计算"""
    # 单元制系统计算（水泵与离心式热泵组一对一布置）
    # 获取4台离心式热泵是否为变频，根据是否为变频，设置不同的计算步长
    # 离心式热泵1
    if chp1.frequency_scaling == True:
        chp1_step = 1
    else:
        chp1_step = 10
    # 离心式热泵2
    if chp2.frequency_scaling == True:
        chp2_step = 1
    else:
        chp2_step = 10
    # 离心式热泵3
    if chp3.frequency_scaling == True:
        chp3_step = 1
    else:
        chp3_step = 10
    # 离心式热泵4
    if chp4.frequency_scaling == True:
        chp4_step = 1
    else:
        chp4_step = 10

    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台离心式热泵的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台离心式热泵的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    chp1_load_ratio_result = []
    chp2_load_ratio_result = []
    chp3_load_ratio_result = []
    chp4_load_ratio_result = []

    # 确定需要几台设备，向上取整
    centrifugal_heat_pump_num_1 = math.ceil(heat_load / chp1.heating_power_rated)
    centrifugal_heat_pump_num = min(centrifugal_heat_pump_num_1, 4) #但是最大数量不可以大于4

    # 列表，储存4台设备计算出的负荷率结果
    chp_load_ratio_result_all = [0, 0, 0, 0]
    # 初始化设备1的负荷率,设备负荷率不可以小于设定的最小值，变量用处储存计算过程中4台设备的实时负荷率
    chp1_load_ratio = chp1.load_min

    if centrifugal_heat_pump_num == 1:
        while chp1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算设备的制热出力
            chp1_heat_out_now = chp1_load_ratio * chp1.heating_power_rated
            chp_heat_out_now_sum = chp1_heat_out_now
            if chp_heat_out_now_sum < heat_load:
                # 增加设备1负荷率
                chp1_load_ratio += chp1_step / 100
            else:
                # 保存4个设备的负荷率
                chp_load_ratio_result_all[0] = chp1_load_ratio
                chp1_load_ratio_result.append(chp_load_ratio_result_all[0])
                chp2_load_ratio_result.append(0)
                chp3_load_ratio_result.append(0)
                chp4_load_ratio_result.append(0)
                # 计算1个设备的总耗电功率
                chp1_power_consumption = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[1]
                chp_power_consumption_total = chp1_power_consumption
                total_power_consumption.append(chp_power_consumption_total)
                # 计算1个设备的总补水量
                chp1_water_supply = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[2]
                chp_water_supply_total = chp1_water_supply
                total_water_supply.append(chp_water_supply_total)
                # 计算1个设备的成本
                chp1_cost = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[0]
                chp_cost_total = chp1_cost
                cost.append(chp_cost_total)
                break

    # 列表，储存4台设备计算出的负荷率结果
    chp_load_ratio_result_all = [0, 0, 0, 0]
    # 初始化设备1、2、3、4的负荷率,设备负荷率不可以小于设定的最小值，变量用处储存计算过程中4太设备的实时负荷率
    chp1_load_ratio = chp1.load_min
    chp2_load_ratio = chp2.load_min

    if centrifugal_heat_pump_num == 1 or centrifugal_heat_pump_num == 2:
        while chp1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            while chp2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                # 计算2个设备的制热出力
                chp1_heat_out_now = chp1_load_ratio * chp1.heating_power_rated
                chp2_heat_out_now = chp2_load_ratio * chp2.heating_power_rated
                chp_heat_out_now_sum = chp1_heat_out_now + chp2_heat_out_now
                if chp_heat_out_now_sum < heat_load:
                    # 增加设备2负荷率
                    chp2_load_ratio += chp2_step / 100
                else:
                    # 保存4个设备的负荷率
                    chp_load_ratio_result_all[0] = chp1_load_ratio
                    chp_load_ratio_result_all[1] = chp2_load_ratio
                    chp1_load_ratio_result.append(chp_load_ratio_result_all[0])
                    chp2_load_ratio_result.append(chp_load_ratio_result_all[1])
                    chp3_load_ratio_result.append(0)
                    chp4_load_ratio_result.append(0)
                    # 计算2个设备的总耗电功率
                    chp1_power_consumption = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[1]
                    chp2_power_consumption = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[1]
                    chp_power_consumption_total = chp1_power_consumption + chp2_power_consumption
                    total_power_consumption.append(chp_power_consumption_total)
                    # 计算2个设备的总补水量
                    chp1_water_supply = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[2]
                    chp2_water_supply = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[2]
                    chp_water_supply_total = chp1_water_supply + chp2_water_supply
                    total_water_supply.append(chp_water_supply_total)
                    # 计算2个设备的成本
                    chp1_cost = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[0]
                    chp2_cost = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[0]
                    chp_cost_total = chp1_cost + chp2_cost
                    cost.append(chp_cost_total)
                    break
            # 增加设备1负荷率，并将设备2负荷率重置回最小值
            chp1_load_ratio += chp1_step / 100
            chp2_load_ratio = chp2.load_min

    # 列表，储存4台设备计算出的负荷率结果
    chp_load_ratio_result_all = [0, 0, 0, 0]
    # 初始化设备1、2、3、4的负荷率,设备负荷率不可以小于设定的最小值，变量用处储存计算过程中4太设备的实时负荷率
    chp1_load_ratio = chp1.load_min
    chp2_load_ratio = chp2.load_min
    chp3_load_ratio = chp3.load_min

    if centrifugal_heat_pump_num == 2 or centrifugal_heat_pump_num == 3:
        while chp1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            while chp2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                while chp3_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                    # 计算3个设备的制热出力
                    chp1_heat_out_now = chp1_load_ratio * chp1.heating_power_rated
                    chp2_heat_out_now = chp2_load_ratio * chp2.heating_power_rated
                    chp3_heat_out_now = chp3_load_ratio * chp3.heating_power_rated
                    chp_heat_out_now_sum = chp1_heat_out_now + chp2_heat_out_now + chp3_heat_out_now
                    if chp_heat_out_now_sum < heat_load:
                        # 增加设备3负荷率
                        chp3_load_ratio += chp3_step / 100
                    else:
                        # 保存3个设备的负荷率
                        chp_load_ratio_result_all[0] = chp1_load_ratio
                        chp_load_ratio_result_all[1] = chp2_load_ratio
                        chp_load_ratio_result_all[2] = chp3_load_ratio
                        chp1_load_ratio_result.append(chp_load_ratio_result_all[0])
                        chp2_load_ratio_result.append(chp_load_ratio_result_all[1])
                        chp3_load_ratio_result.append(chp_load_ratio_result_all[2])
                        chp4_load_ratio_result.append(0)
                        # 计算3个设备的总耗电功率
                        chp1_power_consumption = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[1]
                        chp2_power_consumption = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[1]
                        chp3_power_consumption = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[1]
                        chp_power_consumption_total = chp1_power_consumption + chp2_power_consumption + chp3_power_consumption
                        total_power_consumption.append(chp_power_consumption_total)
                        # 计算3个设备的总补水量
                        chp1_water_supply = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[2]
                        chp2_water_supply = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[2]
                        chp3_water_supply = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[2]
                        chp_water_supply_total = chp1_water_supply + chp2_water_supply + chp3_water_supply
                        total_water_supply.append(chp_water_supply_total)
                        # 计算3个设备的成本
                        chp1_cost = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[0]
                        chp2_cost = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[0]
                        chp3_cost = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[0]
                        chp_cost_total = chp1_cost + chp2_cost + chp3_cost
                        cost.append(chp_cost_total)
                        break
                # 增加设备2负荷率，并将设备3负荷率重置回最小值
                chp2_load_ratio += chp2_step / 100
                chp3_load_ratio = chp3.load_min
            # 增加设备1的负荷率，并将设备2、3的负荷率重置为最小值
            chp1_load_ratio += chp1_step / 100
            chp2_load_ratio = chp2.load_min
            chp3_load_ratio = chp3.load_min

    # 列表，储存4台设备计算出的负荷率结果
    chp_load_ratio_result_all = [0, 0, 0, 0]
    # 初始化设备1、2、3、4的负荷率,设备负荷率不可以小于设定的最小值，变量用处储存计算过程中4太设备的实时负荷率
    chp1_load_ratio = chp1.load_min
    chp2_load_ratio = chp2.load_min
    chp3_load_ratio = chp3.load_min
    chp4_load_ratio = chp4.load_min

    if centrifugal_heat_pump_num == 3 or centrifugal_heat_pump_num == 4:
        while chp1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            while chp2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                while chp3_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                    while chp4_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                        # 计算4个设备的制热出力
                        chp1_heat_out_now = chp1_load_ratio * chp1.heating_power_rated
                        chp2_heat_out_now = chp2_load_ratio * chp2.heating_power_rated
                        chp3_heat_out_now = chp3_load_ratio * chp3.heating_power_rated
                        chp4_heat_out_now = chp4_load_ratio * chp4.heating_power_rated
                        chp_heat_out_now_sum = chp1_heat_out_now + chp2_heat_out_now + chp3_heat_out_now + chp4_heat_out_now
                        if chp_heat_out_now_sum < heat_load:
                            # 增加设备4负荷率
                            chp4_load_ratio += chp4_step / 100
                        else:
                            # 保存4个设备的负荷率
                            chp_load_ratio_result_all[0] = chp1_load_ratio
                            chp_load_ratio_result_all[1] = chp2_load_ratio
                            chp_load_ratio_result_all[2] = chp3_load_ratio
                            chp_load_ratio_result_all[3] = chp4_load_ratio
                            chp1_load_ratio_result.append(chp_load_ratio_result_all[0])
                            chp2_load_ratio_result.append(chp_load_ratio_result_all[1])
                            chp3_load_ratio_result.append(chp_load_ratio_result_all[2])
                            chp4_load_ratio_result.append(chp_load_ratio_result_all[3])
                            # 计算4个设备的总耗电功率
                            chp1_power_consumption = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[1]
                            chp2_power_consumption = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[1]
                            chp3_power_consumption = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[1]
                            chp4_power_consumption = centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[1]
                            chp_power_consumption_total = chp1_power_consumption + chp2_power_consumption + chp3_power_consumption + chp4_power_consumption
                            total_power_consumption.append(chp_power_consumption_total)
                            # 计算4个设备的总补水量
                            chp1_water_supply = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[2]
                            chp2_water_supply = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[2]
                            chp3_water_supply = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[2]
                            chp4_water_supply = centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[2]
                            chp_water_supply_total = chp1_water_supply + chp2_water_supply + chp3_water_supply + chp4_water_supply
                            total_water_supply.append(chp_water_supply_total)
                            # 计算4个设备的成本
                            chp1_cost = centrifugal_heat_pump_cost_heat(chp1, gc, chp1_load_ratio)[0]
                            chp2_cost = centrifugal_heat_pump_cost_heat(chp2, gc, chp2_load_ratio)[0]
                            chp3_cost = centrifugal_heat_pump_cost_heat(chp3, gc, chp3_load_ratio)[0]
                            chp4_cost = centrifugal_heat_pump_cost_heat(chp4, gc, chp4_load_ratio)[0]
                            chp_cost_total = chp1_cost + chp2_cost + chp3_cost + chp4_cost
                            cost.append(chp_cost_total)
                            break
                    # 增加设备3负荷率，并将设备4负荷率重置回0
                    chp3_load_ratio += chp3_step / 100
                    chp4_load_ratio = chp4.load_min
                # 增加设备2的负荷率，并将设备3、4的负荷率重置为最小值
                chp2_load_ratio += chp2_step / 100
                chp3_load_ratio = chp3.load_min
                chp4_load_ratio = chp4.load_min
            # 增加设备1的负荷率，并将设备2、3、4的负荷率重置为最小值
            chp1_load_ratio += chp1_step / 100
            chp2_load_ratio = chp2.load_min
            chp3_load_ratio = chp3.load_min
            chp4_load_ratio = chp4.load_min

    # 返回计算结果
    return cost, chp1_load_ratio_result, chp2_load_ratio_result, chp3_load_ratio_result, chp4_load_ratio_result, total_power_consumption, total_water_supply


def centrifugal_heat_pump_result_heat(ans_chp, chp1, chp2, chp3, chp4):
    """选择出最合适的离心式热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans_chp[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_chp[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    chp1_ratio = ans_chp[1][cost_min_index]
    chp2_ratio = ans_chp[2][cost_min_index]
    chp3_ratio = ans_chp[3][cost_min_index]
    chp4_ratio = ans_chp[4][cost_min_index]
    power_consumption_total = ans_chp[5][cost_min_index]
    water_supply_total = ans_chp[6][cost_min_index]
    heat_load_out = chp1_ratio * chp1.heating_power_rated + chp2_ratio * chp2.heating_power_rated + chp3_ratio * chp3.heating_power_rated + chp4_ratio * chp4.heating_power_rated

    return chp1_ratio, chp2_ratio, chp3_ratio, chp4_ratio, heat_load_out, power_consumption_total, water_supply_total


def centrifugal_heat_pump_cost_heat(chp, gc, load_ratio):
    """离心式热泵组运行成本计算"""
    # 采暖水流量,某一负荷率条件下
    heating_water_flow = chp.heating_water_flow(load_ratio)
    # 低温热源水流量,某一负荷率条件下
    heat_source_water_flow = chp.heat_source_water_flow(load_ratio)
    # 计算此时的离心式热泵低温热源水进口温度和采暖水出口温度
    heating_water_temperature = gc.heating_water_temperature
    heat_source_water_temperature = chp.heat_source_water_temperature(load_ratio)
    # 离心式热泵制热COP,某一负荷率条件下
    centrifugal_heat_pump_cop = chp.centrifugal_heat_pump_cop(load_ratio, heating_water_temperature, heat_source_water_temperature)
    # 离心式热泵本体耗电功率,某一负荷率条件下
    centrifugal_heat_pump_power_consumption = chp.centrifugal_heat_pump_power_consumption(load_ratio, centrifugal_heat_pump_cop)
    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = chp.auxiliary_equipment_power_consumption(heat_source_water_flow, heating_water_flow)
    # 离心式热泵总耗电功率,某一负荷率条件下
    total_power_consumption = centrifugal_heat_pump_power_consumption + auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 低温热源水补水量,某一负荷率条件下
    centrifugal_heat_pump_heat_source_water_supply = heat_source_water_flow * gc.heat_source_water_supply_rate
    # 采暖水补水量,某一负荷率条件下
    centrifugal_heat_pump_chiller_water_supply = heating_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下
    total_water_supply = centrifugal_heat_pump_chiller_water_supply + centrifugal_heat_pump_heat_source_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, centrifugal_heat_pump_power_consumption, heating_water_flow, heat_source_water_flow


def centrifugal_heat_pump_auxiliary_equipment_cost_heat(chp, gc, heating_water_flow, heat_source_water_flow):
    """离心式热泵辅助设备成本计算"""
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = chp.auxiliary_equipment_power_consumption(heat_source_water_flow, heating_water_flow)
    auxiliary_equipment_power_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 返回计算结果
    return auxiliary_equipment_power_consumption, auxiliary_equipment_power_cost


def print_centrifugal_heat_pump_heat(ans, chp1, chp2, chp3, chp4):
    """打印出离心式热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    chp1_ratio = ans[1][cost_min_index]
    chp2_ratio = ans[2][cost_min_index]
    chp3_ratio = ans[3][cost_min_index]
    chp4_ratio = ans[4][cost_min_index]
    heat_load_out = chp1_ratio * chp1.heating_power_rated + chp2_ratio * chp2.heating_power_rated + chp3_ratio * chp3.heating_power_rated + chp4_ratio * chp4.heating_power_rated
    print("离心式热泵最低总运行成本为： " + str(cost_min) + "\n" + "离心式热泵1负荷率为： " + str(chp1_ratio) + "\n" + "离心式热泵2负荷率为： " + str(chp2_ratio) + "\n" + "离心式热泵3负荷率为： " + str(chp3_ratio) + "\n" + "离心式热泵4负荷率为： " + str(chp4_ratio) + "\n" + "离心式热泵总制热出力为： " + str(heat_load_out))


def test_centrifugal_heat_pump_function_heat():
    """测试离心式热泵制热计算"""
    gc = Global_Constant()
    heat_load = 15000
    chp_wp = False
    chp1_wp_heating_water = Water_Pump(900, chp_wp, gc)
    chp2_wp_heating_water = Water_Pump(900, chp_wp, gc)
    chp3_wp_heating_water = Water_Pump(900, chp_wp, gc)
    chp4_wp_heating_water = Water_Pump(900, chp_wp, gc)
    chp1_wp_heat_source_water = Water_Pump(700, chp_wp, gc)
    chp2_wp_heat_source_water = Water_Pump(700, chp_wp, gc)
    chp3_wp_heat_source_water = Water_Pump(700, chp_wp, gc)
    chp4_wp_heat_source_water = Water_Pump(700, chp_wp, gc)
    chp1 = Centrifugal_Heat_Pump(5000, 0.2, False, chp1_wp_heating_water, chp1_wp_heat_source_water, gc)
    chp2 = Centrifugal_Heat_Pump(5000, 0.2, False, chp2_wp_heating_water, chp2_wp_heat_source_water, gc)
    chp3 = Centrifugal_Heat_Pump(5000, 0.2, False, chp3_wp_heating_water, chp3_wp_heat_source_water, gc)
    chp4 = Centrifugal_Heat_Pump(5000, 0.2, False, chp4_wp_heating_water, chp4_wp_heat_source_water, gc)

    ans = centrifugal_heat_pump_function_heat(heat_load, chp1, chp2, chp3, chp4, gc)
    print_centrifugal_heat_pump_heat(ans, chp1, chp2, chp3, chp4)

#test_centrifugal_heat_pump_function_heat()