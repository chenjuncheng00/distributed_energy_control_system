import math
from equipment import Energy_Storage_Equipment_Heat, Water_Pump
from global_constant import Global_Constant


def energy_storage_equipment_heat_function(heat_load_a, eseh1, eseh2, eseh3, gc):
    """蓄能水罐在供热和蓄热时的计算函数"""
    # 实质上是蓄能水罐的1组多个水泵直接的寻优计算
    # 目前仅完成了母管制系统计算程序开发
    # 蓄能水罐，母管制系统
    # 传入的heat_load_a，是一个初试的热负荷需求量，用于判断目前是蓄热状态还是供热状态，如果水罐可以满足heat_load_a的需求，则采用heat_load_a去计算，否则进行修正
    # 判断水罐对应的水泵是变频还是定频，以此采用不同的计算策略
    # 目前的程序仅支持1组多个水泵全部是定频或者全部是变频的情况
    # 计算步长是负荷率（0到100），公用步长
    if eseh1.wp_heating_water.frequency_scaling == True:
        eseh_step = 1
    else:
        eseh_step = 10

    # 列表，储存3台设备计算出的负荷率结果
    eseh_load_ratio_result_all = [0, 0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存3台设备的总耗电功率
    total_power_consumption = []
    # 列表， 储存3台设备的总补水量
    total_water_supply = []
    # 列表，储存3台设备计算出的负荷率结果
    eseh1_load_ratio_result = []
    eseh2_load_ratio_result = []
    eseh3_load_ratio_result = []

    # 确定需要几台设备，向上取整（蓄能水罐水泵可以启动的最大数量）
    eseh_num_max_2 = math.ceil(abs(heat_load_a) / eseh1.heating_power_rated)
    # 如果恰好整除，则向上加1
    if eseh_num_max_2 == int(eseh_num_max_2):
        eseh_num_max_1 = eseh_num_max_2 + 1
    else:
        eseh_num_max_1 = eseh_num_max_2
    # 最大数量不可以超过3
    if eseh_num_max_1 > 3:
        eseh_num_max_a = 3
    else:
        eseh_num_max_a = eseh_num_max_1

    # 3个水罐的剩余蓄热量（单位kWh）
    eseh1_heat_stock = energy_storage_equipment_heat_storage_residual_read()[0]
    eseh2_heat_stock = energy_storage_equipment_heat_storage_residual_read()[1]
    eseh3_heat_stock = energy_storage_equipment_heat_storage_residual_read()[2]
    eseh_heat_stock_sum = eseh1_heat_stock + eseh2_heat_stock + eseh3_heat_stock
    # 3个水罐的额定蓄热量总和
    eseh_heating_storage_rated_sum = eseh1.heating_storage_rated + eseh2.heating_storage_rated + eseh3.heating_storage_rated

    if heat_load_a > 0:
        # 如果此时是供热工况（热负荷功率值大于0），但是水罐内的可以供热总量等于0，则水罐关闭（实际上是水泵关闭），得到的负荷率结果用来判断这个水泵是否可以开启的标签
        if eseh1_heat_stock <= 0 + gc.project_load_error:
            eseh1_load_ratio_a = 0
        else:
            eseh1_load_ratio_a = eseh1.load_min
        if eseh2_heat_stock <= 0 + gc.project_load_error:
            eseh2_load_ratio_a = 0
        else:
            eseh2_load_ratio_a = eseh2.load_min
        if eseh3_heat_stock <= 0 + gc.project_load_error:
            eseh3_load_ratio_a = 0
        else:
            eseh3_load_ratio_a = eseh3.load_min
    elif heat_load_a == 0:
        eseh1_load_ratio_a = 0
        eseh2_load_ratio_a = 0
        eseh3_load_ratio_a = 0
    else:
        # 如果此时是蓄热工况（热负荷功率值小于0），但是水罐内已经有的蓄热总量为额定值 ，则水罐关闭（实际上是水泵关闭），得到的负荷率结果用来判断这个水泵是否可以开启的标签
        if eseh1_heat_stock >= eseh1.heating_storage_rated - gc.project_load_error:
            eseh1_load_ratio_a = 0
        else:
            eseh1_load_ratio_a = eseh1.load_min
        if eseh2_heat_stock >= eseh2.heating_storage_rated - gc.project_load_error:
            eseh2_load_ratio_a = 0
        else:
            eseh2_load_ratio_a = eseh2.load_min
        if eseh3_heat_stock >= eseh3.heating_storage_rated - gc.project_load_error:
            eseh3_load_ratio_a = 0
        else:
            eseh3_load_ratio_a = eseh3.load_min

    # 修正水泵的启动数量最大值
    eseh_num_max_b = 3 # 初始值
    if eseh1_load_ratio_a == 0:
        eseh_num_max_b -= 1
    else:
        eseh_num_max_b -= 0
    if eseh2_load_ratio_a == 0:
        eseh_num_max_b -= 1
    else:
        eseh_num_max_b -= 0
    if eseh3_load_ratio_a == 0:
        eseh_num_max_b -= 1
    else:
        eseh_num_max_b -= 0
    # 确定数量最大值
    eseh_num_max_c = min(eseh_num_max_a, eseh_num_max_b)

    # 如果某个设备的额定功率为0，则不参与计算，从而控制参与计算的设备的最大数量
    eseh_power_0_num = 0  # 初始化额定功率为0的设备数量
    if eseh1.heating_power_rated == 0:
        eseh_power_0_num += 1
    if eseh2.heating_power_rated == 0:
        eseh_power_0_num += 1
    if eseh3.heating_power_rated == 0:
        eseh_power_0_num += 1
    eseh_num_max_d = 3 - eseh_power_0_num
    # 重新修正设备最大数量
    eseh_num_max = min(eseh_num_max_c, eseh_num_max_d)

    # 修正热负荷(heat_load)
    # 如果此时是供热工况（热负荷功率值大于0）
    if heat_load_a > 0:
        if eseh1_load_ratio_a == 0:
            heat_load_b_eseh1 = 0
        else:
            heat_load_b_eseh1 = eseh1.heating_power_rated
        if eseh2_load_ratio_a == 0:
            heat_load_b_eseh2 = 0
        else:
            heat_load_b_eseh2 = eseh2.heating_power_rated
        if eseh3_load_ratio_a == 0:
            heat_load_b_eseh3 = 0
        else:
            heat_load_b_eseh3 = eseh3.heating_power_rated
        # 汇总
        heat_load_b = heat_load_b_eseh1 + heat_load_b_eseh2 + heat_load_b_eseh3
    elif heat_load_a == 0:
        heat_load_b =0
    else:
        # 蓄热工况
        if eseh1_load_ratio_a == 0:
            heat_load_b_eseh1 = 0
        else:
            heat_load_b_eseh1 = - eseh1.heating_power_rated
        if eseh2_load_ratio_a == 0:
            heat_load_b_eseh2 = 0
        else:
            heat_load_b_eseh2 = - eseh2.heating_power_rated
        if eseh3_load_ratio_a == 0:
            heat_load_b_eseh3 = 0
        else:
            heat_load_b_eseh3 = - eseh3.heating_power_rated
        # 汇总
        heat_load_b = heat_load_b_eseh1 + heat_load_b_eseh2 + heat_load_b_eseh3
    # 汇总热负荷情况
    if heat_load_a > 0:
        heat_load = min(heat_load_a, heat_load_b)
    elif heat_load_a == 0:
        heat_load = 0
    else:
        heat_load = max(heat_load_a, heat_load_b)

    # 水泵启动数量初始值
    eseh_num = 1
    while eseh_num <= eseh_num_max:
        # while里采用一个公用的负荷率，初始化
        eseh_load_ratio = eseh1.load_min
        # 初始化设备1、2、3的负荷率
        # 根据目前启动的设备数量将不同的设备负荷率初始化成公用负荷率
        eseh1_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[0]
        eseh2_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[1]
        eseh3_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[2]
        # 对计算出的负荷率进行修正
        eseh1_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh1, heat_load_a, eseh1_load_ratio_b, eseh1_heat_stock)
        eseh2_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh2, heat_load_a, eseh2_load_ratio_b, eseh2_heat_stock)
        eseh3_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh3, heat_load_a, eseh3_load_ratio_b, eseh3_heat_stock)
        # 计算蓄热水罐设备
        while eseh_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算3个设备的制热出力
            # 如果是供热工况（热负荷大于0）
            if heat_load > 0:
                if eseh1_load_ratio_a > 0:
                    eseh1_heat_out_now = eseh1_load_ratio * eseh1.heating_power_rated
                else:
                    eseh1_heat_out_now = 0
                if eseh2_load_ratio_a > 0:
                    eseh2_heat_out_now = eseh2_load_ratio * eseh2.heating_power_rated
                else:
                    eseh2_heat_out_now = 0
                if eseh3_load_ratio_a > 0:
                    eseh3_heat_out_now = eseh3_load_ratio * eseh3.heating_power_rated
                else:
                    eseh3_heat_out_now = 0
                eseh_heat_out_now_sum = eseh1_heat_out_now + eseh2_heat_out_now + eseh3_heat_out_now
            elif heat_load == 0:
                eseh_heat_out_now_sum = 0
            else:
                # 如果是蓄热工况（热负荷小于0）
                if eseh1_load_ratio_a > 0:
                    eseh1_heat_out_now = - eseh1_load_ratio * eseh1.heating_power_rated
                else:
                    eseh1_heat_out_now = 0
                if eseh2_load_ratio_a > 0:
                    eseh2_heat_out_now = - eseh2_load_ratio * eseh2.heating_power_rated
                else:
                    eseh2_heat_out_now = 0
                if eseh3_load_ratio_a > 0:
                    eseh3_heat_out_now = - eseh3_load_ratio * eseh3.heating_power_rated
                else:
                    eseh3_heat_out_now = 0
                eseh_heat_out_now_sum = - (eseh1_heat_out_now + eseh2_heat_out_now + eseh3_heat_out_now)
            # print(eseh_heat_out_now_sum, heat_load - gc.project_load_error, eseh1_heat_stock + eseh2_heat_stock + eseh3_heat_stock - gc.project_load_error)
            # 根据目前是供热状态还是蓄热状态分别判断
            # heat_load_a>0是供热状态 , heat_load_a<0是蓄热状态
            if (heat_load_a > 0 and abs(eseh_heat_out_now_sum) < abs(heat_load) - gc.project_load_error and abs(eseh_heat_out_now_sum) < eseh_heat_stock_sum - gc.project_load_error) \
               or (heat_load_a < 0 and abs(eseh_heat_out_now_sum) < abs(heat_load) - gc.project_load_error and abs(eseh_heat_out_now_sum) < eseh_heating_storage_rated_sum - eseh_heat_stock_sum - gc.project_load_error):
                # 负荷都取绝对值
                # 增加公用负荷率
                eseh_load_ratio += eseh_step / 100
                # 设备1、2、3的负荷率设置成公用负荷率
                # 根据目前启动的设备数量将不同的设备负荷率设置成公用负荷率
                eseh1_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[0]
                eseh2_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[1]
                eseh3_load_ratio_b = energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio)[2]
                # 对计算出的负荷率进行修正
                eseh1_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh1, heat_load_a, eseh1_load_ratio_b, eseh1_heat_stock)
                eseh2_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh2, heat_load_a, eseh2_load_ratio_b, eseh2_heat_stock)
                eseh3_load_ratio = energy_storage_equipment_heat_load_ratio_correction(eseh3, heat_load_a, eseh3_load_ratio_b, eseh3_heat_stock)
            else:
                # 保存3个设备的负荷率
                eseh_load_ratio_result_all[0] = eseh1_load_ratio
                eseh_load_ratio_result_all[1] = eseh2_load_ratio
                eseh_load_ratio_result_all[2] = eseh3_load_ratio
                eseh1_load_ratio_result.append(eseh_load_ratio_result_all[0])
                eseh2_load_ratio_result.append(eseh_load_ratio_result_all[1])
                eseh3_load_ratio_result.append(eseh_load_ratio_result_all[2])
                # 辅助设备（水泵）耗电功率
                eseh1_power_consumption = energy_storage_equipment_heat_cost(eseh1, gc, eseh1_load_ratio)[1]
                eseh2_power_consumption = energy_storage_equipment_heat_cost(eseh2, gc, eseh1_load_ratio)[1]
                eseh3_power_consumption = energy_storage_equipment_heat_cost(eseh3, gc, eseh1_load_ratio)[1]
                # 耗电量总计
                eseh_power_consumption_total = eseh1_power_consumption + eseh2_power_consumption+ eseh3_power_consumption
                total_power_consumption.append(eseh_power_consumption_total)
                # 计算3个设备的总补水量
                eseh1_water_supply = energy_storage_equipment_heat_cost(eseh1, gc, eseh1_load_ratio)[2]
                eseh2_water_supply = energy_storage_equipment_heat_cost(eseh2, gc, eseh2_load_ratio)[2]
                eseh3_water_supply = energy_storage_equipment_heat_cost(eseh3, gc, eseh3_load_ratio)[2]
                eseh_water_supply_total = eseh1_water_supply + eseh2_water_supply + eseh3_water_supply
                total_water_supply.append(eseh_water_supply_total)
                # 计算3个设备的成本
                eseh_cost_total = eseh_power_consumption_total * gc.buy_electricity_price + eseh_water_supply_total * gc.water_price
                cost.append(eseh_cost_total)
                break

        # 增加水泵数量
        eseh_num += 1

    # 返回计算结果
    return cost, eseh1_load_ratio_result, eseh2_load_ratio_result, eseh3_load_ratio_result, total_power_consumption, total_water_supply


