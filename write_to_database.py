from datetime import datetime as dt

def write_to_database_ice1(syncbase, ice1_remote_start, ice1_remote_stop, ice1_black_start, ice1_active_power_set, ice1_reactive_power_set, ice1_power_factor_set,
                           ice1_electrical_efficiency, ice1_residual_heat_efficiency, ice1_electrical_power, ice1_residual_heat_power,
                           ice1_natural_gas_consumption, ice1_power_consumption, ice1_electrical_income, ice1_electrical_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机1的数据

    # 批量写入数据到数据库
    # 1#燃气内燃发电机组远程启机指令
    # 1#燃气内燃发电机组远程停机指令
    # 1#燃气内燃发电机组黑启动指令
    # 1#燃气内燃发电机有功功率给定
    # 1#燃气内燃发电机无功功率给定
    # 1#燃气内燃发电机功率因数给定
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ice1_remote_start', 'ice1_remote_stop', 'ice1_black_start', 'ice1_active_power_set',
         'ice1_reactive_power_set', 'ice1_power_factor_set'],
        [ice1_remote_start, ice1_remote_stop, ice1_black_start, ice1_active_power_set, ice1_reactive_power_set,
         ice1_power_factor_set])

    # 程序计算出的数据
    # #1燃气内燃发电机发电效率
    # #1燃气内燃发电机余热效率
    # #1燃气内燃发电机发电功率
    # #1燃气内燃发电机余热功率
    # #1燃气内燃发电机天然气耗量
    # #1燃气内燃发电机辅助设备耗电量
    # #1燃气内燃发电机发电收入
    # #1燃气内燃发电机发电成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice1_electrical_efficiency', 'ice1_residual_heat_efficiency', 'ice1_electrical_power', 'ice1_residual_heat_power',
         'ice1_natural_gas_consumption', 'ice1_power_consumption', 'ice1_electrical_income', 'ice1_electrical_cost'],
        [ice1_electrical_efficiency*100, ice1_residual_heat_efficiency*100, ice1_electrical_power, ice1_residual_heat_power,
         ice1_natural_gas_consumption, ice1_power_consumption, ice1_electrical_income, ice1_electrical_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("内燃机1写入数据库出错！")


def write_to_database_ice2(syncbase, ice2_remote_start, ice2_remote_stop, ice2_black_start, ice2_active_power_set, ice2_reactive_power_set, ice2_power_factor_set,
                           ice2_electrical_efficiency, ice2_residual_heat_efficiency, ice2_electrical_power,ice2_residual_heat_power,
                           ice2_natural_gas_consumption, ice2_power_consumption, ice2_electrical_income, ice2_electrical_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机2的数据

    # 批量写入数据到数据库
    # 2#燃气内燃发电机组远程启机指令
    # 2#燃气内燃发电机组远程停机指令
    # 2#燃气内燃发电机组黑启动指令
    # 2#燃气内燃发电机有功功率给定
    # 2#燃气内燃发电机无功功率给定
    # 2#燃气内燃发电机功率因数给定
    state1 = syncbase.write_batch_realtime_data_by_name(
            ['ice2_remote_start', 'ice2_remote_stop',
             'ice2_black_start', 'ice2_active_power_set', 'ice2_reactive_power_set', 'ice2_power_factor_set'],
            [ice2_remote_start, ice2_remote_stop, ice2_black_start, ice2_active_power_set,
             ice2_reactive_power_set, ice2_power_factor_set])

    # 程序计算出的数据
    # #2燃气内燃发电机发电功率
    # #2燃气内燃发电机余热功率
    # #2燃气内燃发电机发电效率
    # #2燃气内燃发电机余热效率
    # #2燃气内燃发电机天然气耗量
    # #2燃气内燃发电机辅助设备耗电量
    # #2燃气内燃发电机发电收入
    # #2燃气内燃发电机发电成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice2_electrical_efficiency', 'ice2_residual_heat_efficiency', 'ice2_electrical_power',
         'ice2_residual_heat_power', 'ice2_natural_gas_consumption', 'ice2_power_consumption',
         'ice2_electrical_income', 'ice2_electrical_cost'],
        [ice2_electrical_efficiency*100, ice2_residual_heat_efficiency*100, ice2_electrical_power, ice2_residual_heat_power,
         ice2_natural_gas_consumption, ice2_power_consumption, ice2_electrical_income, ice2_electrical_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("内燃机2写入数据库出错！")


def write_to_database_lb1(syncbase, lb1_remote_start, lb1_remote_stop, lb1_wp_heat_chilled_water_frequency, lb1_wp_cooling_water_frequency,
                          lb1_cold_heat_out, lb1_power_consumption, lb1_chilled_heat_water_flow, lb1_cooling_water_flow,
                          lb1_wp_chilled_heat_water_power_consumption, lb1_wp_cooling_water_power_consumption, lb1_fan_power_consumption,
                          lb1_cold_cop, lb1_heat_cop, lb1_hot_water_cop, lb1_hot_water_out, lb1_cold_cost, lb1_heat_cost,
                          lb1_hot_water_cost, lb1_wp_hot_water_power_consumption, lb1_hot_water_flow, lb1_cold_income, lb1_heat_income, lb1_hot_water_income):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂1的数据

    # 批量写入数据到数据库
    # 1#溴化锂机组机组远程开机
    # 1#溴化锂机组机组远程关机
    # 1#溴化锂机组机组冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#溴化锂机组机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['lb1_remote_start', 'lb1_remote_stop', 'lb1_wp_heat_chilled_water_frequency', 'lb1_wp_cooling_water_frequency'],
        [lb1_remote_start, lb1_remote_stop, lb1_wp_heat_chilled_water_frequency, lb1_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #1溴化锂供冷供热功率
    # #1溴化锂耗电功率
    # #1溴化锂冷冻水/采暖水流量
    # #1溴化锂冷却水流量
    # #1溴化锂冷冻/采暖水泵电功率
    # #1溴化锂冷却水泵电功率
    # #1溴化锂冷却塔电功率
    # #1溴化锂制冷COP
    # #1溴化锂制热COP
    # #1溴化锂生活热水COP
    # #1溴化锂制生活热水功率
    # #1溴化锂制冷成本
    # #1溴化锂制热成本
    # #1溴化锂制生活热水成本
    # #1溴化锂制生活热水泵电功率
    # #1溴化锂制生活热水流量
    # #1溴化锂制冷收入
    # #1溴化锂制热收入
    # #1溴化锂制生活热水收入

    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb1_cold_heat_out', 'lb1_power_consumption', 'lb1_chilled_heat_water_flow', 'lb1_cooling_water_flow',
         'lb1_wp_chilled_heat_water_power_consumption', 'lb1_wp_cooling_water_power_consumption', 'lb1_fan_power_consumption',
         'lb1_cold_cop', 'lb1_heat_cop', 'lb1_hot_water_cop', 'lb1_hot_water_out', 'lb1_cold_cost', 'lb1_heat_cost', 'lb1_hot_water_cost',
         'lb1_wp_hot_water_power_consumption', 'lb1_hot_water_flow', 'lb1_cold_income', 'lb1_heat_income', 'lb1_hot_water_income'],
        [lb1_cold_heat_out, lb1_power_consumption, lb1_chilled_heat_water_flow, lb1_cooling_water_flow, lb1_wp_chilled_heat_water_power_consumption,
         lb1_wp_cooling_water_power_consumption, lb1_fan_power_consumption, lb1_cold_cop, lb1_heat_cop, lb1_hot_water_cop, lb1_hot_water_out,
         lb1_cold_cost, lb1_heat_cost, lb1_hot_water_cost, lb1_wp_hot_water_power_consumption, lb1_hot_water_flow, lb1_cold_income, lb1_heat_income, lb1_hot_water_income])

    # 报错
    if (state1 == False or state2 == False):
        print("烟气热水型溴化锂1写入数据库出错！")


def write_to_database_lb2(syncbase, lb2_remote_start, lb2_remote_stop, lb2_wp_heat_chilled_water_frequency, lb2_wp_cooling_water_frequency, lb2_cold_heat_out,
                          lb2_power_consumption, lb2_chilled_heat_water_flow, lb2_cooling_water_flow, lb2_wp_chilled_heat_water_power_consumption,
                          lb2_wp_cooling_water_power_consumption, lb2_fan_power_consumption, lb2_cold_cop, lb2_heat_cop, lb2_hot_water_cop, lb2_hot_water_out,
                          lb2_cold_cost, lb2_heat_cost, lb2_hot_water_cost, lb2_wp_hot_water_power_consumption, lb2_hot_water_flow, lb2_cold_income,
                          lb2_heat_income, lb2_hot_water_income):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂2的数据

    # 批量写入数据到数据库
    # 2#溴化锂机组机组远程开机
    # 2#溴化锂机组机组远程关机
    # 2#溴化锂机组机组冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 2#溴化锂机组机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['lb2_remote_start', 'lb2_remote_stop', 'lb2_wp_heat_chilled_water_frequency',
         'lb2_wp_cooling_water_frequency'],
        [lb2_remote_start, lb2_remote_stop, lb2_wp_heat_chilled_water_frequency, lb2_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #2溴化锂供冷供热功率
    # #2溴化锂耗电功率
    # #2溴化锂冷冻水/采暖水流量
    # #2溴化锂冷却水流量
    # #2溴化锂冷冻/采暖水泵电功率
    # #2溴化锂冷却水泵电功率
    # #2溴化锂冷却塔电功率
    # #2溴化锂制冷COP
    # #2溴化锂制热COP
    # #2溴化锂生活热水COP
    # #2溴化锂制生活热水功率
    # #2溴化锂制冷成本
    # #2溴化锂制热成本
    # #2溴化锂制生活热水成本
    # #2溴化锂制生活热水泵电功率
    # #2溴化锂制生活热水流量
    # #2溴化锂制冷收入
    # #2溴化锂制热收入
    # #2溴化锂制生活热水收入

    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb2_cold_heat_out', 'lb2_power_consumption', 'lb2_chilled_heat_water_flow', 'lb2_cooling_water_flow',
         'lb2_wp_chilled_heat_water_power_consumption', 'lb2_wp_cooling_water_power_consumption', 'lb2_fan_power_consumption',
         'lb2_cold_cop', 'lb2_heat_cop', 'lb2_hot_water_cop', 'lb2_hot_water_out', 'lb2_cold_cost', 'lb2_heat_cost',
         'lb2_hot_water_cost', 'lb2_wp_hot_water_power_consumption', 'lb2_hot_water_flow', 'lb2_cold_income', 'lb2_heat_income', 'lb2_hot_water_income'],
        [lb2_cold_heat_out, lb2_power_consumption, lb2_chilled_heat_water_flow, lb2_cooling_water_flow,
         lb2_wp_chilled_heat_water_power_consumption, lb2_wp_cooling_water_power_consumption, lb2_fan_power_consumption, lb2_cold_cop, lb2_heat_cop,
         lb2_hot_water_cop, lb2_hot_water_out, lb2_cold_cost, lb2_heat_cost, lb2_hot_water_cost, lb2_wp_hot_water_power_consumption, lb2_hot_water_flow,
         lb2_cold_income, lb2_heat_income, lb2_hot_water_income])

    # 报错
    if (state1 == False or state2 == False):
        print("烟气热水型溴化锂2写入数据库出错！")


