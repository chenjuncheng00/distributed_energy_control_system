from syncbase import SyncBase

def read_from_database_ice1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取内燃机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1号内燃发电机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ice1_state')
    if state1:
        ice1_state = record1.value
    else:
        ice1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ice1_fault')
    if state2:
        ice1_fault = record2.value
    else:
        ice1_fault = True
    # 有功功率实际值
    state3, record3 = syncbase.get_reatime_data_by_name('ice1_actual_value_of_active_power')
    if state3:
        ice1_actual_value_of_active_power = record3.value
    else:
        ice1_actual_value_of_active_power = 0
    # 天然气进气流量
    state4, record4 = syncbase.get_reatime_data_by_name('ice1_natural_gas_inlet_flow')
    if state4:
        ice1_natural_gas_inlet_flow = record4.value
    else:
        ice1_natural_gas_inlet_flow = 0
    # 高温缸套水板换二次侧供水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ice1_cylinder_jacket_water_secondary_side_supply_temperature')
    if state5:
        ice1_cylinder_jacket_water_secondary_side_supply_temperature = record5.value
    else:
        ice1_cylinder_jacket_water_secondary_side_supply_temperature = 0
    # 高温缸套水板换二次侧回水温度
    state6, record6 = syncbase.get_reatime_data_by_name('ice1_cylinder_jacket_water_secondary_side_return_temperature')
    if state6:
        ice1_cylinder_jacket_water_secondary_side_return_temperature = record6.value
    else:
        ice1_cylinder_jacket_water_secondary_side_return_temperature = 0
    # 出口烟气温度
    state7, record7 = syncbase.get_reatime_data_by_name('ice1_outlet_flue_gas_temperature')
    if state7:
        ice1_outlet_flue_gas_temperature = record7.value
    else:
        ice1_outlet_flue_gas_temperature = 0
    # 排烟温度
    state8, record8 = syncbase.get_reatime_data_by_name('ice1_exhaust_temperature')
    if state8:
        ice1_exhaust_temperature = record8.value
    else:
        ice1_exhaust_temperature = 0
    # 排烟流量
    state9, record9 = syncbase.get_reatime_data_by_name('ice1_exhaust_flow')
    if state9:
        ice1_exhaust_flow = record9.value
    else:
        ice1_exhaust_flow = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ice1_state, ice1_fault, ice1_actual_value_of_active_power, ice1_natural_gas_inlet_flow, ice1_cylinder_jacket_water_secondary_side_supply_temperature, ice1_cylinder_jacket_water_secondary_side_return_temperature, ice1_outlet_flue_gas_temperature, ice1_exhaust_temperature, ice1_exhaust_flow


def read_from_database_ice2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取内燃机2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2号内燃发电机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ice2_state')
    if state1:
        ice2_state = record1.value
    else:
        ice2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ice2_fault')
    if state2:
        ice2_fault = record2.value
    else:
        ice2_fault = True
    # 有功功率实际值
    state3, record3 = syncbase.get_reatime_data_by_name('ice2_actual_value_of_active_power')
    if state3:
        ice2_actual_value_of_active_power = record3.value
    else:
        ice2_actual_value_of_active_power = 0
    # 天然气进气流量
    state4, record4 = syncbase.get_reatime_data_by_name('ice2_natural_gas_inlet_flow')
    if state4:
        ice2_natural_gas_inlet_flow = record4.value
    else:
        ice2_natural_gas_inlet_flow = 0
    # 高温缸套水板换二次侧供水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ice2_cylinder_jacket_water_secondary_side_supply_temperature')
    if state5:
        ice2_cylinder_jacket_water_secondary_side_supply_temperature = record5.value
    else:
        ice2_cylinder_jacket_water_secondary_side_supply_temperature = 0
    # 高温缸套水板换二次侧回水温度
    state6, record6 = syncbase.get_reatime_data_by_name('ice2_cylinder_jacket_water_secondary_side_return_temperature')
    if state6:
        ice2_cylinder_jacket_water_secondary_side_return_temperature = record6.value
    else:
        ice2_cylinder_jacket_water_secondary_side_return_temperature = 0
    # 出口烟气温度
    state7, record7 = syncbase.get_reatime_data_by_name('ice2_outlet_flue_gas_temperature')
    if state7:
        ice2_outlet_flue_gas_temperature = record7.value
    else:
        ice2_outlet_flue_gas_temperature = 0
    # 排烟温度
    state8, record8 = syncbase.get_reatime_data_by_name('ice2_exhaust_temperature')
    if state8:
        ice2_exhaust_temperature = record8.value
    else:
        ice2_exhaust_temperature = 0
    # 排烟流量
    state9, record9 = syncbase.get_reatime_data_by_name('ice2_exhaust_flow')
    if state9:
        ice2_exhaust_flow = record9.value
    else:
        ice2_exhaust_flow = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ice2_state, ice2_fault, ice2_actual_value_of_active_power, ice2_natural_gas_inlet_flow, ice2_cylinder_jacket_water_secondary_side_supply_temperature, ice2_cylinder_jacket_water_secondary_side_return_temperature, ice2_outlet_flue_gas_temperature, ice2_exhaust_temperature, ice2_exhaust_flow


