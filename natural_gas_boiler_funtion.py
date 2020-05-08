import math
from equipment import Water_Pump, Natural_Gas_Boiler_heat
from global_constant import Global_Constant


def natural_gas_boiler_heat_funtion(heat_load, ngbh1, ngbh2, gc):
    """天然气采暖锅炉计算方程"""
    # 天然气采暖锅炉母管制系统布置方式"""
    # 天然气采暖锅炉的计算步长
    ngbh1_step = 1
    ngbh2_step = 1
    # 列表，储存2台设备计算出的负荷率结果
    ngbh_load_ratio_result_all = [0, 0]
    # 申明一个列表，储存计算出的总成本
    cost = []
    # 列表，储存2台天然气采暖锅炉的总天然气耗量
    total_natural_gas_consumption = []
    # 列表，储存2台天然气采暖锅炉的总耗电功率
    total_power_consumption = []
    # 列表， 储存2台离心式冷水机的总补水量
    total_water_supply = []
    # 列表，储存2台设备计算出的负荷率结果
    ngbh1_load_ratio_result = []
    ngbh2_load_ratio_result = []

    # 确定需要几台设备，向上取整（天然气采暖可以启动的最大数量）
    ngbh_num_max_2 = math.ceil(heat_load / ngbh1.heating_power_rated)
    # 如果恰好整除，则向上加1
    if ngbh_num_max_2 == int(ngbh_num_max_2):
        ngbh_num_max_1 = ngbh_num_max_2 + 1
    else:
        ngbh_num_max_1 = ngbh_num_max_2
    # 最大数量不可以超过2
    if ngbh_num_max_1 > 2:
        ngbh_num_max = 2
    else:
        ngbh_num_max = ngbh_num_max_1

    # 天然气采暖热水锅炉启动的台数初始值
    ngb_num = 1

    while ngb_num <= ngbh_num_max:
        # 初始化设备1、2的负荷率
        if ngb_num >= 1:
            ngbh1_load_ratio = ngbh1.load_min
        else:
            ngbh1_load_ratio = 0
        if ngb_num >= 2:
            ngbh2_load_ratio = ngbh2.load_min
        else:
            ngbh2_load_ratio = 0
        while ngbh1_load_ratio <= 1 + gc.load_ratio_error_coefficient:
            # 计算2个设备的制热出力
            ngbh1_heat_out_now = ngbh1_load_ratio * ngbh1.heating_power_rated
            ngbh2_heat_out_now = ngbh2_load_ratio * ngbh2.heating_power_rated
            ngbh_heat_out_now_sum = ngbh1_heat_out_now + ngbh2_heat_out_now
            if ngbh_heat_out_now_sum < heat_load:
                # 增加设备1、2负荷率
                if ngb_num >= 1:
                    ngbh1_load_ratio += ngbh1_step / 100
                else:
                    ngbh1_load_ratio = 0
                if ngb_num >= 2:
                    ngbh2_load_ratio += ngbh2_step / 100
                else:
                    ngbh2_load_ratio = 0
            else:
                # 保存2个设备的负荷率
                ngbh_load_ratio_result_all[0] = ngbh1_load_ratio
                ngbh_load_ratio_result_all[1] = ngbh2_load_ratio
                ngbh1_load_ratio_result.append(ngbh_load_ratio_result_all[0])
                ngbh2_load_ratio_result.append(ngbh_load_ratio_result_all[1])
                # 计算2个设备的总天然气耗量
                ngbh1_natural_gas_consumption = natural_gas_boiler_heat_cost(ngbh1, gc, ngbh1_load_ratio)[1]
                ngbh2_natural_gas_consumption = natural_gas_boiler_heat_cost(ngbh2, gc, ngbh2_load_ratio)[1]
                ngbh_natural_gas_consumption_total = ngbh1_natural_gas_consumption + ngbh2_natural_gas_consumption
                total_natural_gas_consumption.append(ngbh_natural_gas_consumption_total)
                # 计算2个设备的总耗电功率
                ngbh1_power_consumption = natural_gas_boiler_heat_cost(ngbh1, gc, ngbh1_load_ratio)[2]
                ngbh2_power_consumption = natural_gas_boiler_heat_cost(ngbh2, gc, ngbh2_load_ratio)[2]
                ngbh_power_consumption_total = ngbh1_power_consumption + ngbh2_power_consumption
                total_power_consumption.append(ngbh_power_consumption_total)
                # 计算2个设备的总补水量
                ngbh1_water_supply = natural_gas_boiler_heat_cost(ngbh1, gc, ngbh1_load_ratio)[3]
                ngbh2_water_supply = natural_gas_boiler_heat_cost(ngbh2, gc, ngbh2_load_ratio)[3]
                ngbh_water_supply_total = ngbh1_water_supply + ngbh2_water_supply
                total_water_supply.append(ngbh_water_supply_total)
                # 计算2个设备的成本
                ngbh1_cost = natural_gas_boiler_heat_cost(ngbh1, gc, ngbh1_load_ratio)[0]
                ngbh2_cost = natural_gas_boiler_heat_cost(ngbh2, gc, ngbh2_load_ratio)[0]
                ngbh_cost_total = ngbh1_cost + ngbh2_cost
                cost.append(ngbh_cost_total)
                break
        # 增加天然气锅炉数量
        ngb_num += 1

    # 返回计算结果
    return cost, ngbh1_load_ratio_result, ngbh2_load_ratio_result, total_natural_gas_consumption, total_power_consumption, total_water_supply


