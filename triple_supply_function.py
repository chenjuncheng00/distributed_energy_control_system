from equipment import Lithium_Bromide_Cold, Lithium_Bromide_Heat, Lithium_Bromide_Transition
from equipment import Water_Pump, Internal_Combustion_Engine
from global_constant import Global_Constant

def triple_supply_cold_function(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_cooling_water,lb2_wp_cooling_water, lb1_wp_chilled_water, lb2_wp_chilled_water,lb1_wp_hot_water, lb2_wp_hot_water, gc):
    """三联供系统计算方程，计算在指定的冷负荷、电负荷情况下，系统（收入-成本）的最大值情况"""
    # 计算2个溴化锂的制冷出力
    lb1_cold_out_now = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water,lb1_wp_hot_water)[0]
    lb2_cold_out_now = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water,lb2_wp_hot_water)[0]
    lb_cold_out_now_sum = lb1_cold_out_now + lb2_cold_out_now
    # 计算2个三联供系统向外供电量
    # 内燃机发电功率
    ice1_electricity_power_out_cold = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water)[4]
    ice2_electricity_power_out_cold = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water)[4]
    ice_electricity_power_out_total_cold = ice1_electricity_power_out_cold + ice2_electricity_power_out_cold
    # 内燃机本体耗电功率
    ice1_power_consumption_cold = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water)[5]
    ice2_power_consumption_cold = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water)[5]
    ice_power_consumption_total_cold = ice1_power_consumption_cold + ice2_power_consumption_cold
    # 溴化锂冷冻水、冷却水流量
    lb1_chilled_water_flow = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water)[6]
    lb1_cooling_water_flow = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water, lb1_wp_hot_water)[7]
    lb2_chilled_water_flow = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water)[6]
    lb2_cooling_water_flow = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water, lb2_wp_hot_water)[7]
    # 流量汇总
    lb_chilled_water_flow_total = lb1_chilled_water_flow + lb2_chilled_water_flow
    lb_cooling_water_flow_total = lb1_cooling_water_flow + lb2_cooling_water_flow
    # 计算溴化锂设备辅机耗电功率
    # 目前运行的溴化锂设备数量
    if ice1_load_ratio > 0 and ice2_load_ratio > 0:
        lb_num = 2
    else:
        lb_num = 1
    # 每一个水泵的流量
    lb_chilled_water_flow = lb_chilled_water_flow_total/lb_num
    lb_cooling_water_flow = lb_cooling_water_flow_total/lb_num
    # 溴化锂辅机耗电功率
    lb_auxiliary_equipment_power_consumption_cold_total = lb_num*(lb1_wp_cooling_water.pump_performance_data(lb_cooling_water_flow, 50)[1] + lb1_wp_chilled_water.pump_performance_data(lb_chilled_water_flow, 50)[1])
    ts_electricity_cold_out_now_sum = ice_electricity_power_out_total_cold - ice_power_consumption_total_cold - lb_auxiliary_equipment_power_consumption_cold_total

    # 计算2个三联供系统的成本
    # 天然气消耗量
    ts1_natural_gas_consumption = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water,lb1_wp_hot_water)[2]
    ts2_natural_gas_consumption = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water,lb2_wp_hot_water)[2]
    ts_natural_gas_consumption_sum = ts1_natural_gas_consumption + ts2_natural_gas_consumption
    # 补水量
    ts1_water_supply = triple_supply_in_out_cold(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_cooling_water, lb1_wp_chilled_water,lb1_wp_hot_water)[3]
    ts2_water_supply = triple_supply_in_out_cold(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_cooling_water, lb2_wp_chilled_water,lb2_wp_hot_water)[3]
    ts_water_supply_sum = ts1_water_supply + ts2_water_supply
    # 成本（元）
    ts1_cost = ts1_natural_gas_consumption * gc.natural_gas_price + ts1_water_supply * gc.water_price
    ts2_cost = ts2_natural_gas_consumption * gc.natural_gas_price + ts2_water_supply * gc.water_price
    ts_cost_sum = ts1_cost + ts2_cost

    # 返回计算结果
    return lb_cold_out_now_sum, ts_electricity_cold_out_now_sum, ts_natural_gas_consumption_sum, ts_water_supply_sum, ts_cost_sum