def write_to_database_cc1(syncbase, cc1_interlock_stop, cc1_remote_stop, cc1_remote_start, cc1_wp_chilled_water_frequency, cc1_wp_cooling_water_frequency,
                          cc1_cold_out, cc1_power_consumption, cc1_chilled_water_flow, cc1_cooling_water_flow, cc1_wp_chilled_water_power_consumption,
                          cc1_wp_cooling_water_power_consumption, cc1_cooling_tower_power_consumption, cc1_cop, cc1_income, cc1_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机1的数据

    # 批量写入数据到数据库
    # 1#离心式冷水机组联锁停机指令
    # 1#离心式冷水机组远方停机指令
    # 1#离心式冷水机组远方开机指令
    # 1#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['cc1_interlock_stop', 'cc1_remote_stop', 'cc1_remote_start', 'cc1_wp_chilled_water_frequency', 'cc1_wp_cooling_water_frequency'],
        [cc1_interlock_stop, cc1_remote_stop, cc1_remote_start, cc1_wp_chilled_water_frequency, cc1_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #1离心式冷水机供冷功率
    # #1离心式冷水机耗电功率
    # #1离心式冷水机冷冻水流量
    # #1离心式冷水机冷却水流量
    # #1离心式冷水机冷冻水泵电功率
    # #1离心式冷水机冷却水泵电功率
    # #1离心式冷水机冷却塔电功率
    # #1离心式冷水机制冷COP
    # #1离心式冷水机制冷收入
    # #1离心式冷水机制冷成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc1_cold_out', 'cc1_power_consumption', 'cc1_chilled_water_flow', 'cc1_cooling_water_flow', 'cc1_wp_chilled_water_power_consumption',
         'cc1_wp_cooling_water_power_consumption', 'cc1_cooling_tower_power_consumption', 'cc1_cop', 'cc1_income', 'cc1_cost'],
        [cc1_cold_out, cc1_power_consumption, cc1_chilled_water_flow, cc1_cooling_water_flow, cc1_wp_chilled_water_power_consumption,
        cc1_wp_cooling_water_power_consumption, cc1_cooling_tower_power_consumption, cc1_cop, cc1_income, cc1_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式冷水机1写入数据库出错！")


def write_to_database_cc2(syncbase, cc2_interlock_stop, cc2_remote_stop, cc2_remote_start, cc2_wp_chilled_water_frequency, cc2_wp_cooling_water_frequency,
                          cc2_cold_out, cc2_power_consumption, cc2_chilled_water_flow, cc2_cooling_water_flow, cc2_wp_chilled_water_power_consumption,
                          cc2_wp_cooling_water_power_consumption, cc2_cooling_tower_power_consumption, cc2_cop, cc2_income, cc2_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机2的数据

    # 批量写入数据到数据库
    # 2#离心式冷水机组联锁停机指令
    # 2#离心式冷水机组远方停机指令
    # 2#离心式冷水机组远方开机指令
    # 2#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 2#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
            ['cc2_interlock_stop', 'cc2_remote_stop', 'cc2_remote_start', 'cc2_wp_chilled_water_frequency', 'cc2_wp_cooling_water_frequency'],
            [cc2_interlock_stop, cc2_remote_stop, cc2_remote_start, cc2_wp_chilled_water_frequency, cc2_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #2离心式冷水机供冷功率
    # #2离心式冷水机耗电功率
    # #2离心式冷水机冷冻水流量
    # #2离心式冷水机冷却水流量
    # #2离心式冷水机冷冻水泵电功率
    # #2离心式冷水机冷却水泵电功率
    # #2离心式冷水机冷却塔电功率
    # #2离心式冷水机制冷COP
    # #2离心式冷水机制冷收入
    # #2离心式冷水机制冷成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc2_cold_out', 'cc2_power_consumption', 'cc2_chilled_water_flow', 'cc2_cooling_water_flow',
         'cc2_wp_chilled_water_power_consumption', 'cc2_wp_cooling_water_power_consumption',
         'cc2_cooling_tower_power_consumption', 'cc2_cop', 'cc2_income', 'cc2_cost'],
        [cc2_cold_out, cc2_power_consumption, cc2_chilled_water_flow, cc2_cooling_water_flow, cc2_wp_chilled_water_power_consumption,
         cc2_wp_cooling_water_power_consumption, cc2_cooling_tower_power_consumption, cc2_cop, cc2_income, cc2_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式冷水机2写入数据库出错！")


def write_to_database_cc3(syncbase, cc3_interlock_stop, cc3_remote_stop, cc3_remote_start, cc3_wp_chilled_water_frequency, cc3_wp_cooling_water_frequency,
                          cc3_cold_out, cc3_power_consumption, cc3_chilled_water_flow, cc3_cooling_water_flow, cc3_wp_chilled_water_power_consumption,
                          cc3_wp_cooling_water_power_consumption, cc3_cooling_tower_power_consumption, cc3_cop, cc3_income, cc3_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机3的数据

    # 批量写入数据到数据库
    # 3#离心式冷水机组联锁停机指令
    # 3#离心式冷水机组远方停机指令
    # 3#离心式冷水机组远方开机指令
    # 3#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 3#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['cc3_interlock_stop', 'cc3_remote_stop', 'cc3_remote_start', 'cc3_wp_chilled_water_frequency', 'cc3_wp_cooling_water_frequency'],
        [cc3_interlock_stop, cc3_remote_stop, cc3_remote_start, cc3_wp_chilled_water_frequency, cc3_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #3离心式冷水机供冷功率
    # #3离心式冷水机耗电功率
    # #3离心式冷水机冷冻水流量
    # #3离心式冷水机冷却水流量
    # #3离心式冷水机冷冻水泵电功率
    # #3离心式冷水机冷却水泵电功率
    # #3离心式冷水机冷却塔电功率
    # #3离心式冷水机制冷COP
    # #3离心式冷水机制冷收入
    # #3离心式冷水机制冷成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc3_cold_out', 'cc3_power_consumption', 'cc3_chilled_water_flow', 'cc3_cooling_water_flow',
         'cc3_wp_chilled_water_power_consumption', 'cc3_wp_cooling_water_power_consumption',
         'cc3_cooling_tower_power_consumption', 'cc3_cop', 'cc3_income', 'cc3_cost'],
        [cc3_cold_out, cc3_power_consumption, cc3_chilled_water_flow, cc3_cooling_water_flow, cc3_wp_chilled_water_power_consumption,
         cc3_wp_cooling_water_power_consumption, cc3_cooling_tower_power_consumption, cc3_cop, cc3_income, cc3_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式冷水机3写入数据库出错！")


def write_to_database_cc4(syncbase, cc4_interlock_stop, cc4_remote_stop, cc4_remote_start, cc4_wp_chilled_water_frequency, cc4_wp_cooling_water_frequency,
                          cc4_cold_out, cc4_power_consumption, cc4_chilled_water_flow, cc4_cooling_water_flow, cc4_wp_chilled_water_power_consumption,
                          cc4_wp_cooling_water_power_consumption, cc4_cooling_tower_power_consumption, cc4_cop, cc4_income, cc4_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机4的数据

    # 批量写入数据到数据库
    # 4#离心式冷水机组联锁停机指令
    # 4#离心式冷水机组远方停机指令
    # 4#离心式冷水机组远方开机指令
    # 4#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 4#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['cc4_interlock_stop', 'cc4_remote_stop', 'cc4_remote_start', 'cc4_wp_chilled_water_frequency', 'cc4_wp_cooling_water_frequency'],
        [cc4_interlock_stop, cc4_remote_stop, cc4_remote_start, cc4_wp_chilled_water_frequency, cc4_wp_cooling_water_frequency])

    # 程序计算出的数据
    # #4离心式冷水机供冷功率
    # #4离心式冷水机耗电功率
    # #4离心式冷水机冷冻水流量
    # #4离心式冷水机冷却水流量
    # #4离心式冷水机冷冻水泵电功率
    # #4离心式冷水机冷却水泵电功率
    # #4离心式冷水机冷却塔电功率
    # #4离心式冷水机制冷COP
    # #4离心式冷水机制冷收入
    # #4离心式冷水机制冷成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc4_cold_out', 'cc4_power_consumption', 'cc4_chilled_water_flow', 'cc4_cooling_water_flow',
         'cc4_wp_chilled_water_power_consumption', 'cc4_wp_cooling_water_power_consumption',
         'cc4_cooling_tower_power_consumption', 'cc4_cop', 'cc4_income', 'cc4_cost'],
        [cc4_cold_out, cc4_power_consumption, cc4_chilled_water_flow, cc4_cooling_water_flow, cc4_wp_chilled_water_power_consumption,
         cc4_wp_cooling_water_power_consumption, cc4_cooling_tower_power_consumption, cc4_cop, cc4_income, cc4_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式冷水机4写入数据库出错！")


def write_to_database_chp1(syncbase, chp1_interlock_stop, chp1_remote_stop, chp1_remote_start, chp1_wp_heat_water_frequency, chp1_wp_source_water_frequency,
                           chp1_heat_out, chp1_power_consumption, chp1_heat_water_flow, chp1_source_water_flow,
                           chp1_wp_heat_water_power_consumption, chp1_wp_source_water_power_consumption, chp1_cop, chp1_income, chp1_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵1的数据

    # 批量写入数据到数据库
    # 1#离心式热泵联锁停机指令
    # 1#离心式热泵远方停机指令
    # 1#离心式热泵远方开机指令
    # 1#离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['chp1_interlock_stop', 'chp1_remote_stop', 'chp1_remote_start', 'chp1_wp_heat_water_frequency', 'chp1_wp_source_water_frequency'],
        [chp1_interlock_stop, chp1_remote_stop, chp1_remote_start, chp1_wp_heat_water_frequency, chp1_wp_source_water_frequency])

    # 程序计算出的数据
    # #1离心式热泵供热功率
    # #1离心式热泵耗电功率
    # #1离心式热泵采暖水流量
    # #1离心式热泵热源水流量
    # #1离心式热泵采暖水泵电功率
    # #1离心式热泵热源水泵电功率
    # #1离心式热泵制热COP
    # #1离心式热泵制热收入
    # #1离心式热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp1_heat_out', 'chp1_power_consumption', 'chp1_heat_water_flow', 'chp1_source_water_flow', 'chp1_wp_heat_water_power_consumption',
         'chp1_wp_source_water_power_consumption', 'chp1_cop', 'chp1_income', 'chp1_cost'],
        [chp1_heat_out, chp1_power_consumption, chp1_heat_water_flow, chp1_source_water_flow, chp1_wp_heat_water_power_consumption,
         chp1_wp_source_water_power_consumption, chp1_cop, chp1_income, chp1_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式热泵1写入数据库出错！")


def write_to_database_chp2(syncbase, chp2_interlock_stop, chp2_remote_stop, chp2_remote_start, chp2_wp_heat_water_frequency, chp2_wp_source_water_frequency,
                           chp2_heat_out, chp2_power_consumption, chp2_heat_water_flow, chp2_source_water_flow,
                           chp2_wp_heat_water_power_consumption, chp2_wp_source_water_power_consumption, chp2_cop, chp2_income, chp2_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵2的数据

    # 批量写入数据到数据库
    # #2离心式热泵联锁停机指令
    # #2离心式热泵远方停机指令
    # #2离心式热泵远方开机指令
    # #2离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # #2离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['chp2_interlock_stop', 'chp2_remote_stop', 'chp2_remote_start', 'chp2_wp_heat_water_frequency', 'chp2_wp_source_water_frequency'],
        [chp2_interlock_stop, chp2_remote_stop, chp2_remote_start, chp2_wp_heat_water_frequency, chp2_wp_source_water_frequency])

    # 程序计算出的数据
    # #2离心式热泵供热功率
    # #2离心式热泵耗电功率
    # #2离心式热泵采暖水流量
    # #2离心式热泵热源水流量
    # #2离心式热泵采暖水泵电功率
    # #2离心式热泵热源水泵电功率
    # #2离心式热泵制热COP
    # #2离心式热泵制热收入
    # #2离心式热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp2_heat_out', 'chp2_power_consumption', 'chp2_heat_water_flow', 'chp2_source_water_flow', 'chp2_wp_heat_water_power_consumption',
         'chp2_wp_source_water_power_consumption', 'chp2_cop', 'chp2_income', 'chp2_cost'],
        [chp2_heat_out, chp2_power_consumption, chp2_heat_water_flow, chp2_source_water_flow, chp2_wp_heat_water_power_consumption,
         chp2_wp_source_water_power_consumption, chp2_cop, chp2_income, chp2_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式热泵2写入数据库出错！")


def write_to_database_chp3(syncbase, chp3_interlock_stop, chp3_remote_stop, chp3_remote_start, chp3_wp_heat_water_frequency, chp3_wp_source_water_frequency,
                           chp3_heat_out, chp3_power_consumption, chp3_heat_water_flow, chp3_source_water_flow,
                           chp3_wp_heat_water_power_consumption, chp3_wp_source_water_power_consumption, chp3_cop, chp3_income, chp3_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵3的数据

    # 批量写入数据到数据库
    # #3离心式热泵联锁停机指令
    # #3离心式热泵远方停机指令
    # #3离心式热泵远方开机指令
    # #3离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # #3离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['chp3_interlock_stop', 'chp3_remote_stop', 'chp3_remote_start', 'chp3_wp_heat_water_frequency', 'chp3_wp_source_water_frequency'],
        [chp3_interlock_stop, chp3_remote_stop, chp3_remote_start, chp3_wp_heat_water_frequency, chp3_wp_source_water_frequency])

    # 程序计算出的数据
    # #3离心式热泵供热功率
    # #3离心式热泵耗电功率
    # #3离心式热泵采暖水流量
    # #3离心式热泵热源水流量
    # #3离心式热泵采暖水泵电功率
    # #3离心式热泵热源水泵电功率
    # #3离心式热泵制热COP
    # #3离心式热泵制热收入
    # #3离心式热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp3_heat_out', 'chp3_power_consumption', 'chp3_heat_water_flow', 'chp3_source_water_flow', 'chp3_wp_heat_water_power_consumption',
         'chp3_wp_source_water_power_consumption', 'chp3_cop', 'chp3_income', 'chp3_cost'],
        [chp3_heat_out, chp3_power_consumption, chp3_heat_water_flow, chp3_source_water_flow, chp3_wp_heat_water_power_consumption,
         chp3_wp_source_water_power_consumption, chp3_cop, chp3_income, chp3_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式热泵3写入数据库出错！")


def write_to_database_chp4(syncbase, chp4_interlock_stop, chp4_remote_stop, chp4_remote_start, chp4_wp_heat_water_frequency, chp4_wp_source_water_frequency,
                           chp4_heat_out, chp4_power_consumption, chp4_heat_water_flow, chp4_source_water_flow,
                           chp4_wp_heat_water_power_consumption, chp4_wp_source_water_power_consumption, chp4_cop, chp4_income, chp4_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵4的数据

    # 批量写入数据到数据库
    # #4离心式热泵联锁停机指令
    # #4离心式热泵远方停机指令
    # #4离心式热泵远方开机指令
    # #4离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # #4离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['chp4_interlock_stop', 'chp4_remote_stop', 'chp4_remote_start', 'chp4_wp_heat_water_frequency', 'chp4_wp_source_water_frequency'],
        [chp4_interlock_stop, chp4_remote_stop, chp4_remote_start, chp4_wp_heat_water_frequency, chp4_wp_source_water_frequency])

    # 程序计算出的数据
    # #4离心式热泵供热功率
    # #4离心式热泵耗电功率
    # #4离心式热泵采暖水流量
    # #4离心式热泵热源水流量
    # #4离心式热泵采暖水泵电功率
    # #4离心式热泵热源水泵电功率
    # #4离心式热泵制热COP
    # #4离心式热泵制热收入
    # #4离心式热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp4_heat_out', 'chp4_power_consumption', 'chp4_heat_water_flow', 'chp4_source_water_flow', 'chp4_wp_heat_water_power_consumption',
         'chp4_wp_source_water_power_consumption', 'chp4_cop', 'chp4_income', 'chp4_cost'],
        [chp4_heat_out, chp4_power_consumption, chp4_heat_water_flow, chp4_source_water_flow, chp4_wp_heat_water_power_consumption,
         chp4_wp_source_water_power_consumption, chp4_cop, chp4_income, chp4_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("离心式热泵4写入数据库出错！")


def write_to_database_ashp1(syncbase, ashp1_interlock_stop, ashp1_remote_stop, ashp1_remote_start, ashp1_wp_water_frequency,
                            ashp1_cold_heat_out, ashp1_power_consumption, ashp1_chilled_heat_water_flow, ashp1_wp_power_consumption,
                            ashp1_fan_power_consumption, ashp1_cold_cop, ashp1_heat_cop, ashp1_cold_income, ashp1_cold_cost, ashp1_heat_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵1的数据

    # 批量写入数据到数据库
    # #1空气源热泵机组联锁停机指令
    # #1空气源热泵机组远方停机指令
    # #1空气源热泵机组远方开机指令
    # #1空气源热泵机组水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ashp1_interlock_stop', 'ashp1_remote_stop', 'ashp1_remote_start', 'ashp1_wp_water_frequency'],
        [ashp1_interlock_stop, ashp1_remote_stop, ashp1_remote_start, ashp1_wp_water_frequency])

    # 程序计算出的数据
    # #1空气源热泵供冷/供热功率
    # #1空气源热泵耗电功率
    # #1空气源热泵冷冻水/采暖水流量
    # #1空气源热泵水泵电功率
    # #1空气源热泵风扇电功率
    # #1空气源热泵制冷COP
    # #1空气源热泵制热COP
    # #1空气源热泵制冷收入
    # #1空气源热泵制冷成本
    # #1空气源热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp1_cold_heat_out', 'ashp1_power_consumption', 'ashp1_chilled_heat_water_flow', 'ashp1_wp_power_consumption',
        'ashp1_fan_power_consumption', 'ashp1_cold_cop', 'ashp1_heat_cop', 'ashp1_cold_income', 'ashp1_cold_cost', 'ashp1_heat_cost'],
        [ashp1_cold_heat_out, ashp1_power_consumption, ashp1_chilled_heat_water_flow, ashp1_wp_power_consumption,
        ashp1_fan_power_consumption, ashp1_cold_cop, ashp1_heat_cop, ashp1_cold_income, ashp1_cold_cost, ashp1_heat_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("空气源热泵1写入数据库出错！")


def write_to_database_ashp2(syncbase, ashp2_interlock_stop, ashp2_remote_stop, ashp2_remote_start, ashp2_wp_water_frequency,
                            ashp2_cold_heat_out, ashp2_power_consumption, ashp2_chilled_heat_water_flow, ashp2_wp_power_consumption,
                            ashp2_fan_power_consumption, ashp2_cold_cop, ashp2_heat_cop, ashp2_cold_income, ashp2_cold_cost, ashp2_heat_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵2的数据

    # 批量写入数据到数据库
    # #2空气源热泵机组联锁停机指令
    # #2空气源热泵机组远方停机指令
    # #2空气源热泵机组远方开机指令
    # #2空气源热泵机组水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ashp2_interlock_stop', 'ashp2_remote_stop', 'ashp2_remote_start', 'ashp2_wp_water_frequency'],
        [ashp2_interlock_stop, ashp2_remote_stop, ashp2_remote_start, ashp2_wp_water_frequency])

    # 程序计算出的数据
    # #2空气源热泵供冷/供热功率
    # #2空气源热泵耗电功率
    # #2空气源热泵冷冻水/采暖水流量
    # #2空气源热泵水泵电功率
    # #2空气源热泵风扇电功率
    # #2空气源热泵制冷COP
    # #2空气源热泵制热COP
    # #2空气源热泵制冷收入
    # #2空气源热泵制冷成本
    # #2空气源热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp2_cold_heat_out', 'ashp2_power_consumption', 'ashp2_chilled_heat_water_flow', 'ashp2_wp_power_consumption',
        'ashp2_fan_power_consumption', 'ashp2_cold_cop', 'ashp2_heat_cop', 'ashp2_cold_income', 'ashp2_cold_cost', 'ashp2_heat_cost'],
        [ashp2_cold_heat_out, ashp2_power_consumption, ashp2_chilled_heat_water_flow, ashp2_wp_power_consumption,
        ashp2_fan_power_consumption, ashp2_cold_cop, ashp2_heat_cop, ashp2_cold_income, ashp2_cold_cost, ashp2_heat_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("空气源热泵2写入数据库出错！")


def write_to_database_ashp3(syncbase, ashp3_interlock_stop, ashp3_remote_stop, ashp3_remote_start, ashp3_wp_water_frequency,
                            ashp3_cold_heat_out, ashp3_power_consumption, ashp3_chilled_heat_water_flow, ashp3_wp_power_consumption,
                            ashp3_fan_power_consumption, ashp3_cold_cop, ashp3_heat_cop, ashp3_cold_income, ashp3_cold_cost, ashp3_heat_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵3的数据

    # 批量写入数据到数据库
    # #3空气源热泵机组联锁停机指令
    # #3空气源热泵机组远方停机指令
    # #3空气源热泵机组远方开机指令
    # #3空气源热泵机组水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ashp3_interlock_stop', 'ashp3_remote_stop', 'ashp3_remote_start', 'ashp3_wp_water_frequency'],
        [ashp3_interlock_stop, ashp3_remote_stop, ashp3_remote_start, ashp3_wp_water_frequency])

    # 程序计算出的数据
    # #3空气源热泵供冷/供热功率
    # #3空气源热泵耗电功率
    # #3空气源热泵冷冻水/采暖水流量
    # #3空气源热泵水泵电功率
    # #3空气源热泵风扇电功率
    # #3空气源热泵制冷COP
    # #3空气源热泵制热COP
    # #3空气源热泵制冷收入
    # #3空气源热泵制冷成本
    # #3空气源热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp3_cold_heat_out', 'ashp3_power_consumption', 'ashp3_chilled_heat_water_flow', 'ashp3_wp_power_consumption',
        'ashp3_fan_power_consumption', 'ashp3_cold_cop', 'ashp3_heat_cop', 'ashp3_cold_income', 'ashp3_cold_cost', 'ashp3_heat_cost'],
        [ashp3_cold_heat_out, ashp3_power_consumption, ashp3_chilled_heat_water_flow, ashp3_wp_power_consumption,
        ashp3_fan_power_consumption, ashp3_cold_cop, ashp3_heat_cop, ashp3_cold_income, ashp3_cold_cost, ashp3_heat_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("空气源热泵3写入数据库出错！")


def write_to_database_ashp4(syncbase, ashp4_interlock_stop, ashp4_remote_stop, ashp4_remote_start, ashp4_wp_water_frequency,
                            ashp4_cold_heat_out, ashp4_power_consumption, ashp4_chilled_heat_water_flow, ashp4_wp_power_consumption,
                            ashp4_fan_power_consumption, ashp4_cold_cop, ashp4_heat_cop, ashp4_cold_income, ashp4_cold_cost, ashp4_heat_cost):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵4的数据

    # 批量写入数据到数据库
    # #4空气源热泵机组联锁停机指令
    # #4空气源热泵机组远方停机指令
    # #4空气源热泵机组远方开机指令
    # #4空气源热泵机组水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ashp4_interlock_stop', 'ashp4_remote_stop', 'ashp4_remote_start', 'ashp4_wp_water_frequency'],
        [ashp4_interlock_stop, ashp4_remote_stop, ashp4_remote_start, ashp4_wp_water_frequency])

    # 程序计算出的数据
    # #4空气源热泵供冷/供热功率
    # #4空气源热泵耗电功率
    # #4空气源热泵冷冻水/采暖水流量
    # #4空气源热泵水泵电功率
    # #4空气源热泵风扇电功率
    # #4空气源热泵制冷COP
    # #4空气源热泵制热COP
    # #4空气源热泵制冷收入
    # #4空气源热泵制冷成本
    # #4空气源热泵制热成本
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp4_cold_heat_out', 'ashp4_power_consumption', 'ashp4_chilled_heat_water_flow', 'ashp4_wp_power_consumption',
        'ashp4_fan_power_consumption', 'ashp4_cold_cop', 'ashp4_heat_cop', 'ashp4_cold_income', 'ashp4_cold_cost', 'ashp4_heat_cost'],
        [ashp4_cold_heat_out, ashp4_power_consumption, ashp4_chilled_heat_water_flow, ashp4_wp_power_consumption,
        ashp4_fan_power_consumption, ashp4_cold_cop, ashp4_heat_cop, ashp4_cold_income, ashp4_cold_cost, ashp4_heat_cost])

    # 报错
    if (state1 == False or state2 == False):
        print("空气源热泵4写入数据库出错！")


def write_to_database_ese(syncbase, ese_cold_heat_out, ese_residual_storage_energy, ese_cost, ese_proportion_in, ese_proportion_out):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热水罐的数据

    # 程序计算出的数据
    # 蓄能水罐供冷供热功率
    # 蓄能水罐剩余蓄冷蓄热能量
    # 蓄能水罐制冷制热成本
    # 蓄能蓄能功率占比（蓄能装置蓄冷占总出力的比例）
    # 蓄能供能功率占比（蓄能装置供能占总出力的比例）

    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ese_cold_heat_out', 'ese_residual_storage_energy', 'ese_cost', 'ese_proportion_in', 'ese_proportion_out'],
        [ese_cold_heat_out, ese_residual_storage_energy, ese_cost, ese_proportion_in*100, ese_proportion_out*100])

    # 报错
    if state1 == False:
        print("蓄能水罐写入数据库出错！")


def write_to_database_ese1(syncbase, ese1_interlock_stop, ese1_remote_stop, ese1_remote_start, ese1_wp_water_frequency,
                           ese1_chilled_heat_water_flow, ese1_wp_power_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置水泵1的数据

    # 批量写入数据到数据库
    # #1蓄能水罐水泵停机指令
    # #1蓄能水罐水泵远方停机指令
    # #1蓄能水罐水泵远方开机指令
    # #1蓄能水罐水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ese1_interlock_stop', 'ese1_remote_stop', 'ese1_remote_start', 'ese1_wp_water_frequency'],
        [ese1_interlock_stop, ese1_remote_stop, ese1_remote_start, ese1_wp_water_frequency])

    # 程序计算出的数据
    # #1蓄能水罐水泵冷热水流量
    # #1蓄能水罐水泵冷热水流量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese1_chilled_heat_water_flow', 'ese1_wp_power_consumption'],
        [ese1_chilled_heat_water_flow, ese1_wp_power_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("蓄能水罐水泵1写入数据库出错！")


def write_to_database_ese2(syncbase, ese2_interlock_stop, ese2_remote_stop, ese2_remote_start, ese2_wp_water_frequency,
                           ese2_chilled_heat_water_flow, ese2_wp_power_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置水泵2的数据

    # 批量写入数据到数据库
    # #2蓄能水罐水泵停机指令
    # #2蓄能水罐水泵远方停机指令
    # #2蓄能水罐水泵远方开机指令
    # #2蓄能水罐水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ese2_interlock_stop', 'ese2_remote_stop', 'ese2_remote_start', 'ese2_wp_water_frequency'],
        [ese2_interlock_stop, ese2_remote_stop, ese2_remote_start, ese2_wp_water_frequency])

    # 程序计算出的数据
    # #2蓄能水罐水泵冷热水流量
    # #2蓄能水罐水泵冷热水流量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese2_chilled_heat_water_flow', 'ese2_wp_power_consumption'],
        [ese2_chilled_heat_water_flow, ese2_wp_power_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("蓄能水罐水泵2写入数据库出错！")


def write_to_database_ese3(syncbase, ese3_interlock_stop, ese3_remote_stop, ese3_remote_start, ese3_wp_water_frequency,
                           ese3_chilled_heat_water_flow, ese3_wp_power_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置水泵3的数据

    # 批量写入数据到数据库
    # #3蓄能水罐水泵停机指令
    # #3蓄能水罐水泵远方停机指令
    # #3蓄能水罐水泵远方开机指令
    # #3蓄能水罐水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ese3_interlock_stop', 'ese3_remote_stop', 'ese3_remote_start', 'ese3_wp_water_frequency'],
        [ese3_interlock_stop, ese3_remote_stop, ese3_remote_start, ese3_wp_water_frequency])

    # 程序计算出的数据
    # #3蓄能水罐水泵冷热水流量
    # #3蓄能水罐水泵冷热水流量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese3_chilled_heat_water_flow', 'ese3_wp_power_consumption'],
        [ese3_chilled_heat_water_flow, ese3_wp_power_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("蓄能水罐水泵3写入数据库出错！")


def write_to_database_ese4(syncbase, ese4_interlock_stop, ese4_remote_stop, ese4_remote_start, ese4_wp_water_frequency,
                           ese4_chilled_heat_water_flow, ese4_wp_power_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置水泵4的数据

    # 批量写入数据到数据库
    # #4蓄能水罐水泵停机指令
    # #4蓄能水罐水泵远方停机指令
    # #4蓄能水罐水泵远方开机指令
    # #4蓄能水罐水泵频率
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ese4_interlock_stop', 'ese4_remote_stop', 'ese4_remote_start', 'ese4_wp_water_frequency'],
        [ese4_interlock_stop, ese4_remote_stop, ese4_remote_start, ese4_wp_water_frequency])

    # 程序计算出的数据
    # #4蓄能水罐水泵冷热水流量
    # #4蓄能水罐水泵冷热水流量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese4_chilled_heat_water_flow', 'ese4_wp_power_consumption'],
        [ese4_chilled_heat_water_flow, ese4_wp_power_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("蓄能水罐水泵4写入数据库出错！")


def write_to_database_ngb1(syncbase, ngb1_remote_start, ngb1_remote_stop, ngb1_wp_heat_water_frequency,
                           ngb1_heat_out, ngb1_power_consumption, ngb1_heat_water_flow, ngb1_wp_heat_water_power_consumption,
                           ngb1_efficiency, ngb1_income, ngb1_cost, ngb1_natural_gas_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉1的数据

    # 批量写入数据到数据库
    # 1#燃气真空热水炉远程启动指令
    # 1#燃气真空热水炉远程停止指令
    # 1#燃气真空热水炉采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ngb1_remote_start', 'ngb1_remote_stop', 'ngb1_wp_heat_water_frequency'],
        [ngb1_remote_start, ngb1_remote_stop, ngb1_wp_heat_water_frequency])

    # 程序计算出的数据
    # #1燃气真空热水炉供热功率
    # #1燃气真空热水炉耗电功率
    # #1燃气真空热水炉采暖水流量
    # #1燃气真空热水炉采暖水泵电功率
    # #1燃气真空热水炉制热效率
    # #1燃气真空热水炉制热收入
    # #1燃气真空热水炉制热成本
    # #1燃气真空热水炉天然气耗量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb1_heat_out', 'ngb1_power_consumption', 'ngb1_heat_water_flow', 'ngb1_wp_heat_water_power_consumption',
         'ngb1_efficiency',' ngb1_income', 'ngb1_cost', 'ngb1_natural_gas_consumption'],
        [ngb1_heat_out, ngb1_power_consumption, ngb1_heat_water_flow, ngb1_wp_heat_water_power_consumption,
         ngb1_efficiency*100, ngb1_income, ngb1_cost, ngb1_natural_gas_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("天然气热水锅炉1写入数据库出错！")


def write_to_database_ngb2(syncbase, ngb2_remote_start, ngb2_remote_stop, ngb2_wp_heat_water_frequency,
                           ngb2_heat_out, ngb2_power_consumption, ngb2_heat_water_flow,
                           ngb2_wp_heat_water_power_consumption,
                           ngb2_efficiency, ngb2_income, ngb2_cost, ngb2_natural_gas_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉2的数据

    # 批量写入数据到数据库
    # 2#燃气真空热水炉远程启动指令
    # 2#燃气真空热水炉远程停止指令
    # 2#燃气真空热水炉采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ngb2_remote_start', 'ngb2_remote_stop', 'ngb2_wp_heat_water_frequency'],
        [ngb2_remote_start, ngb2_remote_stop, ngb2_wp_heat_water_frequency])

    # 程序计算出的数据
    # #2燃气真空热水炉供热功率
    # #2燃气真空热水炉耗电功率
    # #2燃气真空热水炉采暖水流量
    # #2燃气真空热水炉采暖水泵电功率
    # #2燃气真空热水炉制热效率
    # #2燃气真空热水炉制热收入
    # #2燃气真空热水炉制热成本
    # #2燃气真空热水炉天然气耗量
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb2_heat_out', 'ngb2_power_consumption', 'ngb2_heat_water_flow', 'ngb2_wp_heat_water_power_consumption',
         'ngb2_efficiency', 'ngb2_income', 'ngb2_cost', 'ngb2_natural_gas_consumption'],
        [ngb2_heat_out, ngb2_power_consumption, ngb2_heat_water_flow, ngb2_wp_heat_water_power_consumption,
         ngb2_efficiency*100, ngb2_income, ngb2_cost, ngb2_natural_gas_consumption])

    # 报错
    if (state1 == False or state2 == False):
        print("天然气热水锅炉2写入数据库出错！")


def write_to_database_ngb3(syncbase, ngb3_remote_start, ngb3_remote_stop, ngb3_wp_hot_water_frequency,
                           ngb3_hot_water_out, ngb3_power_consumption, ngb3_hot_water_flow,
                           ngb3_wp_hot_water_power_consumption,
                           ngb3_efficiency, ngb3_income, ngb3_cost, ngb3_natural_gas_consumption):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉3的数据

    # 批量写入数据到数据库
    # 3#燃气真空热水炉远程启动指令
    # 3#燃气真空热水炉远程停止指令
    # 3#燃气真空热水炉生活热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['ngb3_remote_start', 'ngb3_remote_stop', 'ngb3_wp_hot_water_frequency'],
        [ngb3_remote_start, ngb3_remote_stop, ngb3_wp_hot_water_frequency])

    # 程序计算出的数据
    # #3燃气真空热水炉供热功率
    # #3燃气真空热水炉耗电功率
    # #3燃气真空热水炉采暖水流量
    # #3燃气真空热水炉采暖水泵电功率
    # #3燃气真空热水炉制热效率
    # #3燃气真空热水炉制热收入
    # #3燃气真空热水炉制热成本
    # #3燃气真空热水炉天然气耗量
    state3 = syncbase.write_batch_realtime_data_by_name(
        ['ngb3_hot_water_out', 'ngb3_power_consumption', 'ngb3_hot_water_flow', 'ngb3_wp_hot_water_power_consumption',
         'ngb3_efficiency', 'ngb3_income', 'ngb3_cost', 'ngb3_natural_gas_consumption'],
        [ngb3_hot_water_out, ngb3_power_consumption, ngb3_hot_water_flow, ngb3_wp_hot_water_power_consumption,
         ngb3_efficiency*100, ngb3_income, ngb3_cost, ngb3_natural_gas_consumption])

    # 报错
    if (state1 == False or state3 == False):
        print("天然气热水锅炉3写入数据库出错！")


def write_to_database_prediction(syncbase, cold_prediction, heat_prediction, hot_water_prediction, electricity_prediction):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入负荷预测数据结果

    # 冷热负荷预测值
    # 热水负荷预测值
    # 电负荷预测值
    state1 = syncbase.write_batch_realtime_data_by_name(['cold_prediction', 'heat_prediction', 'hot_water_prediction', 'electricity_prediction'],
                                                        [cold_prediction, heat_prediction, hot_water_prediction, electricity_prediction])
    # 报错
    if state1 == False:
        print("负荷预测数据写入数据库错误！")


def write_to_database_system_utility(syncbase, cost_total, income_total, profit_total, electricity_out_total, cold_heat_out_total, hot_water_out_total,
                                     natural_gas_consume_total, electricity_consume_total, comprehensive_energy_utilization, proportion_of_renewable_energy_power,
                                     cop_real_time, reduction_in_carbon_emissions, reduction_in_sulfide_emissions, reduction_in_nitride_emissions,
                                     reduction_in_dust_emissions):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入系统公用数据

    # 总成本
    # 总收入
    # 总利润
    # 供电总功率
    # 供冷供热总功率
    # 供热水总功率
    # 天然气总耗量
    # 能源站设备耗电总功率
    # 能源系统综合效率
    # 可再生能源发电占比
    # 空调系统实时能效比
    # 碳排放减少量
    # 硫化物排放减少量
    # 氮化物排放减少量
    # 粉尘排放减少量
    state1 = syncbase.write_batch_realtime_data_by_name(
        ['cost_total', 'income_total', 'profit_total', 'electricity_out_total', 'cold_heat_out_total', 'hot_water_out_total', 'natural_gas_consume_total',
         'electricity_consume_total', 'comprehensive_energy_utilization', 'proportion_of_renewable_energy_power', 'cop_real_time',
         'reduction_in_carbon_emissions', 'reduction_in_sulfide_emissions', 'reduction_in_nitride_emissions', 'reduction_in_dust_emissions'],
        [cost_total, income_total, profit_total, electricity_out_total, cold_heat_out_total, hot_water_out_total, natural_gas_consume_total, electricity_consume_total,
         comprehensive_energy_utilization*100, proportion_of_renewable_energy_power*100, cop_real_time, reduction_in_carbon_emissions, reduction_in_sulfide_emissions,
         reduction_in_nitride_emissions, reduction_in_dust_emissions])

    # 报错
    if state1 == False:
        print("系统通用数据写入数据库错误！")


def write_to_database_station_in_out(syncbase, cold_out_total, heat_out_total, electricity_generation_total, lb_cold_out_total, lb_heat_out_total, lb_hot_water_out_total,
                                     cc_cold_out_total, chp_cold_out_total, chp_heat_out_total, ashp_cold_out_total, ese_cold_out_total, ese_heat_out_total,
                                     ice_electricity_out_total, photovoltaic_electricity_out_total, wind_electricity_out_total, accumulator_electricity_out_total,
                                     buy_electricity_total, ngb_hot_water_out_total):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入能源站冷热电的输入输出功率数据

    # 供冷总功率
    # 供热总功率
    # 发电总功率
    # 溴化锂供冷总出力
    # 溴化锂供热总出力
    # 溴化锂供热水总出力
    # 离心式冷水机供冷总出力
    # 离心式热泵供冷总出力
    # 离心式热泵供热总出力
    # 空气源热泵供冷总出力
    # 蓄能水罐供冷总出力
    # 蓄能水罐供热总出力
    # 内燃机发电总功率
    # 光伏发电总功率
    # 风电发电总功率
    # 蓄电池供电总功率
    # 外购电总功率
    # 天然气锅炉供热水总功率
    state1 = syncbase.write_batch_realtime_data_by_name(
              ['cold_out_total', 'heat_out_total', 'electricity_generation_total', 'lb_cold_out_total', 'lb_heat_out_total',  'lb_hot_water_out_total', 'cc_cold_out_total',
              'chp_cold_out_total', 'chp_heat_out_total', 'ashp_cold_out_total', 'ese_cold_out_total', 'ese_heat_out_total', 'ice_electricity_out_total',
              'photovoltaic_electricity_out_total', 'wind_electricity_out_total', 'accumulator_electricity_out_total', 'buy_electricity_total', 'ngb_hot_water_out_total'],
             [cold_out_total, heat_out_total, electricity_generation_total, lb_cold_out_total, lb_heat_out_total, lb_hot_water_out_total, cc_cold_out_total,
              chp_cold_out_total, chp_heat_out_total, ashp_cold_out_total, ese_cold_out_total, ese_heat_out_total, ice_electricity_out_total,
              photovoltaic_electricity_out_total, wind_electricity_out_total, accumulator_electricity_out_total, buy_electricity_total, ngb_hot_water_out_total])

    # 报错
    if state1 == False:
        print("能源站冷热电的输入输出功率数据写入数据库错误！")


def write_to_database_income_cost(syncbase, ice_income_total, lb_cold_income_total, lb_heat_income_total, lb_hot_water_income_total, cc_cold_income_total,
                                  chp_cold_income_total, chp_heat_income_total, ashp_cold_income_total, ngb_hot_water_income_total,
                                  photovoltaic_income_total, wind_income_total, ice_cost_total, lb_cold_cost_total, lb_heat_cost_total,
                                  lb_hot_water_cost_total, cc_cold_cost_total, chp_cold_cost_total, chp_heat_cost_total,
                                  ashp_cold_cost_total, ashp_heat_cost_total, ngb_hot_water_cost_total):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入能源站冷热电的收入成本数据

    # 内燃机发电总收入
    # 溴化锂制冷总收入
    # 溴化锂制热总收入
    # 溴化锂生活热水总收入
    # 离心式冷水机制冷总收入
    # 离心式热泵制冷总收入
    # 离心式热泵制热总收入
    # 空气源热泵制冷总收入
    # 天然气锅炉生活热水总收入
    # 光伏发电总收入
    # 风力发电总收入
    # 内燃机发电总成本
    # 溴化锂制冷总成本
    # 溴化锂制热总成本
    # 溴化锂生活热水总成本
    # 离心式冷水机制冷总成本
    # 离心式热泵制冷总成本
    # 离心式热泵制热总成本
    # 空气源热泵制冷总成本
    # 空气源热泵制热总成本
    # 天然气锅炉生活热水总成本
    state1 = syncbase.write_batch_realtime_data_by_name(
            ['ice_income_total', 'lb_cold_income_total', 'lb_heat_income_total', 'lb_hot_water_income_total', 'cc_cold_income_total', 'chp_cold_income_total',
             'chp_heat_income_total', 'ashp_cold_income_total', 'ngb_hot_water_income_total', 'photovoltaic_income_total', 'wind_income_total', 'ice_cost_total',
             'lb_cold_cost_total', 'lb_heat_cost_total', 'lb_hot_water_cost_total', 'cc_cold_cost_total', 'chp_cold_cost_total', 'chp_heat_cost_total',
             'ashp_cold_cost_total', 'ashp_heat_cost_total', 'ngb_hot_water_cost_total'],
            [ice_income_total, lb_cold_income_total, lb_heat_income_total, lb_hot_water_income_total, cc_cold_income_total, chp_cold_income_total,
             chp_heat_income_total, ashp_cold_income_total, ngb_hot_water_income_total, photovoltaic_income_total, wind_income_total, ice_cost_total,
             lb_cold_cost_total, lb_heat_cost_total, lb_hot_water_cost_total, cc_cold_cost_total, chp_cold_cost_total, chp_heat_cost_total,
             ashp_cold_cost_total, ashp_heat_cost_total, ngb_hot_water_cost_total])

    # 报错
    if state1 == False:
        print("能源站冷热电的收入成本数据写入数据库错误！")


def write_to_database_equipment_efficiency(syncbase, ice_electrical_efficiency, lb_cold_efficiency, lb_heat_efficiency, lb_hot_water_efficiency,
                                           cc_cold_cop, chp_cold_cop, chp_heat_cop, ashp_cold_cop, ashp_heat_cop,
                                           ngb_hot_water_efficiency, photovoltaic_electrical_efficiency, wind_electrical_efficiency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入设备效率数据

    # 内燃机发电效率
    # 溴化锂制冷效率
    # 溴化锂制热效率
    # 溴化锂生活热水效率
    # 离心式冷水机制冷COP
    # 离心式热泵制冷COP
    # 离心式热泵制热COP
    # 空气源热泵制冷COP
    # 空气源热泵制热COP
    # 天然气锅炉生活热水效率
    # 光伏发电效率
    # 风力发电效率
    state1 = syncbase.write_batch_realtime_data_by_name(
            ['ice_electrical_efficiency', 'lb_cold_efficiency', 'lb_heat_efficiency', 'lb_hot_water_efficiency', 'cc_cold_cop',
             'chp_cold_cop', 'chp_heat_cop', 'ashp_cold_cop', 'ashp_heat_cop', 'ngb_hot_water_efficiency',
             'photovoltaic_electrical_efficiency', 'wind_electrical_efficiency'],
            [ice_electrical_efficiency*100, lb_cold_efficiency*100, lb_heat_efficiency*100, lb_hot_water_efficiency*100, cc_cold_cop,
             chp_cold_cop, chp_heat_cop, ashp_cold_cop, ashp_heat_cop, ngb_hot_water_efficiency*100,
             photovoltaic_electrical_efficiency*100, wind_electrical_efficiency*100])

    # 报错
    if state1 == False:
        print("设备效率数据写入数据库错误！")

def write_to_database_temperature_flow(syncbase, chilled_water_supply_flow_total, chilled_water_supply_temperature, chilled_water_return_temperature,
                                       heat_water_supply_flow_total, heat_water_supply_temperature, heat_water_return_temperature,
                                       hot_water_supply_flow_total, hot_water_supply_temperature, hot_water_return_temperature,
                                       lb1_heat_chilled_water_supply_temperature, lb1_hot_water_supply_temperature, lb2_heat_chilled_water_supply_temperature,
                                       lb2_hot_water_supply_temperature, ngb3_hot_water_supply_temperature, cc1_chilled_water_supply_temperature,
                                       cc2_chilled_water_supply_temperature, cc3_chilled_water_supply_temperature, cc4_chilled_water_supply_temperature,
                                       chp1_heat_water_supply_temperature, chp2_heat_water_supply_temperature, ashp1_water_supply_temperature,
                                       ashp2_water_supply_temperature, ashp3_water_supply_temperature, ashp4_water_supply_temperature, ese_water_supply_temperature):

    """利用SyncBASE，向数据库中写入数据"""
    # 写入冷热水温度和水流量数据

    # 冷冻水供水母管流量
    # 冷冻水供水母管温度
    # 冷冻水回水母管温度
    # 采暖水供水母管流量
    # 采暖水供水母管温度
    # 采暖水回水母管温度
    # 生活热水供水母管流量
    # 生活热水供水母管温度
    # 生活热水回水母管温度"
    # #1溴化锂冷/热水温度
    # #1溴化锂生活热水温度
    # #2溴化锂冷/热水温度
    # #2溴化锂生活热水温度
    # 天然气热水锅炉生活热水温
    # #1离心式冷水机组供水温度
    # #2离心式冷水机组供水温度
    # #3离心式冷水机组供水温度(#1离心式热泵制冷出水温度）
    # #4离心式冷水机组供水温度(#2离心式热泵制冷出水温度）
    # #1离心式热泵组供水温度
    # #1离心式热泵组供水温度
    # #1空气源热泵供水温度
    # #2空气源热泵供水温度
    # #3空气源热泵供水温度
    # #4空气源热泵供水温度
    # 蓄能水罐供水母管温度

    state1 = syncbase.write_batch_realtime_data_by_name(
             ['chilled_water_supply_flow_total', 'chilled_water_supply_temperature', 'chilled_water_return_temperature',
             'heat_water_supply_flow_total', 'heat_water_supply_temperature', 'heat_water_return_temperature',
             'hot_water_supply_flow_total', 'hot_water_supply_temperature', 'hot_water_return_temperature',
             'lb1_heat_chilled_water_supply_temperature', 'lb1_hot_water_supply_temperature', 'lb2_heat_chilled_water_supply_temperature',
             'lb2_hot_water_supply_temperature', 'ngb3_hot_water_supply_temperature', 'cc1_chilled_water_supply_temperature',
             'cc2_chilled_water_supply_temperature', 'cc3_chilled_water_supply_temperature', 'cc4_chilled_water_supply_temperature',
             'chp1_heat_water_supply_temperature', 'chp2_heat_water_supply_temperature', 'ashp1_water_supply_temperature',
             'ashp2_water_supply_temperature', 'ashp3_water_supply_temperature', 'ashp4_water_supply_temperature', 'ese_water_supply_temperature'],
             [chilled_water_supply_flow_total, chilled_water_supply_temperature, chilled_water_return_temperature,
             heat_water_supply_flow_total,heat_water_supply_temperature, heat_water_return_temperature,
             hot_water_supply_flow_total, hot_water_supply_temperature, hot_water_return_temperature,
             lb1_heat_chilled_water_supply_temperature, lb1_hot_water_supply_temperature, lb2_heat_chilled_water_supply_temperature,
             lb2_hot_water_supply_temperature, ngb3_hot_water_supply_temperature, cc1_chilled_water_supply_temperature,
             cc2_chilled_water_supply_temperature, cc3_chilled_water_supply_temperature, cc4_chilled_water_supply_temperature,
             chp1_heat_water_supply_temperature, chp2_heat_water_supply_temperature, ashp1_water_supply_temperature,
             ashp2_water_supply_temperature, ashp3_water_supply_temperature, ashp4_water_supply_temperature, ese_water_supply_temperature])

    # 报错
    if state1 == False:
        print("温度和流量数据写入数据库错误！")

def write_to_database_equipment_state(syncbase, ice1_start_state, ice1_stop_state, ice1_fault_state, ice2_start_state, ice2_stop_state, ice2_fault_state,
                                      lb1_cold_state, lb1_heat_state, lb1_hot_water_state, lb1_stop_state, lb1_fault_state, lb2_cold_state,
                                      lb2_heat_state, lb2_hot_water_state, lb2_stop_state, lb2_fault_state, cc1_cold_state, cc1_stop_state, cc1_fault_state,
                                      cc2_cold_state, cc2_stop_state, cc2_fault_state, chp1_cold_state, chp1_heat_state, chp1_stop_state, chp1_fault_state,
                                      chp2_cold_state, chp2_heat_state, chp2_stop_state, chp2_fault_state, ashp1_cold_state, ashp1_heat_state, ashp1_stop_state,
                                      ashp1_fault_state, ashp2_cold_state, ashp2_heat_state, ashp2_stop_state, ashp2_fault_state, ashp3_cold_state,
                                      ashp3_heat_state, ashp3_stop_state, ashp3_fault_state, ashp4_cold_state, ashp4_heat_state, ashp4_stop_state, ashp4_fault_state,
                                      ese_cold_out_state, ese_heat_out_state, ese_cold_in_state, ese_heat_in_state, ese_stop_state, ese_fault_state,
                                      ngb_hot_water_state, ngb_stop_state, ngb_fault_state, photovoltaic_start_state, photovoltaic_stop_state, photovoltaic_fault_state,
                                      wind_start_state, wind_stop_state, wind_fault_state, cdz_start_state, cdz_stop_state, cdz_fault_state,
                                      accumulator_electricity_out_state, accumulator_electricity_in_state, accumulator_stop_state, accumulator_fault_state,
                                      lamp_start_state, lamp_stop_state, lamp_fault_state):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入设备的运行状态

    # #1内燃机远程启动状态
    # #1内燃机远程停机状态
    # #1内燃机故障状态
    # #2内燃机远程启动状态
    # #2内燃机远程停机状态
    # #2内燃机故障状态
    # #1溴化锂制冷状态
    # #1溴化锂制热状态
    # #1溴化锂制热水状态
    # #1溴化锂停机状态
    # #1溴化锂故障状态
    # #2溴化锂制冷状态
    # #2溴化锂制热状态
    # #2溴化锂制热水状态
    # #2溴化锂停机状态
    # #2溴化锂故障状态
    # #1离心式冷水机制冷状态
    # #1离心式冷水机停机状态
    # #1离心式冷水机故障状态
    # #2离心式冷水机制冷状态
    # #2离心式冷水机停机状态
    # #2离心式冷水机故障状态
    # #1离心式热泵制冷状态
    # #1离心式热泵制热状态
    # #1离心式热泵停机状态
    # #1离心式热泵故障状态
    # #2离心式热泵制冷状态
    # #2离心式热泵制热状态
    # #2离心式热泵停机状态
    # #2离心式热泵故障状态
    # #1空气源热泵制冷状态
    # #1空气源热泵制热状态
    # #1空气源热泵停机状态
    # #1空气源热泵故障状态
    # #2空气源热泵制冷状态
    # #2空气源热泵制热状态
    # #2空气源热泵停机状态
    # #2空气源热泵故障状态
    # #3空气源热泵制冷状态
    # #3空气源热泵制热状态
    # #3空气源热泵停机状态
    # #3空气源热泵故障状态
    # #4空气源热泵制冷状态
    # #4空气源热泵制热状态
    # #4空气源热泵停机状态
    # #4空气源热泵故障状态
    # 蓄能水罐制冷状态
    # 蓄能水罐制热状态
    # 蓄能水罐蓄冷状态
    # 蓄能水罐蓄热状态
    # 蓄能水罐停机状态
    # 蓄能水罐故障状态
    # 天然气锅炉制热水状态
    # 天然气锅炉停机状态
    # 天然气锅炉故障状态
    # 光伏发电状态
    # 光伏停机状态
    # 光伏故障状态
    # 风电发电状态
    # 风电停机状态
    # 风电故障状态
    # 充电桩发电状态
    # 充电桩停机状态
    # 充电桩故障状态
    # 蓄电池充电状态
    # 蓄电池供电状态
    # 蓄电池停机状态
    # 蓄电池故障状态
    # 智慧路灯运行状态
    # 智慧路灯停机状态
    # 智慧路灯故障状态

    state1 = syncbase.write_batch_realtime_data_by_name(['ice1_start_state', 'ice1_stop_state', 'ice1_fault_state', 'ice2_start_state', 'ice2_stop_state', 'ice2_fault_state', 'lb1_cold_state', 'lb1_heat_state',
         'lb1_hot_water_state', 'lb1_stop_state', 'lb1_fault_state', 'lb2_cold_state', 'lb2_heat_state', 'lb2_hot_water_state', 'lb2_stop_state', 'lb2_fault_state',
         'cc1_cold_state', 'cc1_stop_state', 'cc1_fault_state', 'cc2_cold_state', 'cc2_stop_state', 'cc2_fault_state', 'chp1_cold_state', 'chp1_heat_state', 'chp1_stop_state',
         'chp1_fault_state', 'chp2_cold_state', 'chp2_heat_state', 'chp2_stop_state', 'chp2_fault_state', 'ashp1_cold_state', 'ashp1_heat_state', 'ashp1_stop_state',
         'ashp1_fault_state', 'ashp2_cold_state', 'ashp2_heat_state', 'ashp2_stop_state', 'ashp2_fault_state', 'ashp3_cold_state', 'ashp3_heat_state', 'ashp3_stop_state',
         'ashp3_fault_state', 'ashp4_cold_state', 'ashp4_heat_state', 'ashp4_stop_state', 'ashp4_fault_state', 'ese_cold_out_state', 'ese_heat_out_state', 'ese_cold_in_state',
         'ese_heat_in_state', 'ese_stop_state', 'ese_fault_state', 'ngb_hot_water_state', 'ngb_stop_state', 'ngb_fault_state', 'photovoltaic_start_state', 'photovoltaic_stop_state',
         'photovoltaic_fault_state', 'wind_start_state', 'wind_stop_state', 'wind_fault_state', 'cdz_start_state', 'cdz_stop_state', 'cdz_fault_state', 'accumulator_electricity_out_state',
         'accumulator_electricity_in_state', 'accumulator_stop_state', 'accumulator_fault_state', 'lamp_start_state', 'lamp_stop_state', 'lamp_fault_state'],
        [ice1_start_state, ice1_stop_state, ice1_fault_state, ice2_start_state, ice2_stop_state, ice2_fault_state, lb1_cold_state, lb1_heat_state,
         lb1_hot_water_state, lb1_stop_state, lb1_fault_state, lb2_cold_state, lb2_heat_state, lb2_hot_water_state, lb2_stop_state, lb2_fault_state,
         cc1_cold_state, cc1_stop_state, cc1_fault_state, cc2_cold_state, cc2_stop_state, cc2_fault_state, chp1_cold_state, chp1_heat_state, chp1_stop_state,
         chp1_fault_state, chp2_cold_state, chp2_heat_state, chp2_stop_state, chp2_fault_state, ashp1_cold_state, ashp1_heat_state, ashp1_stop_state,
         ashp1_fault_state, ashp2_cold_state, ashp2_heat_state, ashp2_stop_state, ashp2_fault_state, ashp3_cold_state, ashp3_heat_state, ashp3_stop_state,
         ashp3_fault_state, ashp4_cold_state, ashp4_heat_state, ashp4_stop_state, ashp4_fault_state, ese_cold_out_state, ese_heat_out_state, ese_cold_in_state,
         ese_heat_in_state, ese_stop_state, ese_fault_state, ngb_hot_water_state, ngb_stop_state, ngb_fault_state, photovoltaic_start_state, photovoltaic_stop_state,
         photovoltaic_fault_state, wind_start_state, wind_stop_state, wind_fault_state, cdz_start_state, cdz_stop_state, cdz_fault_state, accumulator_electricity_out_state,
         accumulator_electricity_in_state, accumulator_stop_state, accumulator_fault_state, lamp_start_state, lamp_stop_state, lamp_fault_state]
        )

    # 报错
    if state1 == False:
        print("设备运行状态写入数据库错误！")


def _print(records):
    ans = []
    if isinstance(records, dict):
        records = records.values()
    for record in records:
        if isinstance(record, (list, dict)):
            _print(record)
        else:
            ans.append(record.value)
    # 返回结果
    return ans


def write_to_database_cold_prediction_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入冷负荷预测24小时折线图的值

    # 获取当前的时间
    now_year = now.year # 当前的年
    now_month = now.month # 当前的月
    now_day = now.day # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute # 当前的分钟
    now_second = now.second # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cold_prediction',
                                                       dt(now_year, now_month, now_day, 0, 0, 0),
                                                       dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                       period)
    if state1 == False:
        print("从数据库读取冷热负荷预测历史数据错误！")

    cold_prediction_0 = _print(records1)[0]
    cold_prediction_1 = _print(records1)[1]
    cold_prediction_2 = _print(records1)[2]
    cold_prediction_3 = _print(records1)[3]
    cold_prediction_4 = _print(records1)[4]
    cold_prediction_5 = _print(records1)[5]
    cold_prediction_6 = _print(records1)[6]
    cold_prediction_7 = _print(records1)[7]
    cold_prediction_8 = _print(records1)[8]
    cold_prediction_9 = _print(records1)[9]
    cold_prediction_10 = _print(records1)[10]
    cold_prediction_11 = _print(records1)[11]
    cold_prediction_12 = _print(records1)[12]
    cold_prediction_13 = _print(records1)[13]
    cold_prediction_14 = _print(records1)[14]
    cold_prediction_15 = _print(records1)[15]
    cold_prediction_16 = _print(records1)[16]
    cold_prediction_17 = _print(records1)[17]
    cold_prediction_18 = _print(records1)[18]
    cold_prediction_19 = _print(records1)[19]
    cold_prediction_20 = _print(records1)[20]
    cold_prediction_21 = _print(records1)[21]
    cold_prediction_22 = _print(records1)[22]
    cold_prediction_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cold_prediction_0', 'cold_prediction_1', 'cold_prediction_2', 'cold_prediction_3', 'cold_prediction_4',
         'cold_prediction_5', 'cold_prediction_6', 'cold_prediction_7', 'cold_prediction_8', 'cold_prediction_9',
         'cold_prediction_10', 'cold_prediction_11', 'cold_prediction_12', 'cold_prediction_13', 'cold_prediction_14',
         'cold_prediction_15', 'cold_prediction_16', 'cold_prediction_17', 'cold_prediction_18', 'cold_prediction_19',
         'cold_prediction_20', 'cold_prediction_21', 'cold_prediction_22', 'cold_prediction_23'],
        [cold_prediction_0, cold_prediction_1, cold_prediction_2, cold_prediction_3, cold_prediction_4,
         cold_prediction_5, cold_prediction_6, cold_prediction_7, cold_prediction_8, cold_prediction_9,
         cold_prediction_10, cold_prediction_11, cold_prediction_12, cold_prediction_13, cold_prediction_14,
         cold_prediction_15, cold_prediction_16, cold_prediction_17, cold_prediction_18, cold_prediction_19,
         cold_prediction_20, cold_prediction_21, cold_prediction_22, cold_prediction_23])
    # 报错
    if state2 == False:
        print("24小时冷热负荷预测数据写入数据库错误！")


def write_to_database_cold_actual_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入冷负荷实际值24小时折线图的值

    # 获取当前的时间
    now_year = now.year # 当前的年
    now_month = now.month # 当前的月
    now_day = now.day # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute # 当前的分钟
    now_second = now.second # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cold_out_total',
                                                       dt(now_year, now_month, now_day, 0, 0, 0),
                                                       dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                       period)
    if state1 == False:
        print("从数据库读取冷负荷实际值历史数据错误！")

    cold_actual_0 = _print(records1)[0]
    cold_actual_1 = _print(records1)[1]
    cold_actual_2 = _print(records1)[2]
    cold_actual_3 = _print(records1)[3]
    cold_actual_4 = _print(records1)[4]
    cold_actual_5 = _print(records1)[5]
    cold_actual_6 = _print(records1)[6]
    cold_actual_7 = _print(records1)[7]
    cold_actual_8 = _print(records1)[8]
    cold_actual_9 = _print(records1)[9]
    cold_actual_10 = _print(records1)[10]
    cold_actual_11 = _print(records1)[11]
    cold_actual_12 = _print(records1)[12]
    cold_actual_13 = _print(records1)[13]
    cold_actual_14 = _print(records1)[14]
    cold_actual_15 = _print(records1)[15]
    cold_actual_16 = _print(records1)[16]
    cold_actual_17 = _print(records1)[17]
    cold_actual_18 = _print(records1)[18]
    cold_actual_19 = _print(records1)[19]
    cold_actual_20 = _print(records1)[20]
    cold_actual_21 = _print(records1)[21]
    cold_actual_22 = _print(records1)[22]
    cold_actual_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cold_actual_0', 'cold_actual_1', 'cold_actual_2', 'cold_actual_3', 'cold_actual_4',
         'cold_actual_5', 'cold_actual_6', 'cold_actual_7', 'cold_actual_8', 'cold_actual_9',
         'cold_actual_10', 'cold_actual_11', 'cold_actual_12', 'cold_actual_13', 'cold_actual_14',
         'cold_actual_15', 'cold_actual_16', 'cold_actual_17', 'cold_actual_18', 'cold_actual_19',
         'cold_actual_20', 'cold_actual_21', 'cold_actual_22', 'cold_actual_23'],
        [cold_actual_0, cold_actual_1, cold_actual_2, cold_actual_3, cold_actual_4,
         cold_actual_5, cold_actual_6, cold_actual_7, cold_actual_8, cold_actual_9,
         cold_actual_10, cold_actual_11, cold_actual_12, cold_actual_13, cold_actual_14,
         cold_actual_15, cold_actual_16, cold_actual_17, cold_actual_18, cold_actual_19,
         cold_actual_20, cold_actual_21, cold_actual_22, cold_actual_23])
    # 报错
    if state2 == False:
        print("24小时冷负荷实际值数据写入数据库错误！")


