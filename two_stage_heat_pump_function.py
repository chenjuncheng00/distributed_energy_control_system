from centrifugal_heat_pump_heat_function import centrifugal_heat_pump_function_heat as chphfh, centrifugal_heat_pump_result_heat as chphrh
from air_source_heat_pump_heat_function import air_source_heat_pump_function_heat as ashpfh, air_source_heat_pump_result_heat as ashprh

def two_stage_heat_pump_function(heat_load_a, chph1, chph2, chph3, chph4, ashph1, ashph2, ashph3, ashph4,
                   environment_temperature, heating_water_temperature, ashp_heat_source_water_temperature, gc):
    """两级热泵制热计算"""

    # heat_load_a:热负荷初始值，如果初始值大于热水机的总制热率，则修正初始值
    # 对heat_load_a进行判断
    if heat_load_a >= chph1.heating_power_rated + chph2.heating_power_rated + chph3.heating_power_rated + chph4.heating_power_rated:
        heat_load = chph1.heating_power_rated + chph2.heating_power_rated + chph3.heating_power_rated + chph4.heating_power_rated
    else:
        heat_load = heat_load_a

    # 在采暖季制热时，空气源热泵作为一级低温热源，离心式热泵作为二级热源，向外供热
    # 使用计算出离心式热泵的运行模式，将heat_load带入相关模块进行计算
    ans_chph = chphfh(heat_load, chph1, chph2, chph3, chph4, heating_water_temperature, gc)
    # 选择最佳结果
    chph1_load_ratio = chphrh(ans_chph, chph1, chph2, chph3, chph4)[0]
    chph2_load_ratio = chphrh(ans_chph, chph1, chph2, chph3, chph4)[1]
    chph3_load_ratio = chphrh(ans_chph, chph1, chph2, chph3, chph4)[2]
    chph4_load_ratio = chphrh(ans_chph, chph1, chph2, chph3, chph4)[3]
    chph_heat_out_total = chphrh(ans_chph, chph1, chph2, chph3, chph4)[4]
    chph_power_consumption_total = chphrh(ans_chph, chph1, chph2, chph3, chph4)[5]
    chph_water_supply_total = chphrh(ans_chph, chph1, chph2, chph3, chph4)[6]
    # 分别计算此时离心式热泵的制热COP
    chph1_cop = chph1.centrifugal_heat_pump_cop(chph1_load_ratio, heating_water_temperature, 25)
    chph2_cop = chph2.centrifugal_heat_pump_cop(chph2_load_ratio, heating_water_temperature, 25)
    chph3_cop = chph3.centrifugal_heat_pump_cop(chph3_load_ratio, heating_water_temperature, 25)
    chph4_cop = chph4.centrifugal_heat_pump_cop(chph4_load_ratio, heating_water_temperature, 25)
    # 计算此时的设备本体耗电功率
    chph1_electric_power = chph1.heating_power_rated * chph1_load_ratio / chph1_cop
    chph2_electric_power = chph1.heating_power_rated * chph2_load_ratio / chph2_cop
    chph3_electric_power = chph1.heating_power_rated * chph3_load_ratio / chph3_cop
    chph4_electric_power = chph1.heating_power_rated * chph4_load_ratio / chph4_cop
    # 计算此时设备需要的低温热源功率
    chph1_heat_source = chph1.heating_power_rated * chph1_load_ratio - chph1_electric_power
    chph2_heat_source = chph2.heating_power_rated * chph2_load_ratio - chph2_electric_power
    chph3_heat_source = chph3.heating_power_rated * chph3_load_ratio - chph3_electric_power
    chph4_heat_source = chph4.heating_power_rated * chph4_load_ratio - chph4_electric_power
    # 计算此时一级低温热源总热功率
    ashp_heat_power = chph1_heat_source + chph2_heat_source + chph3_heat_source + chph4_heat_source
    # 计算此时空气源热泵的运行策略
    ans_ashp = ashpfh(ashp_heat_power, ashph1, ashph2, ashph3, ashph4, environment_temperature, ashp_heat_source_water_temperature, gc)
    # 选择空气源热泵最优运行策略
    ashph1_load_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[0]
    ashph2_load_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[1]
    ashph3_load_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[2]
    ashph4_load_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[3]
    ashph_power_consumption_total = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[5]
    ashph_water_supply_total = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[6]
    # 两级热泵消耗量汇总
    power_consumption_total = chph_power_consumption_total + ashph_power_consumption_total
    water_supply_total = chph_water_supply_total + ashph_water_supply_total
    # 总成本计算
    cost_total = power_consumption_total * gc.buy_electricity_price + water_supply_total * gc.water_price

    # 返回计算结果
    return cost_total, chph_heat_out_total, power_consumption_total, water_supply_total, chph1_load_ratio, chph2_load_ratio, chph3_load_ratio, chph4_load_ratio, ashph1_load_ratio, ashph2_load_ratio, ashph3_load_ratio, ashph4_load_ratio, chph_power_consumption_total, ashph_power_consumption_total, chph_water_supply_total, ashph_water_supply_total

def print_two_stage_heat_pump_function(ans):
    """打印出两级热泵的计算结果"""
    cost_total = ans[0]
    chph_heat_out_total = ans[1]
    power_consumption_total = ans[2]
    water_supply_total = ans[3]
    chph1_load_ratio = ans[4]
    chph2_load_ratio = ans[5]
    chph3_load_ratio = ans[6]
    chph4_load_ratio = ans[7]
    ashph1_load_ratio = ans[8]
    ashph2_load_ratio = ans[9]
    ashph3_load_ratio = ans[10]
    ashph4_load_ratio = ans[11]
    chph_power_consumption_total = ans[12]
    ashph_power_consumption_total = ans[13]
    chph_water_supply_total = ans[14]
    ashph_water_supply_total = ans[15]

    print("双级热泵最低总运行成本为： " + str(cost_total) + "\n" + "双级热泵总制热出力为： " + str(
        chph_heat_out_total) + "\n" + "双级热泵最低总耗电功率为： " + str(power_consumption_total) + "\n" + "双级热泵总补水量为： " + str(
        water_supply_total) + "\n" + "离心式热泵1负荷率为： " + str(chph1_load_ratio) + "\n" + "离心式热泵2负荷率为： " + str(
        chph2_load_ratio) + "\n" + "离心式热泵3负荷率为： " + str(chph3_load_ratio) + "\n" + "离心式热泵4负荷率为： " + str(
        chph4_load_ratio) + "\n" + "离心式热泵最低总耗电功率为： " + str(chph_power_consumption_total) + "\n" + "离心式热泵热泵总补水量为： " + str(
        chph_water_supply_total) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashph1_load_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(
        ashph2_load_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashph3_load_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(
        ashph4_load_ratio) + "\n" + "风冷螺杆热泵最低总耗电功率为： " + str(ashph_power_consumption_total) + "\n" + "风冷螺杆热泵热泵总补水量为： " + str(
        ashph_water_supply_total) + "\n")