def triple_supply_in_out_cold(load_ratio_ice, hot_water_load, ice, gc, wp_cooling_water, wp_chilled_water, wp_hot_water):
    """三联供系统输出的冷量、电力以及消耗的天然气量、水量计算：内燃机+溴化锂"""
    # 制冷季情况下的计算
    # 内燃机发电功率
    electricity_power_now = internal_combustion_engine_function(load_ratio_ice, ice)[0]
    # 内燃机总热量输入
    total_heat_input = internal_combustion_engine_function(load_ratio_ice, ice)[1]
    # 内燃机余热功率
    residual_heat_power = internal_combustion_engine_function(load_ratio_ice, ice)[2]
    # 实例化一个溴化锂对象，制冷季
    lb_cold = Lithium_Bromide_Cold(residual_heat_power, wp_chilled_water, wp_cooling_water, wp_hot_water, gc)
    # 三联供系统冷负荷输出功率
    triple_supply_cold_load_now = lithium_bromide_cold_function(hot_water_load, load_ratio_ice, lb_cold, gc)[0]
    # 溴化锂冷冻水、冷却水流量
    lb_chilled_water_flow = lithium_bromide_cold_function(hot_water_load, load_ratio_ice, lb_cold, gc)[3]
    lb_cooling_water_flow = lithium_bromide_cold_function(hot_water_load, load_ratio_ice, lb_cold, gc)[4]
    # 如果是单元制系统
    # 三联供系统自耗电功率，供冷时间段
    # 仅内燃机设备辅助设备耗电功率
    internal_combustion_engine_power_consumption_cold = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1]
    # 三联供系统（内燃机+溴化锂）辅助设备耗电功率
    triple_supply_power_consumption_cold = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1] + lithium_bromide_cold_function(hot_water_load, load_ratio_ice, lb_cold, gc)[1]
    # 三联供系统天然气消耗量
    natural_gas_consumption = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[0]
    # 三联供系统外供电功率，供冷时间段
    triple_supply_power_now_cold = electricity_power_now - triple_supply_power_consumption_cold
    #三联供系统补水量计算，溴化锂设备补水量
    total_water_supply = lithium_bromide_cold_function(hot_water_load, load_ratio_ice, lb_cold, gc)[2]

    # 返回计算结果
    return triple_supply_cold_load_now, triple_supply_power_now_cold, natural_gas_consumption, total_water_supply, electricity_power_now, internal_combustion_engine_power_consumption_cold, lb_chilled_water_flow, lb_cooling_water_flow


def triple_supply_heat_function(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_heating_water, lb2_wp_heating_water, lb1_wp_hot_water, lb2_wp_hot_water, gc):
    """三联供系统计算方程，计算在指定的热负荷、电负荷情况下，系统（收入-成本）的最大值情况"""
    # 计算2个溴化锂的制热出力
    lb1_heat_out_now = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[0]
    lb2_heat_out_now = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[0]
    lb_heat_out_now_sum = lb1_heat_out_now + lb2_heat_out_now
    # 计算2个三联供系统向外供电量
    # 内燃机发电功率
    ice1_electricity_power_out_heat = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[4]
    ice2_electricity_power_out_heat = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[4]
    ice_electricity_power_out_total_heat = ice1_electricity_power_out_heat + ice2_electricity_power_out_heat
    # 内燃机本体耗电功率
    ice1_power_consumption_heat = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[5]
    ice2_power_consumption_heat = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[5]
    ice_power_consumption_total_heat = ice1_power_consumption_heat + ice2_power_consumption_heat
    # 溴化锂采暖水流量
    lb1_heating_water_flow = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[6]
    lb2_heating_water_flow = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[6]
    # 流量汇总
    lb_heating_water_flow_total = lb1_heating_water_flow + lb2_heating_water_flow
    # 计算溴化锂设备辅机耗电功率
    # 目前运行的溴化锂设备数量
    if ice1_load_ratio > 0 and ice2_load_ratio > 0:
        lb_num = 2
    else:
        lb_num = 1
    # 每一个水泵的流量
    lb_heating_water_flow = lb_heating_water_flow_total / lb_num
    # 溴化锂辅机耗电功率
    lb_auxiliary_equipment_power_consumption_cold_total = lb_num * (lb1_wp_heating_water.pump_performance_data(lb_heating_water_flow, 50)[1])
    ts_electricity_heat_out_now_sum = ice_electricity_power_out_total_heat - ice_power_consumption_total_heat - lb_auxiliary_equipment_power_consumption_cold_total

    # 计算2个三联供系统的成本
    # 天然气消耗量
    ts1_natural_gas_consumption = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[2]
    ts2_natural_gas_consumption = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[2]
    ts_natural_gas_consumption_sum = ts1_natural_gas_consumption + ts2_natural_gas_consumption
    # 补水量
    ts1_water_supply = triple_supply_in_out_heat(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_heating_water, lb1_wp_hot_water)[3]
    ts2_water_supply = triple_supply_in_out_heat(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_heating_water, lb2_wp_hot_water)[3]
    ts_water_supply_sum = ts1_water_supply + ts2_water_supply
    # 成本（元）
    ts1_cost = ts1_natural_gas_consumption * gc.natural_gas_price + ts1_water_supply * gc.water_price
    ts2_cost = ts2_natural_gas_consumption * gc.natural_gas_price + ts2_water_supply * gc.water_price
    ts_cost_sum = ts1_cost + ts2_cost

    # 返回计算结果
    return lb_heat_out_now_sum, ts_electricity_heat_out_now_sum, ts_natural_gas_consumption_sum, ts_water_supply_sum, ts_cost_sum


