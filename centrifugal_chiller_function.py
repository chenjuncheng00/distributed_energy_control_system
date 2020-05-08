import math
from equipment import Centrifugal_Chiller, Water_Pump
from global_constant import Global_Constant

def centrifugal_chiller_function(cold_load, cc1, cc2, cc3, cc4, gc):
    """离心式冷水机组制冷负荷计算函数"""
    # 不同管道布置方式的离心式冷水机计算
    # 母管制系统计算（水泵与离心式冷水机组不是一对一布置）
    # 获取4台离心式冷水机是否为变频，根据是否为变频，设置不同的计算步长
    # 离心式冷水机1
    if cc1.frequency_scaling == True:
        cc1_step = 1
    else:
        cc1_step = 10
    # 离心式冷水机2
    if cc2.frequency_scaling == True:
        cc2_step = 1
    else:
        cc2_step = 10
    # 离心式冷水机3
    if cc3.frequency_scaling == True:
        cc3_step = 1
    else:
        cc3_step = 10
    # 离心式冷水机4
    if cc4.frequency_scaling == True:
        cc4_step = 1
    else:
        cc4_step = 10

    # 列表，储存4台设备计算出的负荷率结果
    cc_load_ratio_result_all = [0, 0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台离心式冷水机的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台离心式冷水机的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    cc1_load_ratio_result = []
    cc2_load_ratio_result = []
    cc3_load_ratio_result = []
    cc4_load_ratio_result = []

    # 确定需要几台设备，向上取整（离心式冷水机可以启动的最大数量）
    cc_num_max_2 = math.ceil(cold_load / cc1.cooling_power_rated)
    # 如果恰好整除，则向上加1
    if cc_num_max_2 == int(cc_num_max_2):
        cc_num_max_1 = cc_num_max_2 + 1
    else:
        cc_num_max_1 = cc_num_max_2
    # 最大数量不可以超过4
    if cc_num_max_1 > 4:
        cc_num_max = 4
    else:
        cc_num_max = cc_num_max_1

    # 离心式冷水机启动数量初始值
    cc_num = 1

    while cc_num <= cc_num_max:
        # 初始化设备1、2、3、4的负荷率
        if cc_num >= 1:
            cc1_load_ratio = cc1.load_min
        else:
            cc1_load_ratio = 0
        if cc_num >= 2:
            cc2_load_ratio = cc2.load_min
        else:
            cc2_load_ratio = 0
        if cc_num >= 3:
            cc3_load_ratio = cc3.load_min
        else:
            cc3_load_ratio = 0
        if cc_num >= 4:
            cc4_load_ratio = cc4.load_min
        else:
            cc4_load_ratio = 0
        # 计算冷水机设备
        while cc1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算4个设备的制冷出力
            cc1_cold_out_now = cc1_load_ratio * cc1.cooling_power_rated
            cc2_cold_out_now = cc2_load_ratio * cc2.cooling_power_rated
            cc3_cold_out_now = cc3_load_ratio * cc3.cooling_power_rated
            cc4_cold_out_now = cc4_load_ratio * cc4.cooling_power_rated
            cc_cold_out_now_sum = cc1_cold_out_now + cc2_cold_out_now + cc3_cold_out_now + cc4_cold_out_now
            if cc_cold_out_now_sum < cold_load:
                # 增加设备1、2、3、4负荷率
                if cc_num >= 1:
                    cc1_load_ratio += cc1_step / 100
                else:
                    cc1_load_ratio = 0
                if cc_num >= 2:
                    cc2_load_ratio += cc2_step / 100
                else:
                    cc2_load_ratio = 0
                if cc_num >= 3:
                    cc3_load_ratio += cc3_step / 100
                else:
                    cc3_load_ratio = 0
                if cc_num >= 4:
                    cc4_load_ratio += cc4_step / 100
                else:
                    cc4_load_ratio = 0
            else:
                # 保存4个设备的负荷率
                cc_load_ratio_result_all[0] = cc1_load_ratio
                cc_load_ratio_result_all[1] = cc2_load_ratio
                cc_load_ratio_result_all[2] = cc3_load_ratio
                cc_load_ratio_result_all[3] = cc4_load_ratio
                cc1_load_ratio_result.append(cc_load_ratio_result_all[0])
                cc2_load_ratio_result.append(cc_load_ratio_result_all[1])
                cc3_load_ratio_result.append(cc_load_ratio_result_all[2])
                cc4_load_ratio_result.append(cc_load_ratio_result_all[3])
                # 计算4个设备本体的总耗电功率（仅设备本体耗电）
                cc1_centrifugal_chiller_power_consumption = centrifugal_chiller_cost(cc1, gc, cc1_load_ratio)[3]
                cc2_centrifugal_chiller_power_consumption = centrifugal_chiller_cost(cc2, gc, cc2_load_ratio)[3]
                cc3_centrifugal_chiller_power_consumption = centrifugal_chiller_cost(cc3, gc, cc3_load_ratio)[3]
                cc4_centrifugal_chiller_power_consumption = centrifugal_chiller_cost(cc4, gc, cc4_load_ratio)[3]
                # 计算4个设备的冷冻水流量、冷却水流量
                # 冷冻水和冷却水总流量
                chilled_water_flow_total = centrifugal_chiller_cost(cc1, gc, cc1_load_ratio)[4] + \
                                           centrifugal_chiller_cost(cc2, gc, cc2_load_ratio)[4] + \
                                           centrifugal_chiller_cost(cc3, gc, cc3_load_ratio)[4] + \
                                           centrifugal_chiller_cost(cc4, gc, cc4_load_ratio)[4]
                cooling_water_flow_total = centrifugal_chiller_cost(cc1, gc, cc1_load_ratio)[5] + \
                                           centrifugal_chiller_cost(cc2, gc, cc2_load_ratio)[5] + \
                                           centrifugal_chiller_cost(cc3, gc, cc3_load_ratio)[5] + \
                                           centrifugal_chiller_cost(cc4, gc, cc4_load_ratio)[5]
                # 每个水泵的流量为总流量均分（后期可细化流量分配比例）
                cc1_chilled_water_flow = chilled_water_flow_total / cc_num
                cc2_chilled_water_flow = chilled_water_flow_total / cc_num
                cc3_chilled_water_flow = chilled_water_flow_total / cc_num
                cc4_chilled_water_flow = chilled_water_flow_total / cc_num
                cc1_cooling_water_flow = cooling_water_flow_total / cc_num
                cc2_cooling_water_flow = cooling_water_flow_total / cc_num
                cc3_cooling_water_flow = cooling_water_flow_total / cc_num
                cc4_cooling_water_flow = cooling_water_flow_total / cc_num
                # 辅助设备耗电功率
                cc1_auxiliary_equipment_power_consumption = \
                centrifugal_chiller_auxiliary_equipment_cost(cc1, gc, cc1_chilled_water_flow, cc1_cooling_water_flow)[0]
                cc2_auxiliary_equipment_power_consumption = \
                centrifugal_chiller_auxiliary_equipment_cost(cc2, gc, cc2_chilled_water_flow, cc2_cooling_water_flow)[0]
                cc3_auxiliary_equipment_power_consumption = \
                centrifugal_chiller_auxiliary_equipment_cost(cc3, gc, cc3_chilled_water_flow, cc3_cooling_water_flow)[0]
                cc4_auxiliary_equipment_power_consumption = \
                centrifugal_chiller_auxiliary_equipment_cost(cc4, gc, cc4_chilled_water_flow, cc4_cooling_water_flow)[0]
                # 耗电量总计
                cc_power_consumption_total = cc1_centrifugal_chiller_power_consumption + cc2_centrifugal_chiller_power_consumption + cc3_centrifugal_chiller_power_consumption + cc4_centrifugal_chiller_power_consumption + cc1_auxiliary_equipment_power_consumption + cc2_auxiliary_equipment_power_consumption + cc3_auxiliary_equipment_power_consumption + cc4_auxiliary_equipment_power_consumption
                total_power_consumption.append(cc_power_consumption_total)
                # 计算4个设备的总补水量
                cc1_water_supply = centrifugal_chiller_cost(cc1, gc, cc1_load_ratio)[2]
                cc2_water_supply = centrifugal_chiller_cost(cc2, gc, cc2_load_ratio)[2]
                cc3_water_supply = centrifugal_chiller_cost(cc3, gc, cc3_load_ratio)[2]
                cc4_water_supply = centrifugal_chiller_cost(cc4, gc, cc4_load_ratio)[2]
                cc_water_supply_total = cc1_water_supply + cc2_water_supply + cc3_water_supply + cc4_water_supply
                total_water_supply.append(cc_water_supply_total)
                # 计算4个设备的成本
                cc_cost_total = cc_power_consumption_total * gc.buy_electricity_price + cc_water_supply_total * gc.water_price
                cost.append(cc_cost_total)
                break
        # 增加离心式冷水机数量
        cc_num += 1

    # 返回计算结果
    return cost, cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, total_power_consumption, total_water_supply


def centrifugal_chiller_result(ans_cc, cc1, cc2, cc3, cc4):
    """选择出最合适的离心式冷水机的计算结果"""
    # 总成本最小值
    cost_min = min(ans_cc[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_cc[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    cc1_ratio = ans_cc[1][cost_min_index]
    cc2_ratio = ans_cc[2][cost_min_index]
    cc3_ratio = ans_cc[3][cost_min_index]
    cc4_ratio = ans_cc[4][cost_min_index]
    power_consumption_total = ans_cc[5][cost_min_index]
    water_supply_total = ans_cc[6][cost_min_index]
    cold_load_out = cc1_ratio * cc1.cooling_power_rated + cc2_ratio * cc2.cooling_power_rated + cc3_ratio * cc3.cooling_power_rated + cc4_ratio * cc4.cooling_power_rated

    return cc1_ratio, cc2_ratio, cc3_ratio, cc4_ratio, cold_load_out, power_consumption_total, water_supply_total


def centrifugal_chiller_cost(cc, gc, load_ratio):
    """离心式冷水机组运行成本计算"""
    # 冷冻水流量,某一负荷率条件下
    chilled_water_flow = cc.chilled_water_flow(load_ratio)
    # 冷却水流量,某一负荷率条件下
    cooling_water_flow = cc.cooling_water_flow(load_ratio)
    # 计算此时的离心式冷水机冷却水进口温度和冷冻水出口温度
    chilled_water_temperature = gc.chilled_water_temperature
    cooling_water_temperature = cc.cooling_water_temperature(load_ratio)
    # 离心式冷水机制冷COP,某一负荷率条件下
    centrifugal_chiller_cop = cc.centrifugal_chiller_cop(load_ratio, chilled_water_temperature, cooling_water_temperature)
    # 冷水机本体耗电功率,某一负荷率条件下
    centrifugal_chiller_power_consumption = cc.centrifugal_chiller_power_consumption(load_ratio, centrifugal_chiller_cop)
    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = cc.auxiliary_equipment_power_consumption(cooling_water_flow, chilled_water_flow)
    # 离心式冷水机总耗电功率,某一负荷率条件下
    total_power_consumption = centrifugal_chiller_power_consumption + auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 冷却水补水量,某一负荷率条件下
    centrifugal_chiller_cooling_water_supply = cooling_water_flow * gc.cooling_water_supply_rate
    # 冷冻水补水量,某一负荷率条件下
    centrifugal_chiller_chiller_water_supply = chilled_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下
    total_water_supply = centrifugal_chiller_chiller_water_supply + centrifugal_chiller_cooling_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, centrifugal_chiller_power_consumption, chilled_water_flow, cooling_water_flow


def centrifugal_chiller_auxiliary_equipment_cost(cc, gc, chilled_water_flow, cooling_water_flow):
    """离心式冷水机辅助设备成本计算"""
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = cc.auxiliary_equipment_power_consumption(cooling_water_flow, chilled_water_flow)
    auxiliary_equipment_power_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 返回计算结果
    return auxiliary_equipment_power_consumption, auxiliary_equipment_power_cost


def print_centrifugal_chiller(ans, cc1, cc2, cc3, cc4):
    """打印出离心式冷水机的计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    cc1_ratio = ans[1][cost_min_index]
    cc2_ratio = ans[2][cost_min_index]
    cc3_ratio = ans[3][cost_min_index]
    cc4_ratio = ans[4][cost_min_index]
    cold_load_out = cc1_ratio * cc1.cooling_power_rated + cc2_ratio * cc2.cooling_power_rated + cc3_ratio * cc3.cooling_power_rated + cc4_ratio * cc4.cooling_power_rated
    print("离心式冷水机最低总运行成本为： " + str(cost_min) + "\n" + "离心式冷水机1负荷率为： " + str(cc1_ratio) + "\n" + "离心式冷水机2负荷率为： " + str(cc2_ratio) + "\n" + "离心式冷水机3负荷率为： " + str(cc3_ratio) + "\n" + "离心式冷水机4负荷率为： " + str(cc4_ratio) + "\n" + "离心式冷水机总制冷出力为： " + str(cold_load_out))


def test_centrifugal_chiller_function():
    """测试离心式冷水机计算"""
    # 实例化4个离心式冷水机的各种水泵
    gc = Global_Constant()
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
    # 冷负荷
    cold_load = 9000
    ans = centrifugal_chiller_function(cold_load, cc1, cc2, cc3, cc4, gc)
    print_centrifugal_chiller(ans, cc1, cc2, cc3, cc4)

#test_centrifugal_chiller_function()