def read_from_database_lb1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取烟气热水型溴化锂1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    #  1#烟气热水型溴化锂
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('lb1_state')
    if state1:
        lb1_state = record1.value
    else:
        lb1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('lb1_fault')
    if state2:
        lb1_fault = record2.value
    else:
        lb1_fault = True
    # 供水温度(空调冷热水)
    state3, record3 = syncbase.get_reatime_data_by_name('lb1_heat_chilled_water_supply_temperature')
    if state3:
        lb1_heat_chilled_water_supply_temperature = record3.value
    else:
        lb1_heat_chilled_water_supply_temperature = 0
    # 供水流量(空调冷热水)
    state4, record4 = syncbase.get_reatime_data_by_name('lb1_heat_chilled_water_supply_flow')
    if state4:
        lb1_heat_chilled_water_supply_flow = record4.value
    else:
        lb1_heat_chilled_water_supply_flow = 0
    # 回水温度(空调冷热水)
    state5, record5 = syncbase.get_reatime_data_by_name('lb1_heat_chilled_water_return_temperature')
    if state5:
        lb1_heat_chilled_water_return_temperature = record5.value
    else:
        lb1_heat_chilled_water_return_temperature = 0
    # 生活热水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('lb1_hot_water_supply_temperature')
    if state6:
        lb1_hot_water_supply_temperature = record6.value
    else:
        lb1_hot_water_supply_temperature = 0
    # 生活热水供水流量
    state7, record7 = syncbase.get_reatime_data_by_name('lb1_hot_water_supply_flow')
    if state7:
        lb1_hot_water_supply_flow = record7.value
    else:
        lb1_hot_water_supply_flow = 0
    # 生活热水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('lb1_hot_water_return_temperature')
    if state8:
        lb1_hot_water_return_temperature = record8.value
    else:
        lb1_hot_water_return_temperature = 0
    # 冷却水供热温度
    state9, record9 = syncbase.get_reatime_data_by_name('lb1_cooling_water_supply_temperature')
    if state9:
        lb1_cooling_water_supply_temperature = record9.value
    else:
        lb1_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state10, record10 = syncbase.get_reatime_data_by_name('lb1_cooling_water_supply_flow')
    if state10:
        lb1_cooling_water_supply_flow = record10.value
    else:
        lb1_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state11, record11 = syncbase.get_reatime_data_by_name('lb1_cooling_water_return_temperature')
    if state11:
        lb1_cooling_water_return_temperature = record11.value
    else:
        lb1_cooling_water_return_temperature = 0
    # 出口烟气温度
    state12, record12 = syncbase.get_reatime_data_by_name('lb1_outlet_flue_gas_temperature')
    if state12:
        lb1_outlet_flue_gas_temperature = record12.value
    else:
        lb1_outlet_flue_gas_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return lb1_state, lb1_fault, lb1_heat_chilled_water_supply_temperature, lb1_heat_chilled_water_supply_flow, lb1_heat_chilled_water_return_temperature, lb1_hot_water_supply_temperature, lb1_hot_water_supply_flow, lb1_hot_water_return_temperature, lb1_cooling_water_supply_temperature, lb1_cooling_water_supply_flow, lb1_cooling_water_return_temperature, lb1_outlet_flue_gas_temperature


def read_from_database_lb2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取烟气热水型溴化锂2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#烟气热水型溴化锂
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('lb2_state')
    if state1:
        lb2_state = record1.value
    else:
        lb2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('lb2_fault')
    if state2:
        lb2_fault = record2.value
    else:
        lb2_fault = True
    # 供水温度(空调冷热水)
    state3, record3 = syncbase.get_reatime_data_by_name('lb2_heat_chilled_water_supply_temperature')
    if state3:
        lb2_heat_chilled_water_supply_temperature = record3.value
    else:
        lb2_heat_chilled_water_supply_temperature = 0
    # 供水流量(空调冷热水)
    state4, record4 = syncbase.get_reatime_data_by_name('lb2_heat_chilled_water_supply_flow')
    if state4:
        lb2_heat_chilled_water_supply_flow = record4.value
    else:
        lb2_heat_chilled_water_supply_flow = 0
    # 回水温度(空调冷热水)
    state5, record5 = syncbase.get_reatime_data_by_name('lb2_heat_chilled_water_return_temperature')
    if state5:
        lb2_heat_chilled_water_return_temperature = record5.value
    else:
        lb2_heat_chilled_water_return_temperature = 0
    # 生活热水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('lb2_hot_water_supply_temperature')
    if state6:
        lb2_hot_water_supply_temperature = record6.value
    else:
        lb2_hot_water_supply_temperature = 0
    # 生活热水供水流量
    state7, record7 = syncbase.get_reatime_data_by_name('lb2_hot_water_supply_flow')
    if state7:
        lb2_hot_water_supply_flow = record7.value
    else:
        lb2_hot_water_supply_flow = 0
    # 生活热水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('lb2_hot_water_return_temperature')
    if state8:
        lb2_hot_water_return_temperature = record8.value
    else:
        lb2_hot_water_return_temperature = 0
    # 冷却水供热温度
    state9, record9 = syncbase.get_reatime_data_by_name('lb2_cooling_water_supply_temperature')
    if state9:
        lb2_cooling_water_supply_temperature = record9.value
    else:
        lb2_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state10, record10 = syncbase.get_reatime_data_by_name('lb2_cooling_water_supply_flow')
    if state10:
        lb2_cooling_water_supply_flow = record10.value
    else:
        lb2_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state11, record11 = syncbase.get_reatime_data_by_name('lb2_cooling_water_return_temperature')
    if state11:
        lb2_cooling_water_return_temperature = record11.value
    else:
        lb2_cooling_water_return_temperature = 0
    # 出口烟气温度
    state12, record12 = syncbase.get_reatime_data_by_name('lb2_outlet_flue_gas_temperature')
    if state12:
        lb2_outlet_flue_gas_temperature = record12.value
    else:
        lb2_outlet_flue_gas_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return lb2_state, lb2_fault, lb2_heat_chilled_water_supply_temperature, lb2_heat_chilled_water_supply_flow, lb2_heat_chilled_water_return_temperature, lb2_hot_water_supply_temperature, lb2_hot_water_supply_flow, lb2_hot_water_return_temperature, lb2_cooling_water_supply_temperature, lb2_cooling_water_supply_flow, lb2_cooling_water_return_temperature, lb2_outlet_flue_gas_temperature


def read_from_database_lb_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取烟气热水型溴化锂公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 烟气热水型溴化锂公用测点
    # 溴化锂机组冷热媒水供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('lb_heat_chilled_water_supply_temperature')
    if state1:
        lb_heat_chilled_water_supply_temperature = record1.value
    else:
        lb_heat_chilled_water_supply_temperature = 0
    # 溴化锂机组冷热媒水供水母管流量（新增测点）
    state2, record2 = syncbase.get_reatime_data_by_name('lb_heat_chilled_water_supply_flow')
    if state2:
        lb_heat_chilled_water_supply_flow = record2.value
    else:
        lb_heat_chilled_water_supply_flow = 0
    # 溴化锂机组冷热媒水回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('lb_heat_chilled_water_return_temperature')
    if state3:
        lb_heat_chilled_water_return_temperature = record3.value
    else:
        lb_heat_chilled_water_return_temperature = 0
    # 溴化锂机组冷却水供水母管温度（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('lb_cooling_water_supply_temperature')
    if state4:
        lb_cooling_water_supply_temperature = record4.value
    else:
        lb_cooling_water_supply_temperature = 0
    # 溴化锂机组冷却水供水母管流量（新增测点）
    state5, record5 = syncbase.get_reatime_data_by_name('lb_cooling_water_supply_flow')
    if state5:
        lb_cooling_water_supply_flow = record5.value
    else:
        lb_cooling_water_supply_flow = 0
    # 溴化锂机组冷却水回水母管温度（新增测点）
    state6, record6 = syncbase.get_reatime_data_by_name('lb_cooling_water_return_temperature')
    if state6:
        lb_cooling_water_return_temperature = record6.value
    else:
        lb_cooling_water_return_temperature = 0
    # 溴化锂空调水（冷/热）能量
    state7, record7 = syncbase.get_reatime_data_by_name('lb_chilled_heat_water_energy')
    if state7:
        lb_chilled_heat_water_energy = record7.value
    else:
        lb_chilled_heat_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return lb_heat_chilled_water_supply_temperature, lb_heat_chilled_water_supply_flow, lb_heat_chilled_water_return_temperature, lb_cooling_water_supply_temperature, lb_cooling_water_supply_flow, lb_cooling_water_return_temperature, lb_chilled_heat_water_energy


