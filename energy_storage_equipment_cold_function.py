import math
from equipment import Energy_Storage_Equipment_Cold, Water_Pump
from global_constant import Global_Constant


def energy_storage_equipment_cold_function(cold_load_a, esec1, esec2, esec3, gc):
    """蓄能水罐在供冷和蓄冷时的计算函数"""
    # 实质上是蓄能水罐的1组多个水泵直接的寻优计算
    # 目前仅完成了母管制系统计算程序开发
    # 蓄能水罐，母管制系统
    # 传入的cold_load_a，是一个初试的冷负荷需求量，用于判断目前是蓄冷状态还是供冷状态，如果水罐可以满足cold_load_a的需求，则采用cold_load_a去计算，否则进行修正
    # 判断水罐对应的水泵是变频还是定频，以此采用不同的计算策略
    # 目前的程序仅支持1组多个水泵全部是定频或者全部是变频的情况
    # 计算步长是负荷率（0到100），公用步长
    if esec1.wp_chilled_water.frequency_scaling == True:
        esec_step = 1
    else:
        esec_step = 10

    # 列表，储存3台设备计算出的负荷率结果
    esec_load_ratio_result_all = [0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存3台设备的总耗电功率
    total_power_consumption = []
    # 列表， 储存3台设备的总补水量
    total_water_supply = []
    # 列表，储存3台设备计算出的负荷率结果
    esec1_load_ratio_result = []
    esec2_load_ratio_result = []
    esec3_load_ratio_result = []

    # 确定需要几台设备，向上取整（蓄能水罐水泵可以启动的最大数量）
    esec_num_max_2 = math.ceil(abs(cold_load_a) / esec1.cooling_power_rated)
    # 如果恰好整除，则向上加1
    if esec_num_max_2 == int(esec_num_max_2):
        esec_num_max_1 = esec_num_max_2 + 1
    else:
        esec_num_max_1 = esec_num_max_2
    # 最大数量不可以超过3
    if esec_num_max_1 > 3:
        esec_num_max_a = 3
    else:
        esec_num_max_a = esec_num_max_1

    # 3个水罐的剩余蓄冷量（单位kWh）
    esec1_cold_stock = energy_storage_equipment_cold_storage_residual_read()[0]
    esec2_cold_stock = energy_storage_equipment_cold_storage_residual_read()[1]
    esec3_cold_stock = energy_storage_equipment_cold_storage_residual_read()[2]
    esec_cold_stock_sum = esec1_cold_stock + esec2_cold_stock + esec3_cold_stock
    # 3个水罐的额定蓄冷量总和
    esec_cooling_storage_rated_sum = esec1.cooling_storage_rated + esec2.cooling_storage_rated + esec3.cooling_storage_rated

    if cold_load_a > 0:
        # 如果此时是供冷工况（冷负荷功率值大于0），但是水罐内的可以供冷总量等于0，则水罐关闭（实际上是水泵关闭），得到的负荷率结果用来判断这个水泵是否可以开启的标签
        if esec1_cold_stock <= 0 + gc.project_load_error:
            esec1_load_ratio_a = 0
        else:
            esec1_load_ratio_a = esec1.load_min
        if esec2_cold_stock <= 0 + gc.project_load_error:
            esec2_load_ratio_a = 0
        else:
            esec2_load_ratio_a = esec2.load_min
        if esec3_cold_stock <= 0 + gc.project_load_error:
            esec3_load_ratio_a = 0
        else:
            esec3_load_ratio_a = esec3.load_min
    elif cold_load_a == 0:
        esec1_load_ratio_a = 0
        esec2_load_ratio_a = 0
        esec3_load_ratio_a = 0
    else:
        # 如果此时是蓄冷工况（冷负荷功率值小于0），但是水罐内已经有的蓄冷总量为额定值 ，则水罐关闭（实际上是水泵关闭），得到的负荷率结果用来判断这个水泵是否可以开启的标签
        if esec1_cold_stock >= esec1.cooling_storage_rated - gc.project_load_error:
            esec1_load_ratio_a = 0
        else:
            esec1_load_ratio_a = esec1.load_min
        if esec2_cold_stock >= esec2.cooling_storage_rated - gc.project_load_error:
            esec2_load_ratio_a = 0
        else:
            esec2_load_ratio_a = esec2.load_min
        if esec3_cold_stock >= esec3.cooling_storage_rated - gc.project_load_error:
            esec3_load_ratio_a = 0
        else:
            esec3_load_ratio_a = esec3.load_min

    # 修正水泵的启动数量最大值
    esec_num_max_b = 3 # 初始值
    if esec1_load_ratio_a == 0:
        esec_num_max_b -= 1
    else:
        esec_num_max_b -= 0
    if esec2_load_ratio_a == 0:
        esec_num_max_b -= 1
    else:
        esec_num_max_b -= 0
    if esec3_load_ratio_a == 0:
        esec_num_max_b -= 1
    else:
        esec_num_max_b -= 0
    # 确定数量最大值
    esec_num_max_c = min(esec_num_max_a, esec_num_max_b)

    # 如果某个设备的额定功率为0，则不参与计算，从而控制参与计算的设备的最大数量
    esec_power_0_num = 0  # 初始化额定功率为0的设备数量
    if esec1.cooling_power_rated == 0:
        esec_power_0_num += 1
    if esec2.cooling_power_rated == 0:
        esec_power_0_num += 1
    if esec3.cooling_power_rated == 0:
        esec_power_0_num += 1
    esec_num_max_d = 3 - esec_power_0_num
    # 重新修正设备最大数量
    esec_num_max = min(esec_num_max_c, esec_num_max_d)

    # 修正冷负荷(cold_load)
    # 如果此时是供冷工况（冷负荷功率值大于0）
    if cold_load_a > 0:
        if esec1_load_ratio_a == 0:
            cold_load_b_esec1 = 0
        else:
            cold_load_b_esec1 = esec1.cooling_power_rated
        if esec2_load_ratio_a == 0:
            cold_load_b_esec2 = 0
        else:
            cold_load_b_esec2 = esec2.cooling_power_rated
        if esec3_load_ratio_a == 0:
            cold_load_b_esec3 = 0
        else:
            cold_load_b_esec3 = esec3.cooling_power_rated
        # 汇总
        cold_load_b = cold_load_b_esec1 + cold_load_b_esec2 + cold_load_b_esec3
    elif cold_load_a == 0:
        cold_load_b =0
    else:
        # 蓄冷工况
        if esec1_load_ratio_a == 0:
            cold_load_b_esec1 = 0
        else:
            cold_load_b_esec1 = - esec1.cooling_power_rated
        if esec2_load_ratio_a == 0:
            cold_load_b_esec2 = 0
        else:
            cold_load_b_esec2 = - esec2.cooling_power_rated
        if esec3_load_ratio_a == 0:
            cold_load_b_esec3 = 0
        else:
            cold_load_b_esec3 = - esec3.cooling_power_rated
        # 汇总
        cold_load_b = cold_load_b_esec1 + cold_load_b_esec2 + cold_load_b_esec3
    # 汇总冷负荷情况
    if cold_load_a > 0:
        cold_load = min(cold_load_a, cold_load_b)
    elif cold_load_a == 0:
        cold_load = 0
    else:
        cold_load = max(cold_load_a, cold_load_b)
    # 水泵启动数量初始值
    esec_num = 1
    while esec_num <= esec_num_max:
        # while里采用一个公用的负荷率，初始化
        esec_load_ratio = esec1.load_min
        # 初始化设备1、2、3的负荷率
        # 根据目前启动的设备数量将不同的设备负荷率初始化成公用负荷率
        esec1_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[0]
        esec2_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[1]
        esec3_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[2]
        # 对计算出的负荷率进行修正
        esec1_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec1, cold_load_a, esec1_load_ratio_b, esec1_cold_stock)
        esec2_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec2, cold_load_a, esec2_load_ratio_b, esec2_cold_stock)
        esec3_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec3, cold_load_a, esec3_load_ratio_b, esec3_cold_stock)
        # 计算蓄冷水罐设备
        while esec_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算3个设备的制冷出力
            # 如果是供冷工况（冷负荷大于0）
            if cold_load > 0:
                if esec1_load_ratio_a > 0:
                    esec1_cold_out_now = esec1_load_ratio * esec1.cooling_power_rated
                else:
                    esec1_cold_out_now = 0
                if esec2_load_ratio_a > 0:
                    esec2_cold_out_now = esec2_load_ratio * esec2.cooling_power_rated
                else:
                    esec2_cold_out_now = 0
                if esec3_load_ratio_a > 0:
                    esec3_cold_out_now = esec3_load_ratio * esec3.cooling_power_rated
                else:
                    esec3_cold_out_now = 0
                esec_cold_out_now_sum = esec1_cold_out_now + esec2_cold_out_now + esec3_cold_out_now
            elif cold_load == 0:
                esec_cold_out_now_sum = 0
            else:
                # 如果是蓄冷工况（冷负荷小于0）
                if esec1_load_ratio_a > 0:
                    esec1_cold_out_now = - esec1_load_ratio * esec1.cooling_power_rated
                else:
                    esec1_cold_out_now = 0
                if esec2_load_ratio_a > 0:
                    esec2_cold_out_now = - esec2_load_ratio * esec2.cooling_power_rated
                else:
                    esec2_cold_out_now = 0
                if esec3_load_ratio_a > 0:
                    esec3_cold_out_now = - esec3_load_ratio * esec3.cooling_power_rated
                else:
                    esec3_cold_out_now = 0
                esec_cold_out_now_sum = - (esec1_cold_out_now + esec2_cold_out_now + esec3_cold_out_now)
            # print(esec_cold_out_now_sum, abs(cold_load) - gc.project_load_error, esec1_cold_stock + esec2_cold_stock + esec3_cold_stock - gc.project_load_error)
            # 根据目前是供冷状态还是蓄冷状态分别判断
            # cold_load_a>0是供冷状态 , cold_load_a<0是蓄冷状态
            if (cold_load_a > 0 and abs(esec_cold_out_now_sum) < abs(cold_load) - gc.project_load_error and abs(esec_cold_out_now_sum) < esec_cold_stock_sum - gc.project_load_error) \
                or (cold_load_a < 0 and abs(esec_cold_out_now_sum) < abs(cold_load) - gc.project_load_error and abs(esec_cold_out_now_sum) < esec_cooling_storage_rated_sum - esec_cold_stock_sum - gc.project_load_error):
                # 负荷都取绝对值
                # 增加公用负荷率
                esec_load_ratio += esec_step / 100
                # 设备1、2、3的负荷率设置成公用负荷率
                # 根据目前启动的设备数量将不同的设备负荷率设置成公用负荷率
                esec1_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[0]
                esec2_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[1]
                esec3_load_ratio_b = energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio)[2]
                # 对计算出的负荷率进行修正
                esec1_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec1, cold_load_a, esec1_load_ratio_b, esec1_cold_stock)
                esec2_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec2, cold_load_a, esec2_load_ratio_b, esec2_cold_stock)
                esec3_load_ratio = energy_storage_equipment_cold_load_ratio_correction(esec3, cold_load_a, esec3_load_ratio_b, esec3_cold_stock)
            else:
                # 保存3个设备的负荷率
                esec_load_ratio_result_all[0] = esec1_load_ratio
                esec_load_ratio_result_all[1] = esec2_load_ratio
                esec_load_ratio_result_all[2] = esec3_load_ratio
                esec1_load_ratio_result.append(esec_load_ratio_result_all[0])
                esec2_load_ratio_result.append(esec_load_ratio_result_all[1])
                esec3_load_ratio_result.append(esec_load_ratio_result_all[2])
                # 辅助设备（水泵）耗电功率
                esec1_power_consumption = energy_storage_equipment_cold_cost(esec1, gc, esec1_load_ratio)[1]
                esec2_power_consumption = energy_storage_equipment_cold_cost(esec2, gc, esec1_load_ratio)[1]
                esec3_power_consumption = energy_storage_equipment_cold_cost(esec3, gc, esec1_load_ratio)[1]
                # 耗电量总计
                esec_power_consumption_total = esec1_power_consumption + esec2_power_consumption+ esec3_power_consumption
                total_power_consumption.append(esec_power_consumption_total)
                # 计算3个设备的总补水量
                esec1_water_supply = energy_storage_equipment_cold_cost(esec1, gc, esec1_load_ratio)[2]
                esec2_water_supply = energy_storage_equipment_cold_cost(esec2, gc, esec2_load_ratio)[2]
                esec3_water_supply = energy_storage_equipment_cold_cost(esec3, gc, esec3_load_ratio)[2]
                esec_water_supply_total = esec1_water_supply + esec2_water_supply + esec3_water_supply
                total_water_supply.append(esec_water_supply_total)
                # 计算3个设备的成本
                esec_cost_total = esec_power_consumption_total * gc.buy_electricity_price + esec_water_supply_total * gc.water_price
                cost.append(esec_cost_total)
                break

        # 增加水泵数量
        esec_num += 1

    # 返回计算结果
    return cost, esec1_load_ratio_result, esec2_load_ratio_result, esec3_load_ratio_result, total_power_consumption, total_water_supply