def energy_storage_equipment_heat_storage_residual_read():
    """从txt文件读取目前蓄能水罐剩余的蓄热量（单位KWh）"""
    # 列表，储存从txt文件读取的3个水罐的剩余蓄热量（单位kWh）
    eseh_heat_stock = []
    # 读取txt文件，获取当前蓄热水罐剩余的蓄热量（单位kWh）
    f = open("./energy_storage_equipment_stock/energy_storage_equipment_heat_stock.txt", 'r')  # 打开文件
    for line in f.readlines():
        lines = line.strip().split("\t")
        eseh_heat_stock.append(lines[0])
    # 3个水罐的剩余蓄热量（单位kWh）
    eseh1_heat_stock = float(eseh_heat_stock[0])
    eseh2_heat_stock = float(eseh_heat_stock[1])
    eseh3_heat_stock = float(eseh_heat_stock[2])

    return eseh1_heat_stock, eseh2_heat_stock, eseh3_heat_stock


def energy_storage_equipment_heat_storage_residual_write(hour_state, eseh1, eseh2, eseh3, eseh1_load_ratio, eseh2_load_ratio, eseh3_load_ratio, eseh1_heat_stock, eseh2_heat_stock, eseh3_heat_stock):
    """向txt文件中写入计算结果，改变水罐蓄热量（kWh）"""
    f = open("./energy_storage_equipment_stock/energy_storage_equipment_heat_stock.txt", 'w')  # 打开文件
    if hour_state == 1:
        # 供热状态，蓄热量减少
        eseh1_heat_stock_new = eseh1_heat_stock - eseh1_load_ratio * eseh1.heating_power_rated
        eseh2_heat_stock_new = eseh2_heat_stock - eseh2_load_ratio * eseh2.heating_power_rated
        eseh3_heat_stock_new = eseh3_heat_stock - eseh3_load_ratio * eseh3.heating_power_rated
        line1 = str(eseh1_heat_stock_new) + "\n"
        f.writelines(line1)
        line2 = str(eseh2_heat_stock_new) + "\n"
        f.writelines(line2)
        line3 = str(eseh3_heat_stock_new)
        f.writelines(line3)
    else:
        # 蓄热状态，蓄热量增加
        eseh1_heat_stock_new = eseh1_heat_stock + eseh1_load_ratio * eseh1.heating_power_rated
        eseh2_heat_stock_new = eseh2_heat_stock + eseh2_load_ratio * eseh2.heating_power_rated
        eseh3_heat_stock_new = eseh3_heat_stock + eseh3_load_ratio * eseh3.heating_power_rated
        line1 = str(eseh1_heat_stock_new) + "\n"
        f.writelines(line1)
        line2 = str(eseh2_heat_stock_new) + "\n"
        f.writelines(line2)
        line3 = str(eseh3_heat_stock_new)
        f.writelines(line3)