def read_from_database_cc1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式冷水机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1#离心式冷水机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('cc1_state')
    if state1:
        cc1_state = record1.value
    else:
        cc1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('cc1_fault')
    if state2:
        cc1_fault = record2.value
    else:
        cc1_fault = True
    # 冷冻水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('cc1_chilled_water_supply_temperature')
    if state3:
        cc1_chilled_water_supply_temperature = record3.value
    else:
        cc1_chilled_water_supply_temperature = 0
    # 冷冻水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('cc1_chilled_water_supply_flow')
    if state4:
        cc1_chilled_water_supply_flow = record4.value
    else:
        cc1_chilled_water_supply_flow = 0
    # 冷冻水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('cc1_chilled_water_return_temperature')
    if state5:
        cc1_chilled_water_return_temperature = record5.value
    else:
        cc1_chilled_water_return_temperature = 0
    # 冷却水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('cc1_cooling_water_supply_temperature')
    if state6:
        cc1_cooling_water_supply_temperature = record6.value
    else:
        cc1_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('cc1_cooling_water_supply_flow')
    if state7:
        cc1_cooling_water_supply_flow = record7.value
    else:
        cc1_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('cc1_cooling_water_return_temperature')
    if state8:
        cc1_cooling_water_return_temperature = record8.value
    else:
        cc1_cooling_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return cc1_state, cc1_fault, cc1_chilled_water_supply_temperature,cc1_chilled_water_supply_flow, cc1_chilled_water_return_temperature, cc1_cooling_water_supply_temperature,cc1_cooling_water_supply_flow, cc1_cooling_water_return_temperature


def read_from_database_cc2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式冷水机2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#离心式冷水机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('cc2_state')
    if state1:
        cc2_state = record1.value
    else:
        cc2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('cc2_fault')
    if state2:
        cc2_fault = record2.value
    else:
        cc2_fault = True
    # 冷冻水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('cc2_chilled_water_supply_temperature')
    if state3:
        cc2_chilled_water_supply_temperature = record3.value
    else:
        cc2_chilled_water_supply_temperature = 0
    # 冷冻水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('cc2_chilled_water_supply_flow')
    if state4:
        cc2_chilled_water_supply_flow = record4.value
    else:
        cc2_chilled_water_supply_flow = 0
    # 冷冻水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('cc2_chilled_water_return_temperature')
    if state5:
        cc2_chilled_water_return_temperature = record5.value
    else:
        cc2_chilled_water_return_temperature = 0
    # 冷却水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('cc2_cooling_water_supply_temperature')
    if state6:
        cc2_cooling_water_supply_temperature = record6.value
    else:
        cc2_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('cc2_cooling_water_supply_flow')
    if state7:
        cc2_cooling_water_supply_flow = record7.value
    else:
        cc2_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('cc2_cooling_water_return_temperature')
    if state8:
        cc2_cooling_water_return_temperature = record8.value
    else:
        cc2_cooling_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return cc2_state, cc2_fault, cc2_chilled_water_supply_temperature, cc2_chilled_water_supply_flow, cc2_chilled_water_return_temperature, cc2_cooling_water_supply_temperature, cc2_cooling_water_supply_flow, cc2_cooling_water_return_temperature


def read_from_database_cc3():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式冷水机3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 3#离心式冷水机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('cc3_state')
    if state1:
        cc3_state = record1.value
    else:
        cc3_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('cc3_fault')
    if state2:
        cc3_fault = record2.value
    else:
        cc3_fault = True
    # 冷冻水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('cc3_chilled_water_supply_temperature')
    if state3:
        cc3_chilled_water_supply_temperature = record3.value
    else:
        cc3_chilled_water_supply_temperature = 0
    # 冷冻水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('cc3_chilled_water_supply_flow')
    if state4:
        cc3_chilled_water_supply_flow = record4.value
    else:
        cc3_chilled_water_supply_flow = 0
    # 冷冻水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('cc3_chilled_water_return_temperature')
    if state5:
        cc3_chilled_water_return_temperature = record5.value
    else:
        cc3_chilled_water_return_temperature = 0
    # 冷却水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('cc3_cooling_water_supply_temperature')
    if state6:
        cc3_cooling_water_supply_temperature = record6.value
    else:
        cc3_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('cc3_cooling_water_supply_flow')
    if state7:
        cc3_cooling_water_supply_flow = record7.value
    else:
        cc3_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('cc3_cooling_water_return_temperature')
    if state8:
        cc3_cooling_water_return_temperature = record8.value
    else:
        cc3_cooling_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return cc3_state, cc3_fault, cc3_chilled_water_supply_temperature,cc3_chilled_water_supply_flow, cc3_chilled_water_return_temperature, cc3_cooling_water_supply_temperature,cc3_cooling_water_supply_flow, cc3_cooling_water_return_temperature


