# 如要正常使用本程序，需要导入以下几个第三方程序库
# numpy,tensorflow

import datetime
from cooling_season_calculate import cooling_season_function as csf, print_cooling_season as pcs
from heating_season_calculate import heating_season_function as hsf, print_heating_season as phs
from transition_season_calculate import transition_season_function as tsf, print_transition_season as pts
from global_constant import Global_Constant

def run_program():
    """执行主程序"""
    # 实例化一个全局常量类
    gc = Global_Constant()
    # 负荷情况
    cold_load = 8000
    heat_load = 0
    hot_water_load = 1000
    electricity_load = 4000
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
        ans_csf = csf(cold_load, hot_water_load, electricity_load, gc)
        pcs(ans_csf)
    # 采暖季计算
    elif cold_load <= 0 + gc.project_load_error and heat_load > 0 + gc.project_load_error:
        ans_hsf = hsf(heat_load, hot_water_load, electricity_load, gc)
        phs(ans_hsf)
    # 过渡季负荷
    elif cold_load <= 0 + gc.project_load_error and heat_load <= 0 + gc.project_load_error:
        ans_tsf = tsf(hot_water_load, electricity_load, gc)
        pts(ans_tsf)
    else:
        print("输入的负荷信息有误，请检查！")


def test():
    """测试"""
    a=[]
    f = open("./energy_storage_equipment_cold_stock.txt")  # 打开文件
    for line in f.readlines():
        lines = line.strip().split("\t")
        a.append(lines[0])

    print(a[0])
    print(a[1])
    print(a[2])
# 执行程序
#run_program()

#test()