def energy_storage_equipment_cold_storage_residual_read():
    """从txt文件读取目前蓄能水罐剩余的蓄冷量（单位KWh）"""
    # 列表，储存从txt文件读取的3个水罐的剩余蓄冷量（单位kWh）
    esec_cold_stock = []
    # 读取txt文件，获取当前蓄冷水罐剩余的蓄冷量（单位kWh）
    f = open("./energy_storage_equipment_stock/energy_storage_equipment_cold_stock.txt", 'r')  # 打开文件
    for line in f.readlines():
        lines = line.strip().split("\t")
        esec_cold_stock.append(lines[0])
    # 3个水罐的剩余蓄冷量（单位kWh）
    esec1_cold_stock = float(esec_cold_stock[0])
    esec2_cold_stock = float(esec_cold_stock[1])
    esec3_cold_stock = float(esec_cold_stock[2])
    f.close()  # 关闭文件
    # 返回结果
    return esec1_cold_stock, esec2_cold_stock, esec3_cold_stock


def energy_storage_equipment_cold_storage_residual_write(hour_state, esec1, esec2, esec3, esec1_load_ratio, esec2_load_ratio, esec3_load_ratio, esec1_cold_stock, esec2_cold_stock, esec3_cold_stock):
    """向txt文件中写入计算结果，改变水罐蓄冷量（kWh）"""
    f = open("./energy_storage_equipment_stock/energy_storage_equipment_cold_stock.txt", 'w')  # 打开文件
    if hour_state == 1:
        # 供冷状态，蓄冷量减少
        esec1_cold_stock_new = esec1_cold_stock - esec1_load_ratio * esec1.cooling_power_rated
        esec2_cold_stock_new = esec2_cold_stock - esec2_load_ratio * esec2.cooling_power_rated
        esec3_cold_stock_new = esec3_cold_stock - esec3_load_ratio * esec3.cooling_power_rated
        line1 = str(esec1_cold_stock_new) + "\n"
        f.writelines(line1)
        line2 = str(esec2_cold_stock_new) + "\n"
        f.writelines(line2)
        line3 = str(esec3_cold_stock_new)
        f.writelines(line3)
    else:
        # 蓄冷状态，蓄冷量增加
        esec1_cold_stock_new = esec1_cold_stock + esec1_load_ratio * esec1.cooling_power_rated
        esec2_cold_stock_new = esec2_cold_stock + esec2_load_ratio * esec2.cooling_power_rated
        esec3_cold_stock_new = esec3_cold_stock + esec3_load_ratio * esec3.cooling_power_rated
        line1 = str(esec1_cold_stock_new) + "\n"
        f.writelines(line1)
        line2 = str(esec2_cold_stock_new) + "\n"
        f.writelines(line2)
        line3 = str(esec3_cold_stock_new)
        f.writelines(line3)
    # 关闭文件
    f.close()


