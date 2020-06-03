# 如要正常使用本程序，需要导入以下几个第三方程序库
# numpy,tensorflow

from equipment import Centrifugal_Chiller, Internal_Combustion_Engine, Water_Pump, Natural_Gas_Boiler_hot_water, Energy_Storage_Equipment_Cold, Air_Source_Heat_Pump_Cold
from equipment import Energy_Storage_Equipment_Heat, Centrifugal_Heat_Pump_Heat, Air_Source_Heat_Pump_Heat, Natural_Gas_Boiler_heat
from cooling_season_calculate import cooling_season_function as csf, print_cooling_season as pcs
from heating_season_calculate import heating_season_function as hsf, print_heating_season as phs
from transition_season_calculate import transition_season_function as tsf, print_transition_season as pts
from global_constant import Global_Constant

def run_program():
    """执行主程序"""
    # 实例化一个全局常量类
    gc = Global_Constant()
    # 负荷情况
    cold_load = 12000
    heat_load = 0
    hot_water_load = 1000
    electricity_load = 4000

    # 实例化两个内燃机对象
    ice1 = Internal_Combustion_Engine(1500, gc, 0.5)
    ice2 = Internal_Combustion_Engine(1500, gc, 0.5)
    # 实例化4个离心式冷水机的各种水泵（离心式热泵的制冷工况采用离心式冷水机的计算模型）
    cc1_wp_chilled_water = Water_Pump(600, True, 38, gc)
    cc2_wp_chilled_water = Water_Pump(600, True, 38, gc)
    cc3_wp_chilled_water = Water_Pump(600, True, 38, gc)
    cc4_wp_chilled_water = Water_Pump(600, True, 38, gc)
    cc1_wp_cooling_water = Water_Pump(710, True, 32, gc)
    cc2_wp_cooling_water = Water_Pump(710, True, 32, gc)
    cc3_wp_cooling_water = Water_Pump(710, True, 32, gc)
    cc4_wp_cooling_water = Water_Pump(710, True, 32, gc)
    # 实例化4个离心式冷水机类（离心式热泵的制冷工况采用离心式冷水机的计算模型）
    cc1 = Centrifugal_Chiller(3164, 0.1, True, cc1_wp_chilled_water, cc1_wp_cooling_water, gc)
    cc2 = Centrifugal_Chiller(3164, 0.1, True, cc2_wp_chilled_water, cc2_wp_cooling_water, gc)
    cc3 = Centrifugal_Chiller(3164, 0.1, True, cc3_wp_chilled_water, cc3_wp_cooling_water, gc)
    cc4 = Centrifugal_Chiller(3164, 0.1, True, cc4_wp_chilled_water, cc4_wp_cooling_water, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个冷却水泵，2个冷冻水泵，2个生活热水水泵
    lb1_wp_cooling_water = Water_Pump(660, True, 32, gc)
    lb2_wp_cooling_water = Water_Pump(660, True, 32, gc)
    lb1_wp_chilled_water = Water_Pump(330, True, 38, gc)
    lb2_wp_chilled_water = Water_Pump(330, True, 38, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个采暖水泵
    lb1_wp_heating_water = Water_Pump(150, True, 38, gc)
    lb2_wp_heating_water = Water_Pump(150, True, 38, gc)
    # 实例化2个溴化锂生活热水水泵
    lb1_wp_hot_water = Water_Pump(270, False, 35, gc)
    lb2_wp_hot_water = Water_Pump(270, False, 35, gc)
    # 实例化4个风冷螺杆式热泵的冷冻水泵
    ashpc1_wp_chilled_water = Water_Pump(330, True, 35, gc)
    ashpc2_wp_chilled_water = Water_Pump(330, True, 35, gc)
    ashpc3_wp_chilled_water = Water_Pump(330, True, 35, gc)
    ashpc4_wp_chilled_water = Water_Pump(330, True, 35, gc)
    # 实例化4个风冷螺杆式热泵
    ashpc1 = Air_Source_Heat_Pump_Cold(1640, 0.1, True, ashpc1_wp_chilled_water, gc)
    ashpc2 = Air_Source_Heat_Pump_Cold(1640, 0.1, True, ashpc2_wp_chilled_water, gc)
    ashpc3 = Air_Source_Heat_Pump_Cold(1640, 0.1, True, ashpc3_wp_chilled_water, gc)
    ashpc4 = Air_Source_Heat_Pump_Cold(1640, 0.1, True, ashpc4_wp_chilled_water, gc)
    # 实例化2台离心式热泵
    chph1_wp_heating_water = Water_Pump(330, True, 35, gc)
    chph2_wp_heating_water = Water_Pump(330, True, 35, gc)
    chph3_wp_heating_water = Water_Pump(0, True, 0, gc)
    chph4_wp_heating_water = Water_Pump(0, True, 0, gc)
    chph1_wp_heat_source_water = Water_Pump(550, True, 35, gc)
    chph2_wp_heat_source_water = Water_Pump(550, True, 35, gc)
    chph3_wp_heat_source_water = Water_Pump(0, True, 0, gc)
    chph4_wp_heat_source_water = Water_Pump(0, True, 0, gc)
    chph1 = Centrifugal_Heat_Pump_Heat(3500, 0.1, True, chph1_wp_heating_water, chph1_wp_heat_source_water, gc)
    chph2 = Centrifugal_Heat_Pump_Heat(3500, 0.1, True, chph2_wp_heating_water, chph2_wp_heat_source_water, gc)
    chph3 = Centrifugal_Heat_Pump_Heat(0, 0.1, True, chph3_wp_heating_water, chph3_wp_heat_source_water, gc)
    chph4 = Centrifugal_Heat_Pump_Heat(0, 0.1, True, chph4_wp_heating_water, chph4_wp_heat_source_water, gc)
    # 实例化4台风冷螺杆式热泵
    ashph1_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph2_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph3_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph4_wp_heating_water = Water_Pump(330, True, 35, gc)
    ashph1 = Air_Source_Heat_Pump_Heat(1640, 0.1, True, ashph1_wp_heating_water, gc)
    ashph2 = Air_Source_Heat_Pump_Heat(1640, 0.1, True, ashph2_wp_heating_water, gc)
    ashph3 = Air_Source_Heat_Pump_Heat(1640, 0.1, True, ashph3_wp_heating_water, gc)
    ashph4 = Air_Source_Heat_Pump_Heat(1640, 0.1, True, ashph4_wp_heating_water, gc)
    # # 实例化2个天然气采暖锅炉水泵
    # ngbh1_wp_heating_water = Water_Pump(330, True, 32, gc)
    # ngbh2_wp_heating_water = Water_Pump(330, True, 32, gc)
    # # 实例化2个天然气采暖锅炉对象
    # ngbh1 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh1_wp_heating_water, gc)
    # ngbh2 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh2_wp_heating_water, gc)
    # 实例化1组3个蓄冷水罐的循环水泵（水泵3用1备）
    esec1_wp_chilled_water = Water_Pump(330, True, 35, gc)
    esec2_wp_chilled_water = Water_Pump(330, True, 35, gc)
    esec3_wp_chilled_water = Water_Pump(330, True, 35, gc)
    # 实例化3个蓄冷水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    esec1 = Energy_Storage_Equipment_Cold(1750, 0.1, 14000, esec1_wp_chilled_water, gc)
    esec2 = Energy_Storage_Equipment_Cold(1750, 0.1, 14000, esec2_wp_chilled_water, gc)
    esec3 = Energy_Storage_Equipment_Cold(1750, 0.1, 14000, esec3_wp_chilled_water, gc)
    # 实例化1组3个蓄热水罐的循环水泵（水泵2用1备）
    eseh1_wp_heating_water = Water_Pump(330, True, 35, gc)
    eseh2_wp_heating_water = Water_Pump(330, True, 35, gc)
    eseh3_wp_heating_water = Water_Pump(0, True, 0, gc)
    # 实例化3个蓄热水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    eseh1 = Energy_Storage_Equipment_Heat(1750, 0.1, 14000, eseh1_wp_heating_water, gc)
    eseh2 = Energy_Storage_Equipment_Heat(1750, 0.1, 14000, eseh2_wp_heating_water, gc)
    eseh3 = Energy_Storage_Equipment_Heat(0, 0.1, 0, eseh3_wp_heating_water, gc)
    # 实例化天然气生活热水锅炉用到的水泵
    ngb_wp_hot_water = Water_Pump(270, False, 35, gc)
    # 实例化生活热水锅炉
    ngb_hot_water = Natural_Gas_Boiler_hot_water(2800, 0.1, ngb_wp_hot_water, gc)

    # 判断输入的冷热负荷是否超过最大允许值
    if cold_load > gc.cold_load_max:
        print("输入的冷负荷需求量超过了能源站制冷最大值，请重新输入！")
        exit()
    if heat_load > gc.heat_load_max:
        print("输入的热负荷需求量超过了能源站制热最大值，请重新输入！")
        exit()
    if hot_water_load > gc.hot_water_load_max:
        print("输入的生活热水负荷需求量超过了能源站制生活热水最大值，请重新输入！")
        exit()

    # 制冷季计算
    if cold_load > 0 + gc.project_load_error and heat_load <= 0 + gc.project_load_error:
        # 计算制冷季
        ans_csf = csf(cold_load, hot_water_load, electricity_load, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water,
                            lb1_wp_chilled_water, lb2_wp_chilled_water, lb1_wp_hot_water, lb2_wp_hot_water, cc1, cc2, cc3, cc4,
                            ashpc1, ashpc2, ashpc3, ashpc4, esec1, esec2, esec3, ngb_hot_water, gc)
        # 显示制冷季计算结果并写入数据库
        pcs(ans_csf, ice1, ice2, lb1_wp_cooling_water, lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water,
            lb1_wp_hot_water, lb2_wp_hot_water, cc1, cc2, cc3, cc4, ashpc1, ashpc2, ashpc3, ashpc4, esec1, esec2, esec3, ngb_hot_water, gc)

    # 采暖季计算
    elif cold_load <= 0 + gc.project_load_error and heat_load > 0 + gc.project_load_error:
        # 计算采暖季
        ans_hsf = hsf(heat_load, hot_water_load, electricity_load, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water,
                            chph1, chph2, chph3, chph4, ashph1, ashph2, ashph3, ashph4, eseh1, eseh2, eseh3, ngb_hot_water, gc)
        # 显示采暖季计算结果并写入数据库
        phs(ans_hsf, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, chph1, chph2,
                         ashph1, ashph2, ashph3, ashph4, eseh1, eseh2, eseh3, ngb_hot_water, gc)

    # 过渡季负荷
    elif cold_load <= 0 + gc.project_load_error and heat_load <= 0 + gc.project_load_error:
        ans_tsf = tsf(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc)
        pts(ans_tsf, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc)

    else:
        print("输入的负荷信息有误，请检查！")


# 执行程序
run_program()