def energy_storage_equipment_heat_load_ratio(eseh_num, eseh1_load_ratio_a, eseh2_load_ratio_a, eseh3_load_ratio_a, eseh_load_ratio):
    """根据目前启动的设备数量将不同的设备负荷率设置成成公用负荷率"""
    if eseh_num == 1:
        if eseh1_load_ratio_a > 0:
            eseh1_load_ratio = eseh_load_ratio
            eseh2_load_ratio = 0
            eseh3_load_ratio = 0
        elif eseh1_load_ratio_a == 0 and eseh2_load_ratio_a > 0:
            eseh1_load_ratio = 0
            eseh2_load_ratio = eseh_load_ratio
            eseh3_load_ratio = 0
        elif eseh1_load_ratio_a == 0 and eseh2_load_ratio_a == 0 and eseh3_load_ratio_a > 0:
            eseh1_load_ratio = 0
            eseh2_load_ratio = 0
            eseh3_load_ratio = eseh_load_ratio
        else:
            eseh1_load_ratio = 0
            eseh2_load_ratio = 0
            eseh3_load_ratio = 0
    elif eseh_num == 2:
        if eseh1_load_ratio_a > 0 and eseh2_load_ratio_a > 0:
            eseh1_load_ratio = eseh_load_ratio
            eseh2_load_ratio = eseh_load_ratio
            eseh3_load_ratio = 0
        elif eseh1_load_ratio_a > 0 and eseh2_load_ratio_a == 0 and eseh3_load_ratio_a > 0:
            eseh1_load_ratio = eseh_load_ratio
            eseh2_load_ratio = 0
            eseh3_load_ratio = eseh_load_ratio
        elif eseh1_load_ratio_a == 0 and eseh2_load_ratio_a > 0 and eseh3_load_ratio_a > 0:
            eseh1_load_ratio = 0
            eseh2_load_ratio = eseh_load_ratio
            eseh3_load_ratio = eseh_load_ratio
        else:
            eseh1_load_ratio = 0
            eseh2_load_ratio = 0
            eseh3_load_ratio = 0
    elif eseh_num == 3:
        if eseh1_load_ratio_a > 0 and eseh2_load_ratio_a > 0 and eseh3_load_ratio_a > 0:
            eseh1_load_ratio = eseh_load_ratio
            eseh2_load_ratio = eseh_load_ratio
            eseh3_load_ratio = eseh_load_ratio
        else:
            eseh1_load_ratio = 0
            eseh2_load_ratio = 0
            eseh3_load_ratio = 0
    else:
        eseh1_load_ratio = 0
        eseh2_load_ratio = 0
        eseh3_load_ratio = 0

    return eseh1_load_ratio, eseh2_load_ratio, eseh3_load_ratio