def energy_storage_equipment_cold_load_ratio(esec_num, esec1_load_ratio_a, esec2_load_ratio_a, esec3_load_ratio_a, esec_load_ratio):
    """根据目前启动的设备数量将不同的设备负荷率设置成成公用负荷率"""
    if esec_num == 1:
        if esec1_load_ratio_a > 0:
            esec1_load_ratio = esec_load_ratio
            esec2_load_ratio = 0
            esec3_load_ratio = 0
        elif esec1_load_ratio_a == 0 and esec2_load_ratio_a > 0:
            esec1_load_ratio = 0
            esec2_load_ratio = esec_load_ratio
            esec3_load_ratio = 0
        elif esec1_load_ratio_a == 0 and esec2_load_ratio_a == 0 and esec3_load_ratio_a > 0:
            esec1_load_ratio = 0
            esec2_load_ratio = 0
            esec3_load_ratio = esec_load_ratio
        else:
            esec1_load_ratio = 0
            esec2_load_ratio = 0
            esec3_load_ratio = 0
    elif esec_num == 2:
        if esec1_load_ratio_a > 0 and esec2_load_ratio_a > 0:
            esec1_load_ratio = esec_load_ratio
            esec2_load_ratio = esec_load_ratio
            esec3_load_ratio = 0
        elif esec1_load_ratio_a > 0 and esec2_load_ratio_a == 0 and esec3_load_ratio_a > 0:
            esec1_load_ratio = esec_load_ratio
            esec2_load_ratio = 0
            esec3_load_ratio = esec_load_ratio
        elif esec1_load_ratio_a == 0 and esec2_load_ratio_a > 0 and esec3_load_ratio_a > 0:
            esec1_load_ratio = 0
            esec2_load_ratio = esec_load_ratio
            esec3_load_ratio = esec_load_ratio
        else:
            esec1_load_ratio = 0
            esec2_load_ratio = 0
            esec3_load_ratio = 0
    elif esec_num == 3:
        if esec1_load_ratio_a > 0 and esec2_load_ratio_a > 0 and esec3_load_ratio_a > 0:
            esec1_load_ratio = esec_load_ratio
            esec2_load_ratio = esec_load_ratio
            esec3_load_ratio = esec_load_ratio
        else:
            esec1_load_ratio = 0
            esec2_load_ratio = 0
            esec3_load_ratio = 0
    else:
        esec1_load_ratio = 0
        esec2_load_ratio = 0
        esec3_load_ratio = 0

    return esec1_load_ratio, esec2_load_ratio, esec3_load_ratio


