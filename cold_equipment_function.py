from centrifugal_chiller_function import centrifugal_chiller_function as ccf, centrifugal_chiller_result as ccr
from air_source_heat_pump_cold_function import air_source_heat_pump_function_cold as ashpfc, air_source_heat_pump_result_cold as ashprc


def cold_equipment_function(cold_load_a, cc1, cc2, cc3, cc4, ashpc1, ashpc2, ashpc3, ashpc4,
                                      environment_temperature, chilled_water_temperature, gc):
    """制冷季纯设备(离心式冷水机+空气源热泵)优化运行计算"""

    # 离心式冷水机制冷总功率
    cc_cooling_power_rated_sum = cc1.cooling_power_rated + cc2.cooling_power_rated + cc3.cooling_power_rated + cc4.cooling_power_rated
    # 空气源热泵制冷总功率
    ashpc_cooling_power_rated_sum = ashpc1.cooling_power_rated + ashpc2.cooling_power_rated + ashpc3.cooling_power_rated + ashpc4.cooling_power_rated

    # cold_load_a:冷负荷初始值，如果初始值大于冷水机的总制冷率，则修正初始值
    # 对cold_load_a进行判断
    if cold_load_a >= cc_cooling_power_rated_sum + ashpc_cooling_power_rated_sum:
        cold_load_equipment = cc_cooling_power_rated_sum + ashpc_cooling_power_rated_sum
    else:
        cold_load_equipment = cold_load_a

    # 申明一个列表，储存计算出的总成本
    cost = []
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
    # 列表，储存输入输出
    cold_out_total = []
    power_consumption_total = []
    water_supply_total = []

    # 将需要的冷负荷分配给离心式冷水机（包括离心式热泵）和空气源热泵
    # 建立循环，对冷负荷进行分配
    # 控制循环的变量是离心式冷水机提供的冷负荷
    cold_load_cc_now = 0
    while cold_load_cc_now <= min(cold_load_equipment, cc_cooling_power_rated_sum):
        # 离心式冷水机需要补充的冷负荷
        cold_load_cc_1 = min(cold_load_cc_now, cc_cooling_power_rated_sum)
        cold_load_cc = max(cold_load_cc_1, 0)
        # 空气源热泵需要补充的冷负荷
        cold_load_ashpc_1 = min(cold_load_equipment - cold_load_cc, ashpc_cooling_power_rated_sum)
        cold_load_ashpc = max(cold_load_ashpc_1, 0)

        # 如果此时只有内燃机，且内燃机负荷率和设定的冷负荷相差很小，则跳出循环
        if cold_load_cc >= 0 and abs(cold_load_cc) <= gc.project_load_error:
            # 离心式冷水机不进行计算
            cc_calculate = False
        else:
            # 离心式冷水机进行计算
            cc_calculate = True
        if cold_load_cc >= 0 and cc_calculate == True and cold_load_cc + cold_load_ashpc >= cold_load_equipment:
            # 计算离心式冷水机的运行策略
            ans_cc = ccf(cold_load_cc, cc1, cc2, cc3, cc4, chilled_water_temperature, gc)
            # 此时4台设备的负荷率
            cc1_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[0]
            cc2_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[1]
            cc3_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[2]
            cc4_load_ratio = ccr(ans_cc, cc1, cc2, cc3, cc4)[3]
            # 读取此时的冷水机最优计算结果耗电功率
            cc_power_consumption_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[5]
            # 读取此时的冷水机最优计算结果的供冷功率
            cc_cold_out_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[4]
            # 冷水机补水总量
            cc_water_supply_total = ccr(ans_cc, cc1, cc2, cc3, cc4)[6]
        else:
            # 离心式冷水机负荷率都设置为0
            cc1_load_ratio = 0
            cc2_load_ratio = 0
            cc3_load_ratio = 0
            cc4_load_ratio = 0
            # 离心式冷水机的输入输出量
            cc_power_consumption_total = 0
            cc_cold_out_total = 0
            cc_water_supply_total = 0

        # 判断空气源热泵是否需要计算
        if cold_load_ashpc >= 0 and abs(cold_load_ashpc) <= gc.project_load_error:
            # 风冷螺杆热泵不进行计算
            ashpc_calculate = False
        else:
            # 风冷螺杆热泵进行计算
            ashpc_calculate = True
        if cold_load_ashpc >= 0 and ashpc_calculate == True and cold_load_cc + cold_load_ashpc >= cold_load_equipment:
            # 计算风冷螺杆热泵的运行策略
            ans_ashpc = ashpfc(cold_load_ashpc, ashpc1, ashpc2, ashpc3, ashpc4, environment_temperature,
                               chilled_water_temperature, gc)
            # 此时4台设备的负荷率
            ashpc1_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[0]
            ashpc2_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[1]
            ashpc3_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[2]
            ashpc4_load_ratio = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[3]
            # 读取此时的冷水机最优计算结果耗电功率
            ashpc_power_consumption_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[5]
            # 读取此时的冷水机最优计算结果的供冷功率
            ashpc_cold_out_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[4]
            # 补水总量
            ashpc_water_supply_total = ashprc(ans_ashpc, ashpc1, ashpc2, ashpc3, ashpc4)[6]
        else:
            # 风冷螺杆热泵负荷率都设置为0
            ashpc1_load_ratio = 0
            ashpc2_load_ratio = 0
            ashpc3_load_ratio = 0
            ashpc4_load_ratio = 0
            # 风冷螺杆热泵的输入输出量
            ashpc_power_consumption_total = 0
            ashpc_cold_out_total = 0
            ashpc_water_supply_total = 0

        # 制冷设备收入成本合计
        cold_out_equipment_total = cc_cold_out_total + ashpc_cold_out_total
        power_consumption_equipment_total = cc_power_consumption_total + ashpc_power_consumption_total
        water_supply_equipment_total = cc_water_supply_total + ashpc_water_supply_total
        # 求成本
        cost_total = power_consumption_equipment_total * gc.buy_electricity_price + water_supply_equipment_total * gc.water_price

        # 将满足要求的结果存入列表
        if cold_out_equipment_total >= cold_load_equipment:
            # 离心式冷水机负荷率
            cc1_load_ratio_result.append(cc1_load_ratio)
            cc2_load_ratio_result.append(cc2_load_ratio)
            cc3_load_ratio_result.append(cc3_load_ratio)
            cc4_load_ratio_result.append(cc4_load_ratio)
            # 空气源热泵负荷率
            ashpc1_load_ratio_result.append(ashpc1_load_ratio)
            ashpc2_load_ratio_result.append(ashpc2_load_ratio)
            ashpc3_load_ratio_result.append(ashpc3_load_ratio)
            ashpc4_load_ratio_result.append(ashpc4_load_ratio)
            # 输入输出
            cold_out_total.append(cold_out_equipment_total)
            power_consumption_total.append(power_consumption_equipment_total)
            water_supply_total.append(water_supply_equipment_total)
            # 成本
            cost.append(cost_total)

        # 离心式冷水机供冷功率往上加
        cold_load_cc_now += cold_load_equipment / gc.num_allocations_load

    # 返回结果
    return cost, cc1_load_ratio_result, cc2_load_ratio_result, cc3_load_ratio_result, cc4_load_ratio_result, \
           ashpc1_load_ratio_result, ashpc2_load_ratio_result, ashpc3_load_ratio_result, ashpc4_load_ratio_result, \
           cold_out_total, power_consumption_total, water_supply_total


