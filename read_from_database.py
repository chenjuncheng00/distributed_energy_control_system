import datetime
from syncbase import SyncBase

def read_from_database():
    """利用SyncBASE，从数据库总读取数据"""
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 1号内燃发电机
    # 运行状态
    state, record = syncbase.get_reatime_data_by_name('ice1_state')
    if state:
        ice1_state = record.value
    # 故障信号
    state, record = syncbase.get_reatime_data_by_name('ice1_fault')
    if state:
        ice1_fault = record.value
    # 有功功率实际值
    state, record = syncbase.get_reatime_data_by_name('ice1_actual_value_of_active_power')
    if state:
        ice1_actual_value_of_active_power = record.value
    # 天然气进气流量
    state, record = syncbase.get_reatime_data_by_name('ice1_natural_gas_inlet_flow')
    if state:
        ice1_natural_gas_inlet_flow = record.value
    # 高温缸套水板换二次侧供水温度
    state, record = syncbase.get_reatime_data_by_name('ice1_cylinder_jacket_water_secondary_side_supply_temperature')
    if state:
        ice1_cylinder_jacket_water_secondary_side_supply_temperature = record.value
    # 高温缸套水板换二次侧回水温度
    state, record = syncbase.get_reatime_data_by_name('ice1_cylinder_jacket_water_secondary_side_return_temperature')
    if state:
        ice1_cylinder_jacket_water_secondary_side_return_temperature = record.value
    # 出口烟气温度
    state, record = syncbase.get_reatime_data_by_name('ice1_outlet_flue_gas_temperature')
    if state:
        ice1_outlet_flue_gas_temperature = record.value
    # 排烟温度
    state, record = syncbase.get_reatime_data_by_name('ice1_exhaust_temperature')
    if state:
        ice1_exhaust_temperature = record.value
    # 排烟流量
    state, record = syncbase.get_reatime_data_by_name('ice1_exhaust_flow')
    if state:
        ice1_exhaust_flow = record.value

    # 2号内燃发电机
    # 运行状态
    state, record = syncbase.get_reatime_data_by_name('ice2_state')
    if state:
        ice2_state = record.value
    # 故障信号
    state, record = syncbase.get_reatime_data_by_name('ice2_fault')
    if state:
        ice2_fault = record.value
    # 有功功率实际值
    state, record = syncbase.get_reatime_data_by_name('ice2_actual_value_of_active_power')
    if state:
        ice2_actual_value_of_active_power = record.value
    # 天然气进气流量
    state, record = syncbase.get_reatime_data_by_name('ice2_natural_gas_inlet_flow')
    if state:
        ice2_natural_gas_inlet_flow = record.value
    # 高温缸套水板换二次侧供水温度
    state, record = syncbase.get_reatime_data_by_name('ice2_cylinder_jacket_water_secondary_side_supply_temperature')
    if state:
        ice2_cylinder_jacket_water_secondary_side_supply_temperature = record.value
    # 高温缸套水板换二次侧回水温度
    state, record = syncbase.get_reatime_data_by_name('ice2_cylinder_jacket_water_secondary_side_return_temperature')
    if state:
        ice2_cylinder_jacket_water_secondary_side_return_temperature = record.value
    # 出口烟气温度
    state, record = syncbase.get_reatime_data_by_name('ice2_outlet_flue_gas_temperature')
    if state:
        ice2_outlet_flue_gas_temperature = record.value
    # 排烟温度
    state, record = syncbase.get_reatime_data_by_name('ice2_exhaust_temperature')
    if state:
        ice2_exhaust_temperature = record.value
    # 排烟流量
    state, record = syncbase.get_reatime_data_by_name('ice2_exhaust_flow')
    if state:
        ice2_exhaust_flow = record.value