def write_to_database_heat_prediction_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入热负荷预测24小时折线图的值

    # 获取当前的时间
    now_year = now.year # 当前的年
    now_month = now.month # 当前的月
    now_day = now.day # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute # 当前的分钟
    now_second = now.second # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('heat_prediction',
                                                       dt(now_year, now_month, now_day, 0, 0, 0),
                                                       dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                       period)
    if state1 == False:
        print("从数据库读取热热负荷预测历史数据错误！")

    heat_prediction_0 = _print(records1)[0]
    heat_prediction_1 = _print(records1)[1]
    heat_prediction_2 = _print(records1)[2]
    heat_prediction_3 = _print(records1)[3]
    heat_prediction_4 = _print(records1)[4]
    heat_prediction_5 = _print(records1)[5]
    heat_prediction_6 = _print(records1)[6]
    heat_prediction_7 = _print(records1)[7]
    heat_prediction_8 = _print(records1)[8]
    heat_prediction_9 = _print(records1)[9]
    heat_prediction_10 = _print(records1)[10]
    heat_prediction_11 = _print(records1)[11]
    heat_prediction_12 = _print(records1)[12]
    heat_prediction_13 = _print(records1)[13]
    heat_prediction_14 = _print(records1)[14]
    heat_prediction_15 = _print(records1)[15]
    heat_prediction_16 = _print(records1)[16]
    heat_prediction_17 = _print(records1)[17]
    heat_prediction_18 = _print(records1)[18]
    heat_prediction_19 = _print(records1)[19]
    heat_prediction_20 = _print(records1)[20]
    heat_prediction_21 = _print(records1)[21]
    heat_prediction_22 = _print(records1)[22]
    heat_prediction_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['heat_prediction_0', 'heat_prediction_1', 'heat_prediction_2', 'heat_prediction_3', 'heat_prediction_4',
         'heat_prediction_5', 'heat_prediction_6', 'heat_prediction_7', 'heat_prediction_8', 'heat_prediction_9',
         'heat_prediction_10', 'heat_prediction_11', 'heat_prediction_12', 'heat_prediction_13', 'heat_prediction_14',
         'heat_prediction_15', 'heat_prediction_16', 'heat_prediction_17', 'heat_prediction_18', 'heat_prediction_19',
         'heat_prediction_20', 'heat_prediction_21', 'heat_prediction_22', 'heat_prediction_23'],
        [heat_prediction_0, heat_prediction_1, heat_prediction_2, heat_prediction_3, heat_prediction_4,
         heat_prediction_5, heat_prediction_6, heat_prediction_7, heat_prediction_8, heat_prediction_9,
         heat_prediction_10, heat_prediction_11, heat_prediction_12, heat_prediction_13, heat_prediction_14,
         heat_prediction_15, heat_prediction_16, heat_prediction_17, heat_prediction_18, heat_prediction_19,
         heat_prediction_20, heat_prediction_21, heat_prediction_22, heat_prediction_23])
    # 报错
    if state2 == False:
        print("24小时热热负荷预测数据写入数据库错误！")


def write_to_database_heat_actual_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入热负荷实际值24小时折线图的值

    # 获取当前的时间
    now_year = now.year # 当前的年
    now_month = now.month # 当前的月
    now_day = now.day # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute # 当前的分钟
    now_second = now.second # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('heat_out_total',
                                                       dt(now_year, now_month, now_day, 0, 0, 0),
                                                       dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                       period)
    if state1 == False:
        print("从数据库读取热负荷实际值历史数据错误！")

    heat_actual_0 = _print(records1)[0]
    heat_actual_1 = _print(records1)[1]
    heat_actual_2 = _print(records1)[2]
    heat_actual_3 = _print(records1)[3]
    heat_actual_4 = _print(records1)[4]
    heat_actual_5 = _print(records1)[5]
    heat_actual_6 = _print(records1)[6]
    heat_actual_7 = _print(records1)[7]
    heat_actual_8 = _print(records1)[8]
    heat_actual_9 = _print(records1)[9]
    heat_actual_10 = _print(records1)[10]
    heat_actual_11 = _print(records1)[11]
    heat_actual_12 = _print(records1)[12]
    heat_actual_13 = _print(records1)[13]
    heat_actual_14 = _print(records1)[14]
    heat_actual_15 = _print(records1)[15]
    heat_actual_16 = _print(records1)[16]
    heat_actual_17 = _print(records1)[17]
    heat_actual_18 = _print(records1)[18]
    heat_actual_19 = _print(records1)[19]
    heat_actual_20 = _print(records1)[20]
    heat_actual_21 = _print(records1)[21]
    heat_actual_22 = _print(records1)[22]
    heat_actual_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['heat_actual_0', 'heat_actual_1', 'heat_actual_2', 'heat_actual_3', 'heat_actual_4',
         'heat_actual_5', 'heat_actual_6', 'heat_actual_7', 'heat_actual_8', 'heat_actual_9',
         'heat_actual_10', 'heat_actual_11', 'heat_actual_12', 'heat_actual_13', 'heat_actual_14',
         'heat_actual_15', 'heat_actual_16', 'heat_actual_17', 'heat_actual_18', 'heat_actual_19',
         'heat_actual_20', 'heat_actual_21', 'heat_actual_22', 'heat_actual_23'],
        [heat_actual_0, heat_actual_1, heat_actual_2, heat_actual_3, heat_actual_4,
         heat_actual_5, heat_actual_6, heat_actual_7, heat_actual_8, heat_actual_9,
         heat_actual_10, heat_actual_11, heat_actual_12, heat_actual_13, heat_actual_14,
         heat_actual_15, heat_actual_16, heat_actual_17, heat_actual_18, heat_actual_19,
         heat_actual_20, heat_actual_21, heat_actual_22, heat_actual_23])
    # 报错
    if state2 == False:
        print("24小时热负荷实际值数据写入数据库错误！")


def write_to_database_hot_water_prediction_actual_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入生活热水负荷预测和实际值24小时折线图的值

    # 生活热水负荷预测值和实际值一样

    # 获取当前的时间
    now_year = now.year # 当前的年
    now_month = now.month # 当前的月
    now_day = now.day # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute # 当前的分钟
    now_second = now.second # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('hot_water_prediction',
                                                       dt(now_year, now_month, now_day, 0, 0, 0),
                                                       dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                       period)
    if state1 == False:
        print("从数据库读取生活热水热负荷预测历史数据错误！")

    hot_water_prediction_0 = _print(records1)[0]
    hot_water_prediction_1 = _print(records1)[1]
    hot_water_prediction_2 = _print(records1)[2]
    hot_water_prediction_3 = _print(records1)[3]
    hot_water_prediction_4 = _print(records1)[4]
    hot_water_prediction_5 = _print(records1)[5]
    hot_water_prediction_6 = _print(records1)[6]
    hot_water_prediction_7 = _print(records1)[7]
    hot_water_prediction_8 = _print(records1)[8]
    hot_water_prediction_9 = _print(records1)[9]
    hot_water_prediction_10 = _print(records1)[10]
    hot_water_prediction_11 = _print(records1)[11]
    hot_water_prediction_12 = _print(records1)[12]
    hot_water_prediction_13 = _print(records1)[13]
    hot_water_prediction_14 = _print(records1)[14]
    hot_water_prediction_15 = _print(records1)[15]
    hot_water_prediction_16 = _print(records1)[16]
    hot_water_prediction_17 = _print(records1)[17]
    hot_water_prediction_18 = _print(records1)[18]
    hot_water_prediction_19 = _print(records1)[19]
    hot_water_prediction_20 = _print(records1)[20]
    hot_water_prediction_21 = _print(records1)[21]
    hot_water_prediction_22 = _print(records1)[22]
    hot_water_prediction_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['hot_water_prediction_0', 'hot_water_prediction_1', 'hot_water_prediction_2', 'hot_water_prediction_3', 'hot_water_prediction_4',
         'hot_water_prediction_5', 'hot_water_prediction_6', 'hot_water_prediction_7', 'hot_water_prediction_8', 'hot_water_prediction_9',
         'hot_water_prediction_10', 'hot_water_prediction_11', 'hot_water_prediction_12', 'hot_water_prediction_13', 'hot_water_prediction_14',
         'hot_water_prediction_15', 'hot_water_prediction_16', 'hot_water_prediction_17', 'hot_water_prediction_18', 'hot_water_prediction_19',
         'hot_water_prediction_20', 'hot_water_prediction_21', 'hot_water_prediction_22', 'hot_water_prediction_23'],
        [hot_water_prediction_0, hot_water_prediction_1, hot_water_prediction_2, hot_water_prediction_3, hot_water_prediction_4,
         hot_water_prediction_5, hot_water_prediction_6, hot_water_prediction_7, hot_water_prediction_8, hot_water_prediction_9,
         hot_water_prediction_10, hot_water_prediction_11, hot_water_prediction_12, hot_water_prediction_13, hot_water_prediction_14,
         hot_water_prediction_15, hot_water_prediction_16, hot_water_prediction_17, hot_water_prediction_18, hot_water_prediction_19,
         hot_water_prediction_20, hot_water_prediction_21, hot_water_prediction_22, hot_water_prediction_23])
    # 报错
    if state2 == False:
        print("24小时生活热水热负荷预测数据写入数据库错误！")

    hot_water_actual_0 = _print(records1)[0]
    hot_water_actual_1 = _print(records1)[1]
    hot_water_actual_2 = _print(records1)[2]
    hot_water_actual_3 = _print(records1)[3]
    hot_water_actual_4 = _print(records1)[4]
    hot_water_actual_5 = _print(records1)[5]
    hot_water_actual_6 = _print(records1)[6]
    hot_water_actual_7 = _print(records1)[7]
    hot_water_actual_8 = _print(records1)[8]
    hot_water_actual_9 = _print(records1)[9]
    hot_water_actual_10 = _print(records1)[10]
    hot_water_actual_11 = _print(records1)[11]
    hot_water_actual_12 = _print(records1)[12]
    hot_water_actual_13 = _print(records1)[13]
    hot_water_actual_14 = _print(records1)[14]
    hot_water_actual_15 = _print(records1)[15]
    hot_water_actual_16 = _print(records1)[16]
    hot_water_actual_17 = _print(records1)[17]
    hot_water_actual_18 = _print(records1)[18]
    hot_water_actual_19 = _print(records1)[19]
    hot_water_actual_20 = _print(records1)[20]
    hot_water_actual_21 = _print(records1)[21]
    hot_water_actual_22 = _print(records1)[22]
    hot_water_actual_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state3 = syncbase.write_batch_realtime_data_by_name(
        ['hot_water_actual_0', 'hot_water_actual_1', 'hot_water_actual_2', 'hot_water_actual_3', 'hot_water_actual_4',
         'hot_water_actual_5', 'hot_water_actual_6', 'hot_water_actual_7', 'hot_water_actual_8', 'hot_water_actual_9',
         'hot_water_actual_10', 'hot_water_actual_11', 'hot_water_actual_12', 'hot_water_actual_13', 'hot_water_actual_14',
         'hot_water_actual_15', 'hot_water_actual_16', 'hot_water_actual_17', 'hot_water_actual_18', 'hot_water_actual_19',
         'hot_water_actual_20', 'hot_water_actual_21', 'hot_water_actual_22', 'hot_water_actual_23'],
        [hot_water_actual_0, hot_water_actual_1, hot_water_actual_2, hot_water_actual_3, hot_water_actual_4,
         hot_water_actual_5, hot_water_actual_6, hot_water_actual_7, hot_water_actual_8, hot_water_actual_9,
         hot_water_actual_10, hot_water_actual_11, hot_water_actual_12, hot_water_actual_13, hot_water_actual_14,
         hot_water_actual_15, hot_water_actual_16, hot_water_actual_17, hot_water_actual_18, hot_water_actual_19,
         hot_water_actual_20, hot_water_actual_21, hot_water_actual_22, hot_water_actual_23])
    # 报错
    if state3 == False:
        print("24小时生活热水负荷实际值数据写入数据库错误！")


def write_to_database_ice_natural_gas_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机天然气耗量24小时的值

    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据（内燃机1）
    state1, records1 = syncbase.get_history_data_by_name('ice1_natural_gas_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    if state1 == False:
        print("从数据库读取内燃机1天然气耗量历史数据错误！")

    # 从数据库读取历史数据（内燃机2）
    state2, records2 = syncbase.get_history_data_by_name('ice2_natural_gas_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    if state2 == False:
        print("从数据库读取内燃机2天然气耗量历史数据错误！")

    ice_natural_gas_consumption_0 = _print(records1)[0] + _print(records2)[0]
    ice_natural_gas_consumption_1 = _print(records1)[1] + _print(records2)[1]
    ice_natural_gas_consumption_2 = _print(records1)[2] + _print(records2)[2]
    ice_natural_gas_consumption_3 = _print(records1)[3] + _print(records2)[3]
    ice_natural_gas_consumption_4 = _print(records1)[4] + _print(records2)[4]
    ice_natural_gas_consumption_5 = _print(records1)[5] + _print(records2)[5]
    ice_natural_gas_consumption_6 = _print(records1)[6] + _print(records2)[6]
    ice_natural_gas_consumption_7 = _print(records1)[7] + _print(records2)[7]
    ice_natural_gas_consumption_8 = _print(records1)[8] + _print(records2)[8]
    ice_natural_gas_consumption_9 = _print(records1)[9] + _print(records2)[9]
    ice_natural_gas_consumption_10 = _print(records1)[10] + _print(records2)[10]
    ice_natural_gas_consumption_11 = _print(records1)[11] + _print(records2)[11]
    ice_natural_gas_consumption_12 = _print(records1)[12] + _print(records2)[12]
    ice_natural_gas_consumption_13 = _print(records1)[13] + _print(records2)[13]
    ice_natural_gas_consumption_14 = _print(records1)[14] + _print(records2)[14]
    ice_natural_gas_consumption_15 = _print(records1)[15] + _print(records2)[15]
    ice_natural_gas_consumption_16 = _print(records1)[16] + _print(records2)[16]
    ice_natural_gas_consumption_17 = _print(records1)[17] + _print(records2)[17]
    ice_natural_gas_consumption_18 = _print(records1)[18] + _print(records2)[18]
    ice_natural_gas_consumption_19 = _print(records1)[19] + _print(records2)[19]
    ice_natural_gas_consumption_20 = _print(records1)[20] + _print(records2)[20]
    ice_natural_gas_consumption_21 = _print(records1)[21] + _print(records2)[21]
    ice_natural_gas_consumption_22 = _print(records1)[22] + _print(records2)[22]
    ice_natural_gas_consumption_23 = _print(records1)[23] + _print(records2)[23]

    # 向数据库写入批量数据
    state3 = syncbase.write_batch_realtime_data_by_name(
        ['ice_natural_gas_consumption_0', 'ice_natural_gas_consumption_1', 'ice_natural_gas_consumption_2',
         'ice_natural_gas_consumption_3', 'ice_natural_gas_consumption_4', 'ice_natural_gas_consumption_5',
         'ice_natural_gas_consumption_6', 'ice_natural_gas_consumption_7', 'ice_natural_gas_consumption_8',
         'ice_natural_gas_consumption_9', 'ice_natural_gas_consumption_10', 'ice_natural_gas_consumption_11',
         'ice_natural_gas_consumption_12', 'ice_natural_gas_consumption_13', 'ice_natural_gas_consumption_14',
         'ice_natural_gas_consumption_15', 'ice_natural_gas_consumption_16', 'ice_natural_gas_consumption_17',
         'ice_natural_gas_consumption_18', 'ice_natural_gas_consumption_19', 'ice_natural_gas_consumption_20',
         'ice_natural_gas_consumption_21', 'ice_natural_gas_consumption_22', 'ice_natural_gas_consumption_23'],
        [ice_natural_gas_consumption_0, ice_natural_gas_consumption_1, ice_natural_gas_consumption_2,
         ice_natural_gas_consumption_3, ice_natural_gas_consumption_4, ice_natural_gas_consumption_5,
         ice_natural_gas_consumption_6, ice_natural_gas_consumption_7, ice_natural_gas_consumption_8,
         ice_natural_gas_consumption_9, ice_natural_gas_consumption_10, ice_natural_gas_consumption_11,
         ice_natural_gas_consumption_12, ice_natural_gas_consumption_13, ice_natural_gas_consumption_14,
         ice_natural_gas_consumption_15, ice_natural_gas_consumption_16, ice_natural_gas_consumption_17,
         ice_natural_gas_consumption_18, ice_natural_gas_consumption_19, ice_natural_gas_consumption_20,
         ice_natural_gas_consumption_21, ice_natural_gas_consumption_22, ice_natural_gas_consumption_23])
    # 报错
    if state3 == False:
        print("24小时内燃机天然气耗量数据写入数据库错误！")

def write_to_database_ngb_natural_gas_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入天然气锅炉天然气耗量24小时的值

    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ngb3_natural_gas_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    if state1 == False:
        print("从数据库读取生活热水锅炉天然气耗量历史数据错误！")

    ngb_natural_gas_consumption_0 = _print(records1)[0]
    ngb_natural_gas_consumption_1 = _print(records1)[1]
    ngb_natural_gas_consumption_2 = _print(records1)[2]
    ngb_natural_gas_consumption_3 = _print(records1)[3]
    ngb_natural_gas_consumption_4 = _print(records1)[4]
    ngb_natural_gas_consumption_5 = _print(records1)[5]
    ngb_natural_gas_consumption_6 = _print(records1)[6]
    ngb_natural_gas_consumption_7 = _print(records1)[7]
    ngb_natural_gas_consumption_8 = _print(records1)[8]
    ngb_natural_gas_consumption_9 = _print(records1)[9]
    ngb_natural_gas_consumption_10 = _print(records1)[10]
    ngb_natural_gas_consumption_11 = _print(records1)[11]
    ngb_natural_gas_consumption_12 = _print(records1)[12]
    ngb_natural_gas_consumption_13 = _print(records1)[13]
    ngb_natural_gas_consumption_14 = _print(records1)[14]
    ngb_natural_gas_consumption_15 = _print(records1)[15]
    ngb_natural_gas_consumption_16 = _print(records1)[16]
    ngb_natural_gas_consumption_17 = _print(records1)[17]
    ngb_natural_gas_consumption_18 = _print(records1)[18]
    ngb_natural_gas_consumption_19 = _print(records1)[19]
    ngb_natural_gas_consumption_20 = _print(records1)[20]
    ngb_natural_gas_consumption_21 = _print(records1)[21]
    ngb_natural_gas_consumption_22 = _print(records1)[22]
    ngb_natural_gas_consumption_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb_natural_gas_consumption_0', 'ngb_natural_gas_consumption_1', 'ngb_natural_gas_consumption_2', 'ngb_natural_gas_consumption_3',
         'ngb_natural_gas_consumption_4', 'ngb_natural_gas_consumption_5', 'ngb_natural_gas_consumption_6', 'ngb_natural_gas_consumption_7',
         'ngb_natural_gas_consumption_8',  'ngb_natural_gas_consumption_9', 'ngb_natural_gas_consumption_10', 'ngb_natural_gas_consumption_11',
         'ngb_natural_gas_consumption_12', 'ngb_natural_gas_consumption_13', 'ngb_natural_gas_consumption_14', 'ngb_natural_gas_consumption_15',
         'ngb_natural_gas_consumption_16', 'ngb_natural_gas_consumption_17', 'ngb_natural_gas_consumption_18', 'ngb_natural_gas_consumption_19',
         'ngb_natural_gas_consumption_20', 'ngb_natural_gas_consumption_21', 'ngb_natural_gas_consumption_22', 'ngb_natural_gas_consumption_23'],
        [ngb_natural_gas_consumption_0, ngb_natural_gas_consumption_1, ngb_natural_gas_consumption_2, ngb_natural_gas_consumption_3, ngb_natural_gas_consumption_4,
         ngb_natural_gas_consumption_5, ngb_natural_gas_consumption_6, ngb_natural_gas_consumption_7, ngb_natural_gas_consumption_8, ngb_natural_gas_consumption_9,
         ngb_natural_gas_consumption_10, ngb_natural_gas_consumption_11, ngb_natural_gas_consumption_12, ngb_natural_gas_consumption_13, ngb_natural_gas_consumption_14,
         ngb_natural_gas_consumption_15, ngb_natural_gas_consumption_16, ngb_natural_gas_consumption_17, ngb_natural_gas_consumption_18, ngb_natural_gas_consumption_19,
         ngb_natural_gas_consumption_20, ngb_natural_gas_consumption_21, ngb_natural_gas_consumption_22, ngb_natural_gas_consumption_23])

    # 报错
    if state2 == False:
        print("24小时生活热水锅炉天然气耗量数据写入数据库错误！")