def read_from_database_cc4():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式冷水机4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 4#离心式冷水机
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('cc4_state')
    if state1:
        cc4_state = record1.value
    else:
        cc4_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('cc4_fault')
    if state2:
        cc4_fault = record2.value
    else:
        cc4_fault = True
    # 冷冻水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('cc4_chilled_water_supply_temperature')
    if state3:
        cc4_chilled_water_supply_temperature = record3.value
    else:
        cc4_chilled_water_supply_temperature = 0
    # 冷冻水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('cc4_chilled_water_supply_flow')
    if state4:
        cc4_chilled_water_supply_flow = record4.value
    else:
        cc4_chilled_water_supply_flow = 0
    # 冷冻水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('cc4_chilled_water_return_temperature')
    if state5:
        cc4_chilled_water_return_temperature = record5.value
    else:
        cc4_chilled_water_return_temperature = 0
    # 冷却水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('cc4_cooling_water_supply_temperature')
    if state6:
        cc4_cooling_water_supply_temperature = record6.value
    else:
        cc4_cooling_water_supply_temperature = 0
    # 冷却水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('cc4_cooling_water_supply_flow')
    if state7:
        cc4_cooling_water_supply_flow = record7.value
    else:
        cc4_cooling_water_supply_flow = 0
    # 冷却水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('cc4_cooling_water_return_temperature')
    if state8:
        cc4_cooling_water_return_temperature = record8.value
    else:
        cc4_cooling_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return cc4_state, cc4_fault, cc4_chilled_water_supply_temperature,cc4_chilled_water_supply_flow, cc4_chilled_water_return_temperature, cc4_cooling_water_supply_temperature,cc4_cooling_water_supply_flow, cc4_cooling_water_return_temperature


def read_from_database_cc_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式冷水机公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 离心式冷水机公用
    # 离心式冷水机冷冻水供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('cc_chilled_water_supply_temperature')
    if state1:
        cc_chilled_water_supply_temperature = record1.value
    else:
        cc_chilled_water_supply_temperature = 0
    # 离心式冷水机冷冻水供水母管流量(新增测点)
    state2, record2 = syncbase.get_reatime_data_by_name('cc_chilled_water_supply_flow')
    if state2:
        cc_chilled_water_supply_flow = record2.value
    else:
        cc_chilled_water_supply_flow = 0
    # 离心式冷水机冷冻水回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('cc_chilled_water_return_temperature')
    if state3:
        cc_chilled_water_return_temperature = record3.value
    else:
        cc_chilled_water_return_temperature = 0
    # 离心式冷水机冷却水供水母管温度(新增测点)
    state4, record4 = syncbase.get_reatime_data_by_name('cc_cooling_water_supply_temperature')
    if state4:
        cc_cooling_water_supply_temperature = record4.value
    else:
        cc_cooling_water_supply_temperature = 0
    # 离心式冷水机冷却水供水母管流量(新增测点)
    state5, record5 = syncbase.get_reatime_data_by_name('cc_cooling_water_supply_flow')
    if state5:
        cc_cooling_water_supply_flow = record5.value
    else:
        cc_cooling_water_supply_flow = 0
    # 离心式冷水机冷却水回水母管温度(新增测点)
    state6, record6 = syncbase.get_reatime_data_by_name('cc_cooling_water_return_temperature')
    if state6:
        cc_cooling_water_return_temperature = record6.value
    else:
        cc_cooling_water_return_temperature = 0
    # 离心式冷水机空调冷水能量
    state7, record7 = syncbase.get_reatime_data_by_name('cc_chilled_water_energy')
    if state7:
        cc_chilled_water_energy = record7.value
    else:
        cc_chilled_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return cc_chilled_water_supply_temperature, cc_chilled_water_supply_flow, cc_chilled_water_return_temperature, cc_cooling_water_supply_temperature, cc_cooling_water_supply_flow, cc_cooling_water_return_temperature, cc_chilled_water_energy


def read_from_database_chp1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式热泵1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1#离心式热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('chp1_state')
    if state1:
        chp1_state = record1.value
    else:
        chp1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('chp1_fault')
    if state2:
        chp1_fault = record2.value
    else:
        chp1_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('chp1_heat_water_supply_temperature')
    if state3:
        chp1_heat_water_supply_temperature = record3.value
    else:
        chp1_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('chp1_heat_water_supply_flow')
    if state4:
        chp1_heat_water_supply_flow = record4.value
    else:
        chp1_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('chp1_heat_water_return_temperature')
    if state5:
        chp1_heat_water_return_temperature = record5.value
    else:
        chp1_heat_water_return_temperature = 0
    # 低温热源水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('chp1_source_water_supply_temperature')
    if state6:
        chp1_source_water_supply_temperature = record6.value
    else:
        chp1_source_water_supply_temperature = 0
    # 低温热源水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('chp1_source_water_supply_flow')
    if state7:
        chp1_source_water_supply_flow = record7.value
    else:
        chp1_source_water_supply_flow = 0
    # 低温热源水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('chp1_source_water_return_temperature')
    if state8:
        chp1_source_water_return_temperature = record8.value
    else:
        chp1_source_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return chp1_state, chp1_fault, chp1_heat_water_supply_temperature,chp1_heat_water_supply_flow, chp1_heat_water_return_temperature, chp1_source_water_supply_temperature,chp1_source_water_supply_flow, chp1_source_water_return_temperature


def read_from_database_chp2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式热泵2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#离心式热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('chp2_state')
    if state1:
        chp2_state = record1.value
    else:
        chp2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('chp2_fault')
    if state2:
        chp2_fault = record2.value
    else:
        chp2_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('chp2_heat_water_supply_temperature')
    if state3:
        chp2_heat_water_supply_temperature = record3.value
    else:
        chp2_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('chp2_heat_water_supply_flow')
    if state4:
        chp2_heat_water_supply_flow = record4.value
    else:
        chp2_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('chp2_heat_water_return_temperature')
    if state5:
        chp2_heat_water_return_temperature = record5.value
    else:
        chp2_heat_water_return_temperature = 0
    # 低温热源水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('chp2_source_water_supply_temperature')
    if state6:
        chp2_source_water_supply_temperature = record6.value
    else:
        chp2_source_water_supply_temperature = 0
    # 低温热源水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('chp2_source_water_supply_flow')
    if state7:
        chp2_source_water_supply_flow = record7.value
    else:
        chp2_source_water_supply_flow = 0
    # 低温热源水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('chp2_source_water_return_temperature')
    if state8:
        chp2_source_water_return_temperature = record8.value
    else:
        chp2_source_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return chp2_state, chp2_fault, chp2_heat_water_supply_temperature,chp2_heat_water_supply_flow, chp2_heat_water_return_temperature, chp2_source_water_supply_temperature,chp2_source_water_supply_flow, chp2_source_water_return_temperature


