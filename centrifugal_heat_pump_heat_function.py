import math
from equipment import Centrifugal_Heat_Pump_Heat, Water_Pump
from global_constant import Global_Constant

def centrifugal_heat_pump_function_heat(heat_load, chph1, chph2, chph3, chph4, gc):
    """离心式热泵制热负荷计算函数"""
    # 制热，制热，制热
    # 离心式热泵组与水泵的布置方式，header_system（母管制）
    # 不同管道布置方式的离心式热泵计算
    # 母管制系统计算（水泵与离心式热泵组不是一对一布置）
    # 获取4台离心式热泵是否为变频，根据是否为变频，设置不同的计算步长
    # 离心式热泵1
    if chph1.frequency_scaling == True:
        chph1_step = 1
    else:
        chph1_step = 10
    # 离心式热泵2
    if chph2.frequency_scaling == True:
        chph2_step = 1
    else:
        chph2_step = 10
    # 离心式热泵3
    if chph3.frequency_scaling == True:
        chph3_step = 1
    else:
        chph3_step = 10
    # 离心式热泵4
    if chph4.frequency_scaling == True:
        chph4_step = 1
    else:
        chph4_step = 10

    # 列表，储存4台设备计算出的负荷率结果
    chph_load_ratio_result_all = [0, 0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台离心式热泵的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台离心式热泵的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    chph1_load_ratio_result = []
    chph2_load_ratio_result = []
    chph3_load_ratio_result = []
    chph4_load_ratio_result = []

    # 确定需要几台设备，向上取整（离心式热泵可以启动的最大数量）
    chph_num_max_2 = math.ceil(heat_load / chph1.heating_power_rated)
    # 如果恰好整除，则向上加1
    if chph_num_max_2 ==int(chph_num_max_2):
        chph_num_max_1 = chph_num_max_2 + 1
    else:
        chph_num_max_1 = chph_num_max_2
    # 最大数量不可以超过4
    if chph_num_max_1 > 4:
        chph_num_max_a = 4
    else:
        chph_num_max_a = chph_num_max_1

    # 如果某个设备的额定功率为0，则不参与计算，从而控制参与计算的设备的最大数量
    chph_power_0_num = 0 # 初始化额定功率为0的设备数量
    if chph1.heating_power_rated == 0:
        chph_power_0_num += 1
    if chph2.heating_power_rated == 0:
        chph_power_0_num += 1
    if chph3.heating_power_rated == 0:
        chph_power_0_num += 1
    if chph4.heating_power_rated == 0:
        chph_power_0_num += 1
    chph_num_max_b = 4 - chph_power_0_num
    # 重新修正设备最大数量
    chph_num_max = min(chph_num_max_a, chph_num_max_b)

    # 离心式热泵启动数量初始值
    chph_num = 1

    while chph_num <= chph_num_max:
        # 初始化设备1、2、3、4的负荷率
        if chph_num >= 1:
            chph1_load_ratio = chph1.load_min
        else:
            chph1_load_ratio = 0
        if chph_num >= 2:
            chph2_load_ratio = chph2.load_min
        else:
            chph2_load_ratio = 0
        if chph_num >= 3:
            chph3_load_ratio = chph3.load_min
        else:
            chph3_load_ratio = 0
        if chph_num >= 4:
            chph4_load_ratio = chph4.load_min
        else:
            chph4_load_ratio = 0
        # 计算离心式热泵设备
        while chph1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算4个设备的制热出力
            chph1_heat_out_now = chph1_load_ratio * chph1.heating_power_rated
            chph2_heat_out_now = chph2_load_ratio * chph2.heating_power_rated
            chph3_heat_out_now = chph3_load_ratio * chph3.heating_power_rated
            chph4_heat_out_now = chph4_load_ratio * chph4.heating_power_rated
            chph_heat_out_now_sum = chph1_heat_out_now + chph2_heat_out_now + chph3_heat_out_now + chph4_heat_out_now
            # print(chph_num, chph1_heat_out_now, chph2_heat_out_now, chph3_heat_out_now, chph4_heat_out_now)
            if chph_heat_out_now_sum < heat_load:
                # 增加设备1、2、3、4负荷率
                if chph_num >= 1:
                    chph1_load_ratio += chph1_step / 100
                else:
                    chph1_load_ratio = 0
                if chph_num >= 2:
                    chph2_load_ratio += chph2_step / 100
                else:
                    chph2_load_ratio = 0
                if chph_num >= 3:
                    chph3_load_ratio += chph3_step / 100
                else:
                    chph3_load_ratio = 0
                if chph_num >= 4:
                    chph4_load_ratio += chph4_step / 100
                else:
                    chph4_load_ratio = 0
            else:
                # 保存4个设备的负荷率
                chph_load_ratio_result_all[0] = chph1_load_ratio
                chph_load_ratio_result_all[1] = chph2_load_ratio
                chph_load_ratio_result_all[2] = chph3_load_ratio
                chph_load_ratio_result_all[3] = chph4_load_ratio
                chph1_load_ratio_result.append(chph_load_ratio_result_all[0])
                chph2_load_ratio_result.append(chph_load_ratio_result_all[1])
                chph3_load_ratio_result.append(chph_load_ratio_result_all[2])
                chph4_load_ratio_result.append(chph_load_ratio_result_all[3])
                # 计算4个设备本体的总耗电功率（仅设备本体耗电）
                chph1_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chph1, gc, chph1_load_ratio)[3]
                chph2_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chph2, gc, chph2_load_ratio)[3]
                chph3_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chph3, gc, chph3_load_ratio)[3]
                chph4_centrifugal_heat_pump_power_consumption = centrifugal_heat_pump_cost_heat(chph4, gc, chph4_load_ratio)[3]
                # 计算4个设备的采暖水流量、低温热源水流量
                # 采暖水和低温热源水总流量
                heating_water_flow_total = centrifugal_heat_pump_cost_heat(chph1, gc, chph1_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chph2, gc, chph2_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chph3, gc, chph3_load_ratio)[4] + centrifugal_heat_pump_cost_heat(chph4, gc, chph4_load_ratio)[4]
                heat_source_water_flow_total = centrifugal_heat_pump_cost_heat(chph1, gc, chph1_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chph2, gc, chph2_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chph3, gc, chph3_load_ratio)[5] + centrifugal_heat_pump_cost_heat(chph4, gc, chph4_load_ratio)[5]
                # 每个水泵的流量为总流量均分（后期可细化流量分配比例）
                chph1_heating_water_flow = heating_water_flow_total / chph_num
                chph2_heating_water_flow = heating_water_flow_total / chph_num
                chph3_heating_water_flow = heating_water_flow_total / chph_num
                chph4_heating_water_flow = heating_water_flow_total / chph_num
                chph1_heat_source_water_flow = heat_source_water_flow_total / chph_num
                chph2_heat_source_water_flow = heat_source_water_flow_total / chph_num
                chph3_heat_source_water_flow = heat_source_water_flow_total / chph_num
                chph4_heat_source_water_flow = heat_source_water_flow_total / chph_num
                # 辅助设备耗电功率
                chph1_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chph1, gc, chph1_heating_water_flow, chph1_heat_source_water_flow)[0]
                chph2_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chph2, gc, chph2_heating_water_flow, chph2_heat_source_water_flow)[0]
                chph3_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chph3, gc, chph3_heating_water_flow, chph3_heat_source_water_flow)[0]
                chph4_auxiliary_equipment_power_consumption = centrifugal_heat_pump_auxiliary_equipment_cost_heat(chph4, gc, chph4_heating_water_flow, chph4_heat_source_water_flow)[0]
                # 耗电量总计
                chph_power_consumption_total = chph1_centrifugal_heat_pump_power_consumption + chph2_centrifugal_heat_pump_power_consumption + chph3_centrifugal_heat_pump_power_consumption + chph4_centrifugal_heat_pump_power_consumption + chph1_auxiliary_equipment_power_consumption + chph2_auxiliary_equipment_power_consumption + chph3_auxiliary_equipment_power_consumption + chph4_auxiliary_equipment_power_consumption
                total_power_consumption.append(chph_power_consumption_total)
                # 计算4个设备的总补水量
                chph1_water_supply = centrifugal_heat_pump_cost_heat(chph1, gc, chph1_load_ratio)[2]
                chph2_water_supply = centrifugal_heat_pump_cost_heat(chph2, gc, chph2_load_ratio)[2]
                chph3_water_supply = centrifugal_heat_pump_cost_heat(chph3, gc, chph3_load_ratio)[2]
                chph4_water_supply = centrifugal_heat_pump_cost_heat(chph4, gc, chph4_load_ratio)[2]
                chph_water_supply_total = chph1_water_supply + chph2_water_supply + chph3_water_supply + chph4_water_supply
                total_water_supply.append(chph_water_supply_total)
                # 计算4个设备的成本
                chph_cost_total = chph_power_consumption_total * gc.buy_electricity_price + chph_water_supply_total * gc.water_price
                cost.append(chph_cost_total)
                break
        # 增加离心式热泵数量
        chph_num += 1

    # 返回计算结果
    return cost, chph1_load_ratio_result, chph2_load_ratio_result, chph3_load_ratio_result, chph4_load_ratio_result, total_power_consumption, total_water_supply


