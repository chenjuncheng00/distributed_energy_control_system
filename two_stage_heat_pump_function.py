import math
from equipment import Centrifugal_Heat_Pump, Air_Source_Heat_Pump_Heat, Water_Pump
from centrifugal_heat_pump_function import centrifugal_heat_pump_function_heat as chpfh, centrifugal_heat_pump_result_heat as chprh
from air_source_heat_pump_heat_function import air_source_heat_pump_function_heat as ashpfh, air_source_heat_pump_result_heat as ashprh
from global_constant import Global_Constant

def two_stage_heat_pump_function(heat_load, chp1, chp2, chp3, chp4, ashph1, ashph2, ashph3, ashph4, gc):
    """两级热泵制热计算"""
    # 在采暖季制热时，空气源热泵作为一级低温热源，离心式热泵作为二级热源，向外供热
    # 使用计算出离心式热泵的运行模式，将heat_load带入相关模块进行计算
    ans_chp = chpfh(heat_load, chp1, chp2, chp3, chp4, gc)
    # 选择最佳结果
    chp1_ratio = chprh(ans_chp, chp1, chp2, chp3, chp4)[0]
    chp2_ratio = chprh(ans_chp, chp1, chp2, chp3, chp4)[1]
    chp3_ratio = chprh(ans_chp, chp1, chp2, chp3, chp4)[2]
    chp4_ratio = chprh(ans_chp, chp1, chp2, chp3, chp4)[3]
    chp_heat_load_out = chprh(ans_chp, chp1, chp2, chp3, chp4)[4]
    chp_power_consumption_total = chprh(ans_chp, chp1, chp2, chp3, chp4)[5]
    chp_water_supply_total = chprh(ans_chp, chp1, chp2, chp3, chp4)[6]
    # 分别计算此时离心式热泵的制热COP
    chp1_cop = chp1.centrifugal_heat_pump_cop(chp1_ratio, gc.heating_water_temperature, 25)
    chp2_cop = chp2.centrifugal_heat_pump_cop(chp2_ratio, gc.heating_water_temperature, 25)
    chp3_cop = chp3.centrifugal_heat_pump_cop(chp3_ratio, gc.heating_water_temperature, 25)
    chp4_cop = chp4.centrifugal_heat_pump_cop(chp4_ratio, gc.heating_water_temperature, 25)
    # 计算此时的设备本体耗电功率
    chp1_electric_power = chp1.heating_power_rated * chp1_ratio / chp1_cop
    chp2_electric_power = chp1.heating_power_rated * chp2_ratio / chp2_cop
    chp3_electric_power = chp1.heating_power_rated * chp3_ratio / chp3_cop
    chp4_electric_power = chp1.heating_power_rated * chp4_ratio / chp4_cop
    # 计算此时设备需要的低温热源功率
    chp1_heat_source = chp1.heating_power_rated * chp1_ratio - chp1_electric_power
    chp2_heat_source = chp2.heating_power_rated * chp2_ratio - chp2_electric_power
    chp3_heat_source = chp3.heating_power_rated * chp3_ratio - chp3_electric_power
    chp4_heat_source = chp4.heating_power_rated * chp4_ratio - chp4_electric_power
    # 计算此时一级低温热源总热功率
    ashp_heat_power = chp1_heat_source + chp2_heat_source + chp3_heat_source + chp4_heat_source
    # 计算此时空气源热泵的运行策略
    ans_ashp = ashpfh(ashp_heat_power, ashph1, ashph2, ashph3, ashph4, gc)
    # 选择空气源热泵最优运行策略
    ashph1_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[0]
    ashph2_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[1]
    ashph3_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[2]
    ashph4_ratio = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[3]
    ashph_power_consumption_total = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[5]
    ashph_water_supply_total = ashprh(ans_ashp, ashph1, ashph2, ashph3, ashph4)[6]
    # 两级热泵消耗量汇总
    power_consumption_total = chp_power_consumption_total + ashph_power_consumption_total
    water_supply_total = chp_water_supply_total + ashph_water_supply_total
    # 总成本计算
    cost_total = power_consumption_total * gc.buy_electricity_price + water_supply_total * gc.water_price

    # 返回计算结果
    return cost_total, chp_heat_load_out, power_consumption_total, water_supply_total, chp1_ratio, chp2_ratio, chp3_ratio, chp4_ratio, ashph1_ratio, ashph2_ratio, ashph3_ratio, ashph4_ratio, chp_power_consumption_total, ashph_power_consumption_total, chp_water_supply_total, ashph_water_supply_total