def triple_supply_in_out_heat(load_ratio_ice, hot_water_load, ice, gc, wp_heating_water, wp_hot_water):
    """三联供系统输出的热量、电力以及消耗的天然气量、水量计算：内燃机+溴化锂"""
    # 制热季情况下的计算
    # 内燃机发电功率
    electricity_power_now = internal_combustion_engine_function(load_ratio_ice, ice)[0]
    # 内燃机总热量输入
    total_heat_input = internal_combustion_engine_function(load_ratio_ice, ice)[1]
    # 内燃机余热功率
    residual_heat_power = internal_combustion_engine_function(load_ratio_ice, ice)[2]
    # 实例化一个溴化锂对象
    lb_heat = Lithium_Bromide_Heat(residual_heat_power, wp_heating_water, wp_hot_water, gc)
    # 三联供系统热负荷输出功率
    triple_supply_heat_load_now = lithium_bromide_heat_function(hot_water_load, load_ratio_ice, lb_heat, gc)[0]
    # 溴化锂采暖水流量
    lb_heating_water_flow = lithium_bromide_heat_function(hot_water_load, load_ratio_ice, lb_heat, gc)[3]
    # 如果是单元制系统
    # 三联供系统自耗电功率，供热时间段
    triple_supply_power_consumption_heat = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1] + lithium_bromide_heat_function(hot_water_load, load_ratio_ice, lb_heat, gc)[1]
    # 仅内燃机设备辅助设备耗电功率
    internal_combustion_engine_power_consumption_heat = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1]
    # 三联供系统天然气消耗量
    natural_gas_consumption = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[0]
    # 三联供系统外供电功率，供热时间段
    triple_supply_power_now_heat = electricity_power_now - triple_supply_power_consumption_heat
    #三联供系统补水量计算，溴化锂设备补水量
    total_water_supply = lithium_bromide_heat_function(hot_water_load, load_ratio_ice, lb_heat, gc)[2]
    # 返回计算结果
    return triple_supply_heat_load_now, triple_supply_power_now_heat, natural_gas_consumption, total_water_supply, electricity_power_now, internal_combustion_engine_power_consumption_heat, lb_heating_water_flow