def centrifugal_heat_pump_result_heat(ans_chph, chph1, chph2, chph3, chph4):
    """选择出最合适的离心式热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans_chph[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_chph[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    chph1_ratio = ans_chph[1][cost_min_index]
    chph2_ratio = ans_chph[2][cost_min_index]
    chph3_ratio = ans_chph[3][cost_min_index]
    chph4_ratio = ans_chph[4][cost_min_index]
    power_consumption_total = ans_chph[5][cost_min_index]
    water_supply_total = ans_chph[6][cost_min_index]
    heat_load_out = chph1_ratio * chph1.heating_power_rated + chph2_ratio * chph2.heating_power_rated + chph3_ratio * chph3.heating_power_rated + chph4_ratio * chph4.heating_power_rated

    return chph1_ratio, chph2_ratio, chph3_ratio, chph4_ratio, heat_load_out, power_consumption_total, water_supply_total


def centrifugal_heat_pump_cost_heat(chph, gc, load_ratio):
    """离心式热泵组运行成本计算"""
    # 采暖水流量,某一负荷率条件下
    heating_water_flow = chph.heating_water_flow(load_ratio)
    # 低温热源水流量,某一负荷率条件下
    heat_source_water_flow = chph.heat_source_water_flow(load_ratio)
    # 计算此时的离心式热泵低温热源水进口温度和采暖水出口温度
    heating_water_temperature = gc.heating_water_temperature
    heat_source_water_temperature = chph.heat_source_water_temperature(load_ratio)
    # 离心式热泵制热COP,某一负荷率条件下
    centrifugal_heat_pump_cop = chph.centrifugal_heat_pump_cop(load_ratio, heating_water_temperature, heat_source_water_temperature)
    # 离心式热泵本体耗电功率,某一负荷率条件下
    centrifugal_heat_pump_power_consumption = chph.centrifugal_heat_pump_power_consumption(load_ratio, centrifugal_heat_pump_cop)
    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = chph.auxiliary_equipment_power_consumption(heat_source_water_flow, heating_water_flow)
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


def centrifugal_heat_pump_auxiliary_equipment_cost_heat(chph, gc, heating_water_flow, heat_source_water_flow):
    """离心式热泵辅助设备成本计算"""
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = chph.auxiliary_equipment_power_consumption(heat_source_water_flow, heating_water_flow)
    auxiliary_equipment_power_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 返回计算结果
    return auxiliary_equipment_power_consumption, auxiliary_equipment_power_cost


def print_centrifugal_heat_pump_heat(ans, chph1, chph2, chph3, chph4):
    """打印出离心式热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    chph1_ratio = ans[1][cost_min_index]
    chph2_ratio = ans[2][cost_min_index]
    chph3_ratio = ans[3][cost_min_index]
    chph4_ratio = ans[4][cost_min_index]
    heat_load_out = chph1_ratio * chph1.heating_power_rated + chph2_ratio * chph2.heating_power_rated + chph3_ratio * chph3.heating_power_rated + chph4_ratio * chph4.heating_power_rated
    print("离心式热泵最低总运行成本为： " + str(cost_min) + "\n" + "离心式热泵1负荷率为： " + str(chph1_ratio) + "\n" + "离心式热泵2负荷率为： " + str(chph2_ratio) + "\n" + "离心式热泵3负荷率为： " + str(chph3_ratio) + "\n" + "离心式热泵4负荷率为： " + str(chph4_ratio) + "\n" + "离心式热泵总制热出力为： " + str(heat_load_out))