def read_from_database_chp3():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式热泵3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 3#离心式热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('chp3_state')
    if state1:
        chp3_state = record1.value
    else:
        chp3_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('chp3_fault')
    if state2:
        chp3_fault = record2.value
    else:
        chp3_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('chp3_heat_water_supply_temperature')
    if state3:
        chp3_heat_water_supply_temperature = record3.value
    else:
        chp3_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('chp3_heat_water_supply_flow')
    if state4:
        chp3_heat_water_supply_flow = record4.value
    else:
        chp3_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('chp3_heat_water_return_temperature')
    if state5:
        chp3_heat_water_return_temperature = record5.value
    else:
        chp3_heat_water_return_temperature = 0
    # 低温热源水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('chp3_source_water_supply_temperature')
    if state6:
        chp3_source_water_supply_temperature = record6.value
    else:
        chp3_source_water_supply_temperature = 0
    # 低温热源水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('chp3_source_water_supply_flow')
    if state7:
        chp3_source_water_supply_flow = record7.value
    else:
        chp3_source_water_supply_flow = 0
    # 低温热源水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('chp3_source_water_return_temperature')
    if state8:
        chp3_source_water_return_temperature = record8.value
    else:
        chp3_source_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return chp3_state, chp3_fault, chp3_heat_water_supply_temperature,chp3_heat_water_supply_flow, chp3_heat_water_return_temperature, chp3_source_water_supply_temperature,chp3_source_water_supply_flow, chp3_source_water_return_temperature


def read_from_database_chp4():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式热泵4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 4#离心式热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('chp4_state')
    if state1:
        chp4_state = record1.value
    else:
        chp4_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('chp4_fault')
    if state2:
        chp4_fault = record2.value
    else:
        chp4_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('chp4_heat_water_supply_temperature')
    if state3:
        chp4_heat_water_supply_temperature = record3.value
    else:
        chp4_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('chp4_heat_water_supply_flow')
    if state4:
        chp4_heat_water_supply_flow = record4.value
    else:
        chp4_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('chp4_heat_water_return_temperature')
    if state5:
        chp4_heat_water_return_temperature = record5.value
    else:
        chp4_heat_water_return_temperature = 0
    # 低温热源水供水温度
    state6, record6 = syncbase.get_reatime_data_by_name('chp4_source_water_supply_temperature')
    if state6:
        chp4_source_water_supply_temperature = record6.value
    else:
        chp4_source_water_supply_temperature = 0
    # 低温热源水供水流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('chp4_source_water_supply_flow')
    if state7:
        chp4_source_water_supply_flow = record7.value
    else:
        chp4_source_water_supply_flow = 0
    # 低温热源水回水温度
    state8, record8 = syncbase.get_reatime_data_by_name('chp4_source_water_return_temperature')
    if state8:
        chp4_source_water_return_temperature = record8.value
    else:
        chp4_source_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return chp4_state, chp4_fault, chp4_heat_water_supply_temperature,chp4_heat_water_supply_flow, chp4_heat_water_return_temperature, chp4_source_water_supply_temperature,chp4_source_water_supply_flow, chp4_source_water_return_temperature


def read_from_database_chp_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取离心式热泵公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 离心式热泵公用
    # 离心式热泵采暖水供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('chp_heat_water_supply_temperature')
    if state1:
        chp_heat_water_supply_temperature = record1.value
    else:
        chp_heat_water_supply_temperature = 0
    # 离心式热泵采暖水供水母管流量(新增测点)
    state2, record2 = syncbase.get_reatime_data_by_name('chp_heat_water_supply_flow')
    if state2:
        chp_heat_water_supply_flow = record2.value
    else:
        chp_heat_water_supply_flow = 0
    # 离心式热泵采暖水回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('chp_heat_water_return_temperature')
    if state3:
        chp_heat_water_return_temperature = record3.value
    else:
        chp_heat_water_return_temperature = 0
    # 离心式热泵热源水供水母管温度(新增测点)
    state4, record4 = syncbase.get_reatime_data_by_name('chp_source_water_supply_temperature')
    if state4:
        chp_source_water_supply_temperature = record4.value
    else:
        chp_source_water_supply_temperature = 0
    # 离心式热泵热源水供水母管流量(新增测点)
    state5, record5 = syncbase.get_reatime_data_by_name('chp_source_water_supply_flow')
    if state5:
        chp_source_water_supply_flow = record5.value
    else:
        chp_source_water_supply_flow = 0
    # 离心式热泵热源水回水母管温度(新增测点)
    state6, record6 = syncbase.get_reatime_data_by_name('chp_source_water_return_temperature')
    if state6:
        chp_source_water_return_temperature = record6.value
    else:
        chp_source_water_return_temperature = 0
    # 离心式热泵空调热水能量
    state7, record7 = syncbase.get_reatime_data_by_name('chp_heat_water_energy')
    if state7:
        chp_heat_water_energy = record7.value
    else:
        chp_heat_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return chp_heat_water_supply_temperature, chp_heat_water_supply_flow, chp_heat_water_return_temperature, chp_source_water_supply_temperature, chp_source_water_supply_flow, chp_source_water_return_temperature, chp_heat_water_energy


def read_from_database_ashp1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取空气源热泵1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1#空气源热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ashp1_state')
    if state1:
        ashp1_state = record1.value
    else:
        ashp1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ashp1_fault')
    if state2:
        ashp1_fault = record2.value
    else:
        ashp1_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ashp1_water_supply_temperature')
    if state3:
        ashp1_water_supply_temperature = record3.value
    else:
        ashp1_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ashp1_water_supply_flow')
    if state4:
        ashp1_water_supply_flow = record4.value
    else:
        ashp1_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ashp1_water_return_temperature')
    if state5:
        ashp1_water_return_temperature = record5.value
    else:
        ashp1_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ashp1_state, ashp1_fault, ashp1_water_supply_temperature, ashp1_water_supply_flow, ashp1_water_return_temperature


def read_from_database_ashp2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取空气源热泵2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#空气源热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ashp2_state')
    if state1:
        ashp2_state = record1.value
    else:
        ashp2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ashp2_fault')
    if state2:
        ashp2_fault = record2.value
    else:
        ashp2_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ashp2_water_supply_temperature')
    if state3:
        ashp2_water_supply_temperature = record3.value
    else:
        ashp2_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ashp2_water_supply_flow')
    if state4:
        ashp2_water_supply_flow = record4.value
    else:
        ashp2_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ashp2_water_return_temperature')
    if state5:
        ashp2_water_return_temperature = record5.value
    else:
        ashp2_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ashp2_state, ashp2_fault, ashp2_water_supply_temperature, ashp2_water_supply_flow, ashp2_water_return_temperature


