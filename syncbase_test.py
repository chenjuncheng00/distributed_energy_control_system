# -*- coding: utf-8 -*-
"""
syncbase测试模块
版本1.4.0.0
@author: wush
版权归南京科远智慧科技集团股份有限公司所有
All Rignts Reserved for Nanjing SCIYON Automation Group Co.,Ltd
"""

import datetime
from syncbase import SyncBase

def _print(records):
    if isinstance(records, dict):
        records = records.values()
    for record in records:
        if isinstance(record, (list, dict)):
            _print(record)
        else:
            print(record)
        
        
if __name__ == '__main__':
    print('开始测试...')
    
    syncbase = SyncBase('10.88.10.41', '8006')
    syncbase.open()
    
    print('测试根据id读取实时数据，数据回放时是回放时间：')
    state, record = syncbase.get_reatime_data_by_id(0)
    if state:
        print(record)
    
    print()
    print('测试根据id读取实时数据，时间总是当前时间：')
    state, record = syncbase.get_reatime_data_by_id_current(0)
    if state:
        print(record)
    
    print()
    print('测试根据名称读取实时数据：')
    state, record = syncbase.get_reatime_data_by_name('DCS1_AI_00001')
    if state:
        print(record)
    
    print()
    print('测试根据名称读取实时数据，时间总是当前时间：')
    state, record = syncbase.get_reatime_data_by_name_current('DCS1_AI_00001')
    if state:
        print(record)
    
    print()
    print('测试根据id批量读取实时数据，数据回放时是回放时间：')
    state, records = syncbase.get_batch_realtime_data_by_id([22683,22684,22685,22686,22687])
    if state:
        _print(records)
    
    print()
    print('测试根据id批量读取实时数据，时间总是当前时间：')
    state, records = syncbase.get_batch_realtime_data_by_id_current([22683,22684,22685,22686,22687])
    if state:
        _print(records)
    
    print()
    print('测试根据名称批量读取实时数据，数据回放时是回放时间：')
    state, records = syncbase.get_batch_realtime_data_by_name(['DCS1_AI_00055_PRE_22737','DCS1_AI_00002'])
    if state:
        _print(records)
    
    print()
    print('测试根据名称批量读取实时数据，时间总是当前时间：')
    state, records = syncbase.get_batch_realtime_data_by_name_current(['DCS1_AI_00055_PRE_22737','DCS1_AI_00002'])
    if state:
        _print(records)
    
    print()
    print('测试根据id读取历史数据：')
    state, records = syncbase.get_history_data_by_id(0, 
                                                     datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                                     datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                                     10
                                                     )
    if state:
        _print(records)
    
    print()
    print('测试根据名称读取历史数据：')
    state, records = syncbase.get_history_data_by_name('DCS1_AI_00055_PRE_22737', 
                                                     datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                                     datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                                     10
                                                     )
    if state:
        _print(records)
    
    print()
    print('测试根据id批量读取历史数据：')
    state, records = syncbase.get_batch_history_data_by_id([0, 22684], 
                                                     datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                                     datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                                     10
                                                     )
    if state:
        _print(records)
    
    print()
    print('测试根据名称批量读取历史数据：')
    state, records = syncbase.get_batch_history_data_by_name(['DCS1_AI_00055_PRE_22737', 'DCS1_AI_00002'], 
                                                     datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                                     datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                                     10
                                                     )
    if state:
        _print(records)
    
    print()
    print('测试根据测点id写实时数据(37787, 20)：')
    state = syncbase.write_reatime_data_by_id(37787, 20)
    if state:
        print('根据id写实时数据成功。')    
    print('写实时数据后再读取实时数据：')
    state, record = syncbase.get_reatime_data_by_id(37787)
    if state:
        print(record)
    else:
        print('读取实时数据失败。')
    
    print()
    import time
    time.sleep(2)
    print('测试根据测点名称写实时数据：')
    state = syncbase.write_reatime_data_by_name('test4', 30)
    if state:
        print('根据测点名称写实时数据成功。')
    
    print()
    print('测试根据测点id取测点信息：')
    state, tag_info = syncbase.get_tag_info_by_id(37787)
    if state:
        print(tag_info)
    
    print()
    print('测试取服务器时间：')
    state, server_time = syncbase.get_server_time()
    if state:
        print('服务器时间：{}'.format(server_time.strftime('%Y-%m-%d %H:%M:%S')))
    
    print()
    print('测试根据测点id批量写实时数据：')
    state = syncbase.write_batch_realtime_data_by_id([37787, 37788], [60, 80])
    if state:
        print('测试根据测点id批量写实时数据成功。')
    
    print()
    time.sleep(2)
    print('测试根据测点名称批量写实时数据：')
    state = syncbase.write_batch_realtime_data_by_name(['test3', 'test4'], [160, 180])
    if state:
        print('测试根据测点名称批量写实时数据成功。')
    
    print()
    print('测试根据测点名称查询历史数据生成DataFrame：')
    state, frame = syncbase.get_data_frame_by_name(['DCS1_AI_00055_PRE_22737'], 
                                            datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                            datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                            10)
    if state:
        print(frame)
        
    print()
    print('测试根据测点id查询历史数据生成DataFrame：')
    state, frame = syncbase.get_data_frame_by_id([0, 22684], 
                                            datetime.datetime(2018, 10, 7, 10, 0, 0), 
                                            datetime.datetime(2018, 10, 7, 10, 1, 0), 
                                            10)
    if state:
        print(frame)

    syncbase.close()
    del syncbase
        
    print('结束测试。')