def cold_equipment_result(ans, cc1, cc2, cc3, cc4, ashpc1, ashpc2, ashpc3, ashpc4):
    """找出最合适的计算结果"""
    try:
        # 总成本最小值
        cost_min = min(ans[0])
        # 记录总成本最小值的列表索引
        cost_min_index = ans[0].index(cost_min)
        # 读取对应索引下的设备负荷率
        cc1_ratio = ans[1][cost_min_index]
        cc2_ratio = ans[2][cost_min_index]
        cc3_ratio = ans[3][cost_min_index]
        cc4_ratio = ans[4][cost_min_index]
        ashpc1_ratio = ans[5][cost_min_index]
        ashpc2_ratio = ans[6][cost_min_index]
        ashpc3_ratio = ans[7][cost_min_index]
        ashpc4_ratio = ans[8][cost_min_index]
        power_consumption_total = ans[10][cost_min_index]
        water_supply_total = ans[11][cost_min_index]
    except:
        # 读取对应索引下的设备负荷率
        cc1_ratio = 0
        cc2_ratio = 0
        cc3_ratio = 0
        cc4_ratio = 0
        ashpc1_ratio = 0
        ashpc2_ratio = 0
        ashpc3_ratio = 0
        ashpc4_ratio = 0
        power_consumption_total = 0
        water_supply_total = 0

    cold_load_out = cc1_ratio * cc1.cooling_power_rated + cc2_ratio * cc2.cooling_power_rated + cc3_ratio * cc3.cooling_power_rated + \
                    cc4_ratio * cc4.cooling_power_rated + ashpc1_ratio * ashpc1.cooling_power_rated + ashpc2_ratio * ashpc2.cooling_power_rated \
                    + ashpc3_ratio * ashpc3.cooling_power_rated + ashpc4_ratio * ashpc4.cooling_power_rated

    # 返回计算结果
    return cc1_ratio, cc2_ratio, cc3_ratio, cc4_ratio, ashpc1_ratio, ashpc2_ratio, ashpc3_ratio, ashpc4_ratio,\
           cold_load_out, power_consumption_total, water_supply_total