def natural_gas_boiler_heat_cost(ngbh, gc, load_ratio):
    """天然气热水锅炉成本计算"""
    # 此时的锅炉效率
    boiler_efficiency = ngbh.boiler_efficiency(load_ratio)
    # 天然气耗量
    natural_gas_consumption = ngbh.natural_gas_consumption(load_ratio, boiler_efficiency)
    # 天然气成本
    natural_gas_cost = natural_gas_consumption * gc.natural_gas_price
    # 采暖水温差
    heating_water_temperature_difference=ngbh.heating_water_temperature_difference(load_ratio)
    # 采暖水流量
    heating_water_flow = ngbh.heating_water_flow(load_ratio, heating_water_temperature_difference)
    # 采暖水补水量
    heating_water_supply = heating_water_flow * gc.closed_loop_supply_rate
    # 补水成本
    total_water_cost = heating_water_supply * gc.water_price
    # 辅机耗电功率
    auxiliary_equipment_power_consumption = ngbh.auxiliary_equipment_power_consumption(heating_water_flow)
    # 电成本
    total_electricity_cost = auxiliary_equipment_power_consumption * gc.buy_electricity_price
    # 成本金额合计
    total_cost = natural_gas_cost + total_electricity_cost + total_water_cost
    # 返回计算结果
    return total_cost, natural_gas_consumption, auxiliary_equipment_power_consumption, heating_water_supply

def natural_gas_boiler_heat_result(ans_ngbh, ngbh1, ngbh2):
    """选择出最合适的天然气采暖锅炉的计算结果"""
    # 总成本最小值
    cost_min = min(ans_ngbh[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans_ngbh[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ngbh1_ratio = ans_ngbh[1][cost_min_index]
    ngbh2_ratio = ans_ngbh[2][cost_min_index]
    natural_gas_consumption_total = ans_ngbh[3][cost_min_index]
    power_consumption_total = ans_ngbh[4][cost_min_index]
    water_supply_total = ans_ngbh[5][cost_min_index]
    heat_load_out = ngbh1_ratio * ngbh1.heating_power_rated + ngbh2_ratio * ngbh2.heating_power_rated

    return ngbh1_ratio, ngbh2_ratio, heat_load_out, natural_gas_consumption_total, power_consumption_total, water_supply_total


def print_natural_gas_boiler_heat(ans, ngbh1, ngbh2):
    """打印天然气采暖锅炉计算结果"""
    # 总成本最小值
    cost_min = min(ans[0])
    # 记录总成本最小值的列表索引
    cost_min_index = ans[0].index(cost_min)

    # 读取对应索引下的设备负荷率
    ngbh1_ratio = ans[1][cost_min_index]
    ngbh2_ratio = ans[2][cost_min_index]
    heat_load_out = ngbh1_ratio * ngbh1.heating_power_rated + ngbh2_ratio * ngbh2.heating_power_rated
    # 打印计算结果
    print("天然气采暖锅炉最低总运行成本为： " + str(cost_min) + "\n" + "天然气采暖锅炉1负荷率为： " + str(ngbh1_ratio) + "\n" + "天然气采暖锅炉2负荷率为： " + str(ngbh2_ratio) + "\n" + "天然气采暖锅炉总制热出力为： " + str(heat_load_out))


def natural_gas_boiler_in_out_hot_water(hot_water_load_ngb, ngb_hot_water, gc):
    """天然气生活热水锅炉，消耗和产出计算"""
    # 此时天然气生活热水锅炉的负荷率
    ngb_load_ratio = hot_water_load_ngb/ngb_hot_water.heating_power_rated
    # 当前负荷下生活热水流量
    hot_water_flow_now = ngb_hot_water.hot_water_flow()
    # 当前负荷下，锅炉效率
    boiler_efficiency_now = ngb_hot_water.boiler_efficiency(ngb_load_ratio)
    # 当前负荷率下，辅助设备耗电功率
    auxiliary_equipment_power_consumption_now = ngb_hot_water.auxiliary_equipment_power_consumption(hot_water_flow_now)
    # 当前负荷率下，天然气锅炉天然气消耗量
    natural_gas_consumption_now = ngb_hot_water.natural_gas_consumption(ngb_load_ratio, boiler_efficiency_now)
    # 生活热水锅炉补水量
    water_supply = hot_water_flow_now * gc.closed_loop_supply_rate

    # 返回计算结果
    return auxiliary_equipment_power_consumption_now, natural_gas_consumption_now, water_supply

def test_ngbf():
    # 实例化一个全局常量类
    gc = Global_Constant()
    # 实例化2个天然气采暖锅炉水泵
    ngbh1_wp_heating_water = Water_Pump(330, False, gc)
    ngbh2_wp_heating_water = Water_Pump(330, False, gc)
    # 实例化2个天然气采暖锅炉对象
    ngbh1 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh1_wp_heating_water, gc)
    ngbh2 = Natural_Gas_Boiler_heat(3500, 0.2, ngbh2_wp_heating_water, gc)
    ans = natural_gas_boiler_heat_funtion(7000, ngbh1, ngbh2, gc)
    print_natural_gas_boiler_heat(ans, ngbh1, ngbh2)
    #print(ans)

# test_ngbf()