def write_to_database_cc_electricity_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机耗电量24小时的值

    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc1_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state2, records2 = syncbase.get_history_data_by_name('cc1_wp_chilled_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute,now_second),
                                                         period)
    # 从数据库读取历史数据
    state3, records3 = syncbase.get_history_data_by_name('cc1_wp_cooling_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute,now_second),
                                                         period)
    # 从数据库读取历史数据
    state4, records4 = syncbase.get_history_data_by_name('cc1_cooling_tower_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state5, records5 = syncbase.get_history_data_by_name('cc2_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state6, records6 = syncbase.get_history_data_by_name('cc2_wp_chilled_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute,now_second),
                                                         period)
    # 从数据库读取历史数据
    state7, records7 = syncbase.get_history_data_by_name('cc2_wp_cooling_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute,now_second),
                                                         period)
    # 从数据库读取历史数据
    state8, records8 = syncbase.get_history_data_by_name('cc2_cooling_tower_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    cc_electricity_consumption_0 = _print(records1)[0] +_print(records2)[0] + _print(records3)[0] + _print(records4)[0] \
                                   + _print(records5)[0]+ _print(records6)[0] + _print(records7)[0] + _print(records8)[0]
    cc_electricity_consumption_1 = _print(records1)[1] +_print(records2)[1] + _print(records3)[1] + _print(records4)[1] \
                                   + _print(records5)[1]+ _print(records6)[1] + _print(records7)[1] + _print(records8)[1]
    cc_electricity_consumption_2 = _print(records1)[2] +_print(records2)[2] + _print(records3)[2] + _print(records4)[2] \
                                   + _print(records5)[2]+ _print(records6)[2] + _print(records7)[2] + _print(records8)[2]
    cc_electricity_consumption_3 = _print(records1)[3] +_print(records2)[3] + _print(records3)[3] + _print(records4)[3] \
                                   + _print(records5)[3]+ _print(records6)[3] + _print(records7)[3] + _print(records8)[3]
    cc_electricity_consumption_4 = _print(records1)[4] + _print(records2)[4] + _print(records3)[4] + _print(records4)[4] \
                                   + _print(records5)[4] + _print(records6)[4] + _print(records7)[4] + _print(records8)[4]
    cc_electricity_consumption_5 = _print(records1)[5] + _print(records2)[5] + _print(records3)[5] + _print(records4)[5] \
                                   + _print(records5)[5] + _print(records6)[5] + _print(records7)[5] + _print(records8)[5]
    cc_electricity_consumption_6 = _print(records1)[6] + _print(records2)[6] + _print(records3)[6] + _print(records4)[6] \
                                   + _print(records5)[6] + _print(records6)[6] + _print(records7)[6] + _print(records8)[6]
    cc_electricity_consumption_7 = _print(records1)[7] + _print(records2)[7] + _print(records3)[7] + _print(records4)[7] \
                                   + _print(records5)[7] + _print(records6)[7] + _print(records7)[7] + _print(records8)[7]
    cc_electricity_consumption_8 = _print(records1)[8] + _print(records2)[8] + _print(records3)[8] + _print(records4)[8] \
                                   + _print(records5)[8] + _print(records6)[8] + _print(records7)[8] + _print(records8)[8]
    cc_electricity_consumption_9 = _print(records1)[9] + _print(records2)[9] + _print(records3)[9] + _print(records4)[9] \
                                   + _print(records5)[9] + _print(records6)[9] + _print(records7)[9] + _print(records8)[9]
    cc_electricity_consumption_10 = _print(records1)[10] + _print(records2)[10] + _print(records3)[10] + _print(records4)[10] \
                                    + _print(records5)[10] + _print(records6)[10] + _print(records7)[10] + _print(records8)[10]
    cc_electricity_consumption_11 = _print(records1)[11] + _print(records2)[11] + _print(records3)[11] + _print(records4)[11] \
                                    + _print(records5)[11] + _print(records6)[11] + _print(records7)[11] + _print(records8)[11]
    cc_electricity_consumption_12 = _print(records1)[12] + _print(records2)[12] + _print(records3)[12] + _print(records4)[12] \
                                    + _print(records5)[12] + _print(records6)[12] + _print(records7)[12] + _print(records8)[12]
    cc_electricity_consumption_13 = _print(records1)[13] + _print(records2)[13] + _print(records3)[13] + _print(records4)[13] \
                                    + _print(records5)[13] + _print(records6)[13] + _print(records7)[13] + _print(records8)[13]
    cc_electricity_consumption_14 = _print(records1)[14] + _print(records2)[14] + _print(records3)[14] + _print(records4)[14] \
                                    + _print(records5)[14] + _print(records6)[14] + _print(records7)[14] + _print(records8)[14]
    cc_electricity_consumption_15 = _print(records1)[15] + _print(records2)[15] + _print(records3)[15] + _print(records4)[15] \
                                   + _print(records5)[15] + _print(records6)[15] + _print(records7)[15] + _print(records8)[15]
    cc_electricity_consumption_16 = _print(records1)[16] + _print(records2)[16] + _print(records3)[16] + _print(records4)[16] \
                                    + _print(records5)[16] + _print(records6)[16] + _print(records7)[16] + _print(records8)[16]
    cc_electricity_consumption_17 = _print(records1)[17] + _print(records2)[17] + _print(records3)[17] + _print(records4)[17] \
                                    + _print(records5)[17] + _print(records6)[17] + _print(records7)[17] + _print(records8)[17]
    cc_electricity_consumption_18 = _print(records1)[18] + _print(records2)[18] + _print(records3)[18] + _print(records4)[18] \
                                    + _print(records5)[18] + _print(records6)[18] + _print(records7)[18] + _print(records8)[18]
    cc_electricity_consumption_19 = _print(records1)[19] + _print(records2)[19] + _print(records3)[19] + _print(records4)[19] \
                                    + _print(records5)[19] + _print(records6)[19] + _print(records7)[19] + _print(records8)[19]
    cc_electricity_consumption_20 = _print(records1)[20] + _print(records2)[20] + _print(records3)[20] + _print(records4)[20] \
                                    + _print(records5)[20] + _print(records6)[20] + _print(records7)[20] + _print(records8)[20]
    cc_electricity_consumption_21 = _print(records1)[21] + _print(records2)[21] + _print(records3)[21] + _print(records4)[21] \
                                    + _print(records5)[21] + _print(records6)[21] + _print(records7)[21] + _print(records8)[21]
    cc_electricity_consumption_22 = _print(records1)[22] + _print(records2)[22] + _print(records3)[22] + _print(records4)[22] \
                                    + _print(records5)[22] + _print(records6)[22] + _print(records7)[22] + _print(records8)[22]
    cc_electricity_consumption_23 = _print(records1)[23] + _print(records2)[23] + _print(records3)[23] + _print(records4)[23] \
                                    + _print(records5)[23] + _print(records6)[23] + _print(records7)[23] + _print(records8)[23]

    # 向数据库写入批量数据
    state9 = syncbase.write_batch_realtime_data_by_name(
        ['cc_electricity_consumption_0', 'cc_electricity_consumption_1', 'cc_electricity_consumption_2', 'cc_electricity_consumption_3',
         'cc_electricity_consumption_4', 'cc_electricity_consumption_5', 'cc_electricity_consumption_6', 'cc_electricity_consumption_7',
         'cc_electricity_consumption_8',  'cc_electricity_consumption_9', 'cc_electricity_consumption_10', 'cc_electricity_consumption_11',
         'cc_electricity_consumption_12', 'cc_electricity_consumption_13', 'cc_electricity_consumption_14', 'cc_electricity_consumption_15',
         'cc_electricity_consumption_16', 'cc_electricity_consumption_17', 'cc_electricity_consumption_18', 'cc_electricity_consumption_19',
         'cc_electricity_consumption_20', 'cc_electricity_consumption_21', 'cc_electricity_consumption_22', 'cc_electricity_consumption_23'],
        [cc_electricity_consumption_0, cc_electricity_consumption_1, cc_electricity_consumption_2, cc_electricity_consumption_3, cc_electricity_consumption_4,
         cc_electricity_consumption_5, cc_electricity_consumption_6, cc_electricity_consumption_7, cc_electricity_consumption_8, cc_electricity_consumption_9,
         cc_electricity_consumption_10, cc_electricity_consumption_11, cc_electricity_consumption_12, cc_electricity_consumption_13, cc_electricity_consumption_14,
         cc_electricity_consumption_15, cc_electricity_consumption_16, cc_electricity_consumption_17, cc_electricity_consumption_18, cc_electricity_consumption_19,
         cc_electricity_consumption_20, cc_electricity_consumption_21, cc_electricity_consumption_22, cc_electricity_consumption_23])


def write_to_database_chp_cold_electricity_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制冷耗电量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc3_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state2, records2 = syncbase.get_history_data_by_name('cc3_wp_chilled_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state3, records3 = syncbase.get_history_data_by_name('cc3_wp_cooling_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state4, records4 = syncbase.get_history_data_by_name('cc3_cooling_tower_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state5, records5 = syncbase.get_history_data_by_name('cc4_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state6, records6 = syncbase.get_history_data_by_name('cc4_wp_chilled_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state7, records7 = syncbase.get_history_data_by_name('cc4_wp_cooling_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state8, records8 = syncbase.get_history_data_by_name('cc4_cooling_tower_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_electricity_consumption_0 = _print(records1)[0] + _print(records2)[0] + _print(records3)[0] + _print(records4)[0] \
                                    + _print(records5)[0] + _print(records6)[0] + _print(records7)[0] + _print(records8)[0]
    chp_electricity_consumption_1 = _print(records1)[1] + _print(records2)[1] + _print(records3)[1] + _print(records4)[1] \
                                    + _print(records5)[1] + _print(records6)[1] + _print(records7)[1] + _print(records8)[1]
    chp_electricity_consumption_2 = _print(records1)[2] + _print(records2)[2] + _print(records3)[2] + _print(records4)[2] \
                                    + _print(records5)[2] + _print(records6)[2] + _print(records7)[2] + _print(records8)[2]
    chp_electricity_consumption_3 = _print(records1)[3] + _print(records2)[3] + _print(records3)[3] + _print(records4)[3] \
                                    + _print(records5)[3] + _print(records6)[3] + _print(records7)[3] + _print(records8)[3]
    chp_electricity_consumption_4 = _print(records1)[4] + _print(records2)[4] + _print(records3)[4] + _print(records4)[4] \
                                    + _print(records5)[4] + _print(records6)[4] + _print(records7)[4] + _print(records8)[4]
    chp_electricity_consumption_5 = _print(records1)[5] + _print(records2)[5] + _print(records3)[5] + _print(records4)[5] \
                                    + _print(records5)[5] + _print(records6)[5] + _print(records7)[5] + _print(records8)[5]
    chp_electricity_consumption_6 = _print(records1)[6] + _print(records2)[6] + _print(records3)[6] + _print(records4)[6] \
                                    + _print(records5)[6] + _print(records6)[6] + _print(records7)[6] + _print(records8)[6]
    chp_electricity_consumption_7 = _print(records1)[7] + _print(records2)[7] + _print(records3)[7] + _print(records4)[7] \
                                    + _print(records5)[7] + _print(records6)[7] + _print(records7)[7] + _print(records8)[7]
    chp_electricity_consumption_8 = _print(records1)[8] + _print(records2)[8] + _print(records3)[8] + _print(records4)[8] \
                                    + _print(records5)[8] + _print(records6)[8] + _print(records7)[8] + _print(records8)[8]
    chp_electricity_consumption_9 = _print(records1)[9] + _print(records2)[9] + _print(records3)[9] + _print(records4)[9] \
                                    + _print(records5)[9] + _print(records6)[9] + _print(records7)[9] + _print(records8)[9]
    chp_electricity_consumption_10 = _print(records1)[10] + _print(records2)[10] + _print(records3)[10] + _print(records4)[10] \
                                     + _print(records5)[10] + _print(records6)[10] + _print(records7)[10] + _print(records8)[10]
    chp_electricity_consumption_11 = _print(records1)[11] + _print(records2)[11] + _print(records3)[11] + _print(records4)[11] \
                                     + _print(records5)[11] + _print(records6)[11] + _print(records7)[11] + _print(records8)[11]
    chp_electricity_consumption_12 = _print(records1)[12] + _print(records2)[12] + _print(records3)[12] + _print(records4)[12] \
                                     + _print(records5)[12] + _print(records6)[12] + _print(records7)[12] + _print(records8)[12]
    chp_electricity_consumption_13 = _print(records1)[13] + _print(records2)[13] + _print(records3)[13] + _print(records4)[13] \
                                     + _print(records5)[13] + _print(records6)[13] + _print(records7)[13] + _print(records8)[13]
    chp_electricity_consumption_14 = _print(records1)[14] + _print(records2)[14] + _print(records3)[14] + _print(records4)[14] \
                                     + _print(records5)[14] + _print(records6)[14] + _print(records7)[14] + _print(records8)[14]
    chp_electricity_consumption_15 = _print(records1)[15] + _print(records2)[15] + _print(records3)[15] + _print(records4)[15] \
                                     + _print(records5)[15] + _print(records6)[15] + _print(records7)[15] + _print(records8)[15]
    chp_electricity_consumption_16 = _print(records1)[16] + _print(records2)[16] + _print(records3)[16] + _print(records4)[16] \
                                     + _print(records5)[16] + _print(records6)[16] + _print(records7)[16] + _print(records8)[16]
    chp_electricity_consumption_17 = _print(records1)[17] + _print(records2)[17] + _print(records3)[17] + _print(records4)[17] \
                                     + _print(records5)[17] + _print(records6)[17] + _print(records7)[17] + _print(records8)[17]
    chp_electricity_consumption_18 = _print(records1)[18] + _print(records2)[18] + _print(records3)[18] + _print(records4)[18] \
                                     + _print(records5)[18] + _print(records6)[18] + _print(records7)[18] + _print(records8)[18]
    chp_electricity_consumption_19 = _print(records1)[19] + _print(records2)[19] + _print(records3)[19] + _print(records4)[19] \
                                     + _print(records5)[19] + _print(records6)[19] + _print(records7)[19] + _print(records8)[19]
    chp_electricity_consumption_20 = _print(records1)[20] + _print(records2)[20] + _print(records3)[20] + _print(records4)[20] \
                                     + _print(records5)[20] + _print(records6)[20] + _print(records7)[20] + _print(records8)[20]
    chp_electricity_consumption_21 = _print(records1)[21] + _print(records2)[21] + _print(records3)[21] + _print(records4)[21] \
                                     + _print(records5)[21] + _print(records6)[21] + _print(records7)[21] + _print(records8)[21]
    chp_electricity_consumption_22 = _print(records1)[22] + _print(records2)[22] + _print(records3)[22] + _print(records4)[22] \
                                     + _print(records5)[22] + _print(records6)[22] + _print(records7)[22] + _print(records8)[22]
    chp_electricity_consumption_23 = _print(records1)[23] + _print(records2)[23] + _print(records3)[23] + _print(records4)[23] \
                                     + _print(records5)[23] + _print(records6)[23] + _print(records7)[23] + _print(records8)[23]

    # 向数据库写入批量数据
    state9 = syncbase.write_batch_realtime_data_by_name(
        ['chp_electricity_consumption_0', 'chp_electricity_consumption_1', 'chp_electricity_consumption_2',
         'chp_electricity_consumption_3',
         'chp_electricity_consumption_4', 'chp_electricity_consumption_5', 'chp_electricity_consumption_6',
         'chp_electricity_consumption_7',
         'chp_electricity_consumption_8', 'chp_electricity_consumption_9', 'chp_electricity_consumption_10',
         'chp_electricity_consumption_11',
         'chp_electricity_consumption_12', 'chp_electricity_consumption_13', 'chp_electricity_consumption_14',
         'chp_electricity_consumption_15',
         'chp_electricity_consumption_16', 'chp_electricity_consumption_17', 'chp_electricity_consumption_18',
         'chp_electricity_consumption_19',
         'chp_electricity_consumption_20', 'chp_electricity_consumption_21', 'chp_electricity_consumption_22',
         'chp_electricity_consumption_23'],
        [chp_electricity_consumption_0, chp_electricity_consumption_1, chp_electricity_consumption_2,
         chp_electricity_consumption_3, chp_electricity_consumption_4,
         chp_electricity_consumption_5, chp_electricity_consumption_6, chp_electricity_consumption_7,
         chp_electricity_consumption_8, chp_electricity_consumption_9,
         chp_electricity_consumption_10, chp_electricity_consumption_11, chp_electricity_consumption_12,
         chp_electricity_consumption_13, chp_electricity_consumption_14,
         chp_electricity_consumption_15, chp_electricity_consumption_16, chp_electricity_consumption_17,
         chp_electricity_consumption_18, chp_electricity_consumption_19,
         chp_electricity_consumption_20, chp_electricity_consumption_21, chp_electricity_consumption_22,
         chp_electricity_consumption_23])



def write_to_database_chp_heat_electricity_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制热耗电量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp1_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state2, records2 = syncbase.get_history_data_by_name('chp1_wp_heat_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state3, records3 = syncbase.get_history_data_by_name('chp1_wp_source_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state4, records4 = syncbase.get_history_data_by_name('chp2_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state5, records5 = syncbase.get_history_data_by_name('chp2_wp_heat_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state6, records6 = syncbase.get_history_data_by_name('chp2_wp_source_water_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_electricity_consumption_0 = _print(records1)[0] + _print(records2)[0] + _print(records3)[0] + _print(records4)[0] \
                                    + _print(records5)[0] + _print(records6)[0]
    chp_electricity_consumption_1 = _print(records1)[1] + _print(records2)[1] + _print(records3)[1] + _print(records4)[1] \
                                    + _print(records5)[1] + _print(records6)[1]
    chp_electricity_consumption_2 = _print(records1)[2] + _print(records2)[2] + _print(records3)[2] + _print(records4)[2] \
                                    + _print(records5)[2] + _print(records6)[2]
    chp_electricity_consumption_3 = _print(records1)[3] + _print(records2)[3] + _print(records3)[3] + _print(records4)[3] \
                                    + _print(records5)[3] + _print(records6)[3]
    chp_electricity_consumption_4 = _print(records1)[4] + _print(records2)[4] + _print(records3)[4] + _print(records4)[4] \
                                    + _print(records5)[4] + _print(records6)[4]
    chp_electricity_consumption_5 = _print(records1)[5] + _print(records2)[5] + _print(records3)[5] + _print(records4)[5] \
                                    + _print(records5)[5] + _print(records6)[5]
    chp_electricity_consumption_6 = _print(records1)[6] + _print(records2)[6] + _print(records3)[6] + _print(records4)[6] \
                                    + _print(records5)[6] + _print(records6)[6]
    chp_electricity_consumption_7 = _print(records1)[7] + _print(records2)[7] + _print(records3)[7] + _print(records4)[7] \
                                    + _print(records5)[7] + _print(records6)[7]
    chp_electricity_consumption_8 = _print(records1)[8] + _print(records2)[8] + _print(records3)[8] + _print(records4)[8] \
                                    + _print(records5)[8] + _print(records6)[8]
    chp_electricity_consumption_9 = _print(records1)[9] + _print(records2)[9] + _print(records3)[9] + _print(records4)[9] \
                                    + _print(records5)[9] + _print(records6)[9]
    chp_electricity_consumption_10 = _print(records1)[10] + _print(records2)[10] + _print(records3)[10] + \
                                     _print(records4)[10] + _print(records5)[10] + _print(records6)[10]
    chp_electricity_consumption_11 = _print(records1)[11] + _print(records2)[11] + _print(records3)[11] + \
                                     _print(records4)[11] + _print(records5)[11] + _print(records6)[11]
    chp_electricity_consumption_12 = _print(records1)[12] + _print(records2)[12] + _print(records3)[12] + \
                                     _print(records4)[12] + _print(records5)[12] + _print(records6)[12]
    chp_electricity_consumption_13 = _print(records1)[13] + _print(records2)[13] + _print(records3)[13] + \
                                     _print(records4)[13] + _print(records5)[13] + _print(records6)[13]
    chp_electricity_consumption_14 = _print(records1)[14] + _print(records2)[14] + _print(records3)[14] + \
                                     _print(records4)[14] + _print(records5)[14] + _print(records6)[14]
    chp_electricity_consumption_15 = _print(records1)[15] + _print(records2)[15] + _print(records3)[15] + \
                                     _print(records4)[15] + _print(records5)[15] + _print(records6)[15]
    chp_electricity_consumption_16 = _print(records1)[16] + _print(records2)[16] + _print(records3)[16] + \
                                     _print(records4)[16] + _print(records5)[16] + _print(records6)[16]
    chp_electricity_consumption_17 = _print(records1)[17] + _print(records2)[17] + _print(records3)[17] + \
                                     _print(records4)[17] + _print(records5)[17] + _print(records6)[17]
    chp_electricity_consumption_18 = _print(records1)[18] + _print(records2)[18] + _print(records3)[18] + \
                                     _print(records4)[18] + _print(records5)[18] + _print(records6)[18]
    chp_electricity_consumption_19 = _print(records1)[19] + _print(records2)[19] + _print(records3)[19] + \
                                     _print(records4)[19] + _print(records5)[19] + _print(records6)[19]
    chp_electricity_consumption_20 = _print(records1)[20] + _print(records2)[20] + _print(records3)[20] + \
                                     _print(records4)[20] + _print(records5)[20] + _print(records6)[20]
    chp_electricity_consumption_21 = _print(records1)[21] + _print(records2)[21] + _print(records3)[21] + \
                                     _print(records4)[21] + _print(records5)[21] + _print(records6)[21]
    chp_electricity_consumption_22 = _print(records1)[22] + _print(records2)[22] + _print(records3)[22] + \
                                     _print(records4)[22] + _print(records5)[22] + _print(records6)[22]
    chp_electricity_consumption_23 = _print(records1)[23] + _print(records2)[23] + _print(records3)[23] + \
                                     _print(records4)[23] + _print(records5)[23] + _print(records6)[23]

    # 向数据库写入批量数据
    state9 = syncbase.write_batch_realtime_data_by_name(
        ['chp_electricity_consumption_0', 'chp_electricity_consumption_1', 'chp_electricity_consumption_2',
         'chp_electricity_consumption_3',
         'chp_electricity_consumption_4', 'chp_electricity_consumption_5', 'chp_electricity_consumption_6',
         'chp_electricity_consumption_7',
         'chp_electricity_consumption_8', 'chp_electricity_consumption_9', 'chp_electricity_consumption_10',
         'chp_electricity_consumption_11',
         'chp_electricity_consumption_12', 'chp_electricity_consumption_13', 'chp_electricity_consumption_14',
         'chp_electricity_consumption_15',
         'chp_electricity_consumption_16', 'chp_electricity_consumption_17', 'chp_electricity_consumption_18',
         'chp_electricity_consumption_19',
         'chp_electricity_consumption_20', 'chp_electricity_consumption_21', 'chp_electricity_consumption_22',
         'chp_electricity_consumption_23'],
        [chp_electricity_consumption_0, chp_electricity_consumption_1, chp_electricity_consumption_2,
         chp_electricity_consumption_3, chp_electricity_consumption_4,
         chp_electricity_consumption_5, chp_electricity_consumption_6, chp_electricity_consumption_7,
         chp_electricity_consumption_8, chp_electricity_consumption_9,
         chp_electricity_consumption_10, chp_electricity_consumption_11, chp_electricity_consumption_12,
         chp_electricity_consumption_13, chp_electricity_consumption_14,
         chp_electricity_consumption_15, chp_electricity_consumption_16, chp_electricity_consumption_17,
         chp_electricity_consumption_18, chp_electricity_consumption_19,
         chp_electricity_consumption_20, chp_electricity_consumption_21, chp_electricity_consumption_22,
         chp_electricity_consumption_23])


def write_to_database_ashp_electricity_consumption_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制冷、制热耗电量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp1_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state2, records2 = syncbase.get_history_data_by_name('ashp1_wp_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state3, records3 = syncbase.get_history_data_by_name('ashp1_fan_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    # 从数据库读取历史数据
    state4, records4 = syncbase.get_history_data_by_name('ashp2_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state5, records5 = syncbase.get_history_data_by_name('ashp2_wp_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state6, records6 = syncbase.get_history_data_by_name('ashp2_fan_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state7, records7 = syncbase.get_history_data_by_name('ashp3_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state8, records8 = syncbase.get_history_data_by_name('ashp3_wp_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    # 从数据库读取历史数据
    state9, records9 = syncbase.get_history_data_by_name('ashp3_fan_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute,now_second),
                                                         period)

    # 从数据库读取历史数据
    state10, records10 = syncbase.get_history_data_by_name('ashp4_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)
    # 从数据库读取历史数据
    state11, records11 = syncbase.get_history_data_by_name('ashp4_wp_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    # 从数据库读取历史数据
    state12, records12 = syncbase.get_history_data_by_name('ashp4_fan_power_consumption',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_electricity_consumption_0 = _print(records1)[0] + _print(records2)[0] + _print(records3)[0] + _print(records4)[0] \
                                     + _print(records5)[0] + _print(records6)[0] + _print(records7)[0] + _print(records8)[0]\
                                     + _print(records9)[0] + _print(records10)[0] + _print(records11)[0] + _print(records12)[0]
    ashp_electricity_consumption_1 = _print(records1)[1] + _print(records2)[1] + _print(records3)[1] + _print(records4)[1] \
                                     + _print(records5)[1] + _print(records6)[1] + _print(records7)[1] + _print(records8)[1]\
                                     + _print(records9)[1] + _print(records10)[1] + _print(records11)[1] + _print(records12)[1]
    ashp_electricity_consumption_2 = _print(records1)[2] + _print(records2)[2] + _print(records3)[2] + _print(records4)[2] \
                                     + _print(records5)[2] + _print(records6)[2] + _print(records7)[2] + _print(records8)[2]\
                                     + _print(records9)[2] + _print(records10)[2] + _print(records11)[2] + _print(records12)[2]
    ashp_electricity_consumption_3 = _print(records1)[3] + _print(records2)[3] + _print(records3)[3] + _print(records4)[3] \
                                     + _print(records5)[3] + _print(records6)[3] + _print(records7)[3] + _print(records8)[3]\
                                     + _print(records9)[3] + _print(records10)[3] + _print(records11)[3] + _print(records12)[3]
    ashp_electricity_consumption_4 = _print(records1)[4] + _print(records2)[4] + _print(records3)[4] + _print(records4)[4] \
                                     + _print(records5)[4] + _print(records6)[4] + _print(records7)[4] + _print(records8)[4]\
                                     + _print(records9)[4] + _print(records10)[4] + _print(records11)[4] + _print(records12)[4]
    ashp_electricity_consumption_5 = _print(records1)[5] + _print(records2)[5] + _print(records3)[5] + _print(records4)[5] \
                                     + _print(records5)[5] + _print(records6)[5] + _print(records7)[5] + _print(records8)[5]\
                                     + _print(records9)[5] + _print(records10)[5] + _print(records11)[5] + _print(records12)[5]
    ashp_electricity_consumption_6 = _print(records1)[6] + _print(records2)[6] + _print(records3)[6] + _print(records4)[6] \
                                     + _print(records5)[6] + _print(records6)[6] + _print(records7)[6] + _print(records8)[6]\
                                     + _print(records9)[6] + _print(records10)[6] + _print(records11)[6] + _print(records12)[6]
    ashp_electricity_consumption_7 = _print(records1)[7] + _print(records2)[7] + _print(records3)[7] + _print(records4)[7] \
                                     + _print(records5)[7] + _print(records6)[7] + _print(records7)[7] + _print(records8)[7]\
                                     + _print(records9)[7] + _print(records10)[7] + _print(records11)[7] + _print(records12)[7]
    ashp_electricity_consumption_8 = _print(records1)[8] + _print(records2)[8] + _print(records3)[8] + _print(records4)[8] \
                                     + _print(records5)[8] + _print(records6)[8] + _print(records7)[8] + _print(records8)[8]\
                                     + _print(records9)[8] + _print(records10)[8] + _print(records11)[8] + _print(records12)[8]
    ashp_electricity_consumption_9 = _print(records1)[9] + _print(records2)[9] + _print(records3)[9] + _print(records4)[9] \
                                     + _print(records5)[9] + _print(records6)[9] + _print(records7)[9] + _print(records8)[9]\
                                     + _print(records9)[9] + _print(records10)[9] + _print(records11)[9] + _print(records12)[9]
    ashp_electricity_consumption_10 = _print(records1)[10] + _print(records2)[10] + _print(records3)[10] + _print(records4)[10] \
                                      + _print(records5)[10] + _print(records6)[10] + _print(records7)[10] + _print(records8)[10]\
                                      + _print(records9)[10] + _print(records10)[10] + _print(records11)[10] + _print(records12)[10]
    ashp_electricity_consumption_11 = _print(records1)[11] + _print(records2)[11] + _print(records3)[11] + _print(records4)[11] \
                                      + _print(records5)[11] + _print(records6)[11] + _print(records7)[11] + _print(records8)[11]\
                                      + _print(records9)[11] + _print(records10)[11] + _print(records11)[11] + _print(records12)[11]
    ashp_electricity_consumption_12 = _print(records1)[12] + _print(records2)[12] + _print(records3)[12] + _print(records4)[12] \
                                      + _print(records5)[12] + _print(records6)[12] + _print(records7)[12] + _print(records8)[12]\
                                      + _print(records9)[12] + _print(records10)[12] + _print(records11)[12] + _print(records12)[12]
    ashp_electricity_consumption_13 = _print(records1)[13] + _print(records2)[13] + _print(records3)[13] + _print(records4)[13] \
                                      + _print(records5)[13] + _print(records6)[13] + _print(records7)[13] + _print(records8)[13]\
                                      + _print(records9)[13] + _print(records10)[13] + _print(records11)[13] + _print(records12)[13]
    ashp_electricity_consumption_14 = _print(records1)[14] + _print(records2)[14] + _print(records3)[14] + _print(records4)[14] \
                                      + _print(records5)[14] + _print(records6)[14] + _print(records7)[14] + _print(records8)[14]\
                                      + _print(records9)[14] + _print(records10)[14] + _print(records11)[14] + _print(records12)[14]
    ashp_electricity_consumption_15 = _print(records1)[15] + _print(records2)[15] + _print(records3)[15] + _print(records4)[15] \
                                      + _print(records5)[15] + _print(records6)[15] + _print(records7)[15] + _print(records8)[15]\
                                      + _print(records9)[15] + _print(records10)[15] + _print(records11)[15] + _print(records12)[15]
    ashp_electricity_consumption_16 = _print(records1)[16] + _print(records2)[16] + _print(records3)[16] + _print(records4)[16] \
                                      + _print(records5)[16] + _print(records6)[16] + _print(records7)[16] + _print(records8)[16]\
                                      + _print(records9)[16] + _print(records10)[16] + _print(records11)[16] + _print(records12)[16]
    ashp_electricity_consumption_17 = _print(records1)[17] + _print(records2)[17] + _print(records3)[17] + _print(records4)[17] \
                                      + _print(records5)[17] + _print(records6)[17] + _print(records7)[17] + _print(records8)[17]\
                                      + _print(records9)[17] + _print(records10)[17] + _print(records11)[17] + _print(records12)[17]
    ashp_electricity_consumption_18 = _print(records1)[18] + _print(records2)[18] + _print(records3)[18] + _print(records4)[18] \
                                      + _print(records5)[18] + _print(records6)[18] + _print(records7)[18] + _print(records8)[18]\
                                      + _print(records9)[18] + _print(records10)[18] + _print(records11)[18] + _print(records12)[18]
    ashp_electricity_consumption_19 = _print(records1)[19] + _print(records2)[19] + _print(records3)[19] + _print(records4)[19] \
                                      + _print(records5)[19] + _print(records6)[19] + _print(records7)[19] + _print(records8)[19]\
                                      + _print(records9)[19] + _print(records10)[19] + _print(records11)[19] + _print(records12)[19]
    ashp_electricity_consumption_20 = _print(records1)[20] + _print(records2)[20] + _print(records3)[20] + _print(records4)[20] \
                                      + _print(records5)[20] + _print(records6)[20] + _print(records7)[20] + _print(records8)[20]\
                                      + _print(records9)[20] + _print(records10)[20] + _print(records11)[20] + _print(records12)[20]
    ashp_electricity_consumption_21 = _print(records1)[21] + _print(records2)[21] + _print(records3)[21] + _print(records4)[21] \
                                      + _print(records5)[21] + _print(records6)[21] + _print(records7)[21] + _print(records8)[21]\
                                      + _print(records9)[21] + _print(records10)[21] + _print(records11)[21] + _print(records12)[21]
    ashp_electricity_consumption_22 = _print(records1)[22] + _print(records2)[22] + _print(records3)[22] + _print(records4)[22] \
                                      + _print(records5)[22] + _print(records6)[22] + _print(records7)[22] + _print(records8)[22]\
                                      + _print(records9)[22] + _print(records10)[22] + _print(records11)[22] + _print(records12)[22]
    ashp_electricity_consumption_23 = _print(records1)[23] + _print(records2)[23] + _print(records3)[23] + _print(records4)[23] \
                                      + _print(records5)[23] + _print(records6)[23] + _print(records7)[23] + _print(records8)[23]\
                                      + _print(records9)[23] + _print(records10)[23] + _print(records11)[23] + _print(records12)[23]

    # 向数据库写入批量数据
    state9 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_electricity_consumption_0', 'ashp_electricity_consumption_1', 'ashp_electricity_consumption_2',
         'ashp_electricity_consumption_3',
         'ashp_electricity_consumption_4', 'ashp_electricity_consumption_5', 'ashp_electricity_consumption_6',
         'ashp_electricity_consumption_7',
         'ashp_electricity_consumption_8', 'ashp_electricity_consumption_9', 'ashp_electricity_consumption_10',
         'ashp_electricity_consumption_11',
         'ashp_electricity_consumption_12', 'ashp_electricity_consumption_13', 'ashp_electricity_consumption_14',
         'ashp_electricity_consumption_15',
         'ashp_electricity_consumption_16', 'ashp_electricity_consumption_17', 'ashp_electricity_consumption_18',
         'ashp_electricity_consumption_19',
         'ashp_electricity_consumption_20', 'ashp_electricity_consumption_21', 'ashp_electricity_consumption_22',
         'ashp_electricity_consumption_23'],
        [ashp_electricity_consumption_0, ashp_electricity_consumption_1, ashp_electricity_consumption_2,
         ashp_electricity_consumption_3, ashp_electricity_consumption_4,
         ashp_electricity_consumption_5, ashp_electricity_consumption_6, ashp_electricity_consumption_7,
         ashp_electricity_consumption_8, ashp_electricity_consumption_9,
         ashp_electricity_consumption_10, ashp_electricity_consumption_11, ashp_electricity_consumption_12,
         ashp_electricity_consumption_13, ashp_electricity_consumption_14,
         ashp_electricity_consumption_15, ashp_electricity_consumption_16, ashp_electricity_consumption_17,
         ashp_electricity_consumption_18, ashp_electricity_consumption_19,
         ashp_electricity_consumption_20, ashp_electricity_consumption_21, ashp_electricity_consumption_22,
         ashp_electricity_consumption_23])

def write_to_database_ice_electricity_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机发电功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ice_electricity_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ice_electricity_out_0 = _print(records1)[0]
    ice_electricity_out_1 = _print(records1)[1]
    ice_electricity_out_2 = _print(records1)[2]
    ice_electricity_out_3 = _print(records1)[3]
    ice_electricity_out_4 = _print(records1)[4]
    ice_electricity_out_5 = _print(records1)[5]
    ice_electricity_out_6 = _print(records1)[6]
    ice_electricity_out_7 = _print(records1)[7]
    ice_electricity_out_8 = _print(records1)[8]
    ice_electricity_out_9 = _print(records1)[9]
    ice_electricity_out_10 = _print(records1)[10]
    ice_electricity_out_11 = _print(records1)[11]
    ice_electricity_out_12 = _print(records1)[12]
    ice_electricity_out_13 = _print(records1)[13]
    ice_electricity_out_14 = _print(records1)[14]
    ice_electricity_out_15 = _print(records1)[15]
    ice_electricity_out_16 = _print(records1)[16]
    ice_electricity_out_17 = _print(records1)[17]
    ice_electricity_out_18 = _print(records1)[18]
    ice_electricity_out_19 = _print(records1)[19]
    ice_electricity_out_20 = _print(records1)[20]
    ice_electricity_out_21 = _print(records1)[21]
    ice_electricity_out_22 = _print(records1)[22]
    ice_electricity_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice_electricity_out_0', 'ice_electricity_out_1', 'ice_electricity_out_2', 'ice_electricity_out_3',
         'ice_electricity_out_4',
         'ice_electricity_out_5', 'ice_electricity_out_6', 'ice_electricity_out_7', 'ice_electricity_out_8',
         'ice_electricity_out_9',
         'ice_electricity_out_10', 'ice_electricity_out_11', 'ice_electricity_out_12', 'ice_electricity_out_13',
         'ice_electricity_out_14',
         'ice_electricity_out_15', 'ice_electricity_out_16', 'ice_electricity_out_17', 'ice_electricity_out_18',
         'ice_electricity_out_19',
         'ice_electricity_out_20', 'ice_electricity_out_21', 'ice_electricity_out_22', 'ice_electricity_out_23'],
        [ice_electricity_out_0, ice_electricity_out_1, ice_electricity_out_2, ice_electricity_out_3,
         ice_electricity_out_4,
         ice_electricity_out_5, ice_electricity_out_6, ice_electricity_out_7, ice_electricity_out_8,
         ice_electricity_out_9,
         ice_electricity_out_10, ice_electricity_out_11, ice_electricity_out_12, ice_electricity_out_13,
         ice_electricity_out_14,
         ice_electricity_out_15, ice_electricity_out_16, ice_electricity_out_17, ice_electricity_out_18,
         ice_electricity_out_19,
         ice_electricity_out_20, ice_electricity_out_21, ice_electricity_out_22, ice_electricity_out_23])


def write_to_database_photovoltaic_electricity_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入光伏发电功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('photovoltaic_electricity_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    photovoltaic_electricity_out_0 = _print(records1)[0]
    photovoltaic_electricity_out_1 = _print(records1)[1]
    photovoltaic_electricity_out_2 = _print(records1)[2]
    photovoltaic_electricity_out_3 = _print(records1)[3]
    photovoltaic_electricity_out_4 = _print(records1)[4]
    photovoltaic_electricity_out_5 = _print(records1)[5]
    photovoltaic_electricity_out_6 = _print(records1)[6]
    photovoltaic_electricity_out_7 = _print(records1)[7]
    photovoltaic_electricity_out_8 = _print(records1)[8]
    photovoltaic_electricity_out_9 = _print(records1)[9]
    photovoltaic_electricity_out_10 = _print(records1)[10]
    photovoltaic_electricity_out_11 = _print(records1)[11]
    photovoltaic_electricity_out_12 = _print(records1)[12]
    photovoltaic_electricity_out_13 = _print(records1)[13]
    photovoltaic_electricity_out_14 = _print(records1)[14]
    photovoltaic_electricity_out_15 = _print(records1)[15]
    photovoltaic_electricity_out_16 = _print(records1)[16]
    photovoltaic_electricity_out_17 = _print(records1)[17]
    photovoltaic_electricity_out_18 = _print(records1)[18]
    photovoltaic_electricity_out_19 = _print(records1)[19]
    photovoltaic_electricity_out_20 = _print(records1)[20]
    photovoltaic_electricity_out_21 = _print(records1)[21]
    photovoltaic_electricity_out_22 = _print(records1)[22]
    photovoltaic_electricity_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['photovoltaic_electricity_out_0', 'photovoltaic_electricity_out_1', 'photovoltaic_electricity_out_2', 'photovoltaic_electricity_out_3',
         'photovoltaic_electricity_out_4',
         'photovoltaic_electricity_out_5', 'photovoltaic_electricity_out_6', 'photovoltaic_electricity_out_7', 'photovoltaic_electricity_out_8',
         'photovoltaic_electricity_out_9',
         'photovoltaic_electricity_out_10', 'photovoltaic_electricity_out_11', 'photovoltaic_electricity_out_12', 'photovoltaic_electricity_out_13',
         'photovoltaic_electricity_out_14',
         'photovoltaic_electricity_out_15', 'photovoltaic_electricity_out_16', 'photovoltaic_electricity_out_17', 'photovoltaic_electricity_out_18',
         'photovoltaic_electricity_out_19',
         'photovoltaic_electricity_out_20', 'photovoltaic_electricity_out_21', 'photovoltaic_electricity_out_22', 'photovoltaic_electricity_out_23'],
        [photovoltaic_electricity_out_0, photovoltaic_electricity_out_1, photovoltaic_electricity_out_2, photovoltaic_electricity_out_3,
         photovoltaic_electricity_out_4,
         photovoltaic_electricity_out_5, photovoltaic_electricity_out_6, photovoltaic_electricity_out_7, photovoltaic_electricity_out_8,
         photovoltaic_electricity_out_9,
         photovoltaic_electricity_out_10, photovoltaic_electricity_out_11, photovoltaic_electricity_out_12, photovoltaic_electricity_out_13,
         photovoltaic_electricity_out_14,
         photovoltaic_electricity_out_15, photovoltaic_electricity_out_16, photovoltaic_electricity_out_17, photovoltaic_electricity_out_18,
         photovoltaic_electricity_out_19,
         photovoltaic_electricity_out_20, photovoltaic_electricity_out_21, photovoltaic_electricity_out_22, photovoltaic_electricity_out_23])


def write_to_database_wind_electricity_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入风力发电功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('wind_electricity_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    wind_electricity_out_0 = _print(records1)[0]
    wind_electricity_out_1 = _print(records1)[1]
    wind_electricity_out_2 = _print(records1)[2]
    wind_electricity_out_3 = _print(records1)[3]
    wind_electricity_out_4 = _print(records1)[4]
    wind_electricity_out_5 = _print(records1)[5]
    wind_electricity_out_6 = _print(records1)[6]
    wind_electricity_out_7 = _print(records1)[7]
    wind_electricity_out_8 = _print(records1)[8]
    wind_electricity_out_9 = _print(records1)[9]
    wind_electricity_out_10 = _print(records1)[10]
    wind_electricity_out_11 = _print(records1)[11]
    wind_electricity_out_12 = _print(records1)[12]
    wind_electricity_out_13 = _print(records1)[13]
    wind_electricity_out_14 = _print(records1)[14]
    wind_electricity_out_15 = _print(records1)[15]
    wind_electricity_out_16 = _print(records1)[16]
    wind_electricity_out_17 = _print(records1)[17]
    wind_electricity_out_18 = _print(records1)[18]
    wind_electricity_out_19 = _print(records1)[19]
    wind_electricity_out_20 = _print(records1)[20]
    wind_electricity_out_21 = _print(records1)[21]
    wind_electricity_out_22 = _print(records1)[22]
    wind_electricity_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['wind_electricity_out_0', 'wind_electricity_out_1', 'wind_electricity_out_2', 'wind_electricity_out_3',
         'wind_electricity_out_4',
         'wind_electricity_out_5', 'wind_electricity_out_6', 'wind_electricity_out_7', 'wind_electricity_out_8',
         'wind_electricity_out_9',
         'wind_electricity_out_10', 'wind_electricity_out_11', 'wind_electricity_out_12', 'wind_electricity_out_13',
         'wind_electricity_out_14',
         'wind_electricity_out_15', 'wind_electricity_out_16', 'wind_electricity_out_17', 'wind_electricity_out_18',
         'wind_electricity_out_19',
         'wind_electricity_out_20', 'wind_electricity_out_21', 'wind_electricity_out_22', 'wind_electricity_out_23'],
        [wind_electricity_out_0, wind_electricity_out_1, wind_electricity_out_2, wind_electricity_out_3,
         wind_electricity_out_4,
         wind_electricity_out_5, wind_electricity_out_6, wind_electricity_out_7, wind_electricity_out_8,
         wind_electricity_out_9,
         wind_electricity_out_10, wind_electricity_out_11, wind_electricity_out_12, wind_electricity_out_13,
         wind_electricity_out_14,
         wind_electricity_out_15, wind_electricity_out_16, wind_electricity_out_17, wind_electricity_out_18,
         wind_electricity_out_19,
         wind_electricity_out_20, wind_electricity_out_21, wind_electricity_out_22, wind_electricity_out_23])


def write_to_database_lb_cold_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制冷功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_cold_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_cold_out_0 = _print(records1)[0]
    lb_cold_out_1 = _print(records1)[1]
    lb_cold_out_2 = _print(records1)[2]
    lb_cold_out_3 = _print(records1)[3]
    lb_cold_out_4 = _print(records1)[4]
    lb_cold_out_5 = _print(records1)[5]
    lb_cold_out_6 = _print(records1)[6]
    lb_cold_out_7 = _print(records1)[7]
    lb_cold_out_8 = _print(records1)[8]
    lb_cold_out_9 = _print(records1)[9]
    lb_cold_out_10 = _print(records1)[10]
    lb_cold_out_11 = _print(records1)[11]
    lb_cold_out_12 = _print(records1)[12]
    lb_cold_out_13 = _print(records1)[13]
    lb_cold_out_14 = _print(records1)[14]
    lb_cold_out_15 = _print(records1)[15]
    lb_cold_out_16 = _print(records1)[16]
    lb_cold_out_17 = _print(records1)[17]
    lb_cold_out_18 = _print(records1)[18]
    lb_cold_out_19 = _print(records1)[19]
    lb_cold_out_20 = _print(records1)[20]
    lb_cold_out_21 = _print(records1)[21]
    lb_cold_out_22 = _print(records1)[22]
    lb_cold_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_cold_out_0', 'lb_cold_out_1', 'lb_cold_out_2', 'lb_cold_out_3', 'lb_cold_out_4',
         'lb_cold_out_5', 'lb_cold_out_6', 'lb_cold_out_7', 'lb_cold_out_8', 'lb_cold_out_9',
         'lb_cold_out_10', 'lb_cold_out_11', 'lb_cold_out_12', 'lb_cold_out_13', 'lb_cold_out_14',
         'lb_cold_out_15', 'lb_cold_out_16', 'lb_cold_out_17', 'lb_cold_out_18', 'lb_cold_out_19',
         'lb_cold_out_20', 'lb_cold_out_21', 'lb_cold_out_22', 'lb_cold_out_23'],
        [lb_cold_out_0, lb_cold_out_1, lb_cold_out_2, lb_cold_out_3, lb_cold_out_4,
         lb_cold_out_5, lb_cold_out_6, lb_cold_out_7, lb_cold_out_8, lb_cold_out_9,
         lb_cold_out_10, lb_cold_out_11, lb_cold_out_12, lb_cold_out_13, lb_cold_out_14,
         lb_cold_out_15, lb_cold_out_16, lb_cold_out_17, lb_cold_out_18, lb_cold_out_19,
         lb_cold_out_20, lb_cold_out_21, lb_cold_out_22, lb_cold_out_23])


def write_to_database_cc_cold_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机制冷功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc_cold_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    cc_cold_out_0 = _print(records1)[0]
    cc_cold_out_1 = _print(records1)[1]
    cc_cold_out_2 = _print(records1)[2]
    cc_cold_out_3 = _print(records1)[3]
    cc_cold_out_4 = _print(records1)[4]
    cc_cold_out_5 = _print(records1)[5]
    cc_cold_out_6 = _print(records1)[6]
    cc_cold_out_7 = _print(records1)[7]
    cc_cold_out_8 = _print(records1)[8]
    cc_cold_out_9 = _print(records1)[9]
    cc_cold_out_10 = _print(records1)[10]
    cc_cold_out_11 = _print(records1)[11]
    cc_cold_out_12 = _print(records1)[12]
    cc_cold_out_13 = _print(records1)[13]
    cc_cold_out_14 = _print(records1)[14]
    cc_cold_out_15 = _print(records1)[15]
    cc_cold_out_16 = _print(records1)[16]
    cc_cold_out_17 = _print(records1)[17]
    cc_cold_out_18 = _print(records1)[18]
    cc_cold_out_19 = _print(records1)[19]
    cc_cold_out_20 = _print(records1)[20]
    cc_cold_out_21 = _print(records1)[21]
    cc_cold_out_22 = _print(records1)[22]
    cc_cold_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc_cold_out_0', 'cc_cold_out_1', 'cc_cold_out_2', 'cc_cold_out_3', 'cc_cold_out_4',
         'cc_cold_out_5', 'cc_cold_out_6', 'cc_cold_out_7', 'cc_cold_out_8', 'cc_cold_out_9',
         'cc_cold_out_10', 'cc_cold_out_11', 'cc_cold_out_12', 'cc_cold_out_13', 'cc_cold_out_14',
         'cc_cold_out_15', 'cc_cold_out_16', 'cc_cold_out_17', 'cc_cold_out_18', 'cc_cold_out_19',
         'cc_cold_out_20', 'cc_cold_out_21', 'cc_cold_out_22', 'cc_cold_out_23'],
        [cc_cold_out_0, cc_cold_out_1, cc_cold_out_2, cc_cold_out_3, cc_cold_out_4,
         cc_cold_out_5, cc_cold_out_6, cc_cold_out_7, cc_cold_out_8, cc_cold_out_9,
         cc_cold_out_10, cc_cold_out_11, cc_cold_out_12, cc_cold_out_13, cc_cold_out_14,
         cc_cold_out_15, cc_cold_out_16, cc_cold_out_17, cc_cold_out_18, cc_cold_out_19,
         cc_cold_out_20, cc_cold_out_21, cc_cold_out_22, cc_cold_out_23])


def write_to_database_chp_cold_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制冷功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_cold_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_cold_out_0 = _print(records1)[0]
    chp_cold_out_1 = _print(records1)[1]
    chp_cold_out_2 = _print(records1)[2]
    chp_cold_out_3 = _print(records1)[3]
    chp_cold_out_4 = _print(records1)[4]
    chp_cold_out_5 = _print(records1)[5]
    chp_cold_out_6 = _print(records1)[6]
    chp_cold_out_7 = _print(records1)[7]
    chp_cold_out_8 = _print(records1)[8]
    chp_cold_out_9 = _print(records1)[9]
    chp_cold_out_10 = _print(records1)[10]
    chp_cold_out_11 = _print(records1)[11]
    chp_cold_out_12 = _print(records1)[12]
    chp_cold_out_13 = _print(records1)[13]
    chp_cold_out_14 = _print(records1)[14]
    chp_cold_out_15 = _print(records1)[15]
    chp_cold_out_16 = _print(records1)[16]
    chp_cold_out_17 = _print(records1)[17]
    chp_cold_out_18 = _print(records1)[18]
    chp_cold_out_19 = _print(records1)[19]
    chp_cold_out_20 = _print(records1)[20]
    chp_cold_out_21 = _print(records1)[21]
    chp_cold_out_22 = _print(records1)[22]
    chp_cold_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_cold_out_0', 'chp_cold_out_1', 'chp_cold_out_2', 'chp_cold_out_3', 'chp_cold_out_4',
         'chp_cold_out_5', 'chp_cold_out_6', 'chp_cold_out_7', 'chp_cold_out_8', 'chp_cold_out_9',
         'chp_cold_out_10', 'chp_cold_out_11', 'chp_cold_out_12', 'chp_cold_out_13', 'chp_cold_out_14',
         'chp_cold_out_15', 'chp_cold_out_16', 'chp_cold_out_17', 'chp_cold_out_18', 'chp_cold_out_19',
         'chp_cold_out_20', 'chp_cold_out_21', 'chp_cold_out_22', 'chp_cold_out_23'],
        [chp_cold_out_0, chp_cold_out_1, chp_cold_out_2, chp_cold_out_3, chp_cold_out_4,
         chp_cold_out_5, chp_cold_out_6, chp_cold_out_7, chp_cold_out_8, chp_cold_out_9,
         chp_cold_out_10, chp_cold_out_11, chp_cold_out_12, chp_cold_out_13, chp_cold_out_14,
         chp_cold_out_15, chp_cold_out_16, chp_cold_out_17, chp_cold_out_18, chp_cold_out_19,
         chp_cold_out_20, chp_cold_out_21, chp_cold_out_22, chp_cold_out_23])


def write_to_database_ashp_cold_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制冷功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_cold_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_cold_out_0 = _print(records1)[0]
    ashp_cold_out_1 = _print(records1)[1]
    ashp_cold_out_2 = _print(records1)[2]
    ashp_cold_out_3 = _print(records1)[3]
    ashp_cold_out_4 = _print(records1)[4]
    ashp_cold_out_5 = _print(records1)[5]
    ashp_cold_out_6 = _print(records1)[6]
    ashp_cold_out_7 = _print(records1)[7]
    ashp_cold_out_8 = _print(records1)[8]
    ashp_cold_out_9 = _print(records1)[9]
    ashp_cold_out_10 = _print(records1)[10]
    ashp_cold_out_11 = _print(records1)[11]
    ashp_cold_out_12 = _print(records1)[12]
    ashp_cold_out_13 = _print(records1)[13]
    ashp_cold_out_14 = _print(records1)[14]
    ashp_cold_out_15 = _print(records1)[15]
    ashp_cold_out_16 = _print(records1)[16]
    ashp_cold_out_17 = _print(records1)[17]
    ashp_cold_out_18 = _print(records1)[18]
    ashp_cold_out_19 = _print(records1)[19]
    ashp_cold_out_20 = _print(records1)[20]
    ashp_cold_out_21 = _print(records1)[21]
    ashp_cold_out_22 = _print(records1)[22]
    ashp_cold_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_cold_out_0', 'ashp_cold_out_1', 'ashp_cold_out_2', 'ashp_cold_out_3', 'ashp_cold_out_4',
         'ashp_cold_out_5', 'ashp_cold_out_6', 'ashp_cold_out_7', 'ashp_cold_out_8', 'ashp_cold_out_9',
         'ashp_cold_out_10', 'ashp_cold_out_11', 'ashp_cold_out_12', 'ashp_cold_out_13', 'ashp_cold_out_14',
         'ashp_cold_out_15', 'ashp_cold_out_16', 'ashp_cold_out_17', 'ashp_cold_out_18', 'ashp_cold_out_19',
         'ashp_cold_out_20', 'ashp_cold_out_21', 'ashp_cold_out_22', 'ashp_cold_out_23'],
        [ashp_cold_out_0, ashp_cold_out_1, ashp_cold_out_2, ashp_cold_out_3, ashp_cold_out_4,
         ashp_cold_out_5, ashp_cold_out_6, ashp_cold_out_7, ashp_cold_out_8, ashp_cold_out_9,
         ashp_cold_out_10, ashp_cold_out_11, ashp_cold_out_12, ashp_cold_out_13, ashp_cold_out_14,
         ashp_cold_out_15, ashp_cold_out_16, ashp_cold_out_17, ashp_cold_out_18, ashp_cold_out_19,
         ashp_cold_out_20, ashp_cold_out_21, ashp_cold_out_22, ashp_cold_out_23])


def write_to_database_ese_cold_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷水罐制冷功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ese_cold_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ese_cold_out_0 = _print(records1)[0]
    ese_cold_out_1 = _print(records1)[1]
    ese_cold_out_2 = _print(records1)[2]
    ese_cold_out_3 = _print(records1)[3]
    ese_cold_out_4 = _print(records1)[4]
    ese_cold_out_5 = _print(records1)[5]
    ese_cold_out_6 = _print(records1)[6]
    ese_cold_out_7 = _print(records1)[7]
    ese_cold_out_8 = _print(records1)[8]
    ese_cold_out_9 = _print(records1)[9]
    ese_cold_out_10 = _print(records1)[10]
    ese_cold_out_11 = _print(records1)[11]
    ese_cold_out_12 = _print(records1)[12]
    ese_cold_out_13 = _print(records1)[13]
    ese_cold_out_14 = _print(records1)[14]
    ese_cold_out_15 = _print(records1)[15]
    ese_cold_out_16 = _print(records1)[16]
    ese_cold_out_17 = _print(records1)[17]
    ese_cold_out_18 = _print(records1)[18]
    ese_cold_out_19 = _print(records1)[19]
    ese_cold_out_20 = _print(records1)[20]
    ese_cold_out_21 = _print(records1)[21]
    ese_cold_out_22 = _print(records1)[22]
    ese_cold_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese_cold_out_0', 'ese_cold_out_1', 'ese_cold_out_2', 'ese_cold_out_3', 'ese_cold_out_4',
         'ese_cold_out_5', 'ese_cold_out_6', 'ese_cold_out_7', 'ese_cold_out_8', 'ese_cold_out_9',
         'ese_cold_out_10', 'ese_cold_out_11', 'ese_cold_out_12', 'ese_cold_out_13', 'ese_cold_out_14',
         'ese_cold_out_15', 'ese_cold_out_16', 'ese_cold_out_17', 'ese_cold_out_18', 'ese_cold_out_19',
         'ese_cold_out_20', 'ese_cold_out_21', 'ese_cold_out_22', 'ese_cold_out_23'],
        [ese_cold_out_0, ese_cold_out_1, ese_cold_out_2, ese_cold_out_3, ese_cold_out_4,
         ese_cold_out_5, ese_cold_out_6, ese_cold_out_7, ese_cold_out_8, ese_cold_out_9,
         ese_cold_out_10, ese_cold_out_11, ese_cold_out_12, ese_cold_out_13, ese_cold_out_14,
         ese_cold_out_15, ese_cold_out_16, ese_cold_out_17, ese_cold_out_18, ese_cold_out_19,
         ese_cold_out_20, ese_cold_out_21, ese_cold_out_22, ese_cold_out_23])

def write_to_database_lb_heat_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制热功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_heat_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_heat_out_0 = _print(records1)[0]
    lb_heat_out_1 = _print(records1)[1]
    lb_heat_out_2 = _print(records1)[2]
    lb_heat_out_3 = _print(records1)[3]
    lb_heat_out_4 = _print(records1)[4]
    lb_heat_out_5 = _print(records1)[5]
    lb_heat_out_6 = _print(records1)[6]
    lb_heat_out_7 = _print(records1)[7]
    lb_heat_out_8 = _print(records1)[8]
    lb_heat_out_9 = _print(records1)[9]
    lb_heat_out_10 = _print(records1)[10]
    lb_heat_out_11 = _print(records1)[11]
    lb_heat_out_12 = _print(records1)[12]
    lb_heat_out_13 = _print(records1)[13]
    lb_heat_out_14 = _print(records1)[14]
    lb_heat_out_15 = _print(records1)[15]
    lb_heat_out_16 = _print(records1)[16]
    lb_heat_out_17 = _print(records1)[17]
    lb_heat_out_18 = _print(records1)[18]
    lb_heat_out_19 = _print(records1)[19]
    lb_heat_out_20 = _print(records1)[20]
    lb_heat_out_21 = _print(records1)[21]
    lb_heat_out_22 = _print(records1)[22]
    lb_heat_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_heat_out_0', 'lb_heat_out_1', 'lb_heat_out_2', 'lb_heat_out_3', 'lb_heat_out_4',
         'lb_heat_out_5', 'lb_heat_out_6', 'lb_heat_out_7', 'lb_heat_out_8', 'lb_heat_out_9',
         'lb_heat_out_10', 'lb_heat_out_11', 'lb_heat_out_12', 'lb_heat_out_13', 'lb_heat_out_14',
         'lb_heat_out_15', 'lb_heat_out_16', 'lb_heat_out_17', 'lb_heat_out_18', 'lb_heat_out_19',
         'lb_heat_out_20', 'lb_heat_out_21', 'lb_heat_out_22', 'lb_heat_out_23'],
        [lb_heat_out_0, lb_heat_out_1, lb_heat_out_2, lb_heat_out_3, lb_heat_out_4,
         lb_heat_out_5, lb_heat_out_6, lb_heat_out_7, lb_heat_out_8, lb_heat_out_9,
         lb_heat_out_10, lb_heat_out_11, lb_heat_out_12, lb_heat_out_13, lb_heat_out_14,
         lb_heat_out_15, lb_heat_out_16, lb_heat_out_17, lb_heat_out_18, lb_heat_out_19,
         lb_heat_out_20, lb_heat_out_21, lb_heat_out_22, lb_heat_out_23])