def read_from_database_ashp3():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取空气源热泵3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 3#空气源热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ashp3_state')
    if state1:
        ashp3_state = record1.value
    else:
        ashp3_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ashp3_fault')
    if state2:
        ashp3_fault = record2.value
    else:
        ashp3_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ashp3_water_supply_temperature')
    if state3:
        ashp3_water_supply_temperature = record3.value
    else:
        ashp3_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ashp3_water_supply_flow')
    if state4:
        ashp3_water_supply_flow = record4.value
    else:
        ashp3_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ashp3_water_return_temperature')
    if state5:
        ashp3_water_return_temperature = record5.value
    else:
        ashp3_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ashp3_state, ashp3_fault, ashp3_water_supply_temperature, ashp3_water_supply_flow, ashp3_water_return_temperature


def read_from_database_ashp4():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取空气源热泵4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 4#空气源热泵
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ashp4_state')
    if state1:
        ashp4_state = record1.value
    else:
        ashp4_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ashp4_fault')
    if state2:
        ashp4_fault = record2.value
    else:
        ashp4_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ashp4_water_supply_temperature')
    if state3:
        ashp4_water_supply_temperature = record3.value
    else:
        ashp4_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ashp4_water_supply_flow')
    if state4:
        ashp4_water_supply_flow = record4.value
    else:
        ashp4_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ashp4_water_return_temperature')
    if state5:
        ashp4_water_return_temperature = record5.value
    else:
        ashp4_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ashp4_state, ashp4_fault, ashp4_water_supply_temperature, ashp4_water_supply_flow, ashp4_water_return_temperature


def read_from_database_ashp_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取空气源热泵公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 空气源热泵公用
    # 空气源热泵冷热水供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('ashp_water_supply_temperature')
    if state1:
        ashp_water_supply_temperature = record1.value
    else:
        ashp_water_supply_temperature = 0
    # 空气源热泵冷热水供水母管流量(新增测点)
    state2, record2 = syncbase.get_reatime_data_by_name('ashp_water_supply_flow')
    if state2:
        ashp_water_supply_flow = record2.value
    else:
        ashp_water_supply_flow = 0
    # 空气源热泵冷热水回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('ashp_water_return_temperature')
    if state3:
        ashp_water_return_temperature = record3.value
    else:
        ashp_water_return_temperature = 0
    # 空气源热泵空调冷热水能量
    state7, record7 = syncbase.get_reatime_data_by_name('ashp_water_energy')
    if state7:
        ashp_water_energy = record7.value
    else:
        ashp_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ashp_water_supply_temperature, ashp_water_supply_flow, ashp_water_return_temperature, ashp_water_energy


def read_from_database_ese1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取蓄冷蓄热装置1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1#蓄冷蓄热装置
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ese1_state')
    if state1:
        ese1_state = record1.value
    else:
        ese1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ese1_fault')
    if state2:
        ese1_fault = record2.value
    else:
        ese1_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ese1_water_supply_temperature')
    if state3:
        ese1_water_supply_temperature = record3.value
    else:
        ese1_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ese1_water_supply_flow')
    if state4:
        ese1_water_supply_flow = record4.value
    else:
        ese1_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ese1_water_return_temperature')
    if state5:
        ese1_water_return_temperature = record5.value
    else:
        ese1_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ese1_state, ese1_fault, ese1_water_supply_temperature, ese1_water_supply_flow, ese1_water_return_temperature


def read_from_database_ese2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取蓄冷蓄热装置2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#蓄冷蓄热装置
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ese2_state')
    if state1:
        ese2_state = record1.value
    else:
        ese2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ese2_fault')
    if state2:
        ese2_fault = record2.value
    else:
        ese2_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ese2_water_supply_temperature')
    if state3:
        ese2_water_supply_temperature = record3.value
    else:
        ese2_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ese2_water_supply_flow')
    if state4:
        ese2_water_supply_flow = record4.value
    else:
        ese2_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ese2_water_return_temperature')
    if state5:
        ese2_water_return_temperature = record5.value
    else:
        ese2_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ese2_state, ese2_fault, ese2_water_supply_temperature, ese2_water_supply_flow, ese2_water_return_temperature


def read_from_database_ese3():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取蓄冷蓄热装置3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 3#蓄冷蓄热装置
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ese3_state')
    if state1:
        ese3_state = record1.value
    else:
        ese3_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ese3_fault')
    if state2:
        ese3_fault = record2.value
    else:
        ese3_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ese3_water_supply_temperature')
    if state3:
        ese3_water_supply_temperature = record3.value
    else:
        ese3_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ese3_water_supply_flow')
    if state4:
        ese3_water_supply_flow = record4.value
    else:
        ese3_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ese3_water_return_temperature')
    if state5:
        ese3_water_return_temperature = record5.value
    else:
        ese3_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ese3_state, ese3_fault, ese3_water_supply_temperature, ese3_water_supply_flow, ese3_water_return_temperature


def read_from_database_ese4():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取蓄冷蓄热装置4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 4#蓄冷蓄热装置
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ese4_state')
    if state1:
        ese4_state = record1.value
    else:
        ese4_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ese4_fault')
    if state2:
        ese4_fault = record2.value
    else:
        ese4_fault = True
    # 冷热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ese4_water_supply_temperature')
    if state3:
        ese4_water_supply_temperature = record3.value
    else:
        ese4_water_supply_temperature = 0
    # 冷热水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ese4_water_supply_flow')
    if state4:
        ese4_water_supply_flow = record4.value
    else:
        ese4_water_supply_flow = 0
    # 冷热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ese4_water_return_temperature')
    if state5:
        ese4_water_return_temperature = record5.value
    else:
        ese4_water_return_temperature = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ese4_state, ese4_fault, ese4_water_supply_temperature, ese4_water_supply_flow, ese4_water_return_temperature


