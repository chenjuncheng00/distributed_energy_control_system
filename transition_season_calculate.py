import math
from equipment import Lithium_Bromide_Transition
from triple_supply_function import triple_supply_transition_function as tstf, triple_supply_in_out_transition as tsiot, lithium_bromide_transition_function as lbtf
from natural_gas_boiler_funtion import natural_gas_boiler_in_out_hot_water as ngbiohw, natural_gas_boiler_heat_cost as ngbhc

def transition_season_function(hot_water_load, electricity_load, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """过渡季计算"""

    print("正在进行过渡季计算.........")

    # 母管制系统，过渡季计算
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
    if hot_water_load - min(gc.lb1_hot_water_max, gc.lb2_hot_water_max) > ngb_hot_water.heating_power_rated and hot_water_load - gc.lb1_hot_water_max - gc.lb2_hot_water_max <= ngb_hot_water.heating_power_rated:
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
            # print(str(lb_hot_water_total) + '    ' + str(ngb_hot_water_load) + '   ' + str(lb1_hot_water) + '   ' + str(lb2_hot_water))
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


def print_transition_season(ans, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, ngb_hot_water, gc):
    """将过渡季计算结果打印出来"""
    try:
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
    except:
        # 读取对应索引下的参数
        station_profitis_max = 0
        station_cost_min = 0
        station_electricity_out_all = 0
        ice1_load_ratio = 0
        ice2_load_ratio = 0
        # 溴化锂制生活热水量
        lb_hot_water = 0
        # 天然气锅炉制生活热水量
        ngb_hw_hot_water = 0

    # 打印出结果
    print("能源站利润最大值为： " + str(station_profitis_max) + "\n" + "能源站成本最小值为： " + str(station_cost_min) + "\n"
          + "能源站供电功率为： " + str(station_electricity_out_all) + "\n" + "内燃机1负荷率为： " + str(ice1_load_ratio) + "\n" +
          "内燃机2负荷率为： " + str(ice2_load_ratio) + "\n" + "溴化锂供生活热水功率为： " + str(
        lb_hot_water) + "\n" + "天然气锅炉供生活热水功率为： " + str(ngb_hw_hot_water) + "\n")

    # 向数据库写入计算结果
    # 内燃机1和溴化锂1
    if ice1_load_ratio > 0:
        # 内燃机1
        ice1_electrical_efficiency = ice1.electricity_power_efficiency(ice1_load_ratio)
        ice1_residual_heat_efficiency = ice1.residual_heat_efficiency(ice1_load_ratio)
        ice1_electrical_power = ice1.electricity_power_rated * ice1_load_ratio
        ice1_total_heat_input = ice1.total_heat_input(ice1_load_ratio, ice1_electrical_efficiency)
        ice1_residual_heat_power = ice1.residual_heat_power(ice1_total_heat_input, ice1_residual_heat_efficiency)
        ice1_natural_gas_consumption = ice1.natural_gas_consumption(ice1_total_heat_input)
        ice1_power_consumption = ice1.auxiliary_equipment_power_consumption(ice1_load_ratio)
        ice1_electrical_income = ice1_electrical_power * gc.sale_electricity_price
        ice1_electrical_cost = ice1_natural_gas_consumption * gc.natural_gas_price + ice1_power_consumption * gc.buy_electricity_price
        # 写入数据库

        # 溴化锂1
        lb1_transition = Lithium_Bromide_Transition(ice1_residual_heat_power, lb1_wp_hot_water, 0.5, gc)
        lb1_cold_heat_out = 0
        lb1_wp_heat_chilled_water_frequency = 0
        lb1_wp_cooling_water_frequency = 0
        lb1_hot_water_out = lb_hot_water * (ice1_load_ratio / (ice1_load_ratio + ice2_load_ratio))
        lb1_power_consumption = lbtf(lb1_hot_water_out, ice1_load_ratio, lb1_transition, gc)[0]
        lb1_chilled_heat_water_flow = 0
        lb1_cooling_water_flow = 0
        lb1_wp_chilled_heat_water_power_consumption =0
        lb1_wp_cooling_water_power_consumption = 0
        lb1_fan_power_consumption = 0
        lb1_cold_cop = 0
        lb1_heat_cop = 0
        lb1_hot_water_cop = lb1_transition.heating_cop(ice1_load_ratio)
        lb1_cold_cost = 0
        lb1_heat_cost = 0
        lb1_hot_water_cost = lb1_power_consumption * gc.buy_electricity_price + lbtf(lb1_hot_water_out, ice1_load_ratio, lb1_transition, gc)[1]*gc.water_price
        lb1_hot_water_temperature_difference = lb1_transition.hot_water_temperature_difference(ice1_load_ratio)
        lb1_hot_water_flow = lb1_transition.hot_water_flow(lb1_hot_water_out, lb1_hot_water_temperature_difference)
        lb1_wp_hot_water_frequency = 50
        lb1_wp_hot_water_power_consumption = lb1_transition.wp_hot_water.pump_performance_data(lb1_hot_water_flow, lb1_wp_hot_water_frequency)[1]
        lb1_cold_income = 0
        lb1_heat_income = 0
        lb1_hot_water_income = lb1_hot_water_out * gc.hot_water_price
        # 内燃机运行状态
        ice1_start_state = True
        ice1_stop_state = False
        ice1_fault_state = False
        # 溴化锂运行状态
        lb1_cold_state = False
        lb1_heat_state = False
        lb1_hot_water_state = True
        lb1_stop_state = False
        lb1_fault_state = False
        # 写入数据库


    else:
        ice1_electrical_efficiency = 0
        ice1_electrical_power = 0
        ice1_electrical_income = 0
        ice1_electrical_cost = 0
        ice1_natural_gas_consumption = 0
        ice1_power_consumption = 0
        lb1_cold_cop = 0
        lb1_heat_cop = 0
        lb1_hot_water_cop = 0
        lb1_cold_heat_out = 0
        lb1_hot_water_out = 0
        lb1_power_consumption = 0
        lb1_cold_cost = 0
        lb1_heat_cost = 0
        lb1_hot_water_cost = 0
        lb1_cold_income = 0
        lb1_heat_income = 0
        lb1_hot_water_income = 0
        lb1_chilled_heat_water_flow = 0
        lb1_hot_water_flow = 0
        # 1#内燃机运行状态
        ice1_start_state = False
        ice1_stop_state = True
        ice1_fault_state = False
        # 1#溴化锂运行状态
        lb1_cold_state = False
        lb1_heat_state = False
        lb1_hot_water_state = False
        lb1_stop_state = True
        lb1_fault_state = False
        # 写入数据库


    # 内燃机2
    if ice2_load_ratio > 0:
        ice2_electrical_efficiency = ice2.electricity_power_efficiency(ice2_load_ratio)
        ice2_residual_heat_efficiency = ice2.residual_heat_efficiency(ice2_load_ratio)
        ice2_electrical_power = ice2.electricity_power_rated * ice2_load_ratio
        ice2_total_heat_input = ice2.total_heat_input(ice2_load_ratio, ice2_electrical_efficiency)
        ice2_residual_heat_power = ice2.residual_heat_power(ice2_total_heat_input, ice2_residual_heat_efficiency)
        ice2_natural_gas_consumption = ice2.natural_gas_consumption(ice2_total_heat_input)
        ice2_power_consumption = ice2.auxiliary_equipment_power_consumption(ice2_load_ratio)
        ice2_electrical_income = ice2_electrical_power * gc.sale_electricity_price
        ice2_electrical_cost = ice2_natural_gas_consumption * gc.natural_gas_price + ice2_power_consumption * gc.buy_electricity_price

        # 溴化锂2
        lb2_transition = Lithium_Bromide_Transition(ice2_residual_heat_power, lb2_wp_hot_water, 0.5, gc)
        lb2_cold_heat_out = 0
        lb2_wp_heat_chilled_water_frequency = 0
        lb2_wp_cooling_water_frequency = 0
        lb2_hot_water_out = lb_hot_water * (ice2_load_ratio / (ice2_load_ratio + ice2_load_ratio))
        lb2_power_consumption = lbtf(lb2_hot_water_out, ice2_load_ratio, lb2_transition, gc)[0]
        lb2_chilled_heat_water_flow = 0
        lb2_cooling_water_flow = 0
        lb2_wp_chilled_heat_water_power_consumption = 0
        lb2_wp_cooling_water_power_consumption = 0
        lb2_fan_power_consumption = 0
        lb2_cold_cop = 0
        lb2_heat_cop = 0
        lb2_hot_water_cop = lb2_transition.heating_cop(ice2_load_ratio)
        lb2_cold_cost = 0
        lb2_heat_cost = 0
        lb2_hot_water_cost = lb2_power_consumption * gc.buy_electricity_price + lbtf(lb2_hot_water_out, ice2_load_ratio, lb2_transition, gc)[1] * gc.water_price
        lb2_hot_water_temperature_difference = lb2_transition.hot_water_temperature_difference(ice2_load_ratio)
        lb2_hot_water_flow = lb2_transition.hot_water_flow(lb2_hot_water_out, lb2_hot_water_temperature_difference)
        lb2_wp_hot_water_frequency = 50
        lb2_wp_hot_water_power_consumption = lb2_transition.wp_hot_water.pump_performance_data(lb2_hot_water_flow, lb2_wp_hot_water_frequency)[1]
        lb2_cold_income = 0
        lb2_heat_income = 0
        lb2_hot_water_income = lb2_hot_water_out * gc.hot_water_price
        # 2#内燃机运行状态
        ice2_start_state = True
        ice2_stop_state = False
        ice2_fault_state = False
        # 2#溴化锂运行状态
        lb2_cold_state = False
        lb2_heat_state = False
        lb2_hot_water_state = True
        lb2_stop_state = False
        lb2_fault_state = False
        # 写入数据库


    else:
        ice2_electrical_efficiency = 0
        ice2_electrical_power = 0
        ice2_electrical_income = 0
        ice2_electrical_cost = 0
        ice2_natural_gas_consumption = 0
        ice2_power_consumption = 0
        lb2_cold_cop = 0
        lb2_heat_cop = 0
        lb2_hot_water_cop = 0
        lb2_cold_heat_out = 0
        lb2_hot_water_out = 0
        lb2_power_consumption = 0
        lb2_cold_cost = 0
        lb2_heat_cost = 0
        lb2_hot_water_cost = 0
        lb2_cold_income = 0
        lb2_heat_income = 0
        lb2_hot_water_income = 0
        lb2_chilled_heat_water_flow = 0
        lb2_hot_water_flow = 0
        # 内燃机运行状态
        ice2_start_state = False
        ice2_stop_state = True
        ice2_fault_state = False
        # 溴化锂运行状态
        lb2_cold_state = False
        lb2_heat_state = False
        lb2_hot_water_state = False
        lb2_stop_state = True
        lb2_fault_state = False
        # 写入数据库


    # 天然气生活热水锅炉
    if ngb_hw_hot_water > 0:
        ngb3_wp_hot_water_frequency = 50
        ngb3_hot_water_out = ngb_hw_hot_water
        ngb3_load_ratio = ngb3_hot_water_out / ngb_hot_water.heating_power_rated
        ngb3_power_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[0]
        ngb3_hot_water_flow = ngb_hw_hot_water * 3600 / gc.hot_water_temperature_difference_rated / 4.2 / 1000
        ngb3_wp_hot_water_power_consumption = ngb_hot_water.wp_hot_water.pump_performance_data(ngb3_hot_water_flow, ngb3_wp_hot_water_frequency)[1]
        ngb3_efficiency = ngb_hot_water.boiler_efficiency(ngb3_load_ratio)
        ngb3_natural_gas_consumption = ngbiohw(ngb3_hot_water_out, ngb_hot_water, gc)[1]
        ngb3_income = ngb3_hot_water_out * gc.hot_water_price
        ngb3_cost = ngb3_natural_gas_consumption * gc.natural_gas_price + ngb3_natural_gas_consumption * gc.buy_electricity_price
        # 天然气热水锅炉运行状态
        ngb_hot_water_state = True
        ngb_stop_state = False
        ngb_fault_state = False
        # 写入数据库

    else:
        ngb3_efficiency = 0
        ngb3_natural_gas_consumption = 0
        ngb3_power_consumption = 0
        ngb3_income = 0
        ngb3_cost = 0
        ngb3_hot_water_out = 0
        ngb3_hot_water_flow = 0
        # 天然气热水锅炉运行状态
        ngb_hot_water_state = False
        ngb_stop_state = True
        ngb_fault_state = False
        # 写入数据库


    # 写入系统共用数据结果
    cost_total = station_cost_min
    profit_total = station_profitis_max
    income_total = cost_total + profit_total
    electricity_out_total = station_electricity_out_all
    cold_heat_out_total = 0
    hot_water_out_total = lb_hot_water + ngb_hw_hot_water
    natural_gas_consume_total = ice1_natural_gas_consumption + ice2_natural_gas_consumption + ngb3_natural_gas_consumption
    electricity_consume_total = ice1_power_consumption + ice2_power_consumption + lb1_power_consumption + lb2_power_consumption + ngb3_power_consumption
    if (ice1_natural_gas_consumption + ice2_natural_gas_consumption) > 0:
        comprehensive_energy_utilization = (ice1_electrical_power + ice2_electrical_power + lb1_cold_heat_out + lb2_cold_heat_out) * 3600 \
                                           / ((ice1_natural_gas_consumption + ice2_natural_gas_consumption) * gc.natural_gas_calorific_value)
    else:
        comprehensive_energy_utilization = 0
    cop_real_time = 0
    reduction_in_carbon_emissions = 0
    reduction_in_sulfide_emissions = 0
    reduction_in_nitride_emissions = 0
    reduction_in_dust_emissions = 0
    proportion_of_renewable_energy_power = 0


    # 写入能源站冷热电的输入输出功率数据
    photovoltaic_electricity_out_total = 0
    wind_electricity_out_total = 0
    accumulator_electricity_out_total = 0
    electricity_generation_total = ice1_electrical_power + ice2_electrical_power + photovoltaic_electricity_out_total + wind_electricity_out_total + accumulator_electricity_out_total
    ice_electricity_out_total = ice1_electrical_power + ice2_electrical_power
    buy_electricity_total = electricity_consume_total - electricity_generation_total
    lb_cold_out_total = lb1_cold_heat_out + lb2_cold_heat_out
    lb_heat_out_total = 0
    lb_hot_water_out_total = lb1_hot_water_out + lb2_hot_water_out
    ngb_hot_water_out_total = ngb3_hot_water_out
    cc_cold_out_total = 0
    chp_cold_out_total = 0
    chp_heat_out_total = 0
    ashp_cold_out_total = 0
    ese_cold_out_total = 0
    ese_heat_out_total = 0
    cold_out_total = lb_cold_out_total + cc_cold_out_total + chp_cold_out_total + ashp_cold_out_total + ese_cold_out_total
    heat_out_total = lb_heat_out_total + chp_heat_out_total + ese_heat_out_total
    # 写入数据库


    # 写入能源站冷热电的收入成本数据
    ice_income_total = ice1_electrical_income + ice2_electrical_income
    lb_cold_income_total = lb1_cold_income + lb2_cold_income
    lb_heat_income_total = lb1_heat_income + lb2_heat_income
    lb_hot_water_income_total = lb1_hot_water_income + lb2_hot_water_income
    cc_cold_income_total = 0
    chp_cold_income_total = 0
    chp_heat_income_total = 0
    ashp_cold_income_total = 0
    ngb_hot_water_income_total = ngb3_income
    photovoltaic_income_total = photovoltaic_electricity_out_total * gc.sale_electricity_price
    wind_income_total = wind_electricity_out_total * gc.sale_electricity_price
    ice_cost_total = ice1_electrical_cost + ice2_electrical_cost
    lb_cold_cost_total = lb1_cold_cost + lb2_cold_cost
    lb_heat_cost_total = lb1_heat_cost + lb2_heat_cost
    lb_hot_water_cost_total = lb1_hot_water_cost + lb2_hot_water_cost
    cc_cold_cost_total = 0
    chp_cold_cost_total = 0
    chp_heat_cost_total = 0
    ashp_cold_cost_total = 0
    ashp_heat_cost_total = 0
    ngb_hot_water_cost_total = ngb3_cost
    # 写入数据库


    # 写入设备效率数据
    ice_electrical_efficiency = max(ice1_electrical_efficiency, ice2_electrical_efficiency)
    lb_cold_efficiency = max(lb1_cold_cop, lb2_cold_cop)
    lb_heat_efficiency = max(lb1_heat_cop, lb2_heat_cop)
    lb_hot_water_efficiency = max(lb1_hot_water_cop, lb2_hot_water_cop)
    cc_cold_cop = 0
    chp_cold_cop = 0
    chp_heat_cop = 0
    ashp_cold_cop = 0
    ashp_heat_cop = 0
    ngb_hot_water_efficiency = ngb3_efficiency
    photovoltaic_electrical_efficiency = 0
    wind_electrical_efficiency = 0
    # 写入数据库


    # 写入设备冷冻水出水温度和冷水生活热水总流量数据
    chilled_water_supply_flow_total = 0
    chilled_water_supply_temperature = 0
    chilled_water_return_temperature = 0
    heat_water_supply_flow_total = 0
    heat_water_supply_temperature = 0
    heat_water_return_temperature = 0
    hot_water_supply_flow_total = lb1_hot_water_flow + lb2_hot_water_flow + ngb3_hot_water_flow
    hot_water_supply_temperature = gc.hot_water_temperature
    hot_water_return_temperature = gc.hot_water_temperature - gc.hot_water_temperature_difference_rated
    lb1_heat_chilled_water_supply_temperature = 0
    lb2_heat_chilled_water_supply_temperature = 0
    if lb1_hot_water_out > 0:
        lb1_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        lb1_hot_water_supply_temperature = 0
    if lb2_hot_water_out > 0:
        lb2_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        lb2_hot_water_supply_temperature = 0
    if ngb3_hot_water_out > 0:
        ngb3_hot_water_supply_temperature = gc.hot_water_temperature
    else:
        ngb3_hot_water_supply_temperature = 0
    cc1_chilled_water_supply_temperature = 0
    cc2_chilled_water_supply_temperature = 0
    cc3_chilled_water_supply_temperature = 0
    cc4_chilled_water_supply_temperature = 0
    chp1_heat_water_supply_temperature = 0
    chp2_heat_water_supply_temperature = 0
    ashp1_water_supply_temperature = 0
    ashp2_water_supply_temperature = 0
    ashp3_water_supply_temperature = 0
    ashp4_water_supply_temperature = 0
    ese_water_supply_temperature = 0
    # 写入数据库


    # 写入设备运行状态
    cc1_cold_state = False
    cc1_stop_state = True
    cc1_fault_state = False
    cc2_cold_state = False
    cc2_stop_state = True
    cc2_fault_state = False
    chp1_cold_state = False
    chp1_heat_state = False
    chp1_stop_state = True
    chp1_fault_state = False
    chp2_cold_state = False
    chp2_heat_state = False
    chp2_stop_state = True
    chp2_fault_state = False
    ashp1_cold_state = False
    ashp1_heat_state = False
    ashp1_stop_state = True
    ashp1_fault_state = False
    ashp2_cold_state = False
    ashp2_heat_state = False
    ashp2_stop_state = True
    ashp2_fault_state = False
    ashp3_cold_state = False
    ashp3_heat_state = False
    ashp3_stop_state = True
    ashp3_fault_state = False
    ashp4_cold_state = False
    ashp4_heat_state = False
    ashp4_stop_state = True
    ashp4_fault_state = False
    ese_cold_out_state = False
    ese_heat_out_state = False
    ese_cold_in_state = False
    ese_heat_in_state = False
    ese_stop_state = True
    ese_fault_state = False
    photovoltaic_start_state = False
    photovoltaic_stop_state = True
    photovoltaic_fault_state = False
    wind_start_state = False
    wind_stop_state = True
    wind_fault_state = False
    cdz_start_state = False
    cdz_stop_state = True
    cdz_fault_state = False
    accumulator_electricity_out_state = False
    accumulator_electricity_in_state = False
    accumulator_stop_state = True
    accumulator_fault_state = False
    lamp_start_state = False
    lamp_stop_state = True
    lamp_fault_state = False
    # 写入数据库