def write_to_database_chp_heat_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制热功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_heat_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_heat_out_0 = _print(records1)[0]
    chp_heat_out_1 = _print(records1)[1]
    chp_heat_out_2 = _print(records1)[2]
    chp_heat_out_3 = _print(records1)[3]
    chp_heat_out_4 = _print(records1)[4]
    chp_heat_out_5 = _print(records1)[5]
    chp_heat_out_6 = _print(records1)[6]
    chp_heat_out_7 = _print(records1)[7]
    chp_heat_out_8 = _print(records1)[8]
    chp_heat_out_9 = _print(records1)[9]
    chp_heat_out_10 = _print(records1)[10]
    chp_heat_out_11 = _print(records1)[11]
    chp_heat_out_12 = _print(records1)[12]
    chp_heat_out_13 = _print(records1)[13]
    chp_heat_out_14 = _print(records1)[14]
    chp_heat_out_15 = _print(records1)[15]
    chp_heat_out_16 = _print(records1)[16]
    chp_heat_out_17 = _print(records1)[17]
    chp_heat_out_18 = _print(records1)[18]
    chp_heat_out_19 = _print(records1)[19]
    chp_heat_out_20 = _print(records1)[20]
    chp_heat_out_21 = _print(records1)[21]
    chp_heat_out_22 = _print(records1)[22]
    chp_heat_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_heat_out_0', 'chp_heat_out_1', 'chp_heat_out_2', 'chp_heat_out_3', 'chp_heat_out_4',
         'chp_heat_out_5', 'chp_heat_out_6', 'chp_heat_out_7', 'chp_heat_out_8', 'chp_heat_out_9',
         'chp_heat_out_10', 'chp_heat_out_11', 'chp_heat_out_12', 'chp_heat_out_13', 'chp_heat_out_14',
         'chp_heat_out_15', 'chp_heat_out_16', 'chp_heat_out_17', 'chp_heat_out_18', 'chp_heat_out_19',
         'chp_heat_out_20', 'chp_heat_out_21', 'chp_heat_out_22', 'chp_heat_out_23'],
        [chp_heat_out_0, chp_heat_out_1, chp_heat_out_2, chp_heat_out_3, chp_heat_out_4,
         chp_heat_out_5, chp_heat_out_6, chp_heat_out_7, chp_heat_out_8, chp_heat_out_9,
         chp_heat_out_10, chp_heat_out_11, chp_heat_out_12, chp_heat_out_13, chp_heat_out_14,
         chp_heat_out_15, chp_heat_out_16, chp_heat_out_17, chp_heat_out_18, chp_heat_out_19,
         chp_heat_out_20, chp_heat_out_21, chp_heat_out_22, chp_heat_out_23])


def write_to_database_ese_heat_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄热水罐制热功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ese_heat_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ese_heat_out_0 = _print(records1)[0]
    ese_heat_out_1 = _print(records1)[1]
    ese_heat_out_2 = _print(records1)[2]
    ese_heat_out_3 = _print(records1)[3]
    ese_heat_out_4 = _print(records1)[4]
    ese_heat_out_5 = _print(records1)[5]
    ese_heat_out_6 = _print(records1)[6]
    ese_heat_out_7 = _print(records1)[7]
    ese_heat_out_8 = _print(records1)[8]
    ese_heat_out_9 = _print(records1)[9]
    ese_heat_out_10 = _print(records1)[10]
    ese_heat_out_11 = _print(records1)[11]
    ese_heat_out_12 = _print(records1)[12]
    ese_heat_out_13 = _print(records1)[13]
    ese_heat_out_14 = _print(records1)[14]
    ese_heat_out_15 = _print(records1)[15]
    ese_heat_out_16 = _print(records1)[16]
    ese_heat_out_17 = _print(records1)[17]
    ese_heat_out_18 = _print(records1)[18]
    ese_heat_out_19 = _print(records1)[19]
    ese_heat_out_20 = _print(records1)[20]
    ese_heat_out_21 = _print(records1)[21]
    ese_heat_out_22 = _print(records1)[22]
    ese_heat_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ese_heat_out_0', 'ese_heat_out_1', 'ese_heat_out_2', 'ese_heat_out_3', 'ese_heat_out_4',
         'ese_heat_out_5', 'ese_heat_out_6', 'ese_heat_out_7', 'ese_heat_out_8', 'ese_heat_out_9',
         'ese_heat_out_10', 'ese_heat_out_11', 'ese_heat_out_12', 'ese_heat_out_13', 'ese_heat_out_14',
         'ese_heat_out_15', 'ese_heat_out_16', 'ese_heat_out_17', 'ese_heat_out_18', 'ese_heat_out_19',
         'ese_heat_out_20', 'ese_heat_out_21', 'ese_heat_out_22', 'ese_heat_out_23'],
        [ese_heat_out_0, ese_heat_out_1, ese_heat_out_2, ese_heat_out_3, ese_heat_out_4,
         ese_heat_out_5, ese_heat_out_6, ese_heat_out_7, ese_heat_out_8, ese_heat_out_9,
         ese_heat_out_10, ese_heat_out_11, ese_heat_out_12, ese_heat_out_13, ese_heat_out_14,
         ese_heat_out_15, ese_heat_out_16, ese_heat_out_17, ese_heat_out_18, ese_heat_out_19,
         ese_heat_out_20, ese_heat_out_21, ese_heat_out_22, ese_heat_out_23])


def write_to_database_lb_hot_water_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂生活热水功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_hot_water_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_hot_water_out_0 = _print(records1)[0]
    lb_hot_water_out_1 = _print(records1)[1]
    lb_hot_water_out_2 = _print(records1)[2]
    lb_hot_water_out_3 = _print(records1)[3]
    lb_hot_water_out_4 = _print(records1)[4]
    lb_hot_water_out_5 = _print(records1)[5]
    lb_hot_water_out_6 = _print(records1)[6]
    lb_hot_water_out_7 = _print(records1)[7]
    lb_hot_water_out_8 = _print(records1)[8]
    lb_hot_water_out_9 = _print(records1)[9]
    lb_hot_water_out_10 = _print(records1)[10]
    lb_hot_water_out_11 = _print(records1)[11]
    lb_hot_water_out_12 = _print(records1)[12]
    lb_hot_water_out_13 = _print(records1)[13]
    lb_hot_water_out_14 = _print(records1)[14]
    lb_hot_water_out_15 = _print(records1)[15]
    lb_hot_water_out_16 = _print(records1)[16]
    lb_hot_water_out_17 = _print(records1)[17]
    lb_hot_water_out_18 = _print(records1)[18]
    lb_hot_water_out_19 = _print(records1)[19]
    lb_hot_water_out_20 = _print(records1)[20]
    lb_hot_water_out_21 = _print(records1)[21]
    lb_hot_water_out_22 = _print(records1)[22]
    lb_hot_water_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_hot_water_out_0', 'lb_hot_water_out_1', 'lb_hot_water_out_2', 'lb_hot_water_out_3', 'lb_hot_water_out_4',
         'lb_hot_water_out_5', 'lb_hot_water_out_6', 'lb_hot_water_out_7', 'lb_hot_water_out_8', 'lb_hot_water_out_9',
         'lb_hot_water_out_10', 'lb_hot_water_out_11', 'lb_hot_water_out_12', 'lb_hot_water_out_13', 'lb_hot_water_out_14',
         'lb_hot_water_out_15', 'lb_hot_water_out_16', 'lb_hot_water_out_17', 'lb_hot_water_out_18', 'lb_hot_water_out_19',
         'lb_hot_water_out_20', 'lb_hot_water_out_21', 'lb_hot_water_out_22', 'lb_hot_water_out_23'],
        [lb_hot_water_out_0, lb_hot_water_out_1, lb_hot_water_out_2, lb_hot_water_out_3, lb_hot_water_out_4,
         lb_hot_water_out_5, lb_hot_water_out_6, lb_hot_water_out_7, lb_hot_water_out_8, lb_hot_water_out_9,
         lb_hot_water_out_10, lb_hot_water_out_11, lb_hot_water_out_12, lb_hot_water_out_13, lb_hot_water_out_14,
         lb_hot_water_out_15, lb_hot_water_out_16, lb_hot_water_out_17, lb_hot_water_out_18, lb_hot_water_out_19,
         lb_hot_water_out_20, lb_hot_water_out_21, lb_hot_water_out_22, lb_hot_water_out_23])


def write_to_database_ngb_hot_water_out_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入天然气锅炉生活热水功率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ngb_hot_water_out_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ngb_hot_water_out_0 = _print(records1)[0]
    ngb_hot_water_out_1 = _print(records1)[1]
    ngb_hot_water_out_2 = _print(records1)[2]
    ngb_hot_water_out_3 = _print(records1)[3]
    ngb_hot_water_out_4 = _print(records1)[4]
    ngb_hot_water_out_5 = _print(records1)[5]
    ngb_hot_water_out_6 = _print(records1)[6]
    ngb_hot_water_out_7 = _print(records1)[7]
    ngb_hot_water_out_8 = _print(records1)[8]
    ngb_hot_water_out_9 = _print(records1)[9]
    ngb_hot_water_out_10 = _print(records1)[10]
    ngb_hot_water_out_11 = _print(records1)[11]
    ngb_hot_water_out_12 = _print(records1)[12]
    ngb_hot_water_out_13 = _print(records1)[13]
    ngb_hot_water_out_14 = _print(records1)[14]
    ngb_hot_water_out_15 = _print(records1)[15]
    ngb_hot_water_out_16 = _print(records1)[16]
    ngb_hot_water_out_17 = _print(records1)[17]
    ngb_hot_water_out_18 = _print(records1)[18]
    ngb_hot_water_out_19 = _print(records1)[19]
    ngb_hot_water_out_20 = _print(records1)[20]
    ngb_hot_water_out_21 = _print(records1)[21]
    ngb_hot_water_out_22 = _print(records1)[22]
    ngb_hot_water_out_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb_hot_water_out_0', 'ngb_hot_water_out_1', 'ngb_hot_water_out_2', 'ngb_hot_water_out_3', 'ngb_hot_water_out_4',
         'ngb_hot_water_out_5', 'ngb_hot_water_out_6', 'ngb_hot_water_out_7', 'ngb_hot_water_out_8', 'ngb_hot_water_out_9',
         'ngb_hot_water_out_10', 'ngb_hot_water_out_11', 'ngb_hot_water_out_12', 'ngb_hot_water_out_13', 'ngb_hot_water_out_14',
         'ngb_hot_water_out_15', 'ngb_hot_water_out_16', 'ngb_hot_water_out_17', 'ngb_hot_water_out_18', 'ngb_hot_water_out_19',
         'ngb_hot_water_out_20', 'ngb_hot_water_out_21', 'ngb_hot_water_out_22', 'ngb_hot_water_out_23'],
        [ngb_hot_water_out_0, ngb_hot_water_out_1, ngb_hot_water_out_2, ngb_hot_water_out_3, ngb_hot_water_out_4,
         ngb_hot_water_out_5, ngb_hot_water_out_6, ngb_hot_water_out_7, ngb_hot_water_out_8, ngb_hot_water_out_9,
         ngb_hot_water_out_10, ngb_hot_water_out_11, ngb_hot_water_out_12, ngb_hot_water_out_13, ngb_hot_water_out_14,
         ngb_hot_water_out_15, ngb_hot_water_out_16, ngb_hot_water_out_17, ngb_hot_water_out_18, ngb_hot_water_out_19,
         ngb_hot_water_out_20, ngb_hot_water_out_21, ngb_hot_water_out_22, ngb_hot_water_out_23])


def write_to_database_reduction_in_carbon_emissions_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入碳排放减少量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('reduction_in_carbon_emissions',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    reduction_in_carbon_emissions_0 = _print(records1)[0]
    reduction_in_carbon_emissions_1 = _print(records1)[1]
    reduction_in_carbon_emissions_2 = _print(records1)[2]
    reduction_in_carbon_emissions_3 = _print(records1)[3]
    reduction_in_carbon_emissions_4 = _print(records1)[4]
    reduction_in_carbon_emissions_5 = _print(records1)[5]
    reduction_in_carbon_emissions_6 = _print(records1)[6]
    reduction_in_carbon_emissions_7 = _print(records1)[7]
    reduction_in_carbon_emissions_8 = _print(records1)[8]
    reduction_in_carbon_emissions_9 = _print(records1)[9]
    reduction_in_carbon_emissions_10 = _print(records1)[10]
    reduction_in_carbon_emissions_11 = _print(records1)[11]
    reduction_in_carbon_emissions_12 = _print(records1)[12]
    reduction_in_carbon_emissions_13 = _print(records1)[13]
    reduction_in_carbon_emissions_14 = _print(records1)[14]
    reduction_in_carbon_emissions_15 = _print(records1)[15]
    reduction_in_carbon_emissions_16 = _print(records1)[16]
    reduction_in_carbon_emissions_17 = _print(records1)[17]
    reduction_in_carbon_emissions_18 = _print(records1)[18]
    reduction_in_carbon_emissions_19 = _print(records1)[19]
    reduction_in_carbon_emissions_20 = _print(records1)[20]
    reduction_in_carbon_emissions_21 = _print(records1)[21]
    reduction_in_carbon_emissions_22 = _print(records1)[22]
    reduction_in_carbon_emissions_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['reduction_in_carbon_emissions_0', 'reduction_in_carbon_emissions_1', 'reduction_in_carbon_emissions_2',
         'reduction_in_carbon_emissions_3', 'reduction_in_carbon_emissions_4', 'reduction_in_carbon_emissions_5',
         'reduction_in_carbon_emissions_6', 'reduction_in_carbon_emissions_7', 'reduction_in_carbon_emissions_8',
         'reduction_in_carbon_emissions_9', 'reduction_in_carbon_emissions_10', 'reduction_in_carbon_emissions_11',
         'reduction_in_carbon_emissions_12', 'reduction_in_carbon_emissions_13', 'reduction_in_carbon_emissions_14',
         'reduction_in_carbon_emissions_15', 'reduction_in_carbon_emissions_16', 'reduction_in_carbon_emissions_17',
         'reduction_in_carbon_emissions_18', 'reduction_in_carbon_emissions_19', 'reduction_in_carbon_emissions_20',
         'reduction_in_carbon_emissions_21', 'reduction_in_carbon_emissions_22', 'reduction_in_carbon_emissions_23'],
        [reduction_in_carbon_emissions_0, reduction_in_carbon_emissions_1, reduction_in_carbon_emissions_2,
         reduction_in_carbon_emissions_3, reduction_in_carbon_emissions_4, reduction_in_carbon_emissions_5,
         reduction_in_carbon_emissions_6, reduction_in_carbon_emissions_7, reduction_in_carbon_emissions_8,
         reduction_in_carbon_emissions_9, reduction_in_carbon_emissions_10, reduction_in_carbon_emissions_11,
         reduction_in_carbon_emissions_12, reduction_in_carbon_emissions_13, reduction_in_carbon_emissions_14,
         reduction_in_carbon_emissions_15, reduction_in_carbon_emissions_16, reduction_in_carbon_emissions_17,
         reduction_in_carbon_emissions_18, reduction_in_carbon_emissions_19, reduction_in_carbon_emissions_20,
         reduction_in_carbon_emissions_21, reduction_in_carbon_emissions_22, reduction_in_carbon_emissions_23])


def write_to_database_reduction_in_sulfide_emissions_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入硫化物排放减少量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('reduction_in_sulfide_emissions',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    reduction_in_sulfide_emissions_0 = _print(records1)[0]
    reduction_in_sulfide_emissions_1 = _print(records1)[1]
    reduction_in_sulfide_emissions_2 = _print(records1)[2]
    reduction_in_sulfide_emissions_3 = _print(records1)[3]
    reduction_in_sulfide_emissions_4 = _print(records1)[4]
    reduction_in_sulfide_emissions_5 = _print(records1)[5]
    reduction_in_sulfide_emissions_6 = _print(records1)[6]
    reduction_in_sulfide_emissions_7 = _print(records1)[7]
    reduction_in_sulfide_emissions_8 = _print(records1)[8]
    reduction_in_sulfide_emissions_9 = _print(records1)[9]
    reduction_in_sulfide_emissions_10 = _print(records1)[10]
    reduction_in_sulfide_emissions_11 = _print(records1)[11]
    reduction_in_sulfide_emissions_12 = _print(records1)[12]
    reduction_in_sulfide_emissions_13 = _print(records1)[13]
    reduction_in_sulfide_emissions_14 = _print(records1)[14]
    reduction_in_sulfide_emissions_15 = _print(records1)[15]
    reduction_in_sulfide_emissions_16 = _print(records1)[16]
    reduction_in_sulfide_emissions_17 = _print(records1)[17]
    reduction_in_sulfide_emissions_18 = _print(records1)[18]
    reduction_in_sulfide_emissions_19 = _print(records1)[19]
    reduction_in_sulfide_emissions_20 = _print(records1)[20]
    reduction_in_sulfide_emissions_21 = _print(records1)[21]
    reduction_in_sulfide_emissions_22 = _print(records1)[22]
    reduction_in_sulfide_emissions_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['reduction_in_sulfide_emissions_0', 'reduction_in_sulfide_emissions_1', 'reduction_in_sulfide_emissions_2',
         'reduction_in_sulfide_emissions_3', 'reduction_in_sulfide_emissions_4', 'reduction_in_sulfide_emissions_5',
         'reduction_in_sulfide_emissions_6', 'reduction_in_sulfide_emissions_7', 'reduction_in_sulfide_emissions_8',
         'reduction_in_sulfide_emissions_9', 'reduction_in_sulfide_emissions_10', 'reduction_in_sulfide_emissions_11',
         'reduction_in_sulfide_emissions_12', 'reduction_in_sulfide_emissions_13', 'reduction_in_sulfide_emissions_14',
         'reduction_in_sulfide_emissions_15', 'reduction_in_sulfide_emissions_16', 'reduction_in_sulfide_emissions_17',
         'reduction_in_sulfide_emissions_18', 'reduction_in_sulfide_emissions_19', 'reduction_in_sulfide_emissions_20',
         'reduction_in_sulfide_emissions_21', 'reduction_in_sulfide_emissions_22', 'reduction_in_sulfide_emissions_23'],
        [reduction_in_sulfide_emissions_0, reduction_in_sulfide_emissions_1, reduction_in_sulfide_emissions_2,
         reduction_in_sulfide_emissions_3, reduction_in_sulfide_emissions_4, reduction_in_sulfide_emissions_5,
         reduction_in_sulfide_emissions_6, reduction_in_sulfide_emissions_7, reduction_in_sulfide_emissions_8,
         reduction_in_sulfide_emissions_9, reduction_in_sulfide_emissions_10, reduction_in_sulfide_emissions_11,
         reduction_in_sulfide_emissions_12, reduction_in_sulfide_emissions_13, reduction_in_sulfide_emissions_14,
         reduction_in_sulfide_emissions_15, reduction_in_sulfide_emissions_16, reduction_in_sulfide_emissions_17,
         reduction_in_sulfide_emissions_18, reduction_in_sulfide_emissions_19, reduction_in_sulfide_emissions_20,
         reduction_in_sulfide_emissions_21, reduction_in_sulfide_emissions_22, reduction_in_sulfide_emissions_23])


def write_to_database_reduction_in_nitride_emissions_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入氮化物排放减少量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('reduction_in_nitride_emissions',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    reduction_in_nitride_emissions_0 = _print(records1)[0]
    reduction_in_nitride_emissions_1 = _print(records1)[1]
    reduction_in_nitride_emissions_2 = _print(records1)[2]
    reduction_in_nitride_emissions_3 = _print(records1)[3]
    reduction_in_nitride_emissions_4 = _print(records1)[4]
    reduction_in_nitride_emissions_5 = _print(records1)[5]
    reduction_in_nitride_emissions_6 = _print(records1)[6]
    reduction_in_nitride_emissions_7 = _print(records1)[7]
    reduction_in_nitride_emissions_8 = _print(records1)[8]
    reduction_in_nitride_emissions_9 = _print(records1)[9]
    reduction_in_nitride_emissions_10 = _print(records1)[10]
    reduction_in_nitride_emissions_11 = _print(records1)[11]
    reduction_in_nitride_emissions_12 = _print(records1)[12]
    reduction_in_nitride_emissions_13 = _print(records1)[13]
    reduction_in_nitride_emissions_14 = _print(records1)[14]
    reduction_in_nitride_emissions_15 = _print(records1)[15]
    reduction_in_nitride_emissions_16 = _print(records1)[16]
    reduction_in_nitride_emissions_17 = _print(records1)[17]
    reduction_in_nitride_emissions_18 = _print(records1)[18]
    reduction_in_nitride_emissions_19 = _print(records1)[19]
    reduction_in_nitride_emissions_20 = _print(records1)[20]
    reduction_in_nitride_emissions_21 = _print(records1)[21]
    reduction_in_nitride_emissions_22 = _print(records1)[22]
    reduction_in_nitride_emissions_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['reduction_in_nitride_emissions_0', 'reduction_in_nitride_emissions_1', 'reduction_in_nitride_emissions_2',
         'reduction_in_nitride_emissions_3', 'reduction_in_nitride_emissions_4', 'reduction_in_nitride_emissions_5',
         'reduction_in_nitride_emissions_6', 'reduction_in_nitride_emissions_7', 'reduction_in_nitride_emissions_8',
         'reduction_in_nitride_emissions_9', 'reduction_in_nitride_emissions_10', 'reduction_in_nitride_emissions_11',
         'reduction_in_nitride_emissions_12', 'reduction_in_nitride_emissions_13', 'reduction_in_nitride_emissions_14',
         'reduction_in_nitride_emissions_15', 'reduction_in_nitride_emissions_16', 'reduction_in_nitride_emissions_17',
         'reduction_in_nitride_emissions_18', 'reduction_in_nitride_emissions_19', 'reduction_in_nitride_emissions_20',
         'reduction_in_nitride_emissions_21', 'reduction_in_nitride_emissions_22', 'reduction_in_nitride_emissions_23'],
        [reduction_in_nitride_emissions_0, reduction_in_nitride_emissions_1, reduction_in_nitride_emissions_2,
         reduction_in_nitride_emissions_3, reduction_in_nitride_emissions_4, reduction_in_nitride_emissions_5,
         reduction_in_nitride_emissions_6, reduction_in_nitride_emissions_7, reduction_in_nitride_emissions_8,
         reduction_in_nitride_emissions_9, reduction_in_nitride_emissions_10, reduction_in_nitride_emissions_11,
         reduction_in_nitride_emissions_12, reduction_in_nitride_emissions_13, reduction_in_nitride_emissions_14,
         reduction_in_nitride_emissions_15, reduction_in_nitride_emissions_16, reduction_in_nitride_emissions_17,
         reduction_in_nitride_emissions_18, reduction_in_nitride_emissions_19, reduction_in_nitride_emissions_20,
         reduction_in_nitride_emissions_21, reduction_in_nitride_emissions_22, reduction_in_nitride_emissions_23])


def write_to_database_reduction_in_dust_emissions_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入粉尘排放减少量24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('reduction_in_dust_emissions',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    reduction_in_dust_emissions_0 = _print(records1)[0]
    reduction_in_dust_emissions_1 = _print(records1)[1]
    reduction_in_dust_emissions_2 = _print(records1)[2]
    reduction_in_dust_emissions_3 = _print(records1)[3]
    reduction_in_dust_emissions_4 = _print(records1)[4]
    reduction_in_dust_emissions_5 = _print(records1)[5]
    reduction_in_dust_emissions_6 = _print(records1)[6]
    reduction_in_dust_emissions_7 = _print(records1)[7]
    reduction_in_dust_emissions_8 = _print(records1)[8]
    reduction_in_dust_emissions_9 = _print(records1)[9]
    reduction_in_dust_emissions_10 = _print(records1)[10]
    reduction_in_dust_emissions_11 = _print(records1)[11]
    reduction_in_dust_emissions_12 = _print(records1)[12]
    reduction_in_dust_emissions_13 = _print(records1)[13]
    reduction_in_dust_emissions_14 = _print(records1)[14]
    reduction_in_dust_emissions_15 = _print(records1)[15]
    reduction_in_dust_emissions_16 = _print(records1)[16]
    reduction_in_dust_emissions_17 = _print(records1)[17]
    reduction_in_dust_emissions_18 = _print(records1)[18]
    reduction_in_dust_emissions_19 = _print(records1)[19]
    reduction_in_dust_emissions_20 = _print(records1)[20]
    reduction_in_dust_emissions_21 = _print(records1)[21]
    reduction_in_dust_emissions_22 = _print(records1)[22]
    reduction_in_dust_emissions_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['reduction_in_dust_emissions_0', 'reduction_in_dust_emissions_1', 'reduction_in_dust_emissions_2',
         'reduction_in_dust_emissions_3', 'reduction_in_dust_emissions_4', 'reduction_in_dust_emissions_5',
         'reduction_in_dust_emissions_6', 'reduction_in_dust_emissions_7', 'reduction_in_dust_emissions_8',
         'reduction_in_dust_emissions_9', 'reduction_in_dust_emissions_10', 'reduction_in_dust_emissions_11',
         'reduction_in_dust_emissions_12', 'reduction_in_dust_emissions_13', 'reduction_in_dust_emissions_14',
         'reduction_in_dust_emissions_15', 'reduction_in_dust_emissions_16', 'reduction_in_dust_emissions_17',
         'reduction_in_dust_emissions_18', 'reduction_in_dust_emissions_19', 'reduction_in_dust_emissions_20',
         'reduction_in_dust_emissions_21', 'reduction_in_dust_emissions_22', 'reduction_in_dust_emissions_23'],
        [reduction_in_dust_emissions_0, reduction_in_dust_emissions_1, reduction_in_dust_emissions_2,
         reduction_in_dust_emissions_3, reduction_in_dust_emissions_4, reduction_in_dust_emissions_5,
         reduction_in_dust_emissions_6, reduction_in_dust_emissions_7, reduction_in_dust_emissions_8,
         reduction_in_dust_emissions_9, reduction_in_dust_emissions_10, reduction_in_dust_emissions_11,
         reduction_in_dust_emissions_12, reduction_in_dust_emissions_13, reduction_in_dust_emissions_14,
         reduction_in_dust_emissions_15, reduction_in_dust_emissions_16, reduction_in_dust_emissions_17,
         reduction_in_dust_emissions_18, reduction_in_dust_emissions_19, reduction_in_dust_emissions_20,
         reduction_in_dust_emissions_21, reduction_in_dust_emissions_22, reduction_in_dust_emissions_23])


def write_to_database_ice_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机发电收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ice_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ice_income_total_0 = _print(records1)[0]
    ice_income_total_1 = _print(records1)[1]
    ice_income_total_2 = _print(records1)[2]
    ice_income_total_3 = _print(records1)[3]
    ice_income_total_4 = _print(records1)[4]
    ice_income_total_5 = _print(records1)[5]
    ice_income_total_6 = _print(records1)[6]
    ice_income_total_7 = _print(records1)[7]
    ice_income_total_8 = _print(records1)[8]
    ice_income_total_9 = _print(records1)[9]
    ice_income_total_10 = _print(records1)[10]
    ice_income_total_11 = _print(records1)[11]
    ice_income_total_12 = _print(records1)[12]
    ice_income_total_13 = _print(records1)[13]
    ice_income_total_14 = _print(records1)[14]
    ice_income_total_15 = _print(records1)[15]
    ice_income_total_16 = _print(records1)[16]
    ice_income_total_17 = _print(records1)[17]
    ice_income_total_18 = _print(records1)[18]
    ice_income_total_19 = _print(records1)[19]
    ice_income_total_20 = _print(records1)[20]
    ice_income_total_21 = _print(records1)[21]
    ice_income_total_22 = _print(records1)[22]
    ice_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice_income_total_0', 'ice_income_total_1', 'ice_income_total_2',
         'ice_income_total_3', 'ice_income_total_4', 'ice_income_total_5',
         'ice_income_total_6', 'ice_income_total_7', 'ice_income_total_8',
         'ice_income_total_9', 'ice_income_total_10', 'ice_income_total_11',
         'ice_income_total_12', 'ice_income_total_13', 'ice_income_total_14',
         'ice_income_total_15', 'ice_income_total_16', 'ice_income_total_17',
         'ice_income_total_18', 'ice_income_total_19', 'ice_income_total_20',
         'ice_income_total_21', 'ice_income_total_22', 'ice_income_total_23'],
        [ice_income_total_0, ice_income_total_1, ice_income_total_2,
         ice_income_total_3, ice_income_total_4, ice_income_total_5,
         ice_income_total_6, ice_income_total_7, ice_income_total_8,
         ice_income_total_9, ice_income_total_10, ice_income_total_11,
         ice_income_total_12, ice_income_total_13, ice_income_total_14,
         ice_income_total_15, ice_income_total_16, ice_income_total_17,
         ice_income_total_18, ice_income_total_19, ice_income_total_20,
         ice_income_total_21, ice_income_total_22, ice_income_total_23])


def write_to_database_lb_cold_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制冷收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_cold_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_cold_income_total_0 = _print(records1)[0]
    lb_cold_income_total_1 = _print(records1)[1]
    lb_cold_income_total_2 = _print(records1)[2]
    lb_cold_income_total_3 = _print(records1)[3]
    lb_cold_income_total_4 = _print(records1)[4]
    lb_cold_income_total_5 = _print(records1)[5]
    lb_cold_income_total_6 = _print(records1)[6]
    lb_cold_income_total_7 = _print(records1)[7]
    lb_cold_income_total_8 = _print(records1)[8]
    lb_cold_income_total_9 = _print(records1)[9]
    lb_cold_income_total_10 = _print(records1)[10]
    lb_cold_income_total_11 = _print(records1)[11]
    lb_cold_income_total_12 = _print(records1)[12]
    lb_cold_income_total_13 = _print(records1)[13]
    lb_cold_income_total_14 = _print(records1)[14]
    lb_cold_income_total_15 = _print(records1)[15]
    lb_cold_income_total_16 = _print(records1)[16]
    lb_cold_income_total_17 = _print(records1)[17]
    lb_cold_income_total_18 = _print(records1)[18]
    lb_cold_income_total_19 = _print(records1)[19]
    lb_cold_income_total_20 = _print(records1)[20]
    lb_cold_income_total_21 = _print(records1)[21]
    lb_cold_income_total_22 = _print(records1)[22]
    lb_cold_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_cold_income_total_0', 'lb_cold_income_total_1', 'lb_cold_income_total_2',
         'lb_cold_income_total_3', 'lb_cold_income_total_4', 'lb_cold_income_total_5',
         'lb_cold_income_total_6', 'lb_cold_income_total_7', 'lb_cold_income_total_8',
         'lb_cold_income_total_9', 'lb_cold_income_total_10', 'lb_cold_income_total_11',
         'lb_cold_income_total_12', 'lb_cold_income_total_13', 'lb_cold_income_total_14',
         'lb_cold_income_total_15', 'lb_cold_income_total_16', 'lb_cold_income_total_17',
         'lb_cold_income_total_18', 'lb_cold_income_total_19', 'lb_cold_income_total_20',
         'lb_cold_income_total_21', 'lb_cold_income_total_22', 'lb_cold_income_total_23'],
        [lb_cold_income_total_0, lb_cold_income_total_1, lb_cold_income_total_2,
         lb_cold_income_total_3, lb_cold_income_total_4, lb_cold_income_total_5,
         lb_cold_income_total_6, lb_cold_income_total_7, lb_cold_income_total_8,
         lb_cold_income_total_9, lb_cold_income_total_10, lb_cold_income_total_11,
         lb_cold_income_total_12, lb_cold_income_total_13, lb_cold_income_total_14,
         lb_cold_income_total_15, lb_cold_income_total_16, lb_cold_income_total_17,
         lb_cold_income_total_18, lb_cold_income_total_19, lb_cold_income_total_20,
         lb_cold_income_total_21, lb_cold_income_total_22, lb_cold_income_total_23])

def write_to_database_lb_heat_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制热收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_heat_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_heat_income_total_0 = _print(records1)[0]
    lb_heat_income_total_1 = _print(records1)[1]
    lb_heat_income_total_2 = _print(records1)[2]
    lb_heat_income_total_3 = _print(records1)[3]
    lb_heat_income_total_4 = _print(records1)[4]
    lb_heat_income_total_5 = _print(records1)[5]
    lb_heat_income_total_6 = _print(records1)[6]
    lb_heat_income_total_7 = _print(records1)[7]
    lb_heat_income_total_8 = _print(records1)[8]
    lb_heat_income_total_9 = _print(records1)[9]
    lb_heat_income_total_10 = _print(records1)[10]
    lb_heat_income_total_11 = _print(records1)[11]
    lb_heat_income_total_12 = _print(records1)[12]
    lb_heat_income_total_13 = _print(records1)[13]
    lb_heat_income_total_14 = _print(records1)[14]
    lb_heat_income_total_15 = _print(records1)[15]
    lb_heat_income_total_16 = _print(records1)[16]
    lb_heat_income_total_17 = _print(records1)[17]
    lb_heat_income_total_18 = _print(records1)[18]
    lb_heat_income_total_19 = _print(records1)[19]
    lb_heat_income_total_20 = _print(records1)[20]
    lb_heat_income_total_21 = _print(records1)[21]
    lb_heat_income_total_22 = _print(records1)[22]
    lb_heat_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_heat_income_total_0', 'lb_heat_income_total_1', 'lb_heat_income_total_2',
         'lb_heat_income_total_3', 'lb_heat_income_total_4', 'lb_heat_income_total_5',
         'lb_heat_income_total_6', 'lb_heat_income_total_7', 'lb_heat_income_total_8',
         'lb_heat_income_total_9', 'lb_heat_income_total_10', 'lb_heat_income_total_11',
         'lb_heat_income_total_12', 'lb_heat_income_total_13', 'lb_heat_income_total_14',
         'lb_heat_income_total_15', 'lb_heat_income_total_16', 'lb_heat_income_total_17',
         'lb_heat_income_total_18', 'lb_heat_income_total_19', 'lb_heat_income_total_20',
         'lb_heat_income_total_21', 'lb_heat_income_total_22', 'lb_heat_income_total_23'],
        [lb_heat_income_total_0, lb_heat_income_total_1, lb_heat_income_total_2,
         lb_heat_income_total_3, lb_heat_income_total_4, lb_heat_income_total_5,
         lb_heat_income_total_6, lb_heat_income_total_7, lb_heat_income_total_8,
         lb_heat_income_total_9, lb_heat_income_total_10, lb_heat_income_total_11,
         lb_heat_income_total_12, lb_heat_income_total_13, lb_heat_income_total_14,
         lb_heat_income_total_15, lb_heat_income_total_16, lb_heat_income_total_17,
         lb_heat_income_total_18, lb_heat_income_total_19, lb_heat_income_total_20,
         lb_heat_income_total_21, lb_heat_income_total_22, lb_heat_income_total_23])


def write_to_database_lb_hot_water_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂生活热水收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_hot_water_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_hot_water_income_total_0 = _print(records1)[0]
    lb_hot_water_income_total_1 = _print(records1)[1]
    lb_hot_water_income_total_2 = _print(records1)[2]
    lb_hot_water_income_total_3 = _print(records1)[3]
    lb_hot_water_income_total_4 = _print(records1)[4]
    lb_hot_water_income_total_5 = _print(records1)[5]
    lb_hot_water_income_total_6 = _print(records1)[6]
    lb_hot_water_income_total_7 = _print(records1)[7]
    lb_hot_water_income_total_8 = _print(records1)[8]
    lb_hot_water_income_total_9 = _print(records1)[9]
    lb_hot_water_income_total_10 = _print(records1)[10]
    lb_hot_water_income_total_11 = _print(records1)[11]
    lb_hot_water_income_total_12 = _print(records1)[12]
    lb_hot_water_income_total_13 = _print(records1)[13]
    lb_hot_water_income_total_14 = _print(records1)[14]
    lb_hot_water_income_total_15 = _print(records1)[15]
    lb_hot_water_income_total_16 = _print(records1)[16]
    lb_hot_water_income_total_17 = _print(records1)[17]
    lb_hot_water_income_total_18 = _print(records1)[18]
    lb_hot_water_income_total_19 = _print(records1)[19]
    lb_hot_water_income_total_20 = _print(records1)[20]
    lb_hot_water_income_total_21 = _print(records1)[21]
    lb_hot_water_income_total_22 = _print(records1)[22]
    lb_hot_water_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_hot_water_income_total_0', 'lb_hot_water_income_total_1', 'lb_hot_water_income_total_2',
         'lb_hot_water_income_total_3', 'lb_hot_water_income_total_4', 'lb_hot_water_income_total_5',
         'lb_hot_water_income_total_6', 'lb_hot_water_income_total_7', 'lb_hot_water_income_total_8',
         'lb_hot_water_income_total_9', 'lb_hot_water_income_total_10', 'lb_hot_water_income_total_11',
         'lb_hot_water_income_total_12', 'lb_hot_water_income_total_13', 'lb_hot_water_income_total_14',
         'lb_hot_water_income_total_15', 'lb_hot_water_income_total_16', 'lb_hot_water_income_total_17',
         'lb_hot_water_income_total_18', 'lb_hot_water_income_total_19', 'lb_hot_water_income_total_20',
         'lb_hot_water_income_total_21', 'lb_hot_water_income_total_22', 'lb_hot_water_income_total_23'],
        [lb_hot_water_income_total_0, lb_hot_water_income_total_1, lb_hot_water_income_total_2,
         lb_hot_water_income_total_3, lb_hot_water_income_total_4, lb_hot_water_income_total_5,
         lb_hot_water_income_total_6, lb_hot_water_income_total_7, lb_hot_water_income_total_8,
         lb_hot_water_income_total_9, lb_hot_water_income_total_10, lb_hot_water_income_total_11,
         lb_hot_water_income_total_12, lb_hot_water_income_total_13, lb_hot_water_income_total_14,
         lb_hot_water_income_total_15, lb_hot_water_income_total_16, lb_hot_water_income_total_17,
         lb_hot_water_income_total_18, lb_hot_water_income_total_19, lb_hot_water_income_total_20,
         lb_hot_water_income_total_21, lb_hot_water_income_total_22, lb_hot_water_income_total_23])


def write_to_database_cc_cold_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机制冷收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc_cold_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    cc_cold_income_total_0 = _print(records1)[0]
    cc_cold_income_total_1 = _print(records1)[1]
    cc_cold_income_total_2 = _print(records1)[2]
    cc_cold_income_total_3 = _print(records1)[3]
    cc_cold_income_total_4 = _print(records1)[4]
    cc_cold_income_total_5 = _print(records1)[5]
    cc_cold_income_total_6 = _print(records1)[6]
    cc_cold_income_total_7 = _print(records1)[7]
    cc_cold_income_total_8 = _print(records1)[8]
    cc_cold_income_total_9 = _print(records1)[9]
    cc_cold_income_total_10 = _print(records1)[10]
    cc_cold_income_total_11 = _print(records1)[11]
    cc_cold_income_total_12 = _print(records1)[12]
    cc_cold_income_total_13 = _print(records1)[13]
    cc_cold_income_total_14 = _print(records1)[14]
    cc_cold_income_total_15 = _print(records1)[15]
    cc_cold_income_total_16 = _print(records1)[16]
    cc_cold_income_total_17 = _print(records1)[17]
    cc_cold_income_total_18 = _print(records1)[18]
    cc_cold_income_total_19 = _print(records1)[19]
    cc_cold_income_total_20 = _print(records1)[20]
    cc_cold_income_total_21 = _print(records1)[21]
    cc_cold_income_total_22 = _print(records1)[22]
    cc_cold_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc_cold_income_total_0', 'cc_cold_income_total_1', 'cc_cold_income_total_2',
         'cc_cold_income_total_3', 'cc_cold_income_total_4', 'cc_cold_income_total_5',
         'cc_cold_income_total_6', 'cc_cold_income_total_7', 'cc_cold_income_total_8',
         'cc_cold_income_total_9', 'cc_cold_income_total_10', 'cc_cold_income_total_11',
         'cc_cold_income_total_12', 'cc_cold_income_total_13', 'cc_cold_income_total_14',
         'cc_cold_income_total_15', 'cc_cold_income_total_16', 'cc_cold_income_total_17',
         'cc_cold_income_total_18', 'cc_cold_income_total_19', 'cc_cold_income_total_20',
         'cc_cold_income_total_21', 'cc_cold_income_total_22', 'cc_cold_income_total_23'],
        [cc_cold_income_total_0, cc_cold_income_total_1, cc_cold_income_total_2,
         cc_cold_income_total_3, cc_cold_income_total_4, cc_cold_income_total_5,
         cc_cold_income_total_6, cc_cold_income_total_7, cc_cold_income_total_8,
         cc_cold_income_total_9, cc_cold_income_total_10, cc_cold_income_total_11,
         cc_cold_income_total_12, cc_cold_income_total_13, cc_cold_income_total_14,
         cc_cold_income_total_15, cc_cold_income_total_16, cc_cold_income_total_17,
         cc_cold_income_total_18, cc_cold_income_total_19, cc_cold_income_total_20,
         cc_cold_income_total_21, cc_cold_income_total_22, cc_cold_income_total_23])


def write_to_database_chp_cold_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制冷收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_cold_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_cold_income_total_0 = _print(records1)[0]
    chp_cold_income_total_1 = _print(records1)[1]
    chp_cold_income_total_2 = _print(records1)[2]
    chp_cold_income_total_3 = _print(records1)[3]
    chp_cold_income_total_4 = _print(records1)[4]
    chp_cold_income_total_5 = _print(records1)[5]
    chp_cold_income_total_6 = _print(records1)[6]
    chp_cold_income_total_7 = _print(records1)[7]
    chp_cold_income_total_8 = _print(records1)[8]
    chp_cold_income_total_9 = _print(records1)[9]
    chp_cold_income_total_10 = _print(records1)[10]
    chp_cold_income_total_11 = _print(records1)[11]
    chp_cold_income_total_12 = _print(records1)[12]
    chp_cold_income_total_13 = _print(records1)[13]
    chp_cold_income_total_14 = _print(records1)[14]
    chp_cold_income_total_15 = _print(records1)[15]
    chp_cold_income_total_16 = _print(records1)[16]
    chp_cold_income_total_17 = _print(records1)[17]
    chp_cold_income_total_18 = _print(records1)[18]
    chp_cold_income_total_19 = _print(records1)[19]
    chp_cold_income_total_20 = _print(records1)[20]
    chp_cold_income_total_21 = _print(records1)[21]
    chp_cold_income_total_22 = _print(records1)[22]
    chp_cold_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_cold_income_total_0', 'chp_cold_income_total_1', 'chp_cold_income_total_2',
         'chp_cold_income_total_3', 'chp_cold_income_total_4', 'chp_cold_income_total_5',
         'chp_cold_income_total_6', 'chp_cold_income_total_7', 'chp_cold_income_total_8',
         'chp_cold_income_total_9', 'chp_cold_income_total_10', 'chp_cold_income_total_11',
         'chp_cold_income_total_12', 'chp_cold_income_total_13', 'chp_cold_income_total_14',
         'chp_cold_income_total_15', 'chp_cold_income_total_16', 'chp_cold_income_total_17',
         'chp_cold_income_total_18', 'chp_cold_income_total_19', 'chp_cold_income_total_20',
         'chp_cold_income_total_21', 'chp_cold_income_total_22', 'chp_cold_income_total_23'],
        [chp_cold_income_total_0, chp_cold_income_total_1, chp_cold_income_total_2,
         chp_cold_income_total_3, chp_cold_income_total_4, chp_cold_income_total_5,
         chp_cold_income_total_6, chp_cold_income_total_7, chp_cold_income_total_8,
         chp_cold_income_total_9, chp_cold_income_total_10, chp_cold_income_total_11,
         chp_cold_income_total_12, chp_cold_income_total_13, chp_cold_income_total_14,
         chp_cold_income_total_15, chp_cold_income_total_16, chp_cold_income_total_17,
         chp_cold_income_total_18, chp_cold_income_total_19, chp_cold_income_total_20,
         chp_cold_income_total_21, chp_cold_income_total_22, chp_cold_income_total_23])


def write_to_database_chp_heat_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制热收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_heat_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_heat_income_total_0 = _print(records1)[0]
    chp_heat_income_total_1 = _print(records1)[1]
    chp_heat_income_total_2 = _print(records1)[2]
    chp_heat_income_total_3 = _print(records1)[3]
    chp_heat_income_total_4 = _print(records1)[4]
    chp_heat_income_total_5 = _print(records1)[5]
    chp_heat_income_total_6 = _print(records1)[6]
    chp_heat_income_total_7 = _print(records1)[7]
    chp_heat_income_total_8 = _print(records1)[8]
    chp_heat_income_total_9 = _print(records1)[9]
    chp_heat_income_total_10 = _print(records1)[10]
    chp_heat_income_total_11 = _print(records1)[11]
    chp_heat_income_total_12 = _print(records1)[12]
    chp_heat_income_total_13 = _print(records1)[13]
    chp_heat_income_total_14 = _print(records1)[14]
    chp_heat_income_total_15 = _print(records1)[15]
    chp_heat_income_total_16 = _print(records1)[16]
    chp_heat_income_total_17 = _print(records1)[17]
    chp_heat_income_total_18 = _print(records1)[18]
    chp_heat_income_total_19 = _print(records1)[19]
    chp_heat_income_total_20 = _print(records1)[20]
    chp_heat_income_total_21 = _print(records1)[21]
    chp_heat_income_total_22 = _print(records1)[22]
    chp_heat_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_heat_income_total_0', 'chp_heat_income_total_1', 'chp_heat_income_total_2',
         'chp_heat_income_total_3', 'chp_heat_income_total_4', 'chp_heat_income_total_5',
         'chp_heat_income_total_6', 'chp_heat_income_total_7', 'chp_heat_income_total_8',
         'chp_heat_income_total_9', 'chp_heat_income_total_10', 'chp_heat_income_total_11',
         'chp_heat_income_total_12', 'chp_heat_income_total_13', 'chp_heat_income_total_14',
         'chp_heat_income_total_15', 'chp_heat_income_total_16', 'chp_heat_income_total_17',
         'chp_heat_income_total_18', 'chp_heat_income_total_19', 'chp_heat_income_total_20',
         'chp_heat_income_total_21', 'chp_heat_income_total_22', 'chp_heat_income_total_23'],
        [chp_heat_income_total_0, chp_heat_income_total_1, chp_heat_income_total_2,
         chp_heat_income_total_3, chp_heat_income_total_4, chp_heat_income_total_5,
         chp_heat_income_total_6, chp_heat_income_total_7, chp_heat_income_total_8,
         chp_heat_income_total_9, chp_heat_income_total_10, chp_heat_income_total_11,
         chp_heat_income_total_12, chp_heat_income_total_13, chp_heat_income_total_14,
         chp_heat_income_total_15, chp_heat_income_total_16, chp_heat_income_total_17,
         chp_heat_income_total_18, chp_heat_income_total_19, chp_heat_income_total_20,
         chp_heat_income_total_21, chp_heat_income_total_22, chp_heat_income_total_23])


def write_to_database_ashp_cold_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制冷收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_cold_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_cold_income_total_0 = _print(records1)[0]
    ashp_cold_income_total_1 = _print(records1)[1]
    ashp_cold_income_total_2 = _print(records1)[2]
    ashp_cold_income_total_3 = _print(records1)[3]
    ashp_cold_income_total_4 = _print(records1)[4]
    ashp_cold_income_total_5 = _print(records1)[5]
    ashp_cold_income_total_6 = _print(records1)[6]
    ashp_cold_income_total_7 = _print(records1)[7]
    ashp_cold_income_total_8 = _print(records1)[8]
    ashp_cold_income_total_9 = _print(records1)[9]
    ashp_cold_income_total_10 = _print(records1)[10]
    ashp_cold_income_total_11 = _print(records1)[11]
    ashp_cold_income_total_12 = _print(records1)[12]
    ashp_cold_income_total_13 = _print(records1)[13]
    ashp_cold_income_total_14 = _print(records1)[14]
    ashp_cold_income_total_15 = _print(records1)[15]
    ashp_cold_income_total_16 = _print(records1)[16]
    ashp_cold_income_total_17 = _print(records1)[17]
    ashp_cold_income_total_18 = _print(records1)[18]
    ashp_cold_income_total_19 = _print(records1)[19]
    ashp_cold_income_total_20 = _print(records1)[20]
    ashp_cold_income_total_21 = _print(records1)[21]
    ashp_cold_income_total_22 = _print(records1)[22]
    ashp_cold_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_cold_income_total_0', 'ashp_cold_income_total_1', 'ashp_cold_income_total_2',
         'ashp_cold_income_total_3', 'ashp_cold_income_total_4', 'ashp_cold_income_total_5',
         'ashp_cold_income_total_6', 'ashp_cold_income_total_7', 'ashp_cold_income_total_8',
         'ashp_cold_income_total_9', 'ashp_cold_income_total_10', 'ashp_cold_income_total_11',
         'ashp_cold_income_total_12', 'ashp_cold_income_total_13', 'ashp_cold_income_total_14',
         'ashp_cold_income_total_15', 'ashp_cold_income_total_16', 'ashp_cold_income_total_17',
         'ashp_cold_income_total_18', 'ashp_cold_income_total_19', 'ashp_cold_income_total_20',
         'ashp_cold_income_total_21', 'ashp_cold_income_total_22', 'ashp_cold_income_total_23'],
        [ashp_cold_income_total_0, ashp_cold_income_total_1, ashp_cold_income_total_2,
         ashp_cold_income_total_3, ashp_cold_income_total_4, ashp_cold_income_total_5,
         ashp_cold_income_total_6, ashp_cold_income_total_7, ashp_cold_income_total_8,
         ashp_cold_income_total_9, ashp_cold_income_total_10, ashp_cold_income_total_11,
         ashp_cold_income_total_12, ashp_cold_income_total_13, ashp_cold_income_total_14,
         ashp_cold_income_total_15, ashp_cold_income_total_16, ashp_cold_income_total_17,
         ashp_cold_income_total_18, ashp_cold_income_total_19, ashp_cold_income_total_20,
         ashp_cold_income_total_21, ashp_cold_income_total_22, ashp_cold_income_total_23])


def write_to_database_ngb_hot_water_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入天然气锅炉生活热水收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ngb_hot_water_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ngb_hot_water_income_total_0 = _print(records1)[0]
    ngb_hot_water_income_total_1 = _print(records1)[1]
    ngb_hot_water_income_total_2 = _print(records1)[2]
    ngb_hot_water_income_total_3 = _print(records1)[3]
    ngb_hot_water_income_total_4 = _print(records1)[4]
    ngb_hot_water_income_total_5 = _print(records1)[5]
    ngb_hot_water_income_total_6 = _print(records1)[6]
    ngb_hot_water_income_total_7 = _print(records1)[7]
    ngb_hot_water_income_total_8 = _print(records1)[8]
    ngb_hot_water_income_total_9 = _print(records1)[9]
    ngb_hot_water_income_total_10 = _print(records1)[10]
    ngb_hot_water_income_total_11 = _print(records1)[11]
    ngb_hot_water_income_total_12 = _print(records1)[12]
    ngb_hot_water_income_total_13 = _print(records1)[13]
    ngb_hot_water_income_total_14 = _print(records1)[14]
    ngb_hot_water_income_total_15 = _print(records1)[15]
    ngb_hot_water_income_total_16 = _print(records1)[16]
    ngb_hot_water_income_total_17 = _print(records1)[17]
    ngb_hot_water_income_total_18 = _print(records1)[18]
    ngb_hot_water_income_total_19 = _print(records1)[19]
    ngb_hot_water_income_total_20 = _print(records1)[20]
    ngb_hot_water_income_total_21 = _print(records1)[21]
    ngb_hot_water_income_total_22 = _print(records1)[22]
    ngb_hot_water_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb_hot_water_income_total_0', 'ngb_hot_water_income_total_1', 'ngb_hot_water_income_total_2',
         'ngb_hot_water_income_total_3', 'ngb_hot_water_income_total_4', 'ngb_hot_water_income_total_5',
         'ngb_hot_water_income_total_6', 'ngb_hot_water_income_total_7', 'ngb_hot_water_income_total_8',
         'ngb_hot_water_income_total_9', 'ngb_hot_water_income_total_10', 'ngb_hot_water_income_total_11',
         'ngb_hot_water_income_total_12', 'ngb_hot_water_income_total_13', 'ngb_hot_water_income_total_14',
         'ngb_hot_water_income_total_15', 'ngb_hot_water_income_total_16', 'ngb_hot_water_income_total_17',
         'ngb_hot_water_income_total_18', 'ngb_hot_water_income_total_19', 'ngb_hot_water_income_total_20',
         'ngb_hot_water_income_total_21', 'ngb_hot_water_income_total_22', 'ngb_hot_water_income_total_23'],
        [ngb_hot_water_income_total_0, ngb_hot_water_income_total_1, ngb_hot_water_income_total_2,
         ngb_hot_water_income_total_3, ngb_hot_water_income_total_4, ngb_hot_water_income_total_5,
         ngb_hot_water_income_total_6, ngb_hot_water_income_total_7, ngb_hot_water_income_total_8,
         ngb_hot_water_income_total_9, ngb_hot_water_income_total_10, ngb_hot_water_income_total_11,
         ngb_hot_water_income_total_12, ngb_hot_water_income_total_13, ngb_hot_water_income_total_14,
         ngb_hot_water_income_total_15, ngb_hot_water_income_total_16, ngb_hot_water_income_total_17,
         ngb_hot_water_income_total_18, ngb_hot_water_income_total_19, ngb_hot_water_income_total_20,
         ngb_hot_water_income_total_21, ngb_hot_water_income_total_22, ngb_hot_water_income_total_23])


def write_to_database_photovoltaic_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入光伏发电收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('photovoltaic_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    photovoltaic_income_total_0 = _print(records1)[0]
    photovoltaic_income_total_1 = _print(records1)[1]
    photovoltaic_income_total_2 = _print(records1)[2]
    photovoltaic_income_total_3 = _print(records1)[3]
    photovoltaic_income_total_4 = _print(records1)[4]
    photovoltaic_income_total_5 = _print(records1)[5]
    photovoltaic_income_total_6 = _print(records1)[6]
    photovoltaic_income_total_7 = _print(records1)[7]
    photovoltaic_income_total_8 = _print(records1)[8]
    photovoltaic_income_total_9 = _print(records1)[9]
    photovoltaic_income_total_10 = _print(records1)[10]
    photovoltaic_income_total_11 = _print(records1)[11]
    photovoltaic_income_total_12 = _print(records1)[12]
    photovoltaic_income_total_13 = _print(records1)[13]
    photovoltaic_income_total_14 = _print(records1)[14]
    photovoltaic_income_total_15 = _print(records1)[15]
    photovoltaic_income_total_16 = _print(records1)[16]
    photovoltaic_income_total_17 = _print(records1)[17]
    photovoltaic_income_total_18 = _print(records1)[18]
    photovoltaic_income_total_19 = _print(records1)[19]
    photovoltaic_income_total_20 = _print(records1)[20]
    photovoltaic_income_total_21 = _print(records1)[21]
    photovoltaic_income_total_22 = _print(records1)[22]
    photovoltaic_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['photovoltaic_income_total_0', 'photovoltaic_income_total_1', 'photovoltaic_income_total_2',
         'photovoltaic_income_total_3', 'photovoltaic_income_total_4', 'photovoltaic_income_total_5',
         'photovoltaic_income_total_6', 'photovoltaic_income_total_7', 'photovoltaic_income_total_8',
         'photovoltaic_income_total_9', 'photovoltaic_income_total_10', 'photovoltaic_income_total_11',
         'photovoltaic_income_total_12', 'photovoltaic_income_total_13', 'photovoltaic_income_total_14',
         'photovoltaic_income_total_15', 'photovoltaic_income_total_16', 'photovoltaic_income_total_17',
         'photovoltaic_income_total_18', 'photovoltaic_income_total_19', 'photovoltaic_income_total_20',
         'photovoltaic_income_total_21', 'photovoltaic_income_total_22', 'photovoltaic_income_total_23'],
        [photovoltaic_income_total_0, photovoltaic_income_total_1, photovoltaic_income_total_2,
         photovoltaic_income_total_3, photovoltaic_income_total_4, photovoltaic_income_total_5,
         photovoltaic_income_total_6, photovoltaic_income_total_7, photovoltaic_income_total_8,
         photovoltaic_income_total_9, photovoltaic_income_total_10, photovoltaic_income_total_11,
         photovoltaic_income_total_12, photovoltaic_income_total_13, photovoltaic_income_total_14,
         photovoltaic_income_total_15, photovoltaic_income_total_16, photovoltaic_income_total_17,
         photovoltaic_income_total_18, photovoltaic_income_total_19, photovoltaic_income_total_20,
         photovoltaic_income_total_21, photovoltaic_income_total_22, photovoltaic_income_total_23])


def write_to_database_wind_income_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入风力发电收入24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('wind_income_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    wind_income_total_0 = _print(records1)[0]
    wind_income_total_1 = _print(records1)[1]
    wind_income_total_2 = _print(records1)[2]
    wind_income_total_3 = _print(records1)[3]
    wind_income_total_4 = _print(records1)[4]
    wind_income_total_5 = _print(records1)[5]
    wind_income_total_6 = _print(records1)[6]
    wind_income_total_7 = _print(records1)[7]
    wind_income_total_8 = _print(records1)[8]
    wind_income_total_9 = _print(records1)[9]
    wind_income_total_10 = _print(records1)[10]
    wind_income_total_11 = _print(records1)[11]
    wind_income_total_12 = _print(records1)[12]
    wind_income_total_13 = _print(records1)[13]
    wind_income_total_14 = _print(records1)[14]
    wind_income_total_15 = _print(records1)[15]
    wind_income_total_16 = _print(records1)[16]
    wind_income_total_17 = _print(records1)[17]
    wind_income_total_18 = _print(records1)[18]
    wind_income_total_19 = _print(records1)[19]
    wind_income_total_20 = _print(records1)[20]
    wind_income_total_21 = _print(records1)[21]
    wind_income_total_22 = _print(records1)[22]
    wind_income_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['wind_income_total_0', 'wind_income_total_1', 'wind_income_total_2',
         'wind_income_total_3', 'wind_income_total_4', 'wind_income_total_5',
         'wind_income_total_6', 'wind_income_total_7', 'wind_income_total_8',
         'wind_income_total_9', 'wind_income_total_10', 'wind_income_total_11',
         'wind_income_total_12', 'wind_income_total_13', 'wind_income_total_14',
         'wind_income_total_15', 'wind_income_total_16', 'wind_income_total_17',
         'wind_income_total_18', 'wind_income_total_19', 'wind_income_total_20',
         'wind_income_total_21', 'wind_income_total_22', 'wind_income_total_23'],
        [wind_income_total_0, wind_income_total_1, wind_income_total_2,
         wind_income_total_3, wind_income_total_4, wind_income_total_5,
         wind_income_total_6, wind_income_total_7, wind_income_total_8,
         wind_income_total_9, wind_income_total_10, wind_income_total_11,
         wind_income_total_12, wind_income_total_13, wind_income_total_14,
         wind_income_total_15, wind_income_total_16, wind_income_total_17,
         wind_income_total_18, wind_income_total_19, wind_income_total_20,
         wind_income_total_21, wind_income_total_22, wind_income_total_23])


