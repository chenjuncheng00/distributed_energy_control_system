
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
        [ice1_electrical_efficiency, ice1_residual_heat_efficiency, ice1_electrical_power, ice1_residual_heat_power,
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
        [ice2_electrical_efficiency, ice2_residual_heat_efficiency, ice2_electrical_power, ice2_residual_heat_power,
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
        [ese_cold_heat_out, ese_residual_storage_energy, ese_cost, ese_proportion_in, ese_proportion_out])

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
         ngb1_efficiency, ngb1_income, ngb1_cost, ngb1_natural_gas_consumption])

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
         ngb2_efficiency, ngb2_income, ngb2_cost, ngb2_natural_gas_consumption])

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
         ngb3_efficiency, ngb3_income, ngb3_cost, ngb3_natural_gas_consumption])

    # 报错
    if (state1 == False or state3 == False):
        print("天然气热水锅炉3写入数据库出错！")


def write_to_database_prediction(syncbase, cold_heat_prediction, hot_water_prediction, electricity_prediction):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入负荷预测数据结果

    # 冷热负荷预测值
    # 热水负荷预测值
    # 电负荷预测值
    state1 = syncbase.write_batch_realtime_data_by_name(['cold_heat_prediction', 'hot_water_prediction', 'electricity_prediction'],
                                                        [cold_heat_prediction, hot_water_prediction, electricity_prediction])
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
         comprehensive_energy_utilization, proportion_of_renewable_energy_power, cop_real_time, reduction_in_carbon_emissions, reduction_in_sulfide_emissions,
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
            [ice_electrical_efficiency, lb_cold_efficiency, lb_heat_efficiency, lb_hot_water_efficiency, cc_cold_cop,
             chp_cold_cop, chp_heat_cop, ashp_cold_cop, ashp_heat_cop, ngb_hot_water_efficiency,
             photovoltaic_electrical_efficiency, wind_electrical_efficiency])

    # 报错
    if state1 == False:
        print("设备效率数据写入数据库错误！")
