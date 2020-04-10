import math
from equipment import Natural_Gas_Boiler_heat, Internal_Combustion_Engine, Water_Pump, Natural_Gas_Boiler_hot_water
from triple_supply_function import triple_supply_heat_function as tshf
from natural_gas_boiler_funtion import natural_gas_boiler_heat_funtion as ngbhf, natural_gas_boiler_heat_result as ngbhr, natural_gas_boiler_in_out_hot_water as ngbiohw

def heating_season_function(heat_load, hot_water_load, electricity_load, gc):
    """采暖季计算"""

    print("正在进行采暖季计算.........")

    # 实例化两个内燃机对象
    ice1 = Internal_Combustion_Engine(792, gc, 0.5)
    ice2 = Internal_Combustion_Engine(792, gc, 0.5)
    # 实例化2个天然气采暖锅炉水泵
    ngbh1_wp_heating_water = Water_Pump(330, False, gc)
    ngbh2_wp_heating_water = Water_Pump(330, False, gc)
    # 实例化2个天然气采暖锅炉对象
    ngbh1 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh1_wp_heating_water, gc)
    ngbh2 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh2_wp_heating_water, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个采暖水泵
    lb1_wp_heating_water = Water_Pump(170, False, gc)
    lb2_wp_heating_water = Water_Pump(170, False, gc)
    # 实例化2台溴化锂设备用到的各种水泵，2个生活热水水泵
    # 如果是母管制系统
    if gc.header_system == True:
        lb1_wp_hot_water = Water_Pump(44, False, gc)
        lb2_wp_hot_water = Water_Pump(44, False, gc)
        # 实例化天然气生活热水锅炉用到的水泵
        ngb_wp_hot_water = Water_Pump(44, False, gc)
    else:
        lb1_wp_hot_water = Water_Pump(44, False, gc)
        lb2_wp_hot_water = Water_Pump(44, False, gc)
        # 实例化天然气生活热水锅炉用到的水泵
        ngb_wp_hot_water = Water_Pump(170, False, gc)

    # 实例化生活热水锅炉
    ngb_hot_water = Natural_Gas_Boiler_hot_water(2800, 0.2, ngb_wp_hot_water, gc)

    # 如果是母管制系统
    if gc.header_system == True:
        ans_hsc = heating_season_header_system(heat_load, hot_water_load, electricity_load, ice1, ice2, ngbh1, ngbh2, lb1_wp_heating_water, lb1_wp_hot_water, lb2_wp_heating_water, lb2_wp_hot_water, ngb_hot_water, gc)
    else:
        ans_hsc = heating_season_unit_system(heat_load, hot_water_load, electricity_load, ice1, ice2, ngbh1, ngbh2, lb1_wp_heating_water, lb1_wp_hot_water, lb2_wp_heating_water, lb2_wp_hot_water, ngb_hot_water, gc)

    # 读取计算结果
    profits = ans_hsc[0]
    income = ans_hsc[1]
    cost = ans_hsc[2]
    station_heat_out_all = ans_hsc[3]
    station_electricity_out_all = ans_hsc[4]
    ice1_load_ratio_result = ans_hsc[5]
    ice2_load_ratio_result = ans_hsc[6]
    ngbh1_load_ratio_result = ans_hsc[7]
    ngbh2_load_ratio_result = ans_hsc[8]
    lb_heat_load_result = ans_hsc[9]
    lb_hot_water_result = ans_hsc[10]
    ngb_hw_hot_water_result = ans_hsc[11]

    # 返回计算结果
    return profits, income, cost, station_heat_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, ngbh1_load_ratio_result, ngbh2_load_ratio_result, lb_heat_load_result, lb_hot_water_result, ngb_hw_hot_water_result


def heating_season_header_system(heat_load, hot_water_load, electricity_load, ice1, ice2, ngbh1, ngbh2, lb1_wp_heating_water, lb1_wp_hot_water, lb2_wp_heating_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """母管制系统，采暖季计算"""
    # 生活热水总流量
    hot_water_flow_total = hot_water_load * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
    # 生活热水泵启动数量，向上取整，每个泵额定流量44t/h
    hw_wp_num = math.ceil(hot_water_flow_total / 44)
    # 每个水泵生活热水流量
    if hot_water_flow_total > 0:
        hot_water_flow = hot_water_flow_total / hw_wp_num
    else:
        hot_water_flow = 0
    # 生活热水泵耗电计算（定频泵，频率始终为50Hz）
    hw_wp_power_consumption = hw_wp_num * lb1_wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
    # 内燃机设备负荷率调节步长，百分之几
    ice1_step = 5
    ice2_step = 5
    # 迭代计算中内燃机负荷率可以循环到的最小值
    if ngbh1.heating_power_rated + ngbh2.heating_power_rated <= heat_load:
        ice1_load_ratio_min = 1
        ice2_load_ratio_min = 1
    else:
        ice1_load_ratio_min = 0
        ice2_load_ratio_min = 0
    # 列表，储存能源站向外供热供电量
    station_electricity_out_all = []
    station_heat_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存溴化锂供热热量
    lb_heat_load_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存2台天然气采暖锅炉设备计算出的负荷率结果
    ngbh1_load_ratio_result = []
    ngbh2_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_heating_season == True:
        # 溴化锂1、2的生活热水负荷最大值
        lb1_hot_water_max = gc.lb1_hot_water_max
        lb2_hot_water_max = gc.lb2_hot_water_max
        # 溴化锂设备生活热水计算步长
        lb1_hot_water_step = gc.lb1_hot_water_step
        lb2_hot_water_step = gc.lb2_hot_water_step
        # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
        if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
        elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
        else: # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
            lb_hot_water_max = hot_water_load
    else:
        lb1_hot_water_max = 0
        lb_hot_water_max = 0
        # 步长不能为0，否则无限循环
        lb1_hot_water_step = gc.project_load_error
        lb2_hot_water_step = gc.project_load_error

    # 允许启动的内燃机数量最大值
    # 从电负荷角度计算的内燃机启动数量最大值
    ice_num_max_elec_2 = math.ceil(electricity_load / ice1.electricity_power_rated)
    # 如果恰好整除，则向上加1
    if ice_num_max_elec_2 == int(ice_num_max_elec_2):
        ice_num_max_elec_1 = ice_num_max_elec_2 + 1
    else:
        ice_num_max_elec_1 = ice_num_max_elec_2
    # 最大数量不可以超过2
    if ice_num_max_elec_1 > 2:
        ice_num_max_elec = 2
    else:
        ice_num_max_elec = ice_num_max_elec_1
    # 从热负荷角度计算的内燃机启动数量最大值
    ice_num_max_heat_2 = math.ceil(heat_load / gc.lb1_heat_max)
    # 如果恰好整除，则向上加1
    if ice_num_max_heat_2 == int(ice_num_max_heat_2):
        ice_num_max_heat_1 = ice_num_max_heat_2 + 1
    else:
        ice_num_max_heat_1 = ice_num_max_heat_2
    # 最大数量不可以超过2
    if ice_num_max_heat_1 > 2:
        ice_num_max_heat = 2
    else:
        ice_num_max_heat = ice_num_max_heat_1
    # 两个结果取小值
    ice_num_max = min(ice_num_max_heat, ice_num_max_elec)

    # 内燃机启动数量初始值
    ngbh_heating_power_rated_total = ngbh1.heating_power_rated + ngbh2.heating_power_rated #天然气锅炉额定制热量之和
    if heat_load - min(gc.lb1_heat_max, gc.lb2_heat_max) > ngbh_heating_power_rated_total and heat_load - gc.lb1_heat_max- gc.lb2_heat_max <= ngbh_heating_power_rated_total:
        ice_num = 2
    elif heat_load > ngbh_heating_power_rated_total and heat_load - min(gc.lb1_heat_max, gc.lb2_heat_max) <= ngbh_heating_power_rated_total:
        ice_num = 1
    else:
        ice_num = 0

    # 内燃机启动数量，可以是0，可以是1，也可以是2
    while ice_num <= ice_num_max:
        # 重置内燃机、天然气采暖锅炉设备负荷率
        if ice_num >= 1:
            ice1_load_ratio = 1
        else:
            ice1_load_ratio = 0
        if ice_num >= 2:
            ice2_load_ratio = 1
        else:
            ice2_load_ratio = 0
        ngbh1_load_ratio = ngbh1.load_min
        ngbh2_load_ratio = ngbh2.load_min
        # 2台内燃机系统的负荷率
        ice_load_ratio_result_all = [0, 0]
        # 列表，储存2台设备计算出的负荷率结果
        ngbh_load_ratio_result_all = [0, 0]
        # 溴化锂设备制备生活热水总量的初始值
        lb1_hot_water = 0
        lb2_hot_water = 0
        # 溴化锂设备生活热水总产量初始值
        lb_hot_water_total = 0
        # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num0_calculate = 0
        # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num1_calculate = 0
        # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
        ice_num2_calculate = 0
        while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
            # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 0:
                ice_num0_calculate += 1
            # 天然气生活热水锅炉需要补充的生活热水
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 天然气采暖锅炉天然气耗量、耗电总功率，制热总功率、补水量默认值
            ngbh_nature_gas_consumption_total = 0
            ngbh_power_consumption_total = 0
            ngbh_heat_out_total = 0
            ngbh_water_supply_total = 0
            # 电收入成本默认值
            income_electricity = 0
            cost_electricity = 0
            # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 0 and ice_num0_calculate > 1:
                break
            # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 1 and ice_num1_calculate > 1:
                break
            # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 2 and ice_num2_calculate > 1:
                break
            # 改变内燃机负荷率
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                # 内燃机启动数量为1,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
                if ice_num == 1 and ice1_load_ratio == 0 and ice2_load_ratio == 0:
                    ice_num1_calculate += 1
                # 内燃机启动数量为2,负荷率都为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
                if ice_num == 2 and ice1_load_ratio == 0 and ice2_load_ratio == 0:
                    ice_num2_calculate += 1
                # 内燃机+溴化锂+天然气采暖锅炉运行状态计算
                # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                if ice1_load_ratio < ice1.load_min:
                    ice1_load_ratio = 0
                # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                if ice2_load_ratio < ice2.load_min:
                    ice2_load_ratio = 0
                # 计算三联供系统热出力
                global ts_heat_out_total
                ts_heat_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                # 三联供系统的电出力
                # 计算三联供系统电出力
                ts_electricity_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                # 天然气采暖锅炉需要补充的热负荷
                heat_load_natural_gas_boiler = heat_load - ts_heat_out_total
                # print(str(ice1_load_ratio) + '    ' + str(ice2_load_ratio) + '   ' + str(ice_num) + '    ' + str(heat_load_natural_gas_boiler))
                # 如果此时只有内燃机，且内燃机负荷率和设定的热负荷相差很小，则跳出循环
                if heat_load_natural_gas_boiler >= 0 and abs(heat_load_natural_gas_boiler) <= gc.project_load_error:
                    # 天然气采暖锅炉不进行计算
                    ngbh_calculate = False
                    # 天然气采暖锅炉负荷率都设置为0
                    ngbh1_load_ratio = 0
                    ngbh2_load_ratio = 0
                    # 天然气采暖锅炉的输入输出量
                    ngbh_nature_gas_consumption_total = 0
                    ngbh_power_consumption_total = 0
                    ngbh_heat_out_total = 0
                    ngbh_water_supply_total = 0
                else:
                    # 天然气采暖锅炉进行计算
                    ngbh_calculate = True
                if heat_load_natural_gas_boiler >= 0 and ngbh_calculate == True:
                    # 计算天然气采暖锅炉的运行策略
                    ans_ngbh = ngbhf(heat_load_natural_gas_boiler, ngbh1, ngbh2, gc)
                    # 读取此时的天然气采暖锅炉最优计算结果天然气消耗量
                    ngbh_nature_gas_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[3]
                    # 读取此时的天然气采暖锅炉最优计算结果耗电功率
                    ngbh_power_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[4]
                    # 读取此时的天然气采暖锅炉最优计算结果的供热功率
                    ngbh_heat_out_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[2]
                    # 天然气采暖锅炉补水总量
                    ngbh_water_supply_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[5]
                    # 此时2台设备的负荷率
                    ngbh1_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[0]
                    ngbh2_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[1]
                # 此时整个能源站的向外供电功率
                station_electricity_out_total = ts_electricity_out_total - ngbh_power_consumption_total - hw_wp_power_consumption
                # 此时能源站供热总功率
                station_heat_out_total = ts_heat_out_total + ngbh_heat_out_total
                # 如果仅有溴化锂供热，且制热量大于热负荷需求量，则内燃机负荷往下减
                if heat_load_natural_gas_boiler <= 0 and station_heat_out_total > heat_load and ts_heat_out_total > 0:
                    # 减小内燃机设备1、2负荷率
                    if ice_num >= 1:
                        ice1_load_ratio -= ice1_step / 100
                    else:
                        ice1_load_ratio = 0
                    if ice_num >= 2:
                        ice2_load_ratio -= ice2_step / 100
                    else:
                        ice2_load_ratio = 0
                # 如果能源站向外供电量大于电负荷需求量，则内燃机负荷往下减
                elif station_electricity_out_total > electricity_load and ts_heat_out_total > 0 + gc.project_load_error:
                    # 减小内燃机设备1、2负荷率
                    if ice_num >= 1:
                        ice1_load_ratio -= ice1_step / 100
                    else:
                        ice1_load_ratio = 0
                    if ice_num >= 2:
                        ice2_load_ratio -= ice2_step / 100
                    else:
                        ice2_load_ratio = 0
                # 程序跳出条件
                else:
                    # 存储此时的能源站向外供热供电量
                    station_electricity_out_all.append(station_electricity_out_total)
                    station_heat_out_all.append(station_heat_out_total)
                    # 储存此时的内燃机负荷率
                    ice_load_ratio_result_all[0] = ice1_load_ratio
                    ice_load_ratio_result_all[1] = ice2_load_ratio
                    ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                    ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                    # 储存此时天然气采暖锅炉的负荷率
                    ngbh_load_ratio_result_all[0] = ngbh1_load_ratio
                    ngbh_load_ratio_result_all[1] = ngbh2_load_ratio
                    ngbh1_load_ratio_result.append(ngbh_load_ratio_result_all[0])
                    ngbh2_load_ratio_result.append(ngbh_load_ratio_result_all[1])
                    # 储存溴化锂和天然气锅炉供热水量，溴化锂制热量
                    lb_hot_water_result.append(lb_hot_water_total)
                    ngb_hw_hot_water_result.append(ngb_hot_water_load)
                    lb_heat_load_result.append(ts_heat_out_total)
                    # 计算此时的能源站运行成本和收入
                    # 供电收入或者买电成本（大于0是收入，小于0是成本）
                    if station_electricity_out_total > 0:
                        income_electricity = station_electricity_out_total * gc.sale_electricity_price
                    else:
                        cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                    # 供热收入（用热负荷计算，能源站供热量比热负荷多的部分不计算）
                    income_heat = heat_load * gc.heating_price
                    # 生活热水收入
                    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                    income_hot_water = hot_water_load_total * gc.hot_water_price
                    # 三联供系统总成本（天然气+补水）
                    cost_ts = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                    # 天然气采暖锅炉天然气总成本
                    cost_ngbh_nature_gas = ngbh_nature_gas_consumption_total * gc.natural_gas_price
                    # 天然气采暖锅炉补水总成本
                    cost_ngbh_water_supply = ngbh_water_supply_total * gc.water_price
                    # 天然气热水锅炉天然气成本
                    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                    # 天然气热水锅炉补水成本计算
                    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                    # 总收入成本利润
                    income_total = income_heat + income_electricity + income_hot_water
                    cost_total = cost_electricity + cost_ngbh_nature_gas + cost_ngbh_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
                    profits_total = income_total - cost_total
                    income.append(income_total)
                    cost.append(cost_total)
                    profits.append(profits_total)
                    # 如果内燃机1负荷率已经等于0，则跳出循环
                    if ice1_load_ratio == 0:
                        break
                    elif heat_load_natural_gas_boiler <= 0 and ngbh_calculate == False:
                        break
                    # 修改内燃机1、2负荷率
                    else:
                        # 减小内燃机设备1、2负荷率
                        if ice_num >= 1:
                            ice1_load_ratio -= ice1_step / 100
                        else:
                            ice1_load_ratio = 0
                        if ice_num >= 2:
                            ice2_load_ratio -= ice2_step / 100
                        else:
                            ice2_load_ratio = 0

                # 如果溴化锂（三联供系统）外供采暖负荷小于0 ，则跳出循环
                if ice_num >= 1 and ts_heat_out_total < 0 + gc.project_load_error:
                    break
            # 溴化锂1、2制备的生活热水量增加
            if ice_num == 0:
                lb1_hot_water = 0
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 0
                ice2_load_ratio = 0
            elif ice_num == 1:
                lb1_hot_water += lb1_hot_water_step
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 1
                ice2_load_ratio = 0
            elif ice_num == 2:
                lb1_hot_water += lb1_hot_water_step
                lb2_hot_water = lb1_hot_water
                # 重置内燃机负荷率
                ice1_load_ratio = 1
                ice2_load_ratio = 1
            else:
                lb1_hot_water = 0
                lb2_hot_water = 0
                # 重置内燃机负荷率
                ice1_load_ratio = 0
                ice2_load_ratio = 0
            # 溴化锂设备的总生活热水产量
            lb_hot_water_total = lb1_hot_water + lb2_hot_water
        # 内燃机数量+1
        ice_num += 1

    # 返回计算结果
    return profits, income, cost, station_heat_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, ngbh1_load_ratio_result, ngbh2_load_ratio_result, lb_heat_load_result, lb_hot_water_result, ngb_hw_hot_water_result


def heating_season_unit_system(heat_load, hot_water_load, electricity_load, ice1, ice2, ngbh1, ngbh2, lb1_wp_heating_water, lb1_wp_hot_water, lb2_wp_heating_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """单元制系统，采暖季计算"""
    # 设备负荷率调节步长，百分之几
    ice1_step = 5
    ice2_step = 5
    # 迭代计算中内燃机负荷率可以循环到的最小值
    if ngbh1.heating_power_rated + ngbh2.heating_power_rated <= heat_load:
        ice1_load_ratio_min = 1
        ice2_load_ratio_min = 1
    else:
        ice1_load_ratio_min = 0
        ice2_load_ratio_min = 0
    # 列表，储存能源站向外供热供电量
    station_electricity_out_all = []
    station_heat_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存溴化锂供热热量
    lb_heat_load_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存2台天然气采暖锅炉设备计算出的负荷率结果
    ngbh1_load_ratio_result = []
    ngbh2_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
    if gc.lb_hot_water_switch_heating_season == True:
        # 溴化锂1、2的生活热水负荷最大值
        lb1_hot_water_max = gc.lb1_hot_water_max
        lb2_hot_water_max = gc.lb2_hot_water_max
        # 溴化锂设备生活热水计算步长
        lb1_hot_water_step = gc.lb1_hot_water_step
        lb2_hot_water_step = gc.lb2_hot_water_step
        # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
        if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
        elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (lb1_hot_water_max + lb2_hot_water_max):
            lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
        else:  # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
            lb_hot_water_max = hot_water_load
    else:
        lb1_hot_water_max = 0
        lb2_hot_water_max = 0
        lb_hot_water_max = 0
        # 步长不能为0，否则无限循环
        lb1_hot_water_step = gc.project_load_error
        lb2_hot_water_step = gc.project_load_error

    # 溴化锂设备制备生活热水总量的初始值
    lb1_hot_water = 0
    lb2_hot_water = 0
    # 溴化锂设备生活热水总产量初始值
    lb_hot_water_total = 0

    while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
        while lb2_hot_water <= lb2_hot_water_max and lb2_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
            #print(str(lb1_hot_water) + "    " + str(lb2_hot_water))
            # 天然气生活热水锅炉需要补充的生活热水量
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，辅机设备耗电量
            ngb_hw_power_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[0]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 重置内燃机、天然气采暖锅炉设备负荷率
            ice1_load_ratio = 1
            ice2_load_ratio = 1
            ngbh1_load_ratio = ngbh1.load_min
            ngbh2_load_ratio = ngbh2.load_min
            # 2台内燃机系统的负荷率
            ice_load_ratio_result_all = [0, 0]
            # 列表，储存2台设备计算出的负荷率结果
            ngbh_load_ratio_result_all = [0, 0]
            # 天然气采暖锅炉天然气消耗总量、耗电总功率，制热总功率、补水量默认值
            ngbh_nature_gas_consumption_total = 0
            ngbh_power_consumption_total = 0
            ngbh_heat_out_total = 0
            ngbh_water_supply_total = 0
            # 电收入成本默认值
            income_electricity = 0
            cost_electricity = 0
            # 改变内燃机负荷率
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                while ice2_load_ratio >= ice2_load_ratio_min and ice2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                    # 内燃机+溴化锂+天然气采暖锅炉运行状态计算
                    # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                    if ice1_load_ratio < ice1.load_min:
                        ice1_load_ratio = 0
                    # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                    if ice2_load_ratio < ice2.load_min:
                        ice2_load_ratio = 0
                    # 计算三联供系统热出力
                    ts_heat_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                    # 三联供系统的电出力
                    # 计算三联供系统电出力
                    ts_electricity_out_total = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[1]
                    # 天然气采暖锅炉需要补充的热负荷
                    heat_load_natural_gas_boiler = heat_load - ts_heat_out_total
                    # 如果此时只有内燃机，且内燃机负荷率和设定的热负荷相差很小，则跳出循环
                    if heat_load_natural_gas_boiler >= 0 and abs(heat_load_natural_gas_boiler) <= gc.project_load_error:
                        # 天然气采暖锅炉不进行计算
                        ngbh_calculate = False
                        # 天然气采暖锅炉负荷率都设置为0
                        ngbh1_load_ratio = 0
                        ngbh2_load_ratio = 0
                        # 天然气采暖锅炉的输入输出量
                        ngbh_nature_gas_consumption_total = 0
                        ngbh_power_consumption_total = 0
                        ngbh_heat_out_total = 0
                        ngbh_water_supply_total = 0
                    else:
                        # 天然气采暖锅炉进行计算
                        ngbh_calculate = True
                    if heat_load_natural_gas_boiler >= 0 and ngbh_calculate == True:
                        # 计算天然气采暖锅炉的运行策略
                        ans_ngbh = ngbhf(heat_load_natural_gas_boiler, ngbh1, ngbh2, gc)
                        # 读取此时的天然气采暖锅炉最优计算结果天然气消耗量
                        ngbh_nature_gas_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[3]
                        # 读取此时的天然气采暖锅炉最优计算结果耗电功率
                        ngbh_power_consumption_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[4]
                        # 读取此时的天然气采暖锅炉最优计算结果的供热功率
                        ngbh_heat_out_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[2]
                        # 天然气采暖锅炉补水总量
                        ngbh_water_supply_total = ngbhr(ans_ngbh, ngbh1, ngbh2)[5]
                        # 此时4台设备的负荷率
                        ngbh1_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[0]
                        ngbh2_load_ratio = ngbhr(ans_ngbh, ngbh1, ngbh2)[1]
                    # 此时整个能源站的向外供电功率
                    station_electricity_out_total = ts_electricity_out_total - ngbh_power_consumption_total - ngb_hw_power_consumption
                    # 此时能源站供热总功率
                    station_heat_out_total = ts_heat_out_total + ngbh_heat_out_total
                    # 如果仅有溴化锂供热，且制热量大于热负荷需求量，则内燃机负荷往下减
                    if heat_load_natural_gas_boiler <= 0 and station_heat_out_total > heat_load and ts_heat_out_total > 0:
                        # 减小内燃机设备2负荷率
                        ice2_load_ratio -= ice2_step / 100
                    # 如果能源站向外供电量大于电负荷需求量，则内燃机负荷往下减
                    elif station_electricity_out_total > electricity_load and ts_heat_out_total > 0 + gc.project_load_error:
                        # 减小内燃机设备2负荷率
                        ice2_load_ratio -= ice2_step / 100
                    # 程序跳出条件
                    else:
                        # 存储此时的能源站向外供热供电量
                        station_electricity_out_all.append(station_electricity_out_total)
                        station_heat_out_all.append(station_heat_out_total)
                        # 储存此时的内燃机负荷率
                        ice_load_ratio_result_all[0] = ice1_load_ratio
                        ice_load_ratio_result_all[1] = ice2_load_ratio
                        ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                        ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                        # 储存此时天然气采暖锅炉的负荷率
                        ngbh_load_ratio_result_all[0] = ngbh1_load_ratio
                        ngbh_load_ratio_result_all[1] = ngbh2_load_ratio
                        ngbh1_load_ratio_result.append(ngbh_load_ratio_result_all[0])
                        ngbh2_load_ratio_result.append(ngbh_load_ratio_result_all[1])
                        # 储存溴化锂和天然气锅炉供热水量，溴化锂制热量
                        lb_hot_water_result.append(lb_hot_water_total)
                        ngb_hw_hot_water_result.append(ngb_hot_water_load)
                        lb_heat_load_result.append(ts_heat_out_total)
                        # 计算此时的能源站运行成本和收入
                        # 供电收入或者买电成本（大于0是收入，小于0是成本）
                        if station_electricity_out_total > 0:
                            income_electricity = station_electricity_out_total * gc.sale_electricity_price
                        else:
                            cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                        # 供热收入（用热负荷计算，能源站供热量比热负荷多的部分不计算）
                        income_heat = heat_load * gc.heating_price
                        # 生活热水收入
                        hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                        income_hot_water = hot_water_load_total * gc.hot_water_price
                        # 三联供系统总成本（天然气+补水）
                        cost_ts = tshf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc)[4]
                        # 天然气采暖锅炉天然气总成本
                        cost_ngbh_nature_gas = ngbh_nature_gas_consumption_total * gc.natural_gas_price
                        # 天然气采暖锅炉补水总成本
                        cost_ngbh_water_supply = ngbh_water_supply_total * gc.water_price
                        # 天然气热水锅炉天然气成本
                        cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                        # 天然气热水锅炉补水成本计算
                        cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                        # 总收入成本利润
                        income_total = income_heat + income_electricity + income_hot_water
                        cost_total = cost_electricity + cost_ngbh_nature_gas + cost_ngbh_water_supply + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
                        profits_total = income_total - cost_total
                        income.append(income_total)
                        cost.append(cost_total)
                        profits.append(profits_total)
                        # 如果内燃机2负荷率已经等于0，则跳出循环
                        if ice2_load_ratio == 0:
                            break
                        elif heat_load_natural_gas_boiler <= 0 and ngbh_calculate == False:
                            break
                        # 修改内燃机2负荷率
                        else:
                            ice2_load_ratio -= ice2_step / 100
                # 下降内燃机设备1负荷率，内燃机2负荷率重置
                ice1_load_ratio -= ice1_step / 100
                ice2_load_ratio = 1
            # 溴化锂2制备的生活热水量增加
            lb2_hot_water += lb2_hot_water_step
            # 溴化锂设备的总生活热水产量
            lb_hot_water_total = lb1_hot_water + lb2_hot_water
        # 溴化锂1制备的生活热水量增加，设备2重置回默认值
        lb1_hot_water += lb1_hot_water_step
        lb2_hot_water = 0
        # 溴化锂设备的总生活热水产量
        lb_hot_water_total = lb1_hot_water + lb2_hot_water

    # 返回计算结果
    return profits, income, cost, station_heat_out_all, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, ngbh1_load_ratio_result, ngbh2_load_ratio_result, lb_heat_load_result, lb_hot_water_result, ngb_hw_hot_water_result


def print_heating_season(ans):
    """将制热季计算结果打印出来"""
    # 能源站总利润最大值
    profitis_max = max(ans[0])
    # 能源站成本最小值
    cost_min = min(ans[2])
    # 记录列表索引
    # 利润最大索引
    profitis_max_index = ans[0].index(profitis_max)
    # 成本最小索引
    cost_min_index = ans[2].index(cost_min)
    # 采用的索引（利润最大的结果）
    heating_season_index = profitis_max_index

    # 读取对应索引下的参数
    station_profitis_max = ans[0][heating_season_index]
    station_cost_min = ans[2][heating_season_index]
    station_heat_out_all = ans[3][heating_season_index]
    station_electricity_out_all = ans[4][heating_season_index]
    ice1_load_ratio = ans[5][heating_season_index]
    ice2_load_ratio = ans[6][heating_season_index]
    ngbh1_load_ratio = ans[7][heating_season_index]
    ngbh2_load_ratio = ans[8][heating_season_index]
    # 溴化锂制热量，制生活热水量
    lb_heat_load = ans[9][heating_season_index]
    lb_hot_water = ans[10][heating_season_index]
    # 天然气锅炉制生活热水量
    ngb_hw_hot_water = ans[11][heating_season_index]

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(station_cost_min) + "\n"  + "能源站供热功率为： " + str(station_heat_out_all) + "\n" + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(ice1_load_ratio) + "\n" + "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "天然气采暖锅炉1负荷率为： " + str(ngbh1_load_ratio) + "\n" + "天然气采暖锅炉2负荷率为： " + str(ngbh2_load_ratio) + "\n" + "溴化锂设备供热功率为： " + str(lb_heat_load) + "\n" + "溴化锂供生活热水功率为： " + str(lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(ngb_hw_hot_water) + "\n")