def write_to_database_ice_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机发电成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ice_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ice_cost_total_0 = _print(records1)[0]
    ice_cost_total_1 = _print(records1)[1]
    ice_cost_total_2 = _print(records1)[2]
    ice_cost_total_3 = _print(records1)[3]
    ice_cost_total_4 = _print(records1)[4]
    ice_cost_total_5 = _print(records1)[5]
    ice_cost_total_6 = _print(records1)[6]
    ice_cost_total_7 = _print(records1)[7]
    ice_cost_total_8 = _print(records1)[8]
    ice_cost_total_9 = _print(records1)[9]
    ice_cost_total_10 = _print(records1)[10]
    ice_cost_total_11 = _print(records1)[11]
    ice_cost_total_12 = _print(records1)[12]
    ice_cost_total_13 = _print(records1)[13]
    ice_cost_total_14 = _print(records1)[14]
    ice_cost_total_15 = _print(records1)[15]
    ice_cost_total_16 = _print(records1)[16]
    ice_cost_total_17 = _print(records1)[17]
    ice_cost_total_18 = _print(records1)[18]
    ice_cost_total_19 = _print(records1)[19]
    ice_cost_total_20 = _print(records1)[20]
    ice_cost_total_21 = _print(records1)[21]
    ice_cost_total_22 = _print(records1)[22]
    ice_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice_cost_total_0', 'ice_cost_total_1', 'ice_cost_total_2',
         'ice_cost_total_3', 'ice_cost_total_4', 'ice_cost_total_5',
         'ice_cost_total_6', 'ice_cost_total_7', 'ice_cost_total_8',
         'ice_cost_total_9', 'ice_cost_total_10', 'ice_cost_total_11',
         'ice_cost_total_12', 'ice_cost_total_13', 'ice_cost_total_14',
         'ice_cost_total_15', 'ice_cost_total_16', 'ice_cost_total_17',
         'ice_cost_total_18', 'ice_cost_total_19', 'ice_cost_total_20',
         'ice_cost_total_21', 'ice_cost_total_22', 'ice_cost_total_23'],
        [ice_cost_total_0, ice_cost_total_1, ice_cost_total_2,
         ice_cost_total_3, ice_cost_total_4, ice_cost_total_5,
         ice_cost_total_6, ice_cost_total_7, ice_cost_total_8,
         ice_cost_total_9, ice_cost_total_10, ice_cost_total_11,
         ice_cost_total_12, ice_cost_total_13, ice_cost_total_14,
         ice_cost_total_15, ice_cost_total_16, ice_cost_total_17,
         ice_cost_total_18, ice_cost_total_19, ice_cost_total_20,
         ice_cost_total_21, ice_cost_total_22, ice_cost_total_23])


def write_to_database_lb_cold_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制冷成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_cold_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_cold_cost_total_0 = _print(records1)[0]
    lb_cold_cost_total_1 = _print(records1)[1]
    lb_cold_cost_total_2 = _print(records1)[2]
    lb_cold_cost_total_3 = _print(records1)[3]
    lb_cold_cost_total_4 = _print(records1)[4]
    lb_cold_cost_total_5 = _print(records1)[5]
    lb_cold_cost_total_6 = _print(records1)[6]
    lb_cold_cost_total_7 = _print(records1)[7]
    lb_cold_cost_total_8 = _print(records1)[8]
    lb_cold_cost_total_9 = _print(records1)[9]
    lb_cold_cost_total_10 = _print(records1)[10]
    lb_cold_cost_total_11 = _print(records1)[11]
    lb_cold_cost_total_12 = _print(records1)[12]
    lb_cold_cost_total_13 = _print(records1)[13]
    lb_cold_cost_total_14 = _print(records1)[14]
    lb_cold_cost_total_15 = _print(records1)[15]
    lb_cold_cost_total_16 = _print(records1)[16]
    lb_cold_cost_total_17 = _print(records1)[17]
    lb_cold_cost_total_18 = _print(records1)[18]
    lb_cold_cost_total_19 = _print(records1)[19]
    lb_cold_cost_total_20 = _print(records1)[20]
    lb_cold_cost_total_21 = _print(records1)[21]
    lb_cold_cost_total_22 = _print(records1)[22]
    lb_cold_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_cold_cost_total_0', 'lb_cold_cost_total_1', 'lb_cold_cost_total_2',
         'lb_cold_cost_total_3', 'lb_cold_cost_total_4', 'lb_cold_cost_total_5',
         'lb_cold_cost_total_6', 'lb_cold_cost_total_7', 'lb_cold_cost_total_8',
         'lb_cold_cost_total_9', 'lb_cold_cost_total_10', 'lb_cold_cost_total_11',
         'lb_cold_cost_total_12', 'lb_cold_cost_total_13', 'lb_cold_cost_total_14',
         'lb_cold_cost_total_15', 'lb_cold_cost_total_16', 'lb_cold_cost_total_17',
         'lb_cold_cost_total_18', 'lb_cold_cost_total_19', 'lb_cold_cost_total_20',
         'lb_cold_cost_total_21', 'lb_cold_cost_total_22', 'lb_cold_cost_total_23'],
        [lb_cold_cost_total_0, lb_cold_cost_total_1, lb_cold_cost_total_2,
         lb_cold_cost_total_3, lb_cold_cost_total_4, lb_cold_cost_total_5,
         lb_cold_cost_total_6, lb_cold_cost_total_7, lb_cold_cost_total_8,
         lb_cold_cost_total_9, lb_cold_cost_total_10, lb_cold_cost_total_11,
         lb_cold_cost_total_12, lb_cold_cost_total_13, lb_cold_cost_total_14,
         lb_cold_cost_total_15, lb_cold_cost_total_16, lb_cold_cost_total_17,
         lb_cold_cost_total_18, lb_cold_cost_total_19, lb_cold_cost_total_20,
         lb_cold_cost_total_21, lb_cold_cost_total_22, lb_cold_cost_total_23])

def write_to_database_lb_heat_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制热成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_heat_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_heat_cost_total_0 = _print(records1)[0]
    lb_heat_cost_total_1 = _print(records1)[1]
    lb_heat_cost_total_2 = _print(records1)[2]
    lb_heat_cost_total_3 = _print(records1)[3]
    lb_heat_cost_total_4 = _print(records1)[4]
    lb_heat_cost_total_5 = _print(records1)[5]
    lb_heat_cost_total_6 = _print(records1)[6]
    lb_heat_cost_total_7 = _print(records1)[7]
    lb_heat_cost_total_8 = _print(records1)[8]
    lb_heat_cost_total_9 = _print(records1)[9]
    lb_heat_cost_total_10 = _print(records1)[10]
    lb_heat_cost_total_11 = _print(records1)[11]
    lb_heat_cost_total_12 = _print(records1)[12]
    lb_heat_cost_total_13 = _print(records1)[13]
    lb_heat_cost_total_14 = _print(records1)[14]
    lb_heat_cost_total_15 = _print(records1)[15]
    lb_heat_cost_total_16 = _print(records1)[16]
    lb_heat_cost_total_17 = _print(records1)[17]
    lb_heat_cost_total_18 = _print(records1)[18]
    lb_heat_cost_total_19 = _print(records1)[19]
    lb_heat_cost_total_20 = _print(records1)[20]
    lb_heat_cost_total_21 = _print(records1)[21]
    lb_heat_cost_total_22 = _print(records1)[22]
    lb_heat_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_heat_cost_total_0', 'lb_heat_cost_total_1', 'lb_heat_cost_total_2',
         'lb_heat_cost_total_3', 'lb_heat_cost_total_4', 'lb_heat_cost_total_5',
         'lb_heat_cost_total_6', 'lb_heat_cost_total_7', 'lb_heat_cost_total_8',
         'lb_heat_cost_total_9', 'lb_heat_cost_total_10', 'lb_heat_cost_total_11',
         'lb_heat_cost_total_12', 'lb_heat_cost_total_13', 'lb_heat_cost_total_14',
         'lb_heat_cost_total_15', 'lb_heat_cost_total_16', 'lb_heat_cost_total_17',
         'lb_heat_cost_total_18', 'lb_heat_cost_total_19', 'lb_heat_cost_total_20',
         'lb_heat_cost_total_21', 'lb_heat_cost_total_22', 'lb_heat_cost_total_23'],
        [lb_heat_cost_total_0, lb_heat_cost_total_1, lb_heat_cost_total_2,
         lb_heat_cost_total_3, lb_heat_cost_total_4, lb_heat_cost_total_5,
         lb_heat_cost_total_6, lb_heat_cost_total_7, lb_heat_cost_total_8,
         lb_heat_cost_total_9, lb_heat_cost_total_10, lb_heat_cost_total_11,
         lb_heat_cost_total_12, lb_heat_cost_total_13, lb_heat_cost_total_14,
         lb_heat_cost_total_15, lb_heat_cost_total_16, lb_heat_cost_total_17,
         lb_heat_cost_total_18, lb_heat_cost_total_19, lb_heat_cost_total_20,
         lb_heat_cost_total_21, lb_heat_cost_total_22, lb_heat_cost_total_23])


def write_to_database_lb_hot_water_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂生活热水成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_hot_water_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_hot_water_cost_total_0 = _print(records1)[0]
    lb_hot_water_cost_total_1 = _print(records1)[1]
    lb_hot_water_cost_total_2 = _print(records1)[2]
    lb_hot_water_cost_total_3 = _print(records1)[3]
    lb_hot_water_cost_total_4 = _print(records1)[4]
    lb_hot_water_cost_total_5 = _print(records1)[5]
    lb_hot_water_cost_total_6 = _print(records1)[6]
    lb_hot_water_cost_total_7 = _print(records1)[7]
    lb_hot_water_cost_total_8 = _print(records1)[8]
    lb_hot_water_cost_total_9 = _print(records1)[9]
    lb_hot_water_cost_total_10 = _print(records1)[10]
    lb_hot_water_cost_total_11 = _print(records1)[11]
    lb_hot_water_cost_total_12 = _print(records1)[12]
    lb_hot_water_cost_total_13 = _print(records1)[13]
    lb_hot_water_cost_total_14 = _print(records1)[14]
    lb_hot_water_cost_total_15 = _print(records1)[15]
    lb_hot_water_cost_total_16 = _print(records1)[16]
    lb_hot_water_cost_total_17 = _print(records1)[17]
    lb_hot_water_cost_total_18 = _print(records1)[18]
    lb_hot_water_cost_total_19 = _print(records1)[19]
    lb_hot_water_cost_total_20 = _print(records1)[20]
    lb_hot_water_cost_total_21 = _print(records1)[21]
    lb_hot_water_cost_total_22 = _print(records1)[22]
    lb_hot_water_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_hot_water_cost_total_0', 'lb_hot_water_cost_total_1', 'lb_hot_water_cost_total_2',
         'lb_hot_water_cost_total_3', 'lb_hot_water_cost_total_4', 'lb_hot_water_cost_total_5',
         'lb_hot_water_cost_total_6', 'lb_hot_water_cost_total_7', 'lb_hot_water_cost_total_8',
         'lb_hot_water_cost_total_9', 'lb_hot_water_cost_total_10', 'lb_hot_water_cost_total_11',
         'lb_hot_water_cost_total_12', 'lb_hot_water_cost_total_13', 'lb_hot_water_cost_total_14',
         'lb_hot_water_cost_total_15', 'lb_hot_water_cost_total_16', 'lb_hot_water_cost_total_17',
         'lb_hot_water_cost_total_18', 'lb_hot_water_cost_total_19', 'lb_hot_water_cost_total_20',
         'lb_hot_water_cost_total_21', 'lb_hot_water_cost_total_22', 'lb_hot_water_cost_total_23'],
        [lb_hot_water_cost_total_0, lb_hot_water_cost_total_1, lb_hot_water_cost_total_2,
         lb_hot_water_cost_total_3, lb_hot_water_cost_total_4, lb_hot_water_cost_total_5,
         lb_hot_water_cost_total_6, lb_hot_water_cost_total_7, lb_hot_water_cost_total_8,
         lb_hot_water_cost_total_9, lb_hot_water_cost_total_10, lb_hot_water_cost_total_11,
         lb_hot_water_cost_total_12, lb_hot_water_cost_total_13, lb_hot_water_cost_total_14,
         lb_hot_water_cost_total_15, lb_hot_water_cost_total_16, lb_hot_water_cost_total_17,
         lb_hot_water_cost_total_18, lb_hot_water_cost_total_19, lb_hot_water_cost_total_20,
         lb_hot_water_cost_total_21, lb_hot_water_cost_total_22, lb_hot_water_cost_total_23])


def write_to_database_cc_cold_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机制冷成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc_cold_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    cc_cold_cost_total_0 = _print(records1)[0]
    cc_cold_cost_total_1 = _print(records1)[1]
    cc_cold_cost_total_2 = _print(records1)[2]
    cc_cold_cost_total_3 = _print(records1)[3]
    cc_cold_cost_total_4 = _print(records1)[4]
    cc_cold_cost_total_5 = _print(records1)[5]
    cc_cold_cost_total_6 = _print(records1)[6]
    cc_cold_cost_total_7 = _print(records1)[7]
    cc_cold_cost_total_8 = _print(records1)[8]
    cc_cold_cost_total_9 = _print(records1)[9]
    cc_cold_cost_total_10 = _print(records1)[10]
    cc_cold_cost_total_11 = _print(records1)[11]
    cc_cold_cost_total_12 = _print(records1)[12]
    cc_cold_cost_total_13 = _print(records1)[13]
    cc_cold_cost_total_14 = _print(records1)[14]
    cc_cold_cost_total_15 = _print(records1)[15]
    cc_cold_cost_total_16 = _print(records1)[16]
    cc_cold_cost_total_17 = _print(records1)[17]
    cc_cold_cost_total_18 = _print(records1)[18]
    cc_cold_cost_total_19 = _print(records1)[19]
    cc_cold_cost_total_20 = _print(records1)[20]
    cc_cold_cost_total_21 = _print(records1)[21]
    cc_cold_cost_total_22 = _print(records1)[22]
    cc_cold_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc_cold_cost_total_0', 'cc_cold_cost_total_1', 'cc_cold_cost_total_2',
         'cc_cold_cost_total_3', 'cc_cold_cost_total_4', 'cc_cold_cost_total_5',
         'cc_cold_cost_total_6', 'cc_cold_cost_total_7', 'cc_cold_cost_total_8',
         'cc_cold_cost_total_9', 'cc_cold_cost_total_10', 'cc_cold_cost_total_11',
         'cc_cold_cost_total_12', 'cc_cold_cost_total_13', 'cc_cold_cost_total_14',
         'cc_cold_cost_total_15', 'cc_cold_cost_total_16', 'cc_cold_cost_total_17',
         'cc_cold_cost_total_18', 'cc_cold_cost_total_19', 'cc_cold_cost_total_20',
         'cc_cold_cost_total_21', 'cc_cold_cost_total_22', 'cc_cold_cost_total_23'],
        [cc_cold_cost_total_0, cc_cold_cost_total_1, cc_cold_cost_total_2,
         cc_cold_cost_total_3, cc_cold_cost_total_4, cc_cold_cost_total_5,
         cc_cold_cost_total_6, cc_cold_cost_total_7, cc_cold_cost_total_8,
         cc_cold_cost_total_9, cc_cold_cost_total_10, cc_cold_cost_total_11,
         cc_cold_cost_total_12, cc_cold_cost_total_13, cc_cold_cost_total_14,
         cc_cold_cost_total_15, cc_cold_cost_total_16, cc_cold_cost_total_17,
         cc_cold_cost_total_18, cc_cold_cost_total_19, cc_cold_cost_total_20,
         cc_cold_cost_total_21, cc_cold_cost_total_22, cc_cold_cost_total_23])


def write_to_database_chp_cold_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制冷成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_cold_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_cold_cost_total_0 = _print(records1)[0]
    chp_cold_cost_total_1 = _print(records1)[1]
    chp_cold_cost_total_2 = _print(records1)[2]
    chp_cold_cost_total_3 = _print(records1)[3]
    chp_cold_cost_total_4 = _print(records1)[4]
    chp_cold_cost_total_5 = _print(records1)[5]
    chp_cold_cost_total_6 = _print(records1)[6]
    chp_cold_cost_total_7 = _print(records1)[7]
    chp_cold_cost_total_8 = _print(records1)[8]
    chp_cold_cost_total_9 = _print(records1)[9]
    chp_cold_cost_total_10 = _print(records1)[10]
    chp_cold_cost_total_11 = _print(records1)[11]
    chp_cold_cost_total_12 = _print(records1)[12]
    chp_cold_cost_total_13 = _print(records1)[13]
    chp_cold_cost_total_14 = _print(records1)[14]
    chp_cold_cost_total_15 = _print(records1)[15]
    chp_cold_cost_total_16 = _print(records1)[16]
    chp_cold_cost_total_17 = _print(records1)[17]
    chp_cold_cost_total_18 = _print(records1)[18]
    chp_cold_cost_total_19 = _print(records1)[19]
    chp_cold_cost_total_20 = _print(records1)[20]
    chp_cold_cost_total_21 = _print(records1)[21]
    chp_cold_cost_total_22 = _print(records1)[22]
    chp_cold_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_cold_cost_total_0', 'chp_cold_cost_total_1', 'chp_cold_cost_total_2',
         'chp_cold_cost_total_3', 'chp_cold_cost_total_4', 'chp_cold_cost_total_5',
         'chp_cold_cost_total_6', 'chp_cold_cost_total_7', 'chp_cold_cost_total_8',
         'chp_cold_cost_total_9', 'chp_cold_cost_total_10', 'chp_cold_cost_total_11',
         'chp_cold_cost_total_12', 'chp_cold_cost_total_13', 'chp_cold_cost_total_14',
         'chp_cold_cost_total_15', 'chp_cold_cost_total_16', 'chp_cold_cost_total_17',
         'chp_cold_cost_total_18', 'chp_cold_cost_total_19', 'chp_cold_cost_total_20',
         'chp_cold_cost_total_21', 'chp_cold_cost_total_22', 'chp_cold_cost_total_23'],
        [chp_cold_cost_total_0, chp_cold_cost_total_1, chp_cold_cost_total_2,
         chp_cold_cost_total_3, chp_cold_cost_total_4, chp_cold_cost_total_5,
         chp_cold_cost_total_6, chp_cold_cost_total_7, chp_cold_cost_total_8,
         chp_cold_cost_total_9, chp_cold_cost_total_10, chp_cold_cost_total_11,
         chp_cold_cost_total_12, chp_cold_cost_total_13, chp_cold_cost_total_14,
         chp_cold_cost_total_15, chp_cold_cost_total_16, chp_cold_cost_total_17,
         chp_cold_cost_total_18, chp_cold_cost_total_19, chp_cold_cost_total_20,
         chp_cold_cost_total_21, chp_cold_cost_total_22, chp_cold_cost_total_23])


def write_to_database_chp_heat_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制热成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_heat_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_heat_cost_total_0 = _print(records1)[0]
    chp_heat_cost_total_1 = _print(records1)[1]
    chp_heat_cost_total_2 = _print(records1)[2]
    chp_heat_cost_total_3 = _print(records1)[3]
    chp_heat_cost_total_4 = _print(records1)[4]
    chp_heat_cost_total_5 = _print(records1)[5]
    chp_heat_cost_total_6 = _print(records1)[6]
    chp_heat_cost_total_7 = _print(records1)[7]
    chp_heat_cost_total_8 = _print(records1)[8]
    chp_heat_cost_total_9 = _print(records1)[9]
    chp_heat_cost_total_10 = _print(records1)[10]
    chp_heat_cost_total_11 = _print(records1)[11]
    chp_heat_cost_total_12 = _print(records1)[12]
    chp_heat_cost_total_13 = _print(records1)[13]
    chp_heat_cost_total_14 = _print(records1)[14]
    chp_heat_cost_total_15 = _print(records1)[15]
    chp_heat_cost_total_16 = _print(records1)[16]
    chp_heat_cost_total_17 = _print(records1)[17]
    chp_heat_cost_total_18 = _print(records1)[18]
    chp_heat_cost_total_19 = _print(records1)[19]
    chp_heat_cost_total_20 = _print(records1)[20]
    chp_heat_cost_total_21 = _print(records1)[21]
    chp_heat_cost_total_22 = _print(records1)[22]
    chp_heat_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_heat_cost_total_0', 'chp_heat_cost_total_1', 'chp_heat_cost_total_2',
         'chp_heat_cost_total_3', 'chp_heat_cost_total_4', 'chp_heat_cost_total_5',
         'chp_heat_cost_total_6', 'chp_heat_cost_total_7', 'chp_heat_cost_total_8',
         'chp_heat_cost_total_9', 'chp_heat_cost_total_10', 'chp_heat_cost_total_11',
         'chp_heat_cost_total_12', 'chp_heat_cost_total_13', 'chp_heat_cost_total_14',
         'chp_heat_cost_total_15', 'chp_heat_cost_total_16', 'chp_heat_cost_total_17',
         'chp_heat_cost_total_18', 'chp_heat_cost_total_19', 'chp_heat_cost_total_20',
         'chp_heat_cost_total_21', 'chp_heat_cost_total_22', 'chp_heat_cost_total_23'],
        [chp_heat_cost_total_0, chp_heat_cost_total_1, chp_heat_cost_total_2,
         chp_heat_cost_total_3, chp_heat_cost_total_4, chp_heat_cost_total_5,
         chp_heat_cost_total_6, chp_heat_cost_total_7, chp_heat_cost_total_8,
         chp_heat_cost_total_9, chp_heat_cost_total_10, chp_heat_cost_total_11,
         chp_heat_cost_total_12, chp_heat_cost_total_13, chp_heat_cost_total_14,
         chp_heat_cost_total_15, chp_heat_cost_total_16, chp_heat_cost_total_17,
         chp_heat_cost_total_18, chp_heat_cost_total_19, chp_heat_cost_total_20,
         chp_heat_cost_total_21, chp_heat_cost_total_22, chp_heat_cost_total_23])


def write_to_database_ashp_cold_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制冷成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_cold_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_cold_cost_total_0 = _print(records1)[0]
    ashp_cold_cost_total_1 = _print(records1)[1]
    ashp_cold_cost_total_2 = _print(records1)[2]
    ashp_cold_cost_total_3 = _print(records1)[3]
    ashp_cold_cost_total_4 = _print(records1)[4]
    ashp_cold_cost_total_5 = _print(records1)[5]
    ashp_cold_cost_total_6 = _print(records1)[6]
    ashp_cold_cost_total_7 = _print(records1)[7]
    ashp_cold_cost_total_8 = _print(records1)[8]
    ashp_cold_cost_total_9 = _print(records1)[9]
    ashp_cold_cost_total_10 = _print(records1)[10]
    ashp_cold_cost_total_11 = _print(records1)[11]
    ashp_cold_cost_total_12 = _print(records1)[12]
    ashp_cold_cost_total_13 = _print(records1)[13]
    ashp_cold_cost_total_14 = _print(records1)[14]
    ashp_cold_cost_total_15 = _print(records1)[15]
    ashp_cold_cost_total_16 = _print(records1)[16]
    ashp_cold_cost_total_17 = _print(records1)[17]
    ashp_cold_cost_total_18 = _print(records1)[18]
    ashp_cold_cost_total_19 = _print(records1)[19]
    ashp_cold_cost_total_20 = _print(records1)[20]
    ashp_cold_cost_total_21 = _print(records1)[21]
    ashp_cold_cost_total_22 = _print(records1)[22]
    ashp_cold_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_cold_cost_total_0', 'ashp_cold_cost_total_1', 'ashp_cold_cost_total_2',
         'ashp_cold_cost_total_3', 'ashp_cold_cost_total_4', 'ashp_cold_cost_total_5',
         'ashp_cold_cost_total_6', 'ashp_cold_cost_total_7', 'ashp_cold_cost_total_8',
         'ashp_cold_cost_total_9', 'ashp_cold_cost_total_10', 'ashp_cold_cost_total_11',
         'ashp_cold_cost_total_12', 'ashp_cold_cost_total_13', 'ashp_cold_cost_total_14',
         'ashp_cold_cost_total_15', 'ashp_cold_cost_total_16', 'ashp_cold_cost_total_17',
         'ashp_cold_cost_total_18', 'ashp_cold_cost_total_19', 'ashp_cold_cost_total_20',
         'ashp_cold_cost_total_21', 'ashp_cold_cost_total_22', 'ashp_cold_cost_total_23'],
        [ashp_cold_cost_total_0, ashp_cold_cost_total_1, ashp_cold_cost_total_2,
         ashp_cold_cost_total_3, ashp_cold_cost_total_4, ashp_cold_cost_total_5,
         ashp_cold_cost_total_6, ashp_cold_cost_total_7, ashp_cold_cost_total_8,
         ashp_cold_cost_total_9, ashp_cold_cost_total_10, ashp_cold_cost_total_11,
         ashp_cold_cost_total_12, ashp_cold_cost_total_13, ashp_cold_cost_total_14,
         ashp_cold_cost_total_15, ashp_cold_cost_total_16, ashp_cold_cost_total_17,
         ashp_cold_cost_total_18, ashp_cold_cost_total_19, ashp_cold_cost_total_20,
         ashp_cold_cost_total_21, ashp_cold_cost_total_22, ashp_cold_cost_total_23])


def write_to_database_ashp_heat_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制热成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_heat_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_heat_cost_total_0 = _print(records1)[0]
    ashp_heat_cost_total_1 = _print(records1)[1]
    ashp_heat_cost_total_2 = _print(records1)[2]
    ashp_heat_cost_total_3 = _print(records1)[3]
    ashp_heat_cost_total_4 = _print(records1)[4]
    ashp_heat_cost_total_5 = _print(records1)[5]
    ashp_heat_cost_total_6 = _print(records1)[6]
    ashp_heat_cost_total_7 = _print(records1)[7]
    ashp_heat_cost_total_8 = _print(records1)[8]
    ashp_heat_cost_total_9 = _print(records1)[9]
    ashp_heat_cost_total_10 = _print(records1)[10]
    ashp_heat_cost_total_11 = _print(records1)[11]
    ashp_heat_cost_total_12 = _print(records1)[12]
    ashp_heat_cost_total_13 = _print(records1)[13]
    ashp_heat_cost_total_14 = _print(records1)[14]
    ashp_heat_cost_total_15 = _print(records1)[15]
    ashp_heat_cost_total_16 = _print(records1)[16]
    ashp_heat_cost_total_17 = _print(records1)[17]
    ashp_heat_cost_total_18 = _print(records1)[18]
    ashp_heat_cost_total_19 = _print(records1)[19]
    ashp_heat_cost_total_20 = _print(records1)[20]
    ashp_heat_cost_total_21 = _print(records1)[21]
    ashp_heat_cost_total_22 = _print(records1)[22]
    ashp_heat_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_heat_cost_total_0', 'ashp_heat_cost_total_1', 'ashp_heat_cost_total_2',
         'ashp_heat_cost_total_3', 'ashp_heat_cost_total_4', 'ashp_heat_cost_total_5',
         'ashp_heat_cost_total_6', 'ashp_heat_cost_total_7', 'ashp_heat_cost_total_8',
         'ashp_heat_cost_total_9', 'ashp_heat_cost_total_10', 'ashp_heat_cost_total_11',
         'ashp_heat_cost_total_12', 'ashp_heat_cost_total_13', 'ashp_heat_cost_total_14',
         'ashp_heat_cost_total_15', 'ashp_heat_cost_total_16', 'ashp_heat_cost_total_17',
         'ashp_heat_cost_total_18', 'ashp_heat_cost_total_19', 'ashp_heat_cost_total_20',
         'ashp_heat_cost_total_21', 'ashp_heat_cost_total_22', 'ashp_heat_cost_total_23'],
        [ashp_heat_cost_total_0, ashp_heat_cost_total_1, ashp_heat_cost_total_2,
         ashp_heat_cost_total_3, ashp_heat_cost_total_4, ashp_heat_cost_total_5,
         ashp_heat_cost_total_6, ashp_heat_cost_total_7, ashp_heat_cost_total_8,
         ashp_heat_cost_total_9, ashp_heat_cost_total_10, ashp_heat_cost_total_11,
         ashp_heat_cost_total_12, ashp_heat_cost_total_13, ashp_heat_cost_total_14,
         ashp_heat_cost_total_15, ashp_heat_cost_total_16, ashp_heat_cost_total_17,
         ashp_heat_cost_total_18, ashp_heat_cost_total_19, ashp_heat_cost_total_20,
         ashp_heat_cost_total_21, ashp_heat_cost_total_22, ashp_heat_cost_total_23])


def write_to_database_ngb_hot_water_cost_total_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入天然气锅炉生活热水成本24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ngb_hot_water_cost_total',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ngb_hot_water_cost_total_0 = _print(records1)[0]
    ngb_hot_water_cost_total_1 = _print(records1)[1]
    ngb_hot_water_cost_total_2 = _print(records1)[2]
    ngb_hot_water_cost_total_3 = _print(records1)[3]
    ngb_hot_water_cost_total_4 = _print(records1)[4]
    ngb_hot_water_cost_total_5 = _print(records1)[5]
    ngb_hot_water_cost_total_6 = _print(records1)[6]
    ngb_hot_water_cost_total_7 = _print(records1)[7]
    ngb_hot_water_cost_total_8 = _print(records1)[8]
    ngb_hot_water_cost_total_9 = _print(records1)[9]
    ngb_hot_water_cost_total_10 = _print(records1)[10]
    ngb_hot_water_cost_total_11 = _print(records1)[11]
    ngb_hot_water_cost_total_12 = _print(records1)[12]
    ngb_hot_water_cost_total_13 = _print(records1)[13]
    ngb_hot_water_cost_total_14 = _print(records1)[14]
    ngb_hot_water_cost_total_15 = _print(records1)[15]
    ngb_hot_water_cost_total_16 = _print(records1)[16]
    ngb_hot_water_cost_total_17 = _print(records1)[17]
    ngb_hot_water_cost_total_18 = _print(records1)[18]
    ngb_hot_water_cost_total_19 = _print(records1)[19]
    ngb_hot_water_cost_total_20 = _print(records1)[20]
    ngb_hot_water_cost_total_21 = _print(records1)[21]
    ngb_hot_water_cost_total_22 = _print(records1)[22]
    ngb_hot_water_cost_total_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb_hot_water_cost_total_0', 'ngb_hot_water_cost_total_1', 'ngb_hot_water_cost_total_2',
         'ngb_hot_water_cost_total_3', 'ngb_hot_water_cost_total_4', 'ngb_hot_water_cost_total_5',
         'ngb_hot_water_cost_total_6', 'ngb_hot_water_cost_total_7', 'ngb_hot_water_cost_total_8',
         'ngb_hot_water_cost_total_9', 'ngb_hot_water_cost_total_10', 'ngb_hot_water_cost_total_11',
         'ngb_hot_water_cost_total_12', 'ngb_hot_water_cost_total_13', 'ngb_hot_water_cost_total_14',
         'ngb_hot_water_cost_total_15', 'ngb_hot_water_cost_total_16', 'ngb_hot_water_cost_total_17',
         'ngb_hot_water_cost_total_18', 'ngb_hot_water_cost_total_19', 'ngb_hot_water_cost_total_20',
         'ngb_hot_water_cost_total_21', 'ngb_hot_water_cost_total_22', 'ngb_hot_water_cost_total_23'],
        [ngb_hot_water_cost_total_0, ngb_hot_water_cost_total_1, ngb_hot_water_cost_total_2,
         ngb_hot_water_cost_total_3, ngb_hot_water_cost_total_4, ngb_hot_water_cost_total_5,
         ngb_hot_water_cost_total_6, ngb_hot_water_cost_total_7, ngb_hot_water_cost_total_8,
         ngb_hot_water_cost_total_9, ngb_hot_water_cost_total_10, ngb_hot_water_cost_total_11,
         ngb_hot_water_cost_total_12, ngb_hot_water_cost_total_13, ngb_hot_water_cost_total_14,
         ngb_hot_water_cost_total_15, ngb_hot_water_cost_total_16, ngb_hot_water_cost_total_17,
         ngb_hot_water_cost_total_18, ngb_hot_water_cost_total_19, ngb_hot_water_cost_total_20,
         ngb_hot_water_cost_total_21, ngb_hot_water_cost_total_22, ngb_hot_water_cost_total_23])

def write_to_database_ice_electrical_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机发电效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ice_electrical_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ice_electrical_efficiency_0 = _print(records1)[0]
    ice_electrical_efficiency_1 = _print(records1)[1]
    ice_electrical_efficiency_2 = _print(records1)[2]
    ice_electrical_efficiency_3 = _print(records1)[3]
    ice_electrical_efficiency_4 = _print(records1)[4]
    ice_electrical_efficiency_5 = _print(records1)[5]
    ice_electrical_efficiency_6 = _print(records1)[6]
    ice_electrical_efficiency_7 = _print(records1)[7]
    ice_electrical_efficiency_8 = _print(records1)[8]
    ice_electrical_efficiency_9 = _print(records1)[9]
    ice_electrical_efficiency_10 = _print(records1)[10]
    ice_electrical_efficiency_11 = _print(records1)[11]
    ice_electrical_efficiency_12 = _print(records1)[12]
    ice_electrical_efficiency_13 = _print(records1)[13]
    ice_electrical_efficiency_14 = _print(records1)[14]
    ice_electrical_efficiency_15 = _print(records1)[15]
    ice_electrical_efficiency_16 = _print(records1)[16]
    ice_electrical_efficiency_17 = _print(records1)[17]
    ice_electrical_efficiency_18 = _print(records1)[18]
    ice_electrical_efficiency_19 = _print(records1)[19]
    ice_electrical_efficiency_20 = _print(records1)[20]
    ice_electrical_efficiency_21 = _print(records1)[21]
    ice_electrical_efficiency_22 = _print(records1)[22]
    ice_electrical_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ice_electrical_efficiency_0', 'ice_electrical_efficiency_1', 'ice_electrical_efficiency_2',
         'ice_electrical_efficiency_3', 'ice_electrical_efficiency_4', 'ice_electrical_efficiency_5',
         'ice_electrical_efficiency_6', 'ice_electrical_efficiency_7', 'ice_electrical_efficiency_8',
         'ice_electrical_efficiency_9', 'ice_electrical_efficiency_10', 'ice_electrical_efficiency_11',
         'ice_electrical_efficiency_12', 'ice_electrical_efficiency_13', 'ice_electrical_efficiency_14',
         'ice_electrical_efficiency_15', 'ice_electrical_efficiency_16', 'ice_electrical_efficiency_17',
         'ice_electrical_efficiency_18', 'ice_electrical_efficiency_19', 'ice_electrical_efficiency_20',
         'ice_electrical_efficiency_21', 'ice_electrical_efficiency_22', 'ice_electrical_efficiency_23'],
        [ice_electrical_efficiency_0, ice_electrical_efficiency_1, ice_electrical_efficiency_2,
         ice_electrical_efficiency_3, ice_electrical_efficiency_4, ice_electrical_efficiency_5,
         ice_electrical_efficiency_6, ice_electrical_efficiency_7, ice_electrical_efficiency_8,
         ice_electrical_efficiency_9, ice_electrical_efficiency_10, ice_electrical_efficiency_11,
         ice_electrical_efficiency_12, ice_electrical_efficiency_13, ice_electrical_efficiency_14,
         ice_electrical_efficiency_15, ice_electrical_efficiency_16, ice_electrical_efficiency_17,
         ice_electrical_efficiency_18, ice_electrical_efficiency_19, ice_electrical_efficiency_20,
         ice_electrical_efficiency_21, ice_electrical_efficiency_22, ice_electrical_efficiency_23])


