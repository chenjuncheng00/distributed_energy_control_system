from syncbase import SyncBase

def write_to_database_ice1(ice1_remote_start, ice1_remote_stop, ice1_black_start, ice1_active_power_set, ice1_reactive_power_set, ice1_power_factor_set):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#燃气内燃发电机组远程启机指令
    # 1#燃气内燃发电机组远程停机指令
    # 1#燃气内燃发电机组黑启动指令
    # 1#燃气内燃发电机有功功率给定
    # 1#燃气内燃发电机无功功率给定
    # 1#燃气内燃发电机功率因数给定
    state = syncbase.write_batch_realtime_data_by_name(
        ['ice1_remote_start', 'ice1_remote_stop', 'ice1_black_start', 'ice1_active_power_set',
         'ice1_reactive_power_set', 'ice1_power_factor_set'],
        [ice1_remote_start, ice1_remote_stop, ice1_black_start, ice1_active_power_set, ice1_reactive_power_set,
         ice1_power_factor_set])

    # 显示写入结果
    if state:
        print("批量写入内燃机1数据成功！")
    else:
        print("批量写入内燃机1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ice2(ice2_remote_start, ice2_remote_stop, ice2_black_start, ice2_active_power_set, ice2_reactive_power_set, ice2_power_factor_set):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#燃气内燃发电机组远程启机指令
    # 2#燃气内燃发电机组远程停机指令
    # 2#燃气内燃发电机组黑启动指令
    # 2#燃气内燃发电机有功功率给定
    # 2#燃气内燃发电机无功功率给定
    # 2#燃气内燃发电机功率因数给定
    state = syncbase.write_batch_realtime_data_by_name(
            ['ice2_remote_start', 'ice2_remote_stop',
             'ice2_black_start', 'ice2_active_power_set', 'ice2_reactive_power_set', 'ice2_power_factor_set'],
            [ice2_remote_start, ice2_remote_stop, ice2_black_start, ice2_active_power_set,
             ice2_reactive_power_set, ice2_power_factor_set])

    # 显示写入结果
    if state:
        print("批量写入内燃机2数据成功！")
    else:
        print("批量写入内燃机2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_lb1(lb1_remote_start, lb1_remote_stop, lb1_wp_heat_chilled_water_frequency, lb1_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#溴化锂机组机组远程开机
    # 1#溴化锂机组机组远程关机
    # 1#溴化锂机组机组冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#溴化锂机组机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['lb1_remote_start', 'lb1_remote_stop', 'lb1_wp_heat_chilled_water_frequency', 'lb1_wp_cooling_water_frequency'],
        [lb1_remote_start, lb1_remote_stop, lb1_wp_heat_chilled_water_frequency, lb1_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入溴化锂1数据成功！")
    else:
        print("批量写入溴化锂1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_lb2(lb2_remote_start, lb2_remote_stop, lb2_wp_heat_chilled_water_frequency, lb2_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#溴化锂机组机组远程开机
    # 2#溴化锂机组机组远程关机
    # 2#溴化锂机组机组冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 2#溴化锂机组机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['lb2_remote_start', 'lb2_remote_stop', 'lb2_wp_heat_chilled_water_frequency',
         'lb2_wp_cooling_water_frequency'],
        [lb2_remote_start, lb2_remote_stop, lb2_wp_heat_chilled_water_frequency, lb2_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入溴化锂2数据成功！")
    else:
        print("批量写入溴化锂2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc1(cc1_interlock_stop, cc1_remote_stop, cc1_remote_start, cc1_wp_chilled_water_frequency, cc1_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#离心式冷水机组联锁停机指令
    # 1#离心式冷水机组远方停机指令
    # 1#离心式冷水机组远方开机指令
    # 1#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc1_interlock_stop', 'cc1_remote_stop', 'cc1_remote_start', 'cc1_wp_chilled_water_frequency', 'cc1_wp_cooling_water_frequency'],
        [cc1_interlock_stop, cc1_remote_stop, cc1_remote_start, cc1_wp_chilled_water_frequency, cc1_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机1数据成功！")
    else:
        print("批量写入离心式冷水机1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc2(cc2_interlock_stop, cc2_remote_stop, cc2_remote_start, cc2_wp_chilled_water_frequency, cc2_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#离心式冷水机组联锁停机指令
    # 2#离心式冷水机组远方停机指令
    # 2#离心式冷水机组远方开机指令
    # 2#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 2#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
            ['cc2_interlock_stop', 'cc2_remote_stop', 'cc2_remote_start', 'cc2_wp_chilled_water_frequency', 'cc2_wp_cooling_water_frequency'],
            [cc2_interlock_stop, cc2_remote_stop, cc2_remote_start, cc2_wp_chilled_water_frequency, cc2_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机2数据成功！")
    else:
        print("批量写入离心式冷水机2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc3(cc3_interlock_stop, cc3_remote_stop, cc3_remote_start, cc3_wp_chilled_water_frequency, cc3_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3#离心式冷水机组联锁停机指令
    # 3#离心式冷水机组远方停机指令
    # 3#离心式冷水机组远方开机指令
    # 3#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 3#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc3_interlock_stop', 'cc3_remote_stop', 'cc3_remote_start', 'cc3_wp_chilled_water_frequency', 'cc3_wp_cooling_water_frequency'],
        [cc3_interlock_stop, cc3_remote_stop, cc3_remote_start, cc3_wp_chilled_water_frequency, cc3_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机3数据成功！")
    else:
        print("批量写入离心式冷水机3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc4(cc4_interlock_stop, cc4_remote_stop, cc4_remote_start, cc4_wp_chilled_water_frequency, cc4_wp_cooling_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 4#离心式冷水机组联锁停机指令
    # 4#离心式冷水机组远方停机指令
    # 4#离心式冷水机组远方开机指令
    # 4#离心式冷水机组冷冻水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 4#离心式冷水机组冷却水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc4_interlock_stop', 'cc4_remote_stop', 'cc4_remote_start', 'cc4_wp_chilled_water_frequency', 'cc4_wp_cooling_water_frequency'],
        [cc4_interlock_stop, cc4_remote_stop, cc4_remote_start, cc4_wp_chilled_water_frequency, cc4_wp_cooling_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机4数据成功！")
    else:
        print("批量写入离心式冷水机4数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb1(ngb1_remote_start, ngb1_remote_stop, ngb1_wp_heat_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#燃气真空热水炉远程启动指令
    # 1#燃气真空热水炉远程停止指令
    # 1#燃气真空热水炉采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb1_remote_start', 'ngb1_remote_stop', 'ngb1_wp_heat_water_frequency'],
        [ngb1_remote_start, ngb1_remote_stop, ngb1_wp_heat_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉1数据成功！")
    else:
        print("批量写入燃气真空热水炉1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb2(ngb2_remote_start, ngb2_remote_stop, ngb2_wp_heat_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#燃气真空热水炉远程启动指令
    # 2#燃气真空热水炉远程停止指令
    # 2#燃气真空热水炉采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb2_remote_start', 'ngb2_remote_stop', 'ngb2_wp_heat_water_frequency'],
        [ngb2_remote_start, ngb2_remote_stop, ngb2_wp_heat_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉2数据成功！")
    else:
        print("批量写入燃气真空热水炉2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb3(ngb3_remote_start, ngb3_remote_stop, ngb3_wp_hot_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3#燃气真空热水炉远程启动指令
    # 3#燃气真空热水炉远程停止指令
    # 3#燃气真空热水炉生活热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb3_remote_start', 'ngb3_remote_stop', 'ngb3_wp_hot_water_frequency'],
        [ngb3_remote_start, ngb3_remote_stop, ngb3_wp_hot_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉3数据成功！")
    else:
        print("批量写入燃气真空热水炉3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_chp1(chp1_interlock_stop, chp1_remote_stop, chp1_remote_start, chp1_wp_heat_water_frequency, chp1_wp_source_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#离心式热泵联锁停机指令
    # 1#离心式热泵远方停机指令
    # 1#离心式热泵远方开机指令
    # 1#离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 1#离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['chp1_interlock_stop', 'chp1_remote_stop', 'chp1_remote_start', 'chp1_wp_heat_water_frequency', 'chp1_wp_source_water_frequency'],
        [chp1_interlock_stop, chp1_remote_stop, chp1_remote_start, chp1_wp_heat_water_frequency, chp1_wp_source_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式热泵1数据成功！")
    else:
        print("批量写入离心式热泵1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_chp2(chp2_interlock_stop, chp2_remote_stop, chp2_remote_start, chp2_wp_heat_water_frequency, chp2_wp_source_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#离心式热泵联锁停机指令
    # 2#离心式热泵远方停机指令
    # 2#离心式热泵远方开机指令
    # 2#离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 2#离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['chp2_interlock_stop', 'chp2_remote_stop', 'chp2_remote_start', 'chp2_wp_heat_water_frequency', 'chp2_wp_source_water_frequency'],
        [chp2_interlock_stop, chp2_remote_stop, chp2_remote_start, chp2_wp_heat_water_frequency, chp2_wp_source_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式热泵2数据成功！")
    else:
        print("批量写入离心式热泵2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_chp3(chp3_interlock_stop, chp3_remote_stop, chp3_remote_start, chp3_wp_heat_water_frequency, chp3_wp_source_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3#离心式热泵联锁停机指令
    # 3#离心式热泵远方停机指令
    # 3#离心式热泵远方开机指令
    # 3#离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 3#离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['chp3_interlock_stop', 'chp3_remote_stop', 'chp3_remote_start', 'chp3_wp_heat_water_frequency', 'chp3_wp_source_water_frequency'],
        [chp3_interlock_stop, chp3_remote_stop, chp3_remote_start, chp3_wp_heat_water_frequency, chp3_wp_source_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式热泵3数据成功！")
    else:
        print("批量写入离心式热泵3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_chp4(chp4_interlock_stop, chp4_remote_stop, chp4_remote_start, chp4_wp_heat_water_frequency, chp4_wp_source_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式热泵4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 4#离心式热泵联锁停机指令
    # 4#离心式热泵远方停机指令
    # 4#离心式热泵远方开机指令
    # 4#离心式热泵采暖水泵频率（变频水泵，在DCS中转为4~20mA信号）
    # 4#离心式热泵热源水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['chp4_interlock_stop', 'chp4_remote_stop', 'chp4_remote_start', 'chp4_wp_heat_water_frequency', 'chp4_wp_source_water_frequency'],
        [chp4_interlock_stop, chp4_remote_stop, chp4_remote_start, chp4_wp_heat_water_frequency, chp4_wp_source_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入离心式热泵4数据成功！")
    else:
        print("批量写入离心式热泵4数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase

def write_to_database_ashp1(ashp1_interlock_stop, ashp1_remote_stop, ashp1_remote_start, ashp1_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#空气源热泵联锁停机指令
    # 1#空气源热泵远方停机指令
    # 1#空气源热泵远方开机指令
    # 1#空气源热泵冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ashp1_interlock_stop', 'ashp1_remote_stop', 'ashp1_remote_start', 'ashp1_wp_water_frequency'],
        [ashp1_interlock_stop, ashp1_remote_stop, ashp1_remote_start, ashp1_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入空气源热泵1数据成功！")
    else:
        print("批量写入空气源热泵1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ashp2(ashp2_interlock_stop, ashp2_remote_stop, ashp2_remote_start, ashp2_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#空气源热泵联锁停机指令
    # 2#空气源热泵远方停机指令
    # 2#空气源热泵远方开机指令
    # 2#空气源热泵冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ashp2_interlock_stop', 'ashp2_remote_stop', 'ashp2_remote_start', 'ashp2_wp_water_frequency'],
        [ashp2_interlock_stop, ashp2_remote_stop, ashp2_remote_start, ashp2_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入空气源热泵2数据成功！")
    else:
        print("批量写入空气源热泵2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ashp3(ashp3_interlock_stop, ashp3_remote_stop, ashp3_remote_start, ashp3_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3#空气源热泵联锁停机指令
    # 3#空气源热泵远方停机指令
    # 3#空气源热泵远方开机指令
    # 3#空气源热泵冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ashp3_interlock_stop', 'ashp3_remote_stop', 'ashp3_remote_start', 'ashp3_wp_water_frequency'],
        [ashp3_interlock_stop, ashp3_remote_stop, ashp3_remote_start, ashp3_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入空气源热泵3数据成功！")
    else:
        print("批量写入空气源热泵3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ashp4(ashp4_interlock_stop, ashp4_remote_stop, ashp4_remote_start, ashp4_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入空气源热泵4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 4#空气源热泵联锁停机指令
    # 4#空气源热泵远方停机指令
    # 4#空气源热泵远方开机指令
    # 4#空气源热泵冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ashp4_interlock_stop', 'ashp4_remote_stop', 'ashp4_remote_start', 'ashp4_wp_water_frequency'],
        [ashp4_interlock_stop, ashp4_remote_stop, ashp4_remote_start, ashp4_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入空气源热泵4数据成功！")
    else:
        print("批量写入空气源热泵4数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ese1(ese1_interlock_stop, ese1_remote_stop, ese1_remote_start, ese1_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1#蓄冷蓄热装置联锁停机指令
    # 1#蓄冷蓄热装置远方停机指令
    # 1#蓄冷蓄热装置远方开机指令
    # 1#蓄冷蓄热装置冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ese1_interlock_stop', 'ese1_remote_stop', 'ese1_remote_start', 'ese1_wp_water_frequency'],
        [ese1_interlock_stop, ese1_remote_stop, ese1_remote_start, ese1_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入蓄冷蓄热装置1数据成功！")
    else:
        print("批量写入蓄冷蓄热装置1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ese2(ese2_interlock_stop, ese2_remote_stop, ese2_remote_start, ese2_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2#蓄冷蓄热装置联锁停机指令
    # 2#蓄冷蓄热装置远方停机指令
    # 2#蓄冷蓄热装置远方开机指令
    # 2#蓄冷蓄热装置冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ese2_interlock_stop', 'ese2_remote_stop', 'ese2_remote_start', 'ese2_wp_water_frequency'],
        [ese2_interlock_stop, ese2_remote_stop, ese2_remote_start, ese2_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入蓄冷蓄热装置2数据成功！")
    else:
        print("批量写入蓄冷蓄热装置2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ese3(ese3_interlock_stop, ese3_remote_stop, ese3_remote_start, ese3_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3#蓄冷蓄热装置联锁停机指令
    # 3#蓄冷蓄热装置远方停机指令
    # 3#蓄冷蓄热装置远方开机指令
    # 3#蓄冷蓄热装置冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ese3_interlock_stop', 'ese3_remote_stop', 'ese3_remote_start', 'ese3_wp_water_frequency'],
        [ese3_interlock_stop, ese3_remote_stop, ese3_remote_start, ese3_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入蓄冷蓄热装置3数据成功！")
    else:
        print("批量写入蓄冷蓄热装置3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ese4(ese4_interlock_stop, ese4_remote_stop, ese4_remote_start, ese4_wp_water_frequency):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入蓄冷蓄热装置4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 4#蓄冷蓄热装置联锁停机指令
    # 4#蓄冷蓄热装置远方停机指令
    # 4#蓄冷蓄热装置远方开机指令
    # 4#蓄冷蓄热装置冷热水泵频率（变频水泵，在DCS中转为4~20mA信号）
    state = syncbase.write_batch_realtime_data_by_name(
        ['ese4_interlock_stop', 'ese4_remote_stop', 'ese4_remote_start', 'ese4_wp_water_frequency'],
        [ese4_interlock_stop, ese4_remote_stop, ese4_remote_start, ese4_wp_water_frequency])

    # 显示写入结果
    if state:
        print("批量写入蓄冷蓄热装置4数据成功！")
    else:
        print("批量写入蓄冷蓄热装置4数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase