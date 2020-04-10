import math
from equipment import Internal_Combustion_Engine, Water_Pump, Natural_Gas_Boiler_hot_water
from triple_supply_function import triple_supply_transition_function as tstf, triple_supply_in_out_transition as tsiot
from natural_gas_boiler_funtion import natural_gas_boiler_in_out_hot_water as ngbiohw

def transition_season_function(hot_water_load, electricity_load, gc):
    """过渡季计算"""

    print("正在进行过渡季计算.........")

    # 实例化两个内燃机对象
    ice1 = Internal_Combustion_Engine(792, gc, 0.5)
    ice2 = Internal_Combustion_Engine(792, gc, 0.5)
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
        ans_tsc = transition_season_header_system(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc)
    else:
        ans_tsc = transition_season_unit_system(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc)

    # 读取计算结果
    profits = ans_tsc[0]
    income = ans_tsc[1]
    cost = ans_tsc[2]
    station_electricity_out_all = ans_tsc[3]
    ice1_load_ratio_result = ans_tsc[4]
    ice2_load_ratio_result = ans_tsc[5]
    lb_hot_water_result = ans_tsc[6]
    ngb_hw_hot_water_result = ans_tsc[7]

    # 返回计算结果
    return profits, income, cost, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, lb_hot_water_result, ngb_hw_hot_water_result


def transition_season_unit_system(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """单元制系统，过渡季计算"""
    # 设备负荷率调节步长，百分之几
    ice1_step = 5
    ice2_step = 5
    # 迭代计算中内燃机负荷率可以循环到的最小值
    ice1_load_ratio_min = 0
    ice2_load_ratio_min = 0
    # 列表，储存能源站向外供电量
    station_electricity_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 溴化锂1、2的生活热水负荷最大值
    lb1_hot_water_max = gc.lb1_hot_water_max
    lb2_hot_water_max = gc.lb2_hot_water_max
    # 溴化锂设备生活热水计算步长
    lb1_hot_water_step = gc.lb1_hot_water_step
    lb2_hot_water_step = gc.lb2_hot_water_step
    # 根据天然气热水锅炉负荷最低值，确定溴化锂生活热水负荷最大值
    if ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) <= (
            lb1_hot_water_max + lb2_hot_water_max):
        lb_hot_water_max = hot_water_load - ngb_hot_water_load_min + gc.project_load_error
    elif ngb_hot_water_load_min < hot_water_load and (hot_water_load - ngb_hot_water_load_min) > (
            lb1_hot_water_max + lb2_hot_water_max):
        lb_hot_water_max = lb1_hot_water_max + lb2_hot_water_max
    else:  # 如果天然气热水锅炉最小负荷率大于生活热水总负荷
        lb_hot_water_max = hot_water_load

    # 溴化锂设备制备生活热水总量的初始值
    lb1_hot_water = 0
    lb2_hot_water = 0
    # 溴化锂设备生活热水总产量初始值
    lb_hot_water_total = 0

    while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
        while lb2_hot_water <= lb2_hot_water_max and lb2_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max:
            # 天然气生活热水锅炉需要补充的生活热水量
            ngb_hot_water_load = hot_water_load - lb_hot_water_total
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，辅机设备耗电量
            ngb_hw_power_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[0]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
            # 重置内燃机设备负荷率
            ice1_load_ratio = 1
            ice2_load_ratio = 1
            # 2台内燃机系统的负荷率
            ice_load_ratio_result_all = [0, 0]
            # 电收入成本默认值
            income_electricity = 0
            cost_electricity = 0
            # 改变内燃机负荷率
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                while ice2_load_ratio >= ice2_load_ratio_min and ice2_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                    # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                    if ice1_load_ratio < ice1.load_min:
                        ice1_load_ratio = 0
                    # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                    if ice2_load_ratio < ice2.load_min:
                        ice2_load_ratio = 0
                    # 计算三联供系统冷出力
                    # 三联供系统的电出力
                    # 计算三联供系统电出力
                    ts_electricity_out_total = tstf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                    # 计算三联供此时的余热没有被用掉的量
                    ts1_residual_heat_remaining = tsiot(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[5]
                    ts2_residual_heat_remaining = tsiot(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[5]
                    # 此时整个能源站的向外供电功率
                    station_electricity_out_total = ts_electricity_out_total - ngb_hw_power_consumption
                    # 跳出循环的条件
                    if station_electricity_out_total <= electricity_load and ts1_residual_heat_remaining <= 0 + gc.lb1_hot_water_step and ts1_residual_heat_remaining >= - gc.lb1_hot_water_step and ts2_residual_heat_remaining <= 0 + gc.lb2_hot_water_step and ts2_residual_heat_remaining >= - gc.lb2_hot_water_step:
                        # 设置跳出循环条件：电负荷不超，溴化锂1、2的余热浪费量<=0，同时>=-50kW
                        # 记录下此时的各种数据
                        # 存储此时的能源站向外供电量
                        station_electricity_out_all.append(station_electricity_out_total)
                        # 储存此时的内燃机负荷率
                        ice_load_ratio_result_all[0] = ice1_load_ratio
                        ice_load_ratio_result_all[1] = ice2_load_ratio
                        ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                        ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                        # 储存溴化锂和天然气锅炉供热水量
                        lb_hot_water_result.append(lb_hot_water_total)
                        ngb_hw_hot_water_result.append(ngb_hot_water_load)
                        # 计算此时的能源站运行成本和收入
                        # 供电收入或者买电成本（大于0是收入，小于0是成本）
                        if station_electricity_out_total > 0:
                            income_electricity = station_electricity_out_total * gc.sale_electricity_price
                        else:
                            cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                        # 生活热水收入
                        hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                        income_hot_water = hot_water_load_total * gc.hot_water_price
                        # 三联供系统总成本（天然气+补水）
                        cost_ts = tstf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, gc)[3]
                        # 天然气热水锅炉天然气成本
                        cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                        # 天然气热水锅炉补水成本计算
                        cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                        # 总收入成本利润
                        income_total = income_electricity + income_hot_water
                        cost_total = cost_electricity + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
                        profits_total = income_total - cost_total
                        income.append(income_total)
                        cost.append(cost_total)
                        profits.append(profits_total)
                        # 如果内燃机2负荷率已经等于0，则跳出循环
                        if ice2_load_ratio == 0:
                            break
                        # 修改内燃机2负荷率
                        else:
                            ice2_load_ratio -= ice2_step / 100
                    # 不记录，调整负荷率
                    else:
                        # 减小内燃机设备2负荷率
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
    return profits, income, cost, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, lb_hot_water_result, ngb_hw_hot_water_result

def transition_season_header_system(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """母管制系统，过渡季计算"""
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
    if ngb_hot_water.heating_power_rated <= hot_water_load:
        if (hot_water_load - ngb_hot_water.heating_power_rated) / gc.lb1_hot_water_max >= 0.4 and (hot_water_load - ngb_hot_water.heating_power_rated) / gc.lb1_hot_water_max <= 1:
            ice1_load_ratio_min = (hot_water_load - ngb_hot_water.heating_power_rated) / gc.lb1_hot_water_max
        elif (hot_water_load - ngb_hot_water.heating_power_rated) / gc.lb1_hot_water_max > 1:
            ice1_load_ratio_min = 1
        else:
            ice1_load_ratio_min = 0.4
    else:
        ice1_load_ratio_min = 0
    # 列表，储存能源站向外供电量
    station_electricity_out_all = []
    # 列表，储存溴化锂和天然气锅炉供生活热水功率
    lb_hot_water_result = []
    ngb_hw_hot_water_result = []
    # 列表，储存2台内燃机计算出的负荷率结果
    ice1_load_ratio_result = []
    ice2_load_ratio_result = []
    # 列表，储存整个能源站的收入、成本、利润
    income = []
    cost = []
    profits = []
    # 天然气锅炉不可以低于最低运行负荷率，从而确定溴化锂制热水负荷最大值
    ngb_hot_water_load_min = ngb_hot_water.heating_power_rated * ngb_hot_water.load_min
    # 2台溴化锂设备制备生活热水的最大功率
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

    # 允许启动的内燃机数量最大值
    ice_num_max_elec = math.ceil(electricity_load / ice1.electricity_power_rated)  # 从电负荷角度计算的内燃机启动数量最大值
    ice_num_max_hot_water = math.ceil(hot_water_load / gc.lb1_hot_water_max)  # 从生活热水负荷角度计算的内燃机启动数量最大值
    ice_num_max = min(ice_num_max_hot_water, ice_num_max_elec, 2)  # 但是总数不可以大于2

    # 内燃机启动数量初始值
    if hot_water_load - min(gc.lb1_hot_water_max, gc.lb2_hot_water_max) > ngb_hot_water.heating_power_rated and hot_water_load - gc.lb1_hot_water_max- gc.lb2_hot_water_max <= ngb_hot_water.heating_power_rated:
        ice_num = 2
    elif hot_water_load > ngb_hot_water.heating_power_rated and hot_water_load - min(gc.lb1_hot_water_max, gc.lb2_hot_water_max) <= ngb_hot_water.heating_power_rated:
        ice_num = 1
    else:
        ice_num = 0

    # 内燃机启动数量，可以是0，可以是1，也可以是2
    while ice_num <= ice_num_max:
        # 2台内燃机系统的负荷率
        ice_load_ratio_result_all = [0, 0]
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
        while lb1_hot_water <= lb1_hot_water_max and lb1_hot_water >= 0 and lb_hot_water_total <= lb_hot_water_max + gc.project_load_error:
            # 重置内燃机、冷水机设备负荷率
            if ice_num >= 1:
                ice1_load_ratio = 1
            else:
                ice1_load_ratio = 0
            if ice_num >= 2:
                ice2_load_ratio = 1
            else:
                ice2_load_ratio = 0
            # 内燃机启动数量为0情况下的计算次数计数，这种情况下只计算一次，防止死循环
            if ice_num == 0:
                ice_num0_calculate += 1
            # 天然气生活热水锅炉需要补充的生活热水量
            if hot_water_load - lb_hot_water_total > ngb_hot_water.heating_power_rated:
                ngb_hot_water_load = ngb_hot_water.heating_power_rated
            else:
                ngb_hot_water_load = hot_water_load - lb_hot_water_total
            #print(str(lb_hot_water_total) + '    ' + str(ngb_hot_water_load) + '   ' + str(lb1_hot_water) + '   ' + str(lb2_hot_water))
            # 天然气热水锅炉天然气消耗量
            ngb_hw_nature_gas_consumption = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[1]
            # 天然气生活热水锅炉，补水量计算
            ngb_hw_water_supply = ngbiohw(ngb_hot_water_load, ngb_hot_water, gc)[2]
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
            # print(str(ice_num) + '   ' + str(ice1_load_ratio) + '   ' + str(ice2_load_ratio))
            while ice1_load_ratio >= ice1_load_ratio_min and ice1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
                # print(str(ice_num) + '   '  + str(ice1_load_ratio) + '   '  + str(ice2_load_ratio) + '   ' + str(ngb_hot_water_load) + '   ' + str(lb1_hot_water) + '   ' + str(lb2_hot_water) + '   ' + str(lb_hot_water_total))
                # 内燃机+溴化锂运行状态计算
                # 如果内燃机1小于了最低负荷限制，则负荷率设置为0
                if ice1_load_ratio < ice1.load_min + gc.load_ratio_error_coefficient:
                    ice1_load_ratio = 0
                # 如果内燃机2小于了最低负荷限制，则负荷率设置为0
                if ice2_load_ratio < ice2.load_min + gc.load_ratio_error_coefficient:
                    ice2_load_ratio = 0
                # 三联供系统的电出力
                # 计算三联供系统电出力
                ts_electricity_out_total = tstf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, gc)[0]
                # 计算三联供此时的余热没有被用掉的量
                ts1_residual_heat_remaining = tsiot(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[5]
                ts2_residual_heat_remaining = tsiot(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[5]
                # 此时整个能源站的向外供电功率
                station_electricity_out_total = ts_electricity_out_total - hw_wp_power_consumption
                # 此时的整个能源站向外供生活热水总功率
                station_hot_water_out_total = ngb_hot_water_load + lb_hot_water_total
                # 跳出循环的条件
                if station_electricity_out_total <= electricity_load and station_hot_water_out_total >= hot_water_load and ts1_residual_heat_remaining <= 0 + gc.lb1_hot_water_step and ts1_residual_heat_remaining >= - gc.lb1_hot_water_step and ts2_residual_heat_remaining <= 0 + gc.lb2_hot_water_step and ts2_residual_heat_remaining >= - gc.lb2_hot_water_step:
                    # 设置跳出循环条件：电负荷不超，生活热水负荷满足需求，溴化锂1、2的余热浪费量<=0，同时>=-50kW
                    # 记录下此时的各种数据
                    # 存储此时的能源站向外供电量
                    station_electricity_out_all.append(station_electricity_out_total)
                    # 储存此时的内燃机负荷率
                    ice_load_ratio_result_all[0] = ice1_load_ratio
                    ice_load_ratio_result_all[1] = ice2_load_ratio
                    ice1_load_ratio_result.append(ice_load_ratio_result_all[0])
                    ice2_load_ratio_result.append(ice_load_ratio_result_all[1])
                    # 储存溴化锂和天然气锅炉供热水量
                    lb_hot_water_result.append(lb_hot_water_total)
                    ngb_hw_hot_water_result.append(ngb_hot_water_load)
                    # 计算此时的能源站运行成本和收入
                    # 供电收入或者买电成本（大于0是收入，小于0是成本）
                    if station_electricity_out_total > 0:
                        income_electricity = station_electricity_out_total * gc.sale_electricity_price
                    else:
                        cost_electricity = - station_electricity_out_total * gc.buy_electricity_price
                    # 生活热水收入
                    hot_water_load_total = lb_hot_water_total + ngb_hot_water_load
                    income_hot_water = hot_water_load_total * gc.hot_water_price
                    # 三联供系统总成本（天然气+补水）
                    cost_ts = tstf(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, gc)[3]
                    # 天然气热水锅炉天然气成本
                    cost_ngb_hw_nature_gas = ngb_hw_nature_gas_consumption * gc.natural_gas_price
                    # 天然气热水锅炉补水成本计算
                    cost_ngb_hw_water_supply = ngb_hw_water_supply * gc.water_price
                    # 总收入成本利润
                    income_total = income_electricity + income_hot_water
                    cost_total = cost_electricity + cost_ts + cost_ngb_hw_nature_gas + cost_ngb_hw_water_supply
                    profits_total = income_total - cost_total
                    income.append(income_total)
                    cost.append(cost_total)
                    profits.append(profits_total)
                    # 如果内燃机1负荷率已经等于0，则跳出循环
                    if ice1_load_ratio == 0:
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
                # 不记录，调整负荷率
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
            # 溴化锂1、2制备的生活热水量增加
            if ice_num >= 1:
                lb1_hot_water += lb1_hot_water_step
            else:
                lb1_hot_water = 0
            if ice_num >= 2:
                lb2_hot_water += lb2_hot_water_step
            else:
                lb2_hot_water = 0
            # 溴化锂设备的总生活热水产量
            if lb_hot_water_total <= gc.lb1_hot_water_max + gc.lb2_hot_water_max:
                lb_hot_water_total = lb1_hot_water + lb2_hot_water
            else:
                lb_hot_water_total = gc.lb1_hot_water_max + gc.lb2_hot_water_max

        # 内燃机数量+1
        ice_num += 1

    # 返回计算结果
    return profits, income, cost, station_electricity_out_all, ice1_load_ratio_result, ice2_load_ratio_result, lb_hot_water_result, ngb_hw_hot_water_result


def print_transition_season(ans):
    """将过渡季计算结果打印出来"""
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
    transition_season_index = profitis_max_index

    # 读取对应索引下的参数
    station_profitis_max = ans[0][transition_season_index]
    station_cost_min = ans[2][transition_season_index]
    station_electricity_out_all = ans[3][transition_season_index]
    ice1_load_ratio = ans[4][transition_season_index]
    ice2_load_ratio = ans[5][transition_season_index]
    # 溴化锂制生活热水量
    lb_hot_water = ans[6][transition_season_index]
    # 天然气锅炉制生活热水量
    ngb_hw_hot_water = ans[7][transition_season_index]

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(station_cost_min) + "\n" + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(ice1_load_ratio) + "\n" + "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "溴化锂供生活热水功率为： " + str(lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(ngb_hw_hot_water) + "\n")