def write_to_database_lb_cold_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制冷效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_cold_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_cold_efficiency_0 = _print(records1)[0]
    lb_cold_efficiency_1 = _print(records1)[1]
    lb_cold_efficiency_2 = _print(records1)[2]
    lb_cold_efficiency_3 = _print(records1)[3]
    lb_cold_efficiency_4 = _print(records1)[4]
    lb_cold_efficiency_5 = _print(records1)[5]
    lb_cold_efficiency_6 = _print(records1)[6]
    lb_cold_efficiency_7 = _print(records1)[7]
    lb_cold_efficiency_8 = _print(records1)[8]
    lb_cold_efficiency_9 = _print(records1)[9]
    lb_cold_efficiency_10 = _print(records1)[10]
    lb_cold_efficiency_11 = _print(records1)[11]
    lb_cold_efficiency_12 = _print(records1)[12]
    lb_cold_efficiency_13 = _print(records1)[13]
    lb_cold_efficiency_14 = _print(records1)[14]
    lb_cold_efficiency_15 = _print(records1)[15]
    lb_cold_efficiency_16 = _print(records1)[16]
    lb_cold_efficiency_17 = _print(records1)[17]
    lb_cold_efficiency_18 = _print(records1)[18]
    lb_cold_efficiency_19 = _print(records1)[19]
    lb_cold_efficiency_20 = _print(records1)[20]
    lb_cold_efficiency_21 = _print(records1)[21]
    lb_cold_efficiency_22 = _print(records1)[22]
    lb_cold_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_cold_efficiency_0', 'lb_cold_efficiency_1', 'lb_cold_efficiency_2',
         'lb_cold_efficiency_3', 'lb_cold_efficiency_4', 'lb_cold_efficiency_5',
         'lb_cold_efficiency_6', 'lb_cold_efficiency_7', 'lb_cold_efficiency_8',
         'lb_cold_efficiency_9', 'lb_cold_efficiency_10', 'lb_cold_efficiency_11',
         'lb_cold_efficiency_12', 'lb_cold_efficiency_13', 'lb_cold_efficiency_14',
         'lb_cold_efficiency_15', 'lb_cold_efficiency_16', 'lb_cold_efficiency_17',
         'lb_cold_efficiency_18', 'lb_cold_efficiency_19', 'lb_cold_efficiency_20',
         'lb_cold_efficiency_21', 'lb_cold_efficiency_22', 'lb_cold_efficiency_23'],
        [lb_cold_efficiency_0, lb_cold_efficiency_1, lb_cold_efficiency_2,
         lb_cold_efficiency_3, lb_cold_efficiency_4, lb_cold_efficiency_5,
         lb_cold_efficiency_6, lb_cold_efficiency_7, lb_cold_efficiency_8,
         lb_cold_efficiency_9, lb_cold_efficiency_10, lb_cold_efficiency_11,
         lb_cold_efficiency_12, lb_cold_efficiency_13, lb_cold_efficiency_14,
         lb_cold_efficiency_15, lb_cold_efficiency_16, lb_cold_efficiency_17,
         lb_cold_efficiency_18, lb_cold_efficiency_19, lb_cold_efficiency_20,
         lb_cold_efficiency_21, lb_cold_efficiency_22, lb_cold_efficiency_23])

def write_to_database_lb_heat_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂制热效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_heat_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_heat_efficiency_0 = _print(records1)[0]
    lb_heat_efficiency_1 = _print(records1)[1]
    lb_heat_efficiency_2 = _print(records1)[2]
    lb_heat_efficiency_3 = _print(records1)[3]
    lb_heat_efficiency_4 = _print(records1)[4]
    lb_heat_efficiency_5 = _print(records1)[5]
    lb_heat_efficiency_6 = _print(records1)[6]
    lb_heat_efficiency_7 = _print(records1)[7]
    lb_heat_efficiency_8 = _print(records1)[8]
    lb_heat_efficiency_9 = _print(records1)[9]
    lb_heat_efficiency_10 = _print(records1)[10]
    lb_heat_efficiency_11 = _print(records1)[11]
    lb_heat_efficiency_12 = _print(records1)[12]
    lb_heat_efficiency_13 = _print(records1)[13]
    lb_heat_efficiency_14 = _print(records1)[14]
    lb_heat_efficiency_15 = _print(records1)[15]
    lb_heat_efficiency_16 = _print(records1)[16]
    lb_heat_efficiency_17 = _print(records1)[17]
    lb_heat_efficiency_18 = _print(records1)[18]
    lb_heat_efficiency_19 = _print(records1)[19]
    lb_heat_efficiency_20 = _print(records1)[20]
    lb_heat_efficiency_21 = _print(records1)[21]
    lb_heat_efficiency_22 = _print(records1)[22]
    lb_heat_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_heat_efficiency_0', 'lb_heat_efficiency_1', 'lb_heat_efficiency_2',
         'lb_heat_efficiency_3', 'lb_heat_efficiency_4', 'lb_heat_efficiency_5',
         'lb_heat_efficiency_6', 'lb_heat_efficiency_7', 'lb_heat_efficiency_8',
         'lb_heat_efficiency_9', 'lb_heat_efficiency_10', 'lb_heat_efficiency_11',
         'lb_heat_efficiency_12', 'lb_heat_efficiency_13', 'lb_heat_efficiency_14',
         'lb_heat_efficiency_15', 'lb_heat_efficiency_16', 'lb_heat_efficiency_17',
         'lb_heat_efficiency_18', 'lb_heat_efficiency_19', 'lb_heat_efficiency_20',
         'lb_heat_efficiency_21', 'lb_heat_efficiency_22', 'lb_heat_efficiency_23'],
        [lb_heat_efficiency_0, lb_heat_efficiency_1, lb_heat_efficiency_2,
         lb_heat_efficiency_3, lb_heat_efficiency_4, lb_heat_efficiency_5,
         lb_heat_efficiency_6, lb_heat_efficiency_7, lb_heat_efficiency_8,
         lb_heat_efficiency_9, lb_heat_efficiency_10, lb_heat_efficiency_11,
         lb_heat_efficiency_12, lb_heat_efficiency_13, lb_heat_efficiency_14,
         lb_heat_efficiency_15, lb_heat_efficiency_16, lb_heat_efficiency_17,
         lb_heat_efficiency_18, lb_heat_efficiency_19, lb_heat_efficiency_20,
         lb_heat_efficiency_21, lb_heat_efficiency_22, lb_heat_efficiency_23])


def write_to_database_lb_hot_water_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂生活热水效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('lb_hot_water_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    lb_hot_water_efficiency_0 = _print(records1)[0]
    lb_hot_water_efficiency_1 = _print(records1)[1]
    lb_hot_water_efficiency_2 = _print(records1)[2]
    lb_hot_water_efficiency_3 = _print(records1)[3]
    lb_hot_water_efficiency_4 = _print(records1)[4]
    lb_hot_water_efficiency_5 = _print(records1)[5]
    lb_hot_water_efficiency_6 = _print(records1)[6]
    lb_hot_water_efficiency_7 = _print(records1)[7]
    lb_hot_water_efficiency_8 = _print(records1)[8]
    lb_hot_water_efficiency_9 = _print(records1)[9]
    lb_hot_water_efficiency_10 = _print(records1)[10]
    lb_hot_water_efficiency_11 = _print(records1)[11]
    lb_hot_water_efficiency_12 = _print(records1)[12]
    lb_hot_water_efficiency_13 = _print(records1)[13]
    lb_hot_water_efficiency_14 = _print(records1)[14]
    lb_hot_water_efficiency_15 = _print(records1)[15]
    lb_hot_water_efficiency_16 = _print(records1)[16]
    lb_hot_water_efficiency_17 = _print(records1)[17]
    lb_hot_water_efficiency_18 = _print(records1)[18]
    lb_hot_water_efficiency_19 = _print(records1)[19]
    lb_hot_water_efficiency_20 = _print(records1)[20]
    lb_hot_water_efficiency_21 = _print(records1)[21]
    lb_hot_water_efficiency_22 = _print(records1)[22]
    lb_hot_water_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['lb_hot_water_efficiency_0', 'lb_hot_water_efficiency_1', 'lb_hot_water_efficiency_2',
         'lb_hot_water_efficiency_3', 'lb_hot_water_efficiency_4', 'lb_hot_water_efficiency_5',
         'lb_hot_water_efficiency_6', 'lb_hot_water_efficiency_7', 'lb_hot_water_efficiency_8',
         'lb_hot_water_efficiency_9', 'lb_hot_water_efficiency_10', 'lb_hot_water_efficiency_11',
         'lb_hot_water_efficiency_12', 'lb_hot_water_efficiency_13', 'lb_hot_water_efficiency_14',
         'lb_hot_water_efficiency_15', 'lb_hot_water_efficiency_16', 'lb_hot_water_efficiency_17',
         'lb_hot_water_efficiency_18', 'lb_hot_water_efficiency_19', 'lb_hot_water_efficiency_20',
         'lb_hot_water_efficiency_21', 'lb_hot_water_efficiency_22', 'lb_hot_water_efficiency_23'],
        [lb_hot_water_efficiency_0, lb_hot_water_efficiency_1, lb_hot_water_efficiency_2,
         lb_hot_water_efficiency_3, lb_hot_water_efficiency_4, lb_hot_water_efficiency_5,
         lb_hot_water_efficiency_6, lb_hot_water_efficiency_7, lb_hot_water_efficiency_8,
         lb_hot_water_efficiency_9, lb_hot_water_efficiency_10, lb_hot_water_efficiency_11,
         lb_hot_water_efficiency_12, lb_hot_water_efficiency_13, lb_hot_water_efficiency_14,
         lb_hot_water_efficiency_15, lb_hot_water_efficiency_16, lb_hot_water_efficiency_17,
         lb_hot_water_efficiency_18, lb_hot_water_efficiency_19, lb_hot_water_efficiency_20,
         lb_hot_water_efficiency_21, lb_hot_water_efficiency_22, lb_hot_water_efficiency_23])


def write_to_database_cc_cold_cop_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机制冷效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('cc_cold_cop',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    cc_cold_cop_0 = _print(records1)[0]
    cc_cold_cop_1 = _print(records1)[1]
    cc_cold_cop_2 = _print(records1)[2]
    cc_cold_cop_3 = _print(records1)[3]
    cc_cold_cop_4 = _print(records1)[4]
    cc_cold_cop_5 = _print(records1)[5]
    cc_cold_cop_6 = _print(records1)[6]
    cc_cold_cop_7 = _print(records1)[7]
    cc_cold_cop_8 = _print(records1)[8]
    cc_cold_cop_9 = _print(records1)[9]
    cc_cold_cop_10 = _print(records1)[10]
    cc_cold_cop_11 = _print(records1)[11]
    cc_cold_cop_12 = _print(records1)[12]
    cc_cold_cop_13 = _print(records1)[13]
    cc_cold_cop_14 = _print(records1)[14]
    cc_cold_cop_15 = _print(records1)[15]
    cc_cold_cop_16 = _print(records1)[16]
    cc_cold_cop_17 = _print(records1)[17]
    cc_cold_cop_18 = _print(records1)[18]
    cc_cold_cop_19 = _print(records1)[19]
    cc_cold_cop_20 = _print(records1)[20]
    cc_cold_cop_21 = _print(records1)[21]
    cc_cold_cop_22 = _print(records1)[22]
    cc_cold_cop_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['cc_cold_cop_0', 'cc_cold_cop_1', 'cc_cold_cop_2',
         'cc_cold_cop_3', 'cc_cold_cop_4', 'cc_cold_cop_5',
         'cc_cold_cop_6', 'cc_cold_cop_7', 'cc_cold_cop_8',
         'cc_cold_cop_9', 'cc_cold_cop_10', 'cc_cold_cop_11',
         'cc_cold_cop_12', 'cc_cold_cop_13', 'cc_cold_cop_14',
         'cc_cold_cop_15', 'cc_cold_cop_16', 'cc_cold_cop_17',
         'cc_cold_cop_18', 'cc_cold_cop_19', 'cc_cold_cop_20',
         'cc_cold_cop_21', 'cc_cold_cop_22', 'cc_cold_cop_23'],
        [cc_cold_cop_0, cc_cold_cop_1, cc_cold_cop_2,
         cc_cold_cop_3, cc_cold_cop_4, cc_cold_cop_5,
         cc_cold_cop_6, cc_cold_cop_7, cc_cold_cop_8,
         cc_cold_cop_9, cc_cold_cop_10, cc_cold_cop_11,
         cc_cold_cop_12, cc_cold_cop_13, cc_cold_cop_14,
         cc_cold_cop_15, cc_cold_cop_16, cc_cold_cop_17,
         cc_cold_cop_18, cc_cold_cop_19, cc_cold_cop_20,
         cc_cold_cop_21, cc_cold_cop_22, cc_cold_cop_23])


def write_to_database_chp_cold_cop_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制冷效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_cold_cop',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_cold_cop_0 = _print(records1)[0]
    chp_cold_cop_1 = _print(records1)[1]
    chp_cold_cop_2 = _print(records1)[2]
    chp_cold_cop_3 = _print(records1)[3]
    chp_cold_cop_4 = _print(records1)[4]
    chp_cold_cop_5 = _print(records1)[5]
    chp_cold_cop_6 = _print(records1)[6]
    chp_cold_cop_7 = _print(records1)[7]
    chp_cold_cop_8 = _print(records1)[8]
    chp_cold_cop_9 = _print(records1)[9]
    chp_cold_cop_10 = _print(records1)[10]
    chp_cold_cop_11 = _print(records1)[11]
    chp_cold_cop_12 = _print(records1)[12]
    chp_cold_cop_13 = _print(records1)[13]
    chp_cold_cop_14 = _print(records1)[14]
    chp_cold_cop_15 = _print(records1)[15]
    chp_cold_cop_16 = _print(records1)[16]
    chp_cold_cop_17 = _print(records1)[17]
    chp_cold_cop_18 = _print(records1)[18]
    chp_cold_cop_19 = _print(records1)[19]
    chp_cold_cop_20 = _print(records1)[20]
    chp_cold_cop_21 = _print(records1)[21]
    chp_cold_cop_22 = _print(records1)[22]
    chp_cold_cop_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_cold_cop_0', 'chp_cold_cop_1', 'chp_cold_cop_2',
         'chp_cold_cop_3', 'chp_cold_cop_4', 'chp_cold_cop_5',
         'chp_cold_cop_6', 'chp_cold_cop_7', 'chp_cold_cop_8',
         'chp_cold_cop_9', 'chp_cold_cop_10', 'chp_cold_cop_11',
         'chp_cold_cop_12', 'chp_cold_cop_13', 'chp_cold_cop_14',
         'chp_cold_cop_15', 'chp_cold_cop_16', 'chp_cold_cop_17',
         'chp_cold_cop_18', 'chp_cold_cop_19', 'chp_cold_cop_20',
         'chp_cold_cop_21', 'chp_cold_cop_22', 'chp_cold_cop_23'],
        [chp_cold_cop_0, chp_cold_cop_1, chp_cold_cop_2,
         chp_cold_cop_3, chp_cold_cop_4, chp_cold_cop_5,
         chp_cold_cop_6, chp_cold_cop_7, chp_cold_cop_8,
         chp_cold_cop_9, chp_cold_cop_10, chp_cold_cop_11,
         chp_cold_cop_12, chp_cold_cop_13, chp_cold_cop_14,
         chp_cold_cop_15, chp_cold_cop_16, chp_cold_cop_17,
         chp_cold_cop_18, chp_cold_cop_19, chp_cold_cop_20,
         chp_cold_cop_21, chp_cold_cop_22, chp_cold_cop_23])


def write_to_database_chp_heat_cop_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵制热效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('chp_heat_cop',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    chp_heat_cop_0 = _print(records1)[0]
    chp_heat_cop_1 = _print(records1)[1]
    chp_heat_cop_2 = _print(records1)[2]
    chp_heat_cop_3 = _print(records1)[3]
    chp_heat_cop_4 = _print(records1)[4]
    chp_heat_cop_5 = _print(records1)[5]
    chp_heat_cop_6 = _print(records1)[6]
    chp_heat_cop_7 = _print(records1)[7]
    chp_heat_cop_8 = _print(records1)[8]
    chp_heat_cop_9 = _print(records1)[9]
    chp_heat_cop_10 = _print(records1)[10]
    chp_heat_cop_11 = _print(records1)[11]
    chp_heat_cop_12 = _print(records1)[12]
    chp_heat_cop_13 = _print(records1)[13]
    chp_heat_cop_14 = _print(records1)[14]
    chp_heat_cop_15 = _print(records1)[15]
    chp_heat_cop_16 = _print(records1)[16]
    chp_heat_cop_17 = _print(records1)[17]
    chp_heat_cop_18 = _print(records1)[18]
    chp_heat_cop_19 = _print(records1)[19]
    chp_heat_cop_20 = _print(records1)[20]
    chp_heat_cop_21 = _print(records1)[21]
    chp_heat_cop_22 = _print(records1)[22]
    chp_heat_cop_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['chp_heat_cop_0', 'chp_heat_cop_1', 'chp_heat_cop_2',
         'chp_heat_cop_3', 'chp_heat_cop_4', 'chp_heat_cop_5',
         'chp_heat_cop_6', 'chp_heat_cop_7', 'chp_heat_cop_8',
         'chp_heat_cop_9', 'chp_heat_cop_10', 'chp_heat_cop_11',
         'chp_heat_cop_12', 'chp_heat_cop_13', 'chp_heat_cop_14',
         'chp_heat_cop_15', 'chp_heat_cop_16', 'chp_heat_cop_17',
         'chp_heat_cop_18', 'chp_heat_cop_19', 'chp_heat_cop_20',
         'chp_heat_cop_21', 'chp_heat_cop_22', 'chp_heat_cop_23'],
        [chp_heat_cop_0, chp_heat_cop_1, chp_heat_cop_2,
         chp_heat_cop_3, chp_heat_cop_4, chp_heat_cop_5,
         chp_heat_cop_6, chp_heat_cop_7, chp_heat_cop_8,
         chp_heat_cop_9, chp_heat_cop_10, chp_heat_cop_11,
         chp_heat_cop_12, chp_heat_cop_13, chp_heat_cop_14,
         chp_heat_cop_15, chp_heat_cop_16, chp_heat_cop_17,
         chp_heat_cop_18, chp_heat_cop_19, chp_heat_cop_20,
         chp_heat_cop_21, chp_heat_cop_22, chp_heat_cop_23])


def write_to_database_ashp_cold_cop_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制冷效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_cold_cop',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_cold_cop_0 = _print(records1)[0]
    ashp_cold_cop_1 = _print(records1)[1]
    ashp_cold_cop_2 = _print(records1)[2]
    ashp_cold_cop_3 = _print(records1)[3]
    ashp_cold_cop_4 = _print(records1)[4]
    ashp_cold_cop_5 = _print(records1)[5]
    ashp_cold_cop_6 = _print(records1)[6]
    ashp_cold_cop_7 = _print(records1)[7]
    ashp_cold_cop_8 = _print(records1)[8]
    ashp_cold_cop_9 = _print(records1)[9]
    ashp_cold_cop_10 = _print(records1)[10]
    ashp_cold_cop_11 = _print(records1)[11]
    ashp_cold_cop_12 = _print(records1)[12]
    ashp_cold_cop_13 = _print(records1)[13]
    ashp_cold_cop_14 = _print(records1)[14]
    ashp_cold_cop_15 = _print(records1)[15]
    ashp_cold_cop_16 = _print(records1)[16]
    ashp_cold_cop_17 = _print(records1)[17]
    ashp_cold_cop_18 = _print(records1)[18]
    ashp_cold_cop_19 = _print(records1)[19]
    ashp_cold_cop_20 = _print(records1)[20]
    ashp_cold_cop_21 = _print(records1)[21]
    ashp_cold_cop_22 = _print(records1)[22]
    ashp_cold_cop_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_cold_cop_0', 'ashp_cold_cop_1', 'ashp_cold_cop_2',
         'ashp_cold_cop_3', 'ashp_cold_cop_4', 'ashp_cold_cop_5',
         'ashp_cold_cop_6', 'ashp_cold_cop_7', 'ashp_cold_cop_8',
         'ashp_cold_cop_9', 'ashp_cold_cop_10', 'ashp_cold_cop_11',
         'ashp_cold_cop_12', 'ashp_cold_cop_13', 'ashp_cold_cop_14',
         'ashp_cold_cop_15', 'ashp_cold_cop_16', 'ashp_cold_cop_17',
         'ashp_cold_cop_18', 'ashp_cold_cop_19', 'ashp_cold_cop_20',
         'ashp_cold_cop_21', 'ashp_cold_cop_22', 'ashp_cold_cop_23'],
        [ashp_cold_cop_0, ashp_cold_cop_1, ashp_cold_cop_2,
         ashp_cold_cop_3, ashp_cold_cop_4, ashp_cold_cop_5,
         ashp_cold_cop_6, ashp_cold_cop_7, ashp_cold_cop_8,
         ashp_cold_cop_9, ashp_cold_cop_10, ashp_cold_cop_11,
         ashp_cold_cop_12, ashp_cold_cop_13, ashp_cold_cop_14,
         ashp_cold_cop_15, ashp_cold_cop_16, ashp_cold_cop_17,
         ashp_cold_cop_18, ashp_cold_cop_19, ashp_cold_cop_20,
         ashp_cold_cop_21, ashp_cold_cop_22, ashp_cold_cop_23])


def write_to_database_ashp_heat_cop_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵制热效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ashp_heat_cop',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ashp_heat_cop_0 = _print(records1)[0]
    ashp_heat_cop_1 = _print(records1)[1]
    ashp_heat_cop_2 = _print(records1)[2]
    ashp_heat_cop_3 = _print(records1)[3]
    ashp_heat_cop_4 = _print(records1)[4]
    ashp_heat_cop_5 = _print(records1)[5]
    ashp_heat_cop_6 = _print(records1)[6]
    ashp_heat_cop_7 = _print(records1)[7]
    ashp_heat_cop_8 = _print(records1)[8]
    ashp_heat_cop_9 = _print(records1)[9]
    ashp_heat_cop_10 = _print(records1)[10]
    ashp_heat_cop_11 = _print(records1)[11]
    ashp_heat_cop_12 = _print(records1)[12]
    ashp_heat_cop_13 = _print(records1)[13]
    ashp_heat_cop_14 = _print(records1)[14]
    ashp_heat_cop_15 = _print(records1)[15]
    ashp_heat_cop_16 = _print(records1)[16]
    ashp_heat_cop_17 = _print(records1)[17]
    ashp_heat_cop_18 = _print(records1)[18]
    ashp_heat_cop_19 = _print(records1)[19]
    ashp_heat_cop_20 = _print(records1)[20]
    ashp_heat_cop_21 = _print(records1)[21]
    ashp_heat_cop_22 = _print(records1)[22]
    ashp_heat_cop_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ashp_heat_cop_0', 'ashp_heat_cop_1', 'ashp_heat_cop_2',
         'ashp_heat_cop_3', 'ashp_heat_cop_4', 'ashp_heat_cop_5',
         'ashp_heat_cop_6', 'ashp_heat_cop_7', 'ashp_heat_cop_8',
         'ashp_heat_cop_9', 'ashp_heat_cop_10', 'ashp_heat_cop_11',
         'ashp_heat_cop_12', 'ashp_heat_cop_13', 'ashp_heat_cop_14',
         'ashp_heat_cop_15', 'ashp_heat_cop_16', 'ashp_heat_cop_17',
         'ashp_heat_cop_18', 'ashp_heat_cop_19', 'ashp_heat_cop_20',
         'ashp_heat_cop_21', 'ashp_heat_cop_22', 'ashp_heat_cop_23'],
        [ashp_heat_cop_0, ashp_heat_cop_1, ashp_heat_cop_2,
         ashp_heat_cop_3, ashp_heat_cop_4, ashp_heat_cop_5,
         ashp_heat_cop_6, ashp_heat_cop_7, ashp_heat_cop_8,
         ashp_heat_cop_9, ashp_heat_cop_10, ashp_heat_cop_11,
         ashp_heat_cop_12, ashp_heat_cop_13, ashp_heat_cop_14,
         ashp_heat_cop_15, ashp_heat_cop_16, ashp_heat_cop_17,
         ashp_heat_cop_18, ashp_heat_cop_19, ashp_heat_cop_20,
         ashp_heat_cop_21, ashp_heat_cop_22, ashp_heat_cop_23])


def write_to_database_ngb_hot_water_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入天然气锅炉生活热水效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('ngb_hot_water_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    ngb_hot_water_efficiency_0 = _print(records1)[0]
    ngb_hot_water_efficiency_1 = _print(records1)[1]
    ngb_hot_water_efficiency_2 = _print(records1)[2]
    ngb_hot_water_efficiency_3 = _print(records1)[3]
    ngb_hot_water_efficiency_4 = _print(records1)[4]
    ngb_hot_water_efficiency_5 = _print(records1)[5]
    ngb_hot_water_efficiency_6 = _print(records1)[6]
    ngb_hot_water_efficiency_7 = _print(records1)[7]
    ngb_hot_water_efficiency_8 = _print(records1)[8]
    ngb_hot_water_efficiency_9 = _print(records1)[9]
    ngb_hot_water_efficiency_10 = _print(records1)[10]
    ngb_hot_water_efficiency_11 = _print(records1)[11]
    ngb_hot_water_efficiency_12 = _print(records1)[12]
    ngb_hot_water_efficiency_13 = _print(records1)[13]
    ngb_hot_water_efficiency_14 = _print(records1)[14]
    ngb_hot_water_efficiency_15 = _print(records1)[15]
    ngb_hot_water_efficiency_16 = _print(records1)[16]
    ngb_hot_water_efficiency_17 = _print(records1)[17]
    ngb_hot_water_efficiency_18 = _print(records1)[18]
    ngb_hot_water_efficiency_19 = _print(records1)[19]
    ngb_hot_water_efficiency_20 = _print(records1)[20]
    ngb_hot_water_efficiency_21 = _print(records1)[21]
    ngb_hot_water_efficiency_22 = _print(records1)[22]
    ngb_hot_water_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['ngb_hot_water_efficiency_0', 'ngb_hot_water_efficiency_1', 'ngb_hot_water_efficiency_2',
         'ngb_hot_water_efficiency_3', 'ngb_hot_water_efficiency_4', 'ngb_hot_water_efficiency_5',
         'ngb_hot_water_efficiency_6', 'ngb_hot_water_efficiency_7', 'ngb_hot_water_efficiency_8',
         'ngb_hot_water_efficiency_9', 'ngb_hot_water_efficiency_10', 'ngb_hot_water_efficiency_11',
         'ngb_hot_water_efficiency_12', 'ngb_hot_water_efficiency_13', 'ngb_hot_water_efficiency_14',
         'ngb_hot_water_efficiency_15', 'ngb_hot_water_efficiency_16', 'ngb_hot_water_efficiency_17',
         'ngb_hot_water_efficiency_18', 'ngb_hot_water_efficiency_19', 'ngb_hot_water_efficiency_20',
         'ngb_hot_water_efficiency_21', 'ngb_hot_water_efficiency_22', 'ngb_hot_water_efficiency_23'],
        [ngb_hot_water_efficiency_0, ngb_hot_water_efficiency_1, ngb_hot_water_efficiency_2,
         ngb_hot_water_efficiency_3, ngb_hot_water_efficiency_4, ngb_hot_water_efficiency_5,
         ngb_hot_water_efficiency_6, ngb_hot_water_efficiency_7, ngb_hot_water_efficiency_8,
         ngb_hot_water_efficiency_9, ngb_hot_water_efficiency_10, ngb_hot_water_efficiency_11,
         ngb_hot_water_efficiency_12, ngb_hot_water_efficiency_13, ngb_hot_water_efficiency_14,
         ngb_hot_water_efficiency_15, ngb_hot_water_efficiency_16, ngb_hot_water_efficiency_17,
         ngb_hot_water_efficiency_18, ngb_hot_water_efficiency_19, ngb_hot_water_efficiency_20,
         ngb_hot_water_efficiency_21, ngb_hot_water_efficiency_22, ngb_hot_water_efficiency_23])


def write_to_database_photovoltaic_electrical_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入光伏发电效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('photovoltaic_electrical_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    photovoltaic_electrical_efficiency_0 = _print(records1)[0]
    photovoltaic_electrical_efficiency_1 = _print(records1)[1]
    photovoltaic_electrical_efficiency_2 = _print(records1)[2]
    photovoltaic_electrical_efficiency_3 = _print(records1)[3]
    photovoltaic_electrical_efficiency_4 = _print(records1)[4]
    photovoltaic_electrical_efficiency_5 = _print(records1)[5]
    photovoltaic_electrical_efficiency_6 = _print(records1)[6]
    photovoltaic_electrical_efficiency_7 = _print(records1)[7]
    photovoltaic_electrical_efficiency_8 = _print(records1)[8]
    photovoltaic_electrical_efficiency_9 = _print(records1)[9]
    photovoltaic_electrical_efficiency_10 = _print(records1)[10]
    photovoltaic_electrical_efficiency_11 = _print(records1)[11]
    photovoltaic_electrical_efficiency_12 = _print(records1)[12]
    photovoltaic_electrical_efficiency_13 = _print(records1)[13]
    photovoltaic_electrical_efficiency_14 = _print(records1)[14]
    photovoltaic_electrical_efficiency_15 = _print(records1)[15]
    photovoltaic_electrical_efficiency_16 = _print(records1)[16]
    photovoltaic_electrical_efficiency_17 = _print(records1)[17]
    photovoltaic_electrical_efficiency_18 = _print(records1)[18]
    photovoltaic_electrical_efficiency_19 = _print(records1)[19]
    photovoltaic_electrical_efficiency_20 = _print(records1)[20]
    photovoltaic_electrical_efficiency_21 = _print(records1)[21]
    photovoltaic_electrical_efficiency_22 = _print(records1)[22]
    photovoltaic_electrical_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['photovoltaic_electrical_efficiency_0', 'photovoltaic_electrical_efficiency_1', 'photovoltaic_electrical_efficiency_2',
         'photovoltaic_electrical_efficiency_3', 'photovoltaic_electrical_efficiency_4', 'photovoltaic_electrical_efficiency_5',
         'photovoltaic_electrical_efficiency_6', 'photovoltaic_electrical_efficiency_7', 'photovoltaic_electrical_efficiency_8',
         'photovoltaic_electrical_efficiency_9', 'photovoltaic_electrical_efficiency_10', 'photovoltaic_electrical_efficiency_11',
         'photovoltaic_electrical_efficiency_12', 'photovoltaic_electrical_efficiency_13', 'photovoltaic_electrical_efficiency_14',
         'photovoltaic_electrical_efficiency_15', 'photovoltaic_electrical_efficiency_16', 'photovoltaic_electrical_efficiency_17',
         'photovoltaic_electrical_efficiency_18', 'photovoltaic_electrical_efficiency_19', 'photovoltaic_electrical_efficiency_20',
         'photovoltaic_electrical_efficiency_21', 'photovoltaic_electrical_efficiency_22', 'photovoltaic_electrical_efficiency_23'],
        [photovoltaic_electrical_efficiency_0, photovoltaic_electrical_efficiency_1, photovoltaic_electrical_efficiency_2,
         photovoltaic_electrical_efficiency_3, photovoltaic_electrical_efficiency_4, photovoltaic_electrical_efficiency_5,
         photovoltaic_electrical_efficiency_6, photovoltaic_electrical_efficiency_7, photovoltaic_electrical_efficiency_8,
         photovoltaic_electrical_efficiency_9, photovoltaic_electrical_efficiency_10, photovoltaic_electrical_efficiency_11,
         photovoltaic_electrical_efficiency_12, photovoltaic_electrical_efficiency_13, photovoltaic_electrical_efficiency_14,
         photovoltaic_electrical_efficiency_15, photovoltaic_electrical_efficiency_16, photovoltaic_electrical_efficiency_17,
         photovoltaic_electrical_efficiency_18, photovoltaic_electrical_efficiency_19, photovoltaic_electrical_efficiency_20,
         photovoltaic_electrical_efficiency_21, photovoltaic_electrical_efficiency_22, photovoltaic_electrical_efficiency_23])


def write_to_database_wind_electrical_efficiency_24(syncbase, now, period):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入风力发电效率24小时的值
    # 获取当前的时间
    now_year = now.year  # 当前的年
    now_month = now.month  # 当前的月
    now_day = now.day  # 当前的日
    now_hour = now.hour  # 当前的小时
    now_minute = now.minute  # 当前的分钟
    now_second = now.second  # 当前的秒

    # 从数据库读取历史数据
    state1, records1 = syncbase.get_history_data_by_name('wind_electrical_efficiency',
                                                         dt(now_year, now_month, now_day, 0, 0, 0),
                                                         dt(now_year, now_month, now_day, now_hour, now_minute, now_second),
                                                         period)

    wind_electrical_efficiency_0 = _print(records1)[0]
    wind_electrical_efficiency_1 = _print(records1)[1]
    wind_electrical_efficiency_2 = _print(records1)[2]
    wind_electrical_efficiency_3 = _print(records1)[3]
    wind_electrical_efficiency_4 = _print(records1)[4]
    wind_electrical_efficiency_5 = _print(records1)[5]
    wind_electrical_efficiency_6 = _print(records1)[6]
    wind_electrical_efficiency_7 = _print(records1)[7]
    wind_electrical_efficiency_8 = _print(records1)[8]
    wind_electrical_efficiency_9 = _print(records1)[9]
    wind_electrical_efficiency_10 = _print(records1)[10]
    wind_electrical_efficiency_11 = _print(records1)[11]
    wind_electrical_efficiency_12 = _print(records1)[12]
    wind_electrical_efficiency_13 = _print(records1)[13]
    wind_electrical_efficiency_14 = _print(records1)[14]
    wind_electrical_efficiency_15 = _print(records1)[15]
    wind_electrical_efficiency_16 = _print(records1)[16]
    wind_electrical_efficiency_17 = _print(records1)[17]
    wind_electrical_efficiency_18 = _print(records1)[18]
    wind_electrical_efficiency_19 = _print(records1)[19]
    wind_electrical_efficiency_20 = _print(records1)[20]
    wind_electrical_efficiency_21 = _print(records1)[21]
    wind_electrical_efficiency_22 = _print(records1)[22]
    wind_electrical_efficiency_23 = _print(records1)[23]

    # 向数据库写入批量数据
    state2 = syncbase.write_batch_realtime_data_by_name(
        ['wind_electrical_efficiency_0', 'wind_electrical_efficiency_1', 'wind_electrical_efficiency_2',
         'wind_electrical_efficiency_3', 'wind_electrical_efficiency_4', 'wind_electrical_efficiency_5',
         'wind_electrical_efficiency_6', 'wind_electrical_efficiency_7', 'wind_electrical_efficiency_8',
         'wind_electrical_efficiency_9', 'wind_electrical_efficiency_10', 'wind_electrical_efficiency_11',
         'wind_electrical_efficiency_12', 'wind_electrical_efficiency_13', 'wind_electrical_efficiency_14',
         'wind_electrical_efficiency_15', 'wind_electrical_efficiency_16', 'wind_electrical_efficiency_17',
         'wind_electrical_efficiency_18', 'wind_electrical_efficiency_19', 'wind_electrical_efficiency_20',
         'wind_electrical_efficiency_21', 'wind_electrical_efficiency_22', 'wind_electrical_efficiency_23'],
        [wind_electrical_efficiency_0, wind_electrical_efficiency_1, wind_electrical_efficiency_2,
         wind_electrical_efficiency_3, wind_electrical_efficiency_4, wind_electrical_efficiency_5,
         wind_electrical_efficiency_6, wind_electrical_efficiency_7, wind_electrical_efficiency_8,
         wind_electrical_efficiency_9, wind_electrical_efficiency_10, wind_electrical_efficiency_11,
         wind_electrical_efficiency_12, wind_electrical_efficiency_13, wind_electrical_efficiency_14,
         wind_electrical_efficiency_15, wind_electrical_efficiency_16, wind_electrical_efficiency_17,
         wind_electrical_efficiency_18, wind_electrical_efficiency_19, wind_electrical_efficiency_20,
         wind_electrical_efficiency_21, wind_electrical_efficiency_22, wind_electrical_efficiency_23])