def print_two_stage_heat_pump_function(ans):
    """打印出两级热泵的计算结果"""
    cost_total = ans[0]
    chp_heat_load_out = ans[1]
    power_consumption_total = ans[2]
    water_supply_total = ans[3]
    chp1_ratio = ans[4]
    chp2_ratio = ans[5]
    chp3_ratio = ans[6]
    chp4_ratio = ans[7]
    ashph1_ratio = ans[8]
    ashph2_ratio = ans[9]
    ashph3_ratio = ans[10]
    ashph4_ratio = ans[11]
    chp_power_consumption_total = ans[12]
    ashph_power_consumption_total = ans[13]
    chp_water_supply_total = ans[14]
    ashph_water_supply_total = ans[15]

    print("双级热泵最低总运行成本为： " + str(cost_total) + "\n" + "双级热泵总制热出力为： " + str(
        chp_heat_load_out) + "\n" + "双级热泵最低总耗电功率为： " + str(power_consumption_total) + "\n" + "双级热泵总补水量为： " + str(
        water_supply_total) + "\n" + "离心式热泵1负荷率为： " + str(chp1_ratio) + "\n" + "离心式热泵2负荷率为： " + str(
        chp2_ratio) + "\n" + "离心式热泵3负荷率为： " + str(chp3_ratio) + "\n" + "离心式热泵4负荷率为： " + str(
        chp4_ratio) + "\n" + "离心式热泵最低总耗电功率为： " + str(chp_power_consumption_total) + "\n" + "离心式热泵热泵总补水量为： " + str(
        chp_water_supply_total) + "\n" + "风冷螺杆热泵1负荷率为： " + str(ashph1_ratio) + "\n" + "风冷螺杆热泵2负荷率为： " + str(
        ashph2_ratio) + "\n" + "风冷螺杆热泵3负荷率为： " + str(ashph3_ratio) + "\n" + "风冷螺杆热泵4负荷率为： " + str(
        ashph4_ratio) + "\n" + "风冷螺杆热泵最低总耗电功率为： " + str(ashph_power_consumption_total) + "\n" + "风冷螺杆热泵热泵总补水量为： " + str(
        ashph_water_supply_total) + "\n")


def test_two_stage_heat_pump_function():
    """测试双级热泵制热"""
    gc = Global_Constant()
    heat_load = 6500
    # 离心式热泵
    chp1_wp_heating_water = Water_Pump(330, True, 35, gc)
    chp2_wp_heating_water = Water_Pump(330, True, 35, gc)
    chp3_wp_heating_water = Water_Pump(0, True, 0, gc)
    chp4_wp_heating_water = Water_Pump(0, True, 0, gc)
    chp1_wp_heat_source_water = Water_Pump(550, True, 35, gc)
    chp2_wp_heat_source_water = Water_Pump(550, True, 35, gc)
    chp3_wp_heat_source_water = Water_Pump(0, True, 0, gc)
    chp4_wp_heat_source_water = Water_Pump(0, True, 0, gc)
    chp1 = Centrifugal_Heat_Pump(3500, 0.2, False, chp1_wp_heating_water, chp1_wp_heat_source_water, gc)
    chp2 = Centrifugal_Heat_Pump(3500, 0.2, False, chp2_wp_heating_water, chp2_wp_heat_source_water, gc)
    chp3 = Centrifugal_Heat_Pump(0, 0.2, False, chp3_wp_heating_water, chp3_wp_heat_source_water, gc)
    chp4 = Centrifugal_Heat_Pump(0, 0.2, False, chp4_wp_heating_water, chp4_wp_heat_source_water, gc)
    # 空气源热泵
    ashph1_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph2_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph3_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph4_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph1 = Air_Source_Heat_Pump_Heat(1640, 0.2, True, ashph1_wp_heating_water, gc)
    ashph2 = Air_Source_Heat_Pump_Heat(1640, 0.2, True, ashph2_wp_heating_water, gc)
    ashph3 = Air_Source_Heat_Pump_Heat(1640, 0.2, True, ashph3_wp_heating_water, gc)
    ashph4 = Air_Source_Heat_Pump_Heat(1640, 0.2, True, ashph4_wp_heating_water, gc)
    # 测试结果
    ans = two_stage_heat_pump_function(heat_load, chp1, chp2, chp3, chp4, ashph1, ashph2, ashph3, ashph4, gc)
    print_two_stage_heat_pump_function(ans)

test_two_stage_heat_pump_function()