def print_cold_equipment_result(ans, cc1, cc2, cc3, cc4, ashpc1, ashpc2, ashpc3, ashpc4):
    """打印出最合适的计算结果"""
    try:
        # 总成本最小值
        cost_min = min(ans[0])
        # 记录总成本最小值的列表索引
        cost_min_index = ans[0].index(cost_min)
        # 读取对应索引下的设备负荷率
        cc1_ratio = ans[1][cost_min_index]
        cc2_ratio = ans[2][cost_min_index]
        cc3_ratio = ans[3][cost_min_index]
        cc4_ratio = ans[4][cost_min_index]
        ashpc1_ratio = ans[5][cost_min_index]
        ashpc2_ratio = ans[6][cost_min_index]
        ashpc3_ratio = ans[7][cost_min_index]
        ashpc4_ratio = ans[8][cost_min_index]
    except:
        # 读取对应索引下的设备负荷率
        cost_min = 0
        cc1_ratio = 0
        cc2_ratio = 0
        cc3_ratio = 0
        cc4_ratio = 0
        ashpc1_ratio = 0
        ashpc2_ratio = 0
        ashpc3_ratio = 0
        ashpc4_ratio = 0

    cold_load_out = cc1_ratio * cc1.cooling_power_rated + cc2_ratio * cc2.cooling_power_rated + cc3_ratio * cc3.cooling_power_rated + \
                    cc4_ratio * cc4.cooling_power_rated + ashpc1_ratio * ashpc1.cooling_power_rated + ashpc2_ratio * ashpc2.cooling_power_rated \
                    + ashpc3_ratio * ashpc3.cooling_power_rated + ashpc4_ratio * ashpc4.cooling_power_rated

    print("制冷设备最低总运行成本为： " + str(cost_min) + "\n" + "离心式冷水机1负荷率为： " + str(cc1_ratio) + "\n"
          + "离心式冷水机2负荷率为： " + str(cc2_ratio) + "\n" + "离心式冷水机3负荷率为： " + str(cc3_ratio) + "\n"
          + "离心式冷水机4负荷率为： " + str(cc4_ratio) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashpc1_ratio) + "\n"
          + "风冷螺杆热泵2负荷率为： " + str(ashpc2_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashpc3_ratio) + "\n"
          + "风冷螺杆热泵4负荷率为： " + str(ashpc4_ratio) + "\n" + "制冷设备总制冷出力为： " + str(cold_load_out))


