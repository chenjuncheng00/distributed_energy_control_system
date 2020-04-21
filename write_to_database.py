from syncbase import SyncBase

def write_to_database_ice1(ice1_remote_start, ice1_remote_stop, ice1_black_start, ice1_active_power_set, ice1_reactive_power_set, ice1_power_factor_set):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入内燃机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1燃气内燃发电机组远程启机指令
    # 1燃气内燃发电机组远程停机指令
    # 1燃气内燃发电机组黑启动指令
    # 1燃气内燃发电机有功功率给定
    # 1燃气内燃发电机无功功率给定
    # 1燃气内燃发电机功率因数给定
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
    # 2燃气内燃发电机组远程启机指令
    # 2燃气内燃发电机组远程停机指令
    # 2燃气内燃发电机组黑启动指令
    # 2燃气内燃发电机有功功率给定
    # 2燃气内燃发电机无功功率给定
    # 2燃气内燃发电机功率因数给定
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


def write_to_database_lb1(lb1_remote_start, lb1_remote_stop):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1溴化锂机组机组远程开机
    # 1溴化锂机组机组远程关机
    state = syncbase.write_batch_realtime_data_by_name(
        ['lb1_remote_start', 'lb1_remote_stop'],
        [lb1_remote_start, lb1_remote_stop])

    # 显示写入结果
    if state:
        print("批量写入溴化锂1数据成功！")
    else:
        print("批量写入溴化锂1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_lb2(lb2_remote_start, lb2_remote_stop):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入溴化锂2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2溴化锂机组机组远程开机
    # 2溴化锂机组机组远程关机
    state = syncbase.write_batch_realtime_data_by_name(
        ['lb2_remote_start', 'lb2_remote_stop'],
        [lb2_remote_start, lb2_remote_stop])

    # 显示写入结果
    if state:
        print("批量写入溴化锂2数据成功！")
    else:
        print("批量写入溴化锂2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc1(cc1_interlock_stop, cc1_remote_stop, cc1_remote_start):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1离心式冷水机组联锁停机指令
    # 1离心式冷水机组远方停机指令
    # 1离心式冷水机组远方开机指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc1_interlock_stop', 'cc1_remote_stop', 'cc1_remote_start'],
        [cc1_interlock_stop, cc1_remote_stop, cc1_remote_start])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机1数据成功！")
    else:
        print("批量写入离心式冷水机1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc2(cc2_interlock_stop, cc2_remote_stop, cc2_remote_start):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2离心式冷水机组联锁停机指令
    # 2离心式冷水机组远方停机指令
    # 2离心式冷水机组远方开机指令
    state = syncbase.write_batch_realtime_data_by_name(
            ['cc2_interlock_stop', 'cc2_remote_stop', 'cc2_remote_start'],
            [cc2_interlock_stop, cc2_remote_stop, cc2_remote_start])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机2数据成功！")
    else:
        print("批量写入离心式冷水机2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc3(cc3_interlock_stop, cc3_remote_stop, cc3_remote_start):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3离心式冷水机组联锁停机指令
    # 3离心式冷水机组远方停机指令
    # 3离心式冷水机组远方开机指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc3_interlock_stop', 'cc3_remote_stop', 'cc3_remote_start'],
        [cc3_interlock_stop, cc3_remote_stop, cc3_remote_start])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机3数据成功！")
    else:
        print("批量写入离心式冷水机3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_cc4(cc4_interlock_stop, cc4_remote_stop, cc4_remote_start):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入离心式冷水机4的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 4离心式冷水机组联锁停机指令
    # 4离心式冷水机组远方停机指令
    # 4离心式冷水机组远方开机指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['cc4_interlock_stop', 'cc4_remote_stop', 'cc4_remote_start'],
        [cc4_interlock_stop, cc4_remote_stop, cc4_remote_start])

    # 显示写入结果
    if state:
        print("批量写入离心式冷水机4数据成功！")
    else:
        print("批量写入离心式冷水机4数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb1(ngb1_remote_start, ngb1_remote_stop):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉1的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 1燃气真空热水炉远程启动指令
    # 1燃气真空热水炉远程停止指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb1_remote_start', 'ngb1_remote_stop'],
        [ngb1_remote_start, ngb1_remote_stop])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉1数据成功！")
    else:
        print("批量写入燃气真空热水炉1数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb2(ngb2_remote_start, ngb2_remote_stop):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉2的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 2燃气真空热水炉远程启动指令
    # 2燃气真空热水炉远程停止指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb2_remote_start', 'ngb2_remote_stop'],
        [ngb2_remote_start, ngb2_remote_stop])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉2数据成功！")
    else:
        print("批量写入燃气真空热水炉2数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase


def write_to_database_ngb3(ngb3_remote_start, ngb3_remote_stop):
    """利用SyncBASE，向数据库中写入数据"""
    # 写入燃气真空热水炉3的数据
    syncbase = SyncBase('127.0.0.1', '8006')  # ip地址为本机
    syncbase.open()

    # 批量写入数据到数据库
    # 3燃气真空热水炉远程启动指令
    # 3燃气真空热水炉远程停止指令
    state = syncbase.write_batch_realtime_data_by_name(
        ['ngb3_remote_start', 'ngb3_remote_stop'],
        [ngb3_remote_start, ngb3_remote_stop])

    # 显示写入结果
    if state:
        print("批量写入燃气真空热水炉3数据成功！")
    else:
        print("批量写入燃气真空热水炉3数据失败！")

    # 关闭syncbase
    syncbase.close()
    del syncbase