def test_centrifugal_heat_pump_function_heat():
    """测试离心式热泵制热计算"""
    gc = Global_Constant()
    heat_load = 15000
    chph_wp = False
    chph1_wp_heating_water = Water_Pump(900, chph_wp, 35, gc)
    chph2_wp_heating_water = Water_Pump(900, chph_wp, 35, gc)
    chph3_wp_heating_water = Water_Pump(900, chph_wp, 35, gc)
    chph4_wp_heating_water = Water_Pump(900, chph_wp, 35, gc)
    chph1_wp_heat_source_water = Water_Pump(700, chph_wp, 35, gc)
    chph2_wp_heat_source_water = Water_Pump(700, chph_wp, 35, gc)
    chph3_wp_heat_source_water = Water_Pump(700, chph_wp, 35, gc)
    chph4_wp_heat_source_water = Water_Pump(700, chph_wp, 35, gc)
    chph1 = Centrifugal_Heat_Pump_Heat(5000, 0.2, False, chph1_wp_heating_water, chph1_wp_heat_source_water, gc)
    chph2 = Centrifugal_Heat_Pump_Heat(5000, 0.2, False, chph2_wp_heating_water, chph2_wp_heat_source_water, gc)
    chph3 = Centrifugal_Heat_Pump_Heat(5000, 0.2, False, chph3_wp_heating_water, chph3_wp_heat_source_water, gc)
    chph4 = Centrifugal_Heat_Pump_Heat(5000, 0.2, False, chph4_wp_heating_water, chph4_wp_heat_source_water, gc)

    ans = centrifugal_heat_pump_function_heat(heat_load, chph1, chph2, chph3, chph4, gc)
    print_centrifugal_heat_pump_heat(ans, chph1, chph2, chph3, chph4)

#test_centrifugal_heat_pump_function_heat()