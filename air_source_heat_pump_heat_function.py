import math
from equipment import Air_Source_Heat_Pump_Heat, Water_Pump
from global_constant import Global_Constant

def air_source_heat_pump_function_heat(heat_load, ashph1, ashph2, ashph3, ashph4, gc):
    """风冷螺杆热泵制热负荷计算函数"""
    # 制热，制热，制热
    # 风冷螺杆热泵组与水泵的布置方式，header_system（母管制）
    # 不同管道布置方式的风冷螺杆热泵计算
    # 母管制系统计算（水泵与风冷螺杆热泵组不是一对一布置）
    # 获取4台风冷螺杆热泵是否为变频，根据是否为变频，设置不同的计算步长
    # 风冷螺杆热泵1
    if ashph1.frequency_scaling == True:
        ashph1_step = 1
    else:
        ashph1_step = 10
    # 风冷螺杆热泵2
    if ashph2.frequency_scaling == True:
        ashph2_step = 1
    else:
        ashph2_step = 10
    # 风冷螺杆热泵3
    if ashph3.frequency_scaling == True:
        ashph3_step = 1
    else:
        ashph3_step = 10
    # 风冷螺杆热泵4
    if ashph4.frequency_scaling == True:
        ashph4_step = 1
    else:
        ashph4_step = 10

    # 列表，储存4台设备计算出的负荷率结果
    ashph_load_ratio_result_all = [0, 0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存4台风冷螺杆热泵的总耗电功率
    total_power_consumption = []
    # 列表， 储存4台风冷螺杆热泵的总补水量
    total_water_supply = []
    # 列表，储存4台设备计算出的负荷率结果
    ashph1_load_ratio_result = []
    ashph2_load_ratio_result = []
    ashph3_load_ratio_result = []
    ashph4_load_ratio_result = []

    # 确定需要几台设备，向上取整（风冷螺杆热泵可以启动的最大数量）
    ashph_num_max_2 = math.ceil(heat_load / ashph1.heating_power_rated)
    # 如果恰好整除，则向上加1
    if ashph_num_max_2 ==int(ashph_num_max_2):
        ashph_num_max_1 = ashph_num_max_2 + 1
    else:
        ashph_num_max_1 = ashph_num_max_2
    # 最大数量不可以超过4
    if ashph_num_max_1 > 4:
        ashph_num_max = 4
    else:
        ashph_num_max = ashph_num_max_1

    # 风冷螺杆热泵启动数量初始值
    ashph_num = 1

    while ashph_num <= ashph_num_max:
        # 初始化设备1、2、3、4的负荷率
        if ashph_num >= 1:
            ashph1_load_ratio = ashph1.load_min
        else:
            ashph1_load_ratio = 0
        if ashph_num >= 2:
            ashph2_load_ratio = ashph2.load_min
        else:
            ashph2_load_ratio = 0
        if ashph_num >= 3:
            ashph3_load_ratio = ashph3.load_min
        else:
            ashph3_load_ratio = 0
        if ashph_num >= 4:
            ashph4_load_ratio = ashph4.load_min
        else:
            ashph4_load_ratio = 0
        # 计算风冷螺杆热泵设备
        while ashph1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算4个设备的制热出力
            ashph1_heat_out_now = ashph1_load_ratio * ashph1.heating_power_rated
            ashph2_heat_out_now = ashph2_load_ratio * ashph2.heating_power_rated
            ashph3_heat_out_now = ashph3_load_ratio * ashph3.heating_power_rated
            ashph4_heat_out_now = ashph4_load_ratio * ashph4.heating_power_rated
            ashph_heat_out_now_sum = ashph1_heat_out_now + ashph2_heat_out_now + ashph3_heat_out_now + ashph4_heat_out_now
            # print(ashph_num, ashph1_heat_out_now, ashph2_heat_out_now, ashph3_heat_out_now, ashph4_heat_out_now)
            if ashph_heat_out_now_sum < heat_load:
                # 增加设备1、2、3、4负荷率
                if ashph_num >= 1:
                    ashph1_load_ratio += ashph1_step / 100
                else:
                    ashph1_load_ratio = 0
                if ashph_num >= 2:
                    ashph2_load_ratio += ashph2_step / 100
                else:
                    ashph2_load_ratio = 0
                if ashph_num >= 3:
                    ashph3_load_ratio += ashph3_step / 100
                else:
                    ashph3_load_ratio = 0
                if ashph_num >= 4:
                    ashph4_load_ratio += ashph4_step / 100
                else:
                    ashph4_load_ratio = 0
            else:
                # 保存4个设备的负荷率
                ashph_load_ratio_result_all[0] = ashph1_load_ratio
                ashph_load_ratio_result_all[1] = ashph2_load_ratio
                ashph_load_ratio_result_all[2] = ashph3_load_ratio
                ashph_load_ratio_result_all[3] = ashph4_load_ratio
                ashph1_load_ratio_result.append(ashph_load_ratio_result_all[0])
                ashph2_load_ratio_result.append(ashph_load_ratio_result_all[1])
                ashph3_load_ratio_result.append(ashph_load_ratio_result_all[2])
                ashph4_load_ratio_result.append(ashph_load_ratio_result_all[3])
                # 计算4个设备本体的总耗电功率（仅设备本体耗电）
                ashph1_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_heat(ashph1, gc, ashph1_load_ratio)[3]
                ashph2_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_heat(ashph2, gc, ashph2_load_ratio)[3]
                ashph3_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_heat(ashph3, gc, ashph3_load_ratio)[3]
                ashph4_air_source_heat_pump_power_consumption = air_source_heat_pump_cost_heat(ashph4, gc, ashph4_load_ratio)[3]
                # 计算4个设备的采暖水流量、低温热源水流量
                # 采暖水总流量
                heating_water_flow_total = air_source_heat_pump_cost_heat(ashph1, gc, ashph1_load_ratio)[4] + air_source_heat_pump_cost_heat(ashph2, gc, ashph2_load_ratio)[4] + air_source_heat_pump_cost_heat(ashph3, gc, ashph3_load_ratio)[4] + air_source_heat_pump_cost_heat(ashph4, gc, ashph4_load_ratio)[4]
                # 每个水泵的流量为总流量均分（后期可细化流量分配比例）
                ashph1_heating_water_flow = heating_water_flow_total / ashph_num
                ashph2_heating_water_flow = heating_water_flow_total / ashph_num
                ashph3_heating_water_flow = heating_water_flow_total / ashph_num
                ashph4_heating_water_flow = heating_water_flow_total / ashph_num
                # 辅助设备耗电功率
                ashph1_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_heat(ashph1, gc, ashph1_heating_water_flow)[0]
                ashph2_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_heat(ashph2, gc, ashph2_heating_water_flow)[0]
                ashph3_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_heat(ashph3, gc, ashph3_heating_water_flow)[0]
                ashph4_auxiliary_equipment_power_consumption = air_source_heat_pump_auxiliary_equipment_cost_heat(ashph4, gc, ashph4_heating_water_flow)[0]
                # 耗电量总计
                ashph_power_consumption_total = ashph1_air_source_heat_pump_power_consumption + ashph2_air_source_heat_pump_power_consumption + ashph3_air_source_heat_pump_power_consumption + ashph4_air_source_heat_pump_power_consumption + ashph1_auxiliary_equipment_power_consumption + ashph2_auxiliary_equipment_power_consumption + ashph3_auxiliary_equipment_power_consumption + ashph4_auxiliary_equipment_power_consumption
                total_power_consumption.append(ashph_power_consumption_total)
                # 计算4个设备的总补水量
                ashph1_water_supply = air_source_heat_pump_cost_heat(ashph1, gc, ashph1_load_ratio)[2]
                ashph2_water_supply = air_source_heat_pump_cost_heat(ashph2, gc, ashph2_load_ratio)[2]
                ashph3_water_supply = air_source_heat_pump_cost_heat(ashph3, gc, ashph3_load_ratio)[2]
                ashph4_water_supply = air_source_heat_pump_cost_heat(ashph4, gc, ashph4_load_ratio)[2]
                ashph_water_supply_total = ashph1_water_supply + ashph2_water_supply + ashph3_water_supply + ashph4_water_supply
                total_water_supply.append(ashph_water_supply_total)
                # 计算4个设备的成本
                ashph_cost_total = ashph_power_consumption_total * gc.buy_electricity_price + ashph_water_supply_total * gc.water_price
                cost.append(ashph_cost_total)
                break
        # 增加风冷螺杆热泵数量
        ashph_num += 1

    # 返回计算结果
    return cost, ashph1_load_ratio_result, ashph2_load_ratio_result, ashph3_load_ratio_result, ashph4_load_ratio_result, total_power_consumption, total_water_supply


def air_source_heat_pump_result_heat(ans_ashph, ashph1, ashph2, ashph3, ashph4):
    """选择出最合适的风冷螺杆热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans_ashph[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_ashph[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ashph1_ratio = ans_ashph[1][cost_min_index]
    ashph2_ratio = ans_ashph[2][cost_min_index]
    ashph3_ratio = ans_ashph[3][cost_min_index]
    ashph4_ratio = ans_ashph[4][cost_min_index]
    power_consumption_total = ans_ashph[5][cost_min_index]
    water_supply_total = ans_ashph[6][cost_min_index]
    heat_load_out = ashph1_ratio * ashph1.heating_power_rated + ashph2_ratio * ashph2.heating_power_rated + ashph3_ratio * ashph3.heating_power_rated + ashph4_ratio * ashph4.heating_power_rated

    return ashph1_ratio, ashph2_ratio, ashph3_ratio, ashph4_ratio, heat_load_out, power_consumption_total, water_supply_total


def air_source_heat_pump_cost_heat(ashph, gc, load_ratio):
    """风冷螺杆热泵组运行成本计算"""
    # 采暖水流量,某一负荷率条件下
    heating_water_flow = ashph.heating_water_flow(load_ratio)
    # 计算此时的风冷螺杆热泵采暖水出口温度
    heating_water_temperature = gc.heating_water_temperature
    # 风冷螺杆热泵制热COP,某一负荷率条件下
    air_source_heat_pump_cop = ashph.air_source_heat_pump_heat_cop(load_ratio, heating_water_temperature, gc.environment_temperature)
    # 风冷螺杆热泵本体耗电功率,某一负荷率条件下
    air_source_heat_pump_power_consumption = ashph.air_source_heat_pump_heat_power_consumption(load_ratio, air_source_heat_pump_cop)
    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = ashph.auxiliary_equipment_power_consumption(heating_water_flow)
    # 风冷螺杆热泵总耗电功率,某一负荷率条件下
    total_power_consumption = air_source_heat_pump_power_consumption + auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 采暖水补水量,某一负荷率条件下
    air_source_heat_pump_chiller_water_supply = heating_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下
    total_water_supply = air_source_heat_pump_chiller_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, air_source_heat_pump_power_consumption, heating_water_flow


def air_source_heat_pump_auxiliary_equipment_cost_heat(ashph, gc, heating_water_flow):
    """风冷螺杆热泵辅助设备成本计算"""
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = ashph.auxiliary_equipment_power_consumption(heating_water_flow)
    auxiliary_equipment_power_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 返回计算结果
    return auxiliary_equipment_power_consumption, auxiliary_equipment_power_cost


def print_air_source_heat_pump_heat(ans, ashph1, ashph2, ashph3, ashph4):
    """打印出风冷螺杆热泵的计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ashph1_ratio = ans[1][cost_min_index]
    ashph2_ratio = ans[2][cost_min_index]
    ashph3_ratio = ans[3][cost_min_index]
    ashph4_ratio = ans[4][cost_min_index]
    heat_load_out = ashph1_ratio * ashph1.heating_power_rated + ashph2_ratio * ashph2.heating_power_rated + ashph3_ratio * ashph3.heating_power_rated + ashph4_ratio * ashph4.heating_power_rated
    print("风冷螺杆热泵最低总运行成本为： " + str(cost_min) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashph1_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(ashph2_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashph3_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(ashph4_ratio) + "\n" + "风冷螺杆热泵总制热出力为： " + str(heat_load_out))


def test_air_source_heat_pump_function_heat():
    """测试风冷螺杆热泵制热计算"""
    gc = Global_Constant()
    heat_load = 2000
    ashph_wp = False
    ashph1_wp_heating_water = Water_Pump(150, ashph_wp, 35, gc)
    ashph2_wp_heating_water = Water_Pump(150, ashph_wp, 35, gc)
    ashph3_wp_heating_water = Water_Pump(150, ashph_wp, 35, gc)
    ashph4_wp_heating_water = Water_Pump(150, ashph_wp, 35, gc)
    ashph1 = Air_Source_Heat_Pump_Heat(760, 0.2, False, ashph1_wp_heating_water, gc)
    ashph2 = Air_Source_Heat_Pump_Heat(760, 0.2, False, ashph2_wp_heating_water, gc)
    ashph3 = Air_Source_Heat_Pump_Heat(760, 0.2, False, ashph3_wp_heating_water, gc)
    ashph4 = Air_Source_Heat_Pump_Heat(760, 0.2, False, ashph4_wp_heating_water, gc)

    ans = air_source_heat_pump_function_heat(heat_load, ashph1, ashph2, ashph3, ashph4, gc)
    print_air_source_heat_pump_heat(ans, ashph1, ashph2, ashph3, ashph4)

# test_air_source_heat_pump_function_heat()