def energy_storage_equipment_heat_load_ratio_correction(eseh, heat_load_a, load_ratio, eseh_heat_stock):
    """对计算出的设备负荷率进行修正"""
    # 如果是向外供热的工况
    if heat_load_a > 0:
        if eseh_heat_stock < eseh.heating_power_rated * load_ratio:
            load_ratio_correction = eseh_heat_stock / eseh.heating_power_rated
        else:
            load_ratio_correction = load_ratio
    elif heat_load_a ==0:
        load_ratio_correction = 0
    else:
        # 如果是蓄热的工况
        if eseh.heating_storage_rated - eseh_heat_stock < eseh.heating_power_rated * load_ratio:
            load_ratio_correction = (eseh.heating_storage_rated - eseh_heat_stock) / eseh.heating_power_rated
        else:
            load_ratio_correction = load_ratio

    return load_ratio_correction


def energy_storage_equipment_heat_result(ans_eseh, eseh1, eseh2, eseh3):
    """选择出最合适的蓄热水罐（实际上是水泵）的计算结果"""
    # 总成本最小值
    cost_min = min(ans_eseh[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_eseh[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    eseh1_ratio = ans_eseh[1][cost_min_index]
    eseh2_ratio = ans_eseh[2][cost_min_index]
    eseh3_ratio = ans_eseh[3][cost_min_index]
    heat_load_out = eseh1_ratio * eseh1.heating_power_rated + eseh2_ratio * eseh2.heating_power_rated + eseh3_ratio * eseh3.heating_power_rated
    power_consumption_total = ans_eseh[4][cost_min_index]
    water_supply_total = ans_eseh[5][cost_min_index]

    return eseh1_ratio, eseh2_ratio, eseh3_ratio, heat_load_out, power_consumption_total, water_supply_total


def print_energy_storage_equipment_heat(ans_eseh, eseh1, eseh2, eseh3):
    """打印出最合适的蓄热水罐（实际上是水泵）的计算结果"""
    # 总成本最小值
    cost_min = min(ans_eseh[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_eseh[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    eseh1_ratio = ans_eseh[1][cost_min_index]
    eseh2_ratio = ans_eseh[2][cost_min_index]
    eseh3_ratio = ans_eseh[3][cost_min_index]
    heat_load_out = eseh1_ratio * eseh1.heating_power_rated + eseh2_ratio * eseh2.heating_power_rated + eseh3_ratio * eseh3.heating_power_rated

    print("蓄能水罐最低总运行成本为： " + str(cost_min) + "\n" + "蓄能水罐水泵1负荷率为： " + str(eseh1_ratio) + "\n" + "蓄能水罐水泵2负荷率为： " + str(eseh2_ratio) + "\n" + "蓄能水罐水泵3负荷率为： " + str(eseh3_ratio) + "\n" + "蓄能水罐总制热出力为： " + str(heat_load_out))


def energy_storage_equipment_heat_cost(eseh, gc, load_ratio):
    """蓄热水罐成本计算"""
    # 热冻水流量,某一负荷率条件下
    heating_water_flow = eseh.heating_water_flow(load_ratio)
    # 辅助设备耗电功率,某一负荷率条件下
    auxiliary_equipment_power_consumption = eseh.auxiliary_equipment_power_consumption(heating_water_flow)
    # 总耗电功率,某一负荷率条件下（只有水泵耗电）
    total_power_consumption = auxiliary_equipment_power_consumption
    # 电成本（元）,某一负荷率条件下
    total_electricity_cost = total_power_consumption * gc.buy_electricity_price
    # 在计算补水成本
    # 热冻水补水量,某一负荷率条件下
    centrifugal_chiller_chiller_water_supply = heating_water_flow * gc.closed_loop_supply_rate
    # 总补水量,某一负荷率条件下（只有热冻水补水）
    total_water_supply = centrifugal_chiller_chiller_water_supply
    # 补水成本,某一负荷率条件下
    total_water_cost = total_water_supply * gc.water_price
    # 成本合计
    cost_total = total_electricity_cost + total_water_cost
    # 返回计算结果
    return cost_total, total_power_consumption, total_water_supply, heating_water_flow


def test_energy_storage_equipment_heat_function():
    """测试蓄能水罐计算"""
    gc = Global_Constant()
    # 实例化1组3个蓄热水罐的循环水泵（水泵3用1备）
    eseh1_wp_heating_water = Water_Pump(50, False, 35, gc)
    eseh2_wp_heating_water = Water_Pump(50, False, 35, gc)
    eseh3_wp_heating_water = Water_Pump(50, False, 35, gc)
    # 实例化3个蓄热水罐（实际上只有1个水罐，但是有3个水泵，将水泵假想3等分，作为3个水罐，与水泵一一对应去计算）
    eseh1 = Energy_Storage_Equipment_Heat(1000, 0.1, 8000, eseh1_wp_heating_water, gc)
    eseh2 = Energy_Storage_Equipment_Heat(1000, 0.1, 8000, eseh2_wp_heating_water, gc)
    eseh3 = Energy_Storage_Equipment_Heat(1000, 0.1, 8000, eseh3_wp_heating_water, gc)
    # 热负荷
    heat_load_a = 3000
    ans_eseh = energy_storage_equipment_heat_function(heat_load_a, eseh1, eseh2, eseh3, gc)
    print_energy_storage_equipment_heat(ans_eseh, eseh1, eseh2, eseh3)
    # 写入txt文件
    # hour_state = 1
    # eseh1_heat_stock = energy_storage_equipment_heat_storage_residual_read()[0]
    # eseh2_heat_stock = energy_storage_equipment_heat_storage_residual_read()[1]
    # eseh3_heat_stock = energy_storage_equipment_heat_storage_residual_read()[2]
    # energy_storage_equipment_heat_storage_residual_write(hour_state, eseh1, eseh2, eseh3, 1, 1, 1, eseh1_heat_stock, eseh2_heat_stock, eseh3_heat_stock)

# test_energy_storage_equipment_heat_function()