def energy_storage_equipment_cold_load_ratio_correction(esec, cold_load_a, load_ratio, esec_cold_stock):
    """对计算出的设备负荷率进行修正"""
    # 如果是向外供冷的工况
    if cold_load_a > 0:
        if esec_cold_stock < esec.cooling_power_rated * load_ratio:
            load_ratio_correction = esec_cold_stock / esec.cooling_power_rated
        else:
            load_ratio_correction = load_ratio
    elif cold_load_a ==0:
        load_ratio_correction = 0
    else:
        # 如果是蓄冷的工况
        if esec.cooling_storage_rated - esec_cold_stock < esec.cooling_power_rated * load_ratio:
            load_ratio_correction = (esec.cooling_storage_rated - esec_cold_stock) / esec.cooling_power_rated
        else:
            load_ratio_correction = load_ratio

    return load_ratio_correction


def energy_storage_equipment_cold_result(ans_esec, esec1, esec2, esec3):
    """选择出最合适的蓄冷水罐（实际上是水泵）的计算结果"""
    # 总成本最小值
    cost_min = min(ans_esec[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_esec[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    esec1_ratio = ans_esec[1][cost_min_index]
    esec2_ratio = ans_esec[2][cost_min_index]
    esec3_ratio = ans_esec[3][cost_min_index]
    cold_load_out = esec1_ratio * esec1.cooling_power_rated + esec2_ratio * esec2.cooling_power_rated + esec3_ratio * esec3.cooling_power_rated
    power_consumption_total = ans_esec[4][cost_min_index]
    water_supply_total = ans_esec[5][cost_min_index]

    return esec1_ratio, esec2_ratio, esec3_ratio, cold_load_out, power_consumption_total, water_supply_total


def print_energy_storage_equipment_cold(ans_esec, esec1, esec2, esec3):
    """打印出最合适的蓄冷水罐（实际上是水泵）的计算结果"""
    # 总成本最小值
    cost_min = min(ans_esec[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_esec[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    esec1_ratio = ans_esec[1][cost_min_index]
    esec2_ratio = ans_esec[2][cost_min_index]
    esec3_ratio = ans_esec[3][cost_min_index]
    cold_load_out = esec1_ratio * esec1.cooling_power_rated + esec2_ratio * esec2.cooling_power_rated + esec3_ratio * esec3.cooling_power_rated

    print("蓄能水罐最低总运行成本为： " + str(cost_min) + "\n" + "蓄能水罐水泵1负荷率为： " + str(esec1_ratio) + "\n" + "蓄能水罐水泵2负荷率为： " + str(esec2_ratio) + "\n" + "蓄能水罐水泵3负荷率为： " + str(esec3_ratio) + "\n" + "蓄能水罐总制冷出力为： " + str(cold_load_out))


def energy_storage_equipment_cold_cost(esec, gc, load_ratio):
    """蓄冷水罐成本计算"""
    # 冷冻水流量,某一负荷率条件下
    chilled_water_flow = esec.chilled_water_flow(load_ratio)
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = esec.auxiliary_equipment_power_consumption(chilled_water_flow)
    # 总耗电功率,某一负荷率条件下（只有水泵耗电）
    total_power_consumption = auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 冷冻水补水量,某一负荷率条件下
    centrifugal_chiller_chiller_water_supply = chilled_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下（只有冷冻水补水）
    total_water_supply = centrifugal_chiller_chiller_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, chilled_water_flow


def test_energy_storage_equipment_cold_function():
    """测试蓄能水罐计算"""
    gc = Global_Constant()
    # 实例化1组3个蓄冷水罐的循环水泵（水泵3用1备）
    esec1_wp_chilled_water = Water_Pump(50, False, 35, gc)
    esec2_wp_chilled_water = Water_Pump(50, False, 35, gc)
    esec3_wp_chilled_water = Water_Pump(50, False, 35, gc)
    # 实例化3个蓄冷水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    esec1 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec1_wp_chilled_water, gc)
    esec2 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec2_wp_chilled_water, gc)
    esec3 = Energy_Storage_Equipment_Cold(1000, 0.1, 8000, esec3_wp_chilled_water, gc)
    # 冷负荷
    cold_load_a = 3000
    ans_esec = energy_storage_equipment_cold_function(cold_load_a, esec1, esec2, esec3, gc)
    print_energy_storage_equipment_cold(ans_esec, esec1, esec2, esec3)
    # 写入txt文件
    # hour_state = 1
    # esec1_cold_stock = energy_storage_equipment_cold_storage_residual_read()[0]
    # esec2_cold_stock = energy_storage_equipment_cold_storage_residual_read()[1]
    # esec3_cold_stock = energy_storage_equipment_cold_storage_residual_read()[2]
    # energy_storage_equipment_cold_storage_residual_write(hour_state, esec1, esec2, esec3, 1, 1, 1, esec1_cold_stock, esec2_cold_stock, esec3_cold_stock)

# test_energy_storage_equipment_cold_function()

