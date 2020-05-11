import math
from equipment import Air_Source_Heat_Pump_Cold, Water_Pump
from global_constant import Global_Constant

def air_source_heat_pump_function_cold(cold_load, ashpc1, ashpc2, ashpc3, ashpc4, gc):
    """风冷螺杆热泵制冷负荷计算函数"""
    # 制冷，制冷，制冷
    # 风冷螺杆热泵组与水泵的布置方式，header_system（母管制）
    # 不同管道布置方式的风冷螺杆热泵计算
    # 母管制系统计算（水泵与风冷螺杆热泵组不是一对一布置）
    # 获取4台风冷螺杆热泵是否为变频，根据是否为变频，设置不同的计算步长
    # 风冷螺杆热泵1
    if ashpc1.frequency_scaling == True:
        ashpc1_step = 1
    else:
        ashpc1_step = 10
    # 风冷螺杆热泵2
    if ashpc2.frequency_scaling == True:
        ashpc2_step = 1
    else:
        ashpc2_step = 10
    # 风冷螺杆热泵3
    if ashpc3.frequency_scaling == True:
        ashpc3_step = 1
    else:
        ashpc3_step = 10
    # 风冷螺杆热泵4
    if ashpc4.frequency_scaling == True:
        ashpc4_step = 1
    else:
        ashpc4_step = 10

    # 列表，储存4台设备计算出的负荷率结果
    ashpc_load_ratio_result_all = [0, 0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台风冷螺杆热泵的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台风冷螺杆热泵的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    ashpc1_load_ratio_result = []
    ashpc2_load_ratio_result = []
    ashpc3_load_ratio_result = []
    ashpc4_load_ratio_result = []

    # 确定需要几台设备，向上取整（风冷螺杆热泵可以启动的最大数量）
    ashpc_num_max_2 = math.ceil(cold_load / ashpc1.cooling_power_rated)
    # 如果恰好整除，则向上加1
    if ashpc_num_max_2 == int(ashpc_num_max_2):
        ashpc_num_max_1 = ashpc_num_max_2 + 1
    else:
        ashpc_num_max_1 = ashpc_num_max_2
    # 最大数量不可以超过4
    if ashpc_num_max_1 > 4:
        ashpc_num_max_a = 4
    else:
        ashpc_num_max_a = ashpc_num_max_1

    # 如果某个设备的额定功率为0，则不参与计算，从而控制参与计算的设备的最大数量
    ashpc_power_0_num = 0  # 初始化额定功率为0的设备数量
    if ashpc1.cooling_power_rated == 0:
        ashpc_power_0_num += 1
    if ashpc2.cooling_power_rated == 0:
        ashpc_power_0_num += 1
    if ashpc3.cooling_power_rated == 0:
        ashpc_power_0_num += 1
    if ashpc4.cooling_power_rated == 0:
        ashpc_power_0_num += 1
    ashpc_num_max_b = 4 - ashpc_power_0_num
    # 重新修正设备最大数量
    ashpc_num_max = min(ashpc_num_max_a, ashpc_num_max_b)

    # 风冷螺杆热泵启动数量初始值
    ashpc_num = 1

    while ashpc_num <= ashpc_num_max:
        # 初始化设备1、2、3、4的负荷率
        if ashpc_num >= 1:
            ashpc1_load_ratio = ashpc1.load_min
        else:
            ashpc1_load_ratio = 0
        if ashpc_num >= 2:
            ashpc2_load_ratio = ashpc2.load_min
        else:
            ashpc2_load_ratio = 0
        if ashpc_num >= 3:
            ashpc3_load_ratio = ashpc3.load_min
        else:
            ashpc3_load_ratio = 0
        if ashpc_num >= 4:
            ashpc4_load_ratio = ashpc4.load_min
        else:
            ashpc4_load_ratio = 0
        # 计算风冷螺杆热泵设备
        while ashpc1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算4个设备的制冷出力
            ashpc1_cold_out_now = ashpc1_load_ratio * ashpc1.cooling_power_rated
            ashpc2_cold_out_now = ashpc2_load_ratio * ashpc2.cooling_power_rated
            ashpc3_cold_out_now = ashpc3_load_ratio * ashpc3.cooling_power_rated
            ashpc4_cold_out_now = ashpc4_load_ratio * ashpc4.cooling_power_rated
            ashpc_cold_out_now_sum = ashpc1_cold_out_now + ashpc2_cold_out_now + ashpc3_cold_out_now + ashpc4_cold_out_now
            
            if ashpc_cold_out_now_sum < cold_load:
                # 增加设备1、2、3、4负荷率
                if ashpc_num >= 1:
                    ashpc1_load_ratio += ashpc1_step / 100
                else:
                    ashpc1_load_ratio = 0
                if ashpc_num >= 2:
                    ashpc2_load_ratio += ashpc2_step / 100
                else:
                    ashpc2_load_ratio = 0
                if ashpc_num >= 3:
                    ashpc3_load_ratio += ashpc3_step / 100
                else:
                    ashpc3_load_ratio = 0
                if ashpc_num >= 4:
                    ashpc4_load_ratio += ashpc4_step / 100
                else:
                    ashpc4_load_ratio = 0
            else:
                # 保存4个设备的负荷率
                ashpc_load_ratio_result_all[0] = ashpc1_load_ratio
                ashpc_load_ratio_result_all[1] = ashpc2_load_ratio
                ashpc_load_ratio_result_all[2] = ashpc3_load_ratio
                ashpc_load_ratio_result_all[3] = ashpc4_load_ratio
                ashpc1_load_ratio_result.append(ashpc_load_ratio_result_all[0])
                ashpc2_load_ratio_result.append(ashpc_load_ratio_result_all[1])
                ashpc3_load_ratio_result.append(ashpc_load_ratio_result_all[2])
                ashpc4_load_ratio_result.append(ashpc_load_ratio_result_all[3])
                # 计算4个设备本体的总耗电功率（仅设备本体耗电）
                ashpc1_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_cold(ashpc1, gc, ashpc1_load_ratio)[3]
                ashpc2_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_cold(ashpc2, gc, ashpc2_load_ratio)[3]
                ashpc3_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_cold(ashpc3, gc, ashpc3_load_ratio)[3]
                ashpc4_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_cold(ashpc4, gc, ashpc4_load_ratio)[3]
                # 计算4个设备的冷冻水流量、低温热源水流量
                # 冷冻水总流量
                chilled_water_flow_total = air_source_heat_pump_cost_cold(ashpc1, gc, ashpc1_load_ratio)[4] + air_source_heat_pump_cost_cold(ashpc2, gc, ashpc2_load_ratio)[4] + air_source_heat_pump_cost_cold(ashpc3, gc, ashpc3_load_ratio)[4] + air_source_heat_pump_cost_cold(ashpc4, gc, ashpc4_load_ratio)[4]
                # 每个水泵的流量为总流量均分（后期可细化流量分配比例）
                ashpc1_chilled_water_flow = chilled_water_flow_total / ashpc_num
                ashpc2_chilled_water_flow = chilled_water_flow_total / ashpc_num
                ashpc3_chilled_water_flow = chilled_water_flow_total / ashpc_num
                ashpc4_chilled_water_flow = chilled_water_flow_total / ashpc_num
                # 辅助设备耗电功率
                ashpc1_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_cold(ashpc1, gc, ashpc1_chilled_water_flow)[0]
                ashpc2_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_cold(ashpc2, gc, ashpc2_chilled_water_flow)[0]
                ashpc3_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_cold(ashpc3, gc, ashpc3_chilled_water_flow)[0]
                ashpc4_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_cold(ashpc4, gc, ashpc4_chilled_water_flow)[0]
                # 耗电量总计
                ashpc_power_consumption_total = ashpc1_air_source_heat_pump_power_consumption + ashpc2_air_source_heat_pump_power_consumption + ashpc3_air_source_heat_pump_power_consumption + ashpc4_air_source_heat_pump_power_consumption + ashpc1_auxiliary_equipment_power_consumption + ashpc2_auxiliary_equipment_power_consumption + ashpc3_auxiliary_equipment_power_consumption + ashpc4_auxiliary_equipment_power_consumption
                total_power_consumption.append(ashpc_power_consumption_total)
                # 计算4个设备的总补水量
                ashpc1_water_supply = air_source_heat_pump_cost_cold(ashpc1, gc, ashpc1_load_ratio)[2]
                ashpc2_water_supply = air_source_heat_pump_cost_cold(ashpc2, gc, ashpc2_load_ratio)[2]
                ashpc3_water_supply = air_source_heat_pump_cost_cold(ashpc3, gc, ashpc3_load_ratio)[2]
                ashpc4_water_supply = air_source_heat_pump_cost_cold(ashpc4, gc, ashpc4_load_ratio)[2]
                ashpc_water_supply_total = ashpc1_water_supply + ashpc2_water_supply + ashpc3_water_supply + ashpc4_water_supply
                total_water_supply.append(ashpc_water_supply_total)
                # 计算4个设备的成本
                ashpc_cost_total = ashpc_power_consumption_total * gc.buy_electricity_price + ashpc_water_supply_total * gc.water_price
                cost.append(ashpc_cost_total)
                break
        # 增加风冷螺杆热泵数量
        ashpc_num += 1

    # 返回计算结果
    return cost, ashpc1_load_ratio_result, ashpc2_load_ratio_result, ashpc3_load_ratio_result, ashpc4_load_ratio_result, total_power_consumption, total_water_supply


def air_source_heat_pump_result_cold(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4):
    """选择出最合适的风冷螺杆热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans_ashpc[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_ashpc[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ashpc1_ratio = ans_ashpc[1][cost_min_index]
    ashpc2_ratio = ans_ashpc[2][cost_min_index]
    ashpc3_ratio = ans_ashpc[3][cost_min_index]
    ashpc4_ratio = ans_ashpc[4][cost_min_index]
    power_consumption_total = ans_ashpc[5][cost_min_index]
    water_supply_total = ans_ashpc[6][cost_min_index]
    cold_load_out = ashpc1_ratio * ashpc1.cooling_power_rated + ashpc2_ratio * ashpc2.cooling_power_rated + ashpc3_ratio * ashpc3.cooling_power_rated + ashpc4_ratio * ashpc4.cooling_power_rated

    return ashpc1_ratio, ashpc2_ratio, ashpc3_ratio, ashpc4_ratio, cold_load_out, power_consumption_total, water_supply_total


def air_source_heat_pump_cost_cold(ashpc, gc, load_ratio):
    """风冷螺杆热泵组运行成本计算"""
    # 冷冻水流量,某一负荷率条件下
    chilled_water_flow = ashpc.chilled_water_flow(load_ratio)
    # 计算此时的风冷螺杆热泵冷冻水出口温度
    chilled_water_temperature = gc.chilled_water_temperature
    # 风冷螺杆热泵制冷COP,某一负荷率条件下
    air_source_heat_pump_cop = ashpc.air_source_heat_pump_cold_cop(load_ratio, chilled_water_temperature, 30)
    # 风冷螺杆热泵本体耗电功率,某一负荷率条件下
    air_source_heat_pump_power_consumption = ashpc.air_source_heat_pump_cold_power_consumption(load_ratio, air_source_heat_pump_cop)
    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = ashpc.auxiliary_equipment_power_consumption(chilled_water_flow)
    # 风冷螺杆热泵总耗电功率,某一负荷率条件下
    total_power_consumption = air_source_heat_pump_power_consumption + auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 冷冻水补水量,某一负荷率条件下
    air_source_heat_pump_chiller_water_supply = chilled_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下
    total_water_supply = air_source_heat_pump_chiller_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, air_source_heat_pump_power_consumption, chilled_water_flow


def air_source_heat_pump_auxiliary_equipment_cost_cold(ashpc, gc, chilled_water_flow):
    """风冷螺杆热泵辅助设备成本计算"""
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = ashpc.auxiliary_equipment_power_consumption(chilled_water_flow)
    auxiliary_equipment_power_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 返回计算结果
    return auxiliary_equipment_power_consumption, auxiliary_equipment_power_cost


def print_air_source_heat_pump_cold(ans, ashpc1, ashpc2, ashpc3, ashpc4):
    """打印出风冷螺杆热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ashpc1_ratio = ans[1][cost_min_index]
    ashpc2_ratio = ans[2][cost_min_index]
    ashpc3_ratio = ans[3][cost_min_index]
    ashpc4_ratio = ans[4][cost_min_index]
    cold_load_out = ashpc1_ratio * ashpc1.cooling_power_rated + ashpc2_ratio * ashpc2.cooling_power_rated + ashpc3_ratio * ashpc3.cooling_power_rated + ashpc4_ratio * ashpc4.cooling_power_rated
    print("风冷螺杆热泵最低总运行成本为： " + str(cost_min) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashpc1_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(ashpc2_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashpc3_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(ashpc4_ratio) + "\n" + "风冷螺杆热泵总制冷出力为： " + str(cold_load_out))


def test_air_source_heat_pump_function_cold():
    """测试风冷螺杆热泵制冷计算"""
    gc = Global_Constant()
    cold_load = 2800
    ashpc_wp = False
    ashpc1_wp_chilled_water = Water_Pump(150, ashpc_wp, 35, gc)
    ashpc2_wp_chilled_water = Water_Pump(150, ashpc_wp, 35, gc)
    ashpc3_wp_chilled_water = Water_Pump(150, ashpc_wp, 35, gc)
    ashpc4_wp_chilled_water = Water_Pump(150, ashpc_wp, 35, gc)
    ashpc1 = Air_Source_Heat_Pump_Cold(767, 0.2, False, ashpc1_wp_chilled_water, gc)
    ashpc2 = Air_Source_Heat_Pump_Cold(767, 0.2, False, ashpc2_wp_chilled_water, gc)
    ashpc3 = Air_Source_Heat_Pump_Cold(767, 0.2, False, ashpc3_wp_chilled_water, gc)
    ashpc4 = Air_Source_Heat_Pump_Cold(767, 0.2, False, ashpc4_wp_chilled_water, gc)

    ans = air_source_heat_pump_function_cold(cold_load, ashpc1, ashpc2, ashpc3, ashpc4, gc)
    print_air_source_heat_pump_cold(ans, ashpc1, ashpc2, ashpc3, ashpc4)

# test_air_source_heat_pump_function_cold()