def read_from_database_ese_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取蓄冷蓄热装置公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 蓄冷蓄热装置公用
    # 蓄能水罐本体运行状态反馈
    state4, record4 = syncbase.get_reatime_data_by_name('ese_state')
    if state4:
        ese_state = record4.value
    else:
        ese_state = 0
    # 蓄能水罐本体故障信号反馈
    state5, record5 = syncbase.get_reatime_data_by_name('ese_fault')
    if state5:
        ese_fault = record5.value
    else:
        ese_fault = 0
    # 蓄冷蓄热装置冷热水供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('ese_water_supply_temperature')
    if state1:
        ese_water_supply_temperature = record1.value
    else:
        ese_water_supply_temperature = 0
    # 蓄冷蓄热装置冷热水供水母管流量(新增测点)
    state2, record2 = syncbase.get_reatime_data_by_name('ese_water_supply_flow')
    if state2:
        ese_water_supply_flow = record2.value
    else:
        ese_water_supply_flow = 0
    # 蓄冷蓄热装置冷热水回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('ese_water_return_temperature')
    if state3:
        ese_water_return_temperature = record3.value
    else:
        ese_water_return_temperature = 0
    # 蓄冷蓄热装置空调冷热水能量
    state7, record7 = syncbase.get_reatime_data_by_name('ese_water_energy')
    if state7:
        ese_water_energy = record7.value
    else:
        ese_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ese_state, ese_fault, ese_water_supply_temperature, ese_water_supply_flow, ese_water_return_temperature, ese_water_energy


def read_from_database_ngb1():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取天然气热水锅炉1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1#天然气热水锅炉
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ngb1_state')
    if state1:
        ngb1_state = record1.value
    else:
        ngb1_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ngb1_fault')
    if state2:
        ngb1_fault = record2.value
    else:
        ngb1_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ngb1_heat_water_supply_temperature')
    if state3:
        ngb1_heat_water_supply_temperature = record3.value
    else:
        ngb1_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ngb1_heat_water_supply_flow')
    if state4:
        ngb1_heat_water_supply_flow = record4.value
    else:
        ngb1_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ngb1_heat_water_return_temperature')
    if state5:
        ngb1_heat_water_return_temperature = record5.value
    else:
        ngb1_heat_water_return_temperature = 0
    # 出口烟气温度
    state6, record6 = syncbase.get_reatime_data_by_name('ngb1_outlet_flue_gas_temperature')
    if state6:
        ngb1_outlet_flue_gas_temperature = record6.value
    else:
        ngb1_outlet_flue_gas_temperature = 0
    # 出口烟气流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('ngb1_outlet_flue_gas_flow')
    if state7:
        ngb1_outlet_flue_gas_flow = record7.value
    else:
        ngb1_outlet_flue_gas_flow = 0
    # 天然气进气流量
    state8, record8 = syncbase.get_reatime_data_by_name('ngb1_natural_gas_inlet_flow')
    if state8:
        ngb1_natural_gas_inlet_flow = record8.value
    else:
        ngb1_natural_gas_inlet_flow = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ngb1_state, ngb1_fault, ngb1_heat_water_supply_temperature, ngb1_heat_water_supply_flow, ngb1_heat_water_return_temperature, ngb1_outlet_flue_gas_temperature, ngb1_outlet_flue_gas_flow, ngb1_natural_gas_inlet_flow


def read_from_database_ngb2():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取天然气热水锅炉2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 2#天然气热水锅炉
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ngb2_state')
    if state1:
        ngb2_state = record1.value
    else:
        ngb2_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ngb2_fault')
    if state2:
        ngb2_fault = record2.value
    else:
        ngb2_fault = True
    # 采暖水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ngb2_heat_water_supply_temperature')
    if state3:
        ngb2_heat_water_supply_temperature = record3.value
    else:
        ngb2_heat_water_supply_temperature = 0
    # 采暖水供水流量（新增测点）
    state4, record4 = syncbase.get_reatime_data_by_name('ngb2_heat_water_supply_flow')
    if state4:
        ngb2_heat_water_supply_flow = record4.value
    else:
        ngb2_heat_water_supply_flow = 0
    # 采暖水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ngb2_heat_water_return_temperature')
    if state5:
        ngb2_heat_water_return_temperature = record5.value
    else:
        ngb2_heat_water_return_temperature = 0
    # 出口烟气温度
    state6, record6 = syncbase.get_reatime_data_by_name('ngb2_outlet_flue_gas_temperature')
    if state6:
        ngb2_outlet_flue_gas_temperature = record6.value
    else:
        ngb2_outlet_flue_gas_temperature = 0
    # 出口烟气流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('ngb2_outlet_flue_gas_flow')
    if state7:
        ngb2_outlet_flue_gas_flow = record7.value
    else:
        ngb2_outlet_flue_gas_flow = 0
    # 天然气进气流量
    state8, record8 = syncbase.get_reatime_data_by_name('ngb2_natural_gas_inlet_flow')
    if state8:
        ngb2_natural_gas_inlet_flow = record8.value
    else:
        ngb2_natural_gas_inlet_flow = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ngb2_state, ngb2_fault, ngb2_heat_water_supply_temperature, ngb2_heat_water_supply_flow, ngb2_heat_water_return_temperature, ngb2_outlet_flue_gas_temperature, ngb2_outlet_flue_gas_flow, ngb2_natural_gas_inlet_flow


def read_from_database_ngb3():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取天然气热水锅炉3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 3#天然气热水锅炉
    # 运行状态（新增逻辑点）
    state1, record1 = syncbase.get_reatime_data_by_name('ngb3_state')
    if state1:
        ngb3_state = record1.value
    else:
        ngb3_state = False
    # 故障信号（新增逻辑点）
    state2, record2 = syncbase.get_reatime_data_by_name('ngb3_fault')
    if state2:
        ngb3_fault = record2.value
    else:
        ngb3_fault = True
    # 生活热水供水温度
    state3, record3 = syncbase.get_reatime_data_by_name('ngb3_hot_water_supply_temperature')
    if state3:
        ngb3_hot_water_supply_temperature = record3.value
    else:
        ngb3_hot_water_supply_temperature = 0
    # 生活热水供水流量
    state4, record4 = syncbase.get_reatime_data_by_name('ngb3_hot_water_supply_flow')
    if state4:
        ngb3_hot_water_supply_flow = record4.value
    else:
        ngb3_hot_water_supply_flow = 0
    # 生活热水回水温度
    state5, record5 = syncbase.get_reatime_data_by_name('ngb3_hot_water_return_temperature')
    if state5:
        ngb3_hot_water_return_temperature = record5.value
    else:
        ngb3_hot_water_return_temperature = 0
    # 出口烟气温度
    state6, record6 = syncbase.get_reatime_data_by_name('ngb3_outlet_flue_gas_temperature')
    if state6:
        ngb3_outlet_flue_gas_temperature = record6.value
    else:
        ngb3_outlet_flue_gas_temperature = 0
    # 出口烟气流量（新增测点）
    state7, record7 = syncbase.get_reatime_data_by_name('ngb3_outlet_flue_gas_flow')
    if state7:
        ngb3_outlet_flue_gas_flow = record7.value
    else:
        ngb3_outlet_flue_gas_flow = 0
    # 天然气进气流量
    state8, record8 = syncbase.get_reatime_data_by_name('ngb3_natural_gas_inlet_flow')
    if state8:
        ngb3_natural_gas_inlet_flow = record8.value
    else:
        ngb3_natural_gas_inlet_flow = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return ngb3_state, ngb3_fault, ngb3_hot_water_supply_temperature, ngb3_hot_water_supply_flow, ngb3_hot_water_return_temperature, ngb3_outlet_flue_gas_temperature, ngb3_outlet_flue_gas_flow, ngb3_natural_gas_inlet_flow