def triple_supply_transition_function(ice1_load_ratio, ice2_load_ratio, lb1_hot_water, lb2_hot_water, ice1, ice2, lb1_wp_hot_water, lb2_wp_hot_water, gc):
    """过渡季三联供系统计算方程"""
    # 过渡季仅有生活热水负荷需求，没有冷负荷和热负荷需求，输入需要的生活热水负荷，反算此时的内燃机负荷率
    # 计算2个三联供系统向外供电量
    # 母管制系统发电量仅仅减去内燃机本体耗电量，溴化锂设备制生活热水的耗电量单独计算，不在此处计算
    # 内燃机发电功率
    ice1_electricity_power_out_transition = triple_supply_in_out_transition(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[3]
    ice2_electricity_power_out_transition = triple_supply_in_out_transition(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[3]
    ice_electricity_power_out_total_transition = ice1_electricity_power_out_transition + ice2_electricity_power_out_transition
    # 内燃机本体耗电功率
    ice1_power_consumption_transition = triple_supply_in_out_transition(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[4]
    ice2_power_consumption_transition = triple_supply_in_out_transition(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[4]
    ice_power_consumption_total_transition = ice1_power_consumption_transition + ice2_power_consumption_transition
    # 三联供向外供电量
    ts_electricity_transition_out_now_sum = ice_electricity_power_out_total_transition - ice_power_consumption_total_transition
    # 计算2个三联供系统的成本
    # 天然气消耗量
    ts1_natural_gas_consumption = triple_supply_in_out_transition(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[1]
    ts2_natural_gas_consumption = triple_supply_in_out_transition(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[1]
    ts_natural_gas_consumption_sum = ts1_natural_gas_consumption + ts2_natural_gas_consumption
    # 补水量
    ts1_water_supply = triple_supply_in_out_transition(ice1_load_ratio, lb1_hot_water, ice1, gc, lb1_wp_hot_water)[2]
    ts2_water_supply = triple_supply_in_out_transition(ice2_load_ratio, lb2_hot_water, ice2, gc, lb2_wp_hot_water)[2]
    ts_water_supply_sum = ts1_water_supply + ts2_water_supply
    # 成本（元）
    ts1_cost = ts1_natural_gas_consumption * gc.natural_gas_price + ts1_water_supply * gc.water_price
    ts2_cost = ts2_natural_gas_consumption * gc.natural_gas_price + ts2_water_supply * gc.water_price
    ts_cost_sum = ts1_cost + ts2_cost

    # 返还计算结果
    return ts_electricity_transition_out_now_sum, ts_natural_gas_consumption_sum, ts_water_supply_sum, ts_cost_sum


def triple_supply_in_out_transition(load_ratio_ice, hot_water_load, ice, gc, wp_hot_water):
    """三联供系统输出的热量、电力以及消耗的天然气量、水量计算：内燃机+溴化锂"""
    # 过渡季情况下的计算
    # 内燃机发电功率
    electricity_power_now = internal_combustion_engine_function(load_ratio_ice, ice)[0]
    # 内燃机总热量输入
    total_heat_input = internal_combustion_engine_function(load_ratio_ice, ice)[1]
    # 内燃机余热功率
    residual_heat_power = internal_combustion_engine_function(load_ratio_ice, ice)[2]
    # 实例化一个溴化锂对象
    lb_transition = Lithium_Bromide_Transition(residual_heat_power, wp_hot_water, gc)
    # 如果是单元制系统
    # 三联供系统自耗电功率，过渡季
    triple_supply_power_consumption_transition =internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1] + lithium_bromide_transition_function(hot_water_load, load_ratio_ice, lb_transition, gc)[0]
    # 仅内燃机设备辅助设备耗电功率
    internal_combustion_engine_power_consumption_heat = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[1]
    # 此时内燃机余热没有被用掉的量
    triple_supply_residual_heat_remaining = lithium_bromide_transition_function(hot_water_load, load_ratio_ice, lb_transition, gc)[2]
    # 三联供系统天然气消耗量
    natural_gas_consumption = internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice)[0]
    # 三联供系统外供电功率，过渡季
    triple_supply_power_now_transition = electricity_power_now - triple_supply_power_consumption_transition
    #三联供系统补水量计算，溴化锂设备补水量
    total_water_supply = lithium_bromide_transition_function(hot_water_load, load_ratio_ice, lb_transition, gc)[1]
    # 返回计算结果
    return triple_supply_power_now_transition, natural_gas_consumption, total_water_supply, electricity_power_now, internal_combustion_engine_power_consumption_heat, triple_supply_residual_heat_remaining


def internal_combustion_engine_function(load_ratio_ice, ice):
    """内燃机性能计算"""
    # 内燃机发电功率
    electricity_power_now = load_ratio_ice * ice.electricity_power_rated
    # 内燃机发电效率
    electricity_power_efficiency = ice.electricity_power_efficiency(load_ratio_ice)
    # 内燃机总输入热量
    total_heat_input = ice.total_heat_input(load_ratio_ice, electricity_power_efficiency)
    # 内燃机余热效率
    residual_heat_efficiency = ice.residual_heat_efficiency(load_ratio_ice)
    # 内燃机余热功率
    residual_heat_power = ice.residual_heat_power(total_heat_input, residual_heat_efficiency)
    # 返回计算结果
    return electricity_power_now, total_heat_input, residual_heat_power


def internal_combustion_engine_cost(total_heat_input, load_ratio_ice, ice):
    """内燃机各种消耗量计算：天然气，辅机耗电等"""
    # 内燃机天然气消耗量
    natural_gas_consumption = ice.natural_gas_consumption(total_heat_input)
    # 内燃机辅机耗电功率
    auxiliary_equipment_power_consumption = ice.auxiliary_equipment_power_consumption(load_ratio_ice)
    # 返回计算结果
    return natural_gas_consumption, auxiliary_equipment_power_consumption


def lithium_bromide_cold_function(hot_water_load, load_ratio, lb_cold, gc):
    """溴化锂性能计算函数，制冷季"""
    # 传入的负荷率为内燃机负荷率
    # 传入的余热功率为内燃机余热功率
    # 计算此时溴化锂设备的制冷，制热COP（用于生活热水计算）
    cooling_cop = lb_cold.cooling_cop(load_ratio)
    heating_cop = lb_cold.heating_cop(load_ratio)
    # 溴化锂制备生活热水消耗掉的内燃机余热
    hot_water_residual_heat_consumption = lb_cold.hot_water_residual_heat_consumption(hot_water_load, heating_cop)
    # 计算此时的溴化锂设备制冷
    cool_load_now = lb_cold.cooling_power(cooling_cop, hot_water_residual_heat_consumption)
    # 溴化锂生活热水温差
    hot_water_temperature_difference = lb_cold.hot_water_temperature_difference(load_ratio)
    # 内燃机余热中，用于制冷的比例
    if lb_cold.residual_heat_power == 0:
        residual_heat_cooling_ratio = 1
    else:
        residual_heat_cooling_ratio = 1 - (hot_water_residual_heat_consumption/lb_cold.residual_heat_power)
    # 冷冻水流量
    chilled_water_flow = lb_cold.chilled_water_flow(load_ratio, residual_heat_cooling_ratio)
    # 冷却水流量
    cooling_water_flow = lb_cold.cooling_water_flow(load_ratio, residual_heat_cooling_ratio)
    # 母管制系统，生活热水流量为0，生活热水泵耗电功率在别的程序中单独计算，这里不做计算
    hot_water_flow = 0

    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，要重新计算
    # 制冷辅机耗电
    auxiliary_equipment_power_consumption_cooling = lb_cold.auxiliary_equipment_power_consumption_cooling(cooling_water_flow, chilled_water_flow, residual_heat_cooling_ratio)
    # 生活热水辅机耗电
    auxiliary_equipment_power_consumption_hot_water = lb_cold.auxiliary_equipment_power_consumption_hot_water(hot_water_flow)
    # 制冷季总辅机耗电
    total_power_consumption_cooling = auxiliary_equipment_power_consumption_cooling + auxiliary_equipment_power_consumption_hot_water
    #溴化锂系统补水量计算
    total_water_supply=(chilled_water_flow + hot_water_flow) * gc.closed_loop_supply_rate + cooling_water_flow * gc.cooling_water_supply_rate

    # 返回计算结果
    return cool_load_now, total_power_consumption_cooling, total_water_supply, chilled_water_flow, cooling_water_flow


def lithium_bromide_heat_function(hot_water_load, load_ratio, lb_heat, gc):
    """溴化锂性能计算函数，制热季"""
    # 传入的负荷率为内燃机负荷率
    # 传入的余热功率为内燃机余热功率
    # 计算此时溴化锂设备的制热COP
    heating_cop = lb_heat.heating_cop(load_ratio)
    # 溴化锂制备生活热水消耗掉的内燃机余热
    hot_water_residual_heat_consumption = lb_heat.hot_water_residual_heat_consumption(hot_water_load, heating_cop)
    # 计算此时的溴化锂设备制热出力
    heat_load_now = lb_heat.heating_power(heating_cop, hot_water_residual_heat_consumption)
    # 溴化锂生活热水温差
    hot_water_temperature_difference = lb_heat.hot_water_temperature_difference(load_ratio)
    # 内燃机余热中，用于采暖的比例
    if lb_heat.residual_heat_power == 0:
        residual_heat_heating_ratio = 1
    else:
        residual_heat_heating_ratio = 1 - (hot_water_residual_heat_consumption / lb_heat.residual_heat_power)
    # 采暖水流量
    heating_water_flow = lb_heat.heating_water_flow(load_ratio, residual_heat_heating_ratio)
    # 母管制系统，生活热水流量为0，生活热水泵耗电功率在别的程序中单独计算，这里不做计算
    hot_water_flow = 0

    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 制热辅机耗电
    auxiliary_equipment_power_consumption_heating = lb_heat.auxiliary_equipment_power_consumption_heating(heating_water_flow, residual_heat_heating_ratio)
    # 生活热水辅机耗电
    auxiliary_equipment_power_consumption_hot_water = lb_heat.auxiliary_equipment_power_consumption_hot_water(hot_water_flow)
    # 采暖季总辅机耗电
    total_power_consumption_heating = auxiliary_equipment_power_consumption_heating + auxiliary_equipment_power_consumption_hot_water
    #溴化锂系统补水量计算
    total_water_supply=(heating_water_flow + hot_water_flow) * gc.closed_loop_supply_rate
    # 返回计算结果
    return heat_load_now, total_power_consumption_heating, total_water_supply, heating_water_flow


def lithium_bromide_transition_function(hot_water_load, load_ratio, lb_transition, gc):
    """溴化锂性能计算函数，过渡季"""
    # 已知生活热水负荷需求量，反算此时的设备负荷率（过渡季仅有生活热水负荷）
    # 设备负荷率初始值
    # 计算此时溴化锂设备的制热COP（用于计算生活热水）
    heating_cop = lb_transition.heating_cop(load_ratio)
    # 溴化锂制备生活热水消耗掉的内燃机余热
    hot_water_residual_heat_consumption = lb_transition.hot_water_residual_heat_consumption(hot_water_load, heating_cop)
    # 计算此时溴化锂剩余没用完的余热量
    residual_heat_remaining = lb_transition.residual_heat_remaining(hot_water_residual_heat_consumption)
    # 溴化锂生活热水温差
    hot_water_temperature_difference = lb_transition.hot_water_temperature_difference(load_ratio)
    # 母管制系统，生活热水流量为0，生活热水泵耗电功率在别的程序中单独计算，这里不做计算
    hot_water_flow = 0

    # 以下辅机耗电计算针对的是单元制系统，及泵与设备一对一布置；如果是母管制系统，需要单独重新计算
    # 生活热水辅机耗电
    auxiliary_equipment_power_consumption_hot_water = lb_transition.auxiliary_equipment_power_consumption_hot_water(hot_water_flow)
    # 过渡季总辅机耗电
    total_power_consumption_transition = auxiliary_equipment_power_consumption_hot_water
    #溴化锂系统补水量计算
    total_water_supply=(hot_water_flow) * gc.closed_loop_supply_rate
    # 返回计算结果
    return total_power_consumption_transition, total_water_supply, residual_heat_remaining

def test_triple_supply_in_out_transition():
    load_ratio_ice = 1
    hot_water_load = 850
    # 实例化一个全局常量类
    gc = Global_Constant()
    # 实例化对象
    ice = Internal_Combustion_Engine(792, gc, 0.5)
    wp_hot_water = Water_Pump(44, False, 35, gc)
    ans = triple_supply_in_out_transition(load_ratio_ice, hot_water_load, ice, gc, wp_hot_water)
    print(ans)

# test_triple_supply_in_out_transition()