def read_from_database_ngb_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取天然气热水锅炉公用部分的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 天然气热水锅炉公用数据(1#和2#锅炉公用数据)
    # 天然气热水锅炉供水母管温度
    state1, record1 = syncbase.get_reatime_data_by_name('ngb_heat_water_supply_temperature')
    if state1:
        ngb_heat_water_supply_temperature = record1.value
    else:
        ngb_heat_water_supply_temperature = 0
    # 天然气热水锅炉供水母管流量（新增测点）
    state2, record2 = syncbase.get_reatime_data_by_name('ngb_heat_water_supply_flow')
    if state2:
        ngb_heat_water_supply_flow = record2.value
    else:
        ngb_heat_water_supply_flow = 0
    # 天然气热水锅炉回水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('ngb_heat_water_return_temperature')
    if state3:
        ngb_heat_water_return_temperature = record3.value
    else:
        ngb_heat_water_return_temperature = 0
    # 天然气锅炉排烟温度
    state4, record4 = syncbase.get_reatime_data_by_name('ngb_exhaust_temperature')
    if state4:
        ngb_exhaust_temperature = record4.value
    else:
        ngb_exhaust_temperature = 0
    # 天然气锅炉排烟流量
    state5, record5 = syncbase.get_reatime_data_by_name('ngb_exhaust_flow')
    if state5:
        ngb_exhaust_flow = record5.value
    else:
        ngb_exhaust_flow = 0
    # 天然气热水锅炉空调热水能量
    state6, record6 = syncbase.get_reatime_data_by_name('ngb_heat_water_energy')
    if state5:
        ngb_heat_water_energy = record6.value
    else:
        ngb_heat_water_energy = 0

    return ngb_heat_water_supply_temperature, ngb_heat_water_supply_flow, ngb_heat_water_return_temperature, ngb_exhaust_temperature, ngb_exhaust_flow, ngb_heat_water_energy


def read_from_database_system_utility():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取系统公用数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 分水器温度
    state1, record1 = syncbase.get_reatime_data_by_name('manifold_temperature')
    if state1:
        manifold_temperature = record1.value
    else:
        manifold_temperature = 0
    # 集水器温度
    state2, record2 = syncbase.get_reatime_data_by_name('water_collector_temperature')
    if state2:
        water_collector_temperature = record2.value
    else:
        water_collector_temperature = 0
    # 生活热水供水母管温度
    state3, record3 = syncbase.get_reatime_data_by_name('hot_water_supply_temperature')
    if state3:
        hot_water_supply_pipe_temperature = record3.value
    else:
        hot_water_supply_pipe_temperature = 0
    # 生活热水回水母管温度
    state4, record4 = syncbase.get_reatime_data_by_name('hot_water_return_temperature')
    if state4:
        hot_water_return_pipe_temperature = record4.value
    else:
        hot_water_return_pipe_temperature = 0
    # 天然气母管流量1
    state5, record5 = syncbase.get_reatime_data_by_name('natural_gas_flow_1')
    if state5:
        natural_gas_pipe_flow_1 = record5.value
    else:
        natural_gas_pipe_flow_1 = 0
    # 天然气母管流量2
    state6, record6 = syncbase.get_reatime_data_by_name('natural_gas_flow_2')
    if state6:
        natural_gas_pipe_flow_2 = record6.value
    else:
        natural_gas_pipe_flow_2 = 0
    # 生活热水能量
    state7, record7 = syncbase.get_reatime_data_by_name('hot_water_energy')
    if state7:
        hot_water_energy = record7.value
    else:
        hot_water_energy = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return manifold_temperature, water_collector_temperature, hot_water_supply_pipe_temperature, hot_water_return_pipe_temperature, natural_gas_pipe_flow_1, natural_gas_pipe_flow_2, hot_water_energy


def read_from_database_load_forecast():
    """利用SyncBASE，从数据库中读取数据"""
    # 读取系环境数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 环境干球温度
    state1, record1 = syncbase.get_reatime_data_by_name('environment_temperature')
    if state1:
        environment_temperature = record1.value
    else:
        environment_temperature = 0
    # 环境湿度
    state2, record2 = syncbase.get_reatime_data_by_name('environment_humidity')
    if state2:
        environment_humidity = record2.value
    else:
        environment_humidity = 0
    # 太阳辐射强度
    state3, record3 = syncbase.get_reatime_data_by_name('sun_radiation')
    if state3:
        sun_radiation = record3.value
    else:
        sun_radiation = 0
    # 风速
    state4, record4 = syncbase.get_reatime_data_by_name('wind_speed')
    if state4:
        wind_speed = record4.value
    else:
        wind_speed = 0
    # 风向
    state5, record5 = syncbase.get_reatime_data_by_name('wind_direction')
    if state5:
        wind_direction = record5.value
    else:
        wind_direction = 0

    # 人员密度
    state6, record6 = syncbase.get_reatime_data_by_name('personnel_density')
    if state6:
        personnel_density = record6.value
    else:
        personnel_density = 0
    # 设备发热程度
    state7, record7 = syncbase.get_reatime_data_by_name('equipment_fever')
    if state7:
        equipment_fever = record7.value
    else:
        equipment_fever = 0

    # 关闭syncbase
    syncbase.close()
    del syncbase

    return environment_temperature, environment_humidity, sun_radiation, wind_speed, wind_direction, personnel_density, equipment_fever