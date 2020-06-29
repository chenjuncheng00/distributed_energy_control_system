# -*- coding: utf-8 -*-
"""
SyncBase5接口类
版本1.4.0.0
@author: wush
版权归南京科远智慧科技集团股份有限公司所有
All Rignts Reserved for Nanjing SCIYON Automation Group Co.,Ltd
"""

import ctypes
import datetime
import pandas as pd

class Record(object):
    """历史数据记录类"""
    
    def __init__(self, id, time, value, quality):
        """构造函数"""
        self.__id = id
        self.__time = time
        self.__value = value
        self.__quality = quality
        
    @property
    def id(self):
        """测点id"""
        return self.__id
    
    @property
    def time(self):
        """时间"""
        return self.__time
    
    @property
    def value(self):
        """测点值"""
        return self.__value
    
    @property
    def quality(self):
        """测点值的质量"""
        return self.__quality
    
    def __str__(self):
        return str((self.__id, self.__time.strftime('%Y-%m-%d %H:%M:%S'), self.__value, self.__quality))


class _DataValUnion(ctypes.Union):
    """值联合体"""
    
    _pack_ = 1
    
    _fields_ = [
        ('fval', ctypes.c_float),
        ('dval', ctypes.c_double),
        ('bval', ctypes.c_bool)
    ]

  
class _ValueStruct(ctypes.Structure):
    """值结构"""
    
    _pack_ = 1
    
    _fields_ = [
        ('value_union', _DataValUnion),
        ('value_type', ctypes.c_byte)
    ]
    
    def get_value(self):
        """浮点型：0；布尔型；整型；长整型；无符号长整型；双精度；字符串"""
        if self.value_type == 0:
            return self.value_union.fval
        elif self.value_type == 5:
            return self.value_union.dval
        elif self.value_type == 1:
            return self.value_union.bval
        else:
            raise TypeError('数值类型未定义')
    
    @property
    def value(self):
        return self.get_value()
    
    def __str__(self):
        return str((self.value, self.value_type))


class _TimeStruct(ctypes.Structure):
    """时间结构"""
    
    _pack_ = 1
    
    _fields_ = [
        ('year', ctypes.c_byte),
        ('month', ctypes.c_byte),
        ('day', ctypes.c_byte),
        ('hour', ctypes.c_byte),
        ('minute', ctypes.c_byte),
        ('second', ctypes.c_byte),
        ('millisecond', ctypes.c_short)
    ]

class _RecordStruct(ctypes.Structure):
    """历史记录结构"""
    
    _pack_ = 1
    
    _fields_ = [
        ('id', ctypes.c_uint32),
        ('time', _TimeStruct),
        ('value', _ValueStruct),
        ('quality', ctypes.c_ubyte)
    ]
    
    def to_record(self):
        """转换为历史记录对象"""
        record_time = self.time
        year = 2000 + record_time.year
        time = datetime.datetime(year, record_time.month, record_time.day, record_time.hour, 
                                 record_time.minute, record_time.second)
        return Record(self.id, time, self.value.value, self.quality)


class _InputTimeStruct(ctypes.Structure):
    """输入时间结构"""
    
    _pack_ = 1
    
    _fields_ = [
        ('year', ctypes.c_byte),
        ('month', ctypes.c_byte),
        ('day', ctypes.c_byte),
        ('hour', ctypes.c_byte),
        ('minute', ctypes.c_byte),
        ('second', ctypes.c_byte)
    ]
    
    @staticmethod
    def get_from_datetime(one_time):
        """从时间对象获取等价的输入时间结构"""
        time_struct = _InputTimeStruct()
        time_struct.year = one_time.year % 100
        time_struct.month = one_time.month
        time_struct.day = one_time.day
        time_struct.hour = one_time.hour
        time_struct.minute = one_time.minute
        time_struct.second = one_time.second
        
        return time_struct
    
    
class _TagInfoStruct(ctypes.Structure):
    """测点信息结构"""
    
    _pack_ = 1
    
    _fields_ = [
        ('nTagId', ctypes.c_int),
        ('nNodeId', ctypes.c_ushort),
        ('szTagName', ctypes.c_char * 65),
        ('szComment', ctypes.c_char * 101),
        ('nDataType', ctypes.c_ubyte),
        ('nPointNum', ctypes.c_ubyte),
        ('szUnit', ctypes.c_char * 7),
        ('fMinVal', ctypes.c_float),
        ('fMaxVal', ctypes.c_float)
    ]

    def to_tag_info(self):
        """转换为测点信息类"""
        return TagInfo(
            int(self.nTagId), 
            int(self.nNodeId), 
            str(self.szTagName, encoding="utf8"), 
            str(self.szComment, encoding="gb2312"), 
            int(self.nDataType), 
            int(self.nPointNum), 
            str(self.szUnit, encoding="utf8").strip(), 
            self.fMinVal, 
            self.fMaxVal
        )
    
    
class TagInfo(object):
    """测点信息类"""
    
    def __init__(self, id, node_id, tag_name, description, data_type, precision, unit, low_limit, high_limit):
        """构造函数"""
        self._id = id
        self._node_id = node_id
        self._tag_name = tag_name
        self._description = description
        self._data_type = data_type
        self._precision = precision
        self._unit = unit
        self._low_limit = low_limit
        self._high_limit = high_limit
        
    @property
    def id(self):
        """测点id"""
        return self._id
    
    @property
    def node_id(self):
        """测点所属的结点id"""
        return self._node_id
        
    @property
    def tag_name(self):
        """测点名称"""
        return self._tag_name
    
    @property
    def description(self):
        """测点描述"""
        return self._description
    
    @property
    def data_type(self):
        """测点类型"""
        return self._data_type
    
    @property
    def precision(self):
        """测点小数位数"""
        return self._precision    
    
    @property
    def unit(self):
        """测点单位"""
        return self._unit
    
    @property
    def low_limit(self):
        """测点工程下限"""
        return self._low_limit
    
    @property
    def high_limit(self):
        """测点工程上限"""
        return self._high_limit
    
    def __str__(self):
        return str(('测点id：' + str(self.id), '测点结点id：' + str(self.node_id), 
                    '测点名称：' + self.tag_name, '测点描述：' + self.description, 
                    '测点类型：' + str(self.data_type), '测点小数位数：' + str(self.precision), 
                    '测点单位：' + self.unit, '测点工程下限：' + str(self.low_limit), 
                    '测点工程上限：' + str(self.high_limit)))


class SyncBase_API(object):
    """读取SyncBase实时数据库的类"""
    
    def __init__(self, server_ip, server_port):
        """构造函数"""
        self._syncbase_api = ctypes.windll.LoadLibrary(r'.\syncbaseapi.dll')
        self._hsyncbase = self._syncbase_api.sync_CreateDB()
        self._server_ip = server_ip
        self._server_port = server_port
        
    def open(self):
        """连接服务器"""
        if self.is_opened():
            return True
        
        server_ip = str.encode(self._server_ip)
        server_port = int(self._server_port)
        state = self._syncbase_api.sync_Open(self._hsyncbase, server_ip, server_port)
        if (not state):
            print('连接服务器失败。')
            return False
        else:
            return True
            
    def is_opened(self):
        """查询是否已连接服务器"""
        return True if self._syncbase_api.sync_IsOpened(self._hsyncbase) else False
    
    def close(self):
        """关闭服务器连接"""
        if self.is_opened():
            state = self._syncbase_api.sync_Close(self._hsyncbase)
            return True if state else False
        else:
            return True
    
    def get_reatime_data_by_id(self, tag_id):
        """根据测点id取单个测点的实时数据"""
        self.__check_tag_id(tag_id)
        return self.__get_reatime_data_by_id(tag_id)

    def __get_reatime_data_by_id(self, tag_id):
        """根据测点id取单个测点的实时数据；若是数据回放，则时间为回放时间。"""
        try:
            state, record_struct = self.__get_realtime_record_struct_by_id(tag_id)            
            if state:
                return True, record_struct.to_record()

            return False, None
        except Exception as e:
            print(repr(e))
            return False, None

    def __get_realtime_record_struct_by_id(self, tag_id):
        """根据测点id取单个测点的实时记录结构；若是数据回放，则实时记录结构的时间为回放时间。"""
        record_struct = _RecordStruct()
        state = self._syncbase_api.sync_ReadRealData(self._hsyncbase, tag_id, ctypes.byref(record_struct))
        if state:
            return True, record_struct
        
        return False, None
    
    def get_reatime_data_by_id_current(self, tag_id):
        """根据测点id取单个测点的实时数据，时间总是当前时间。"""
        self.__check_tag_id(tag_id)
        return self.__get_reatime_data_by_id_current(tag_id)
    
    def __get_reatime_data_by_id_current(self, tag_id):
        """根据测点id取单个测点的实时数据"""
        try:
            state, record_struct = self.__get_realtime_record_struct_by_id(tag_id)
            
            if state:
                state, server_time = self.get_server_time()
                if state:
                    return True, Record(tag_id, server_time, record_struct.value.value, record_struct.quality)

            return False, None
        except Exception as e:
            print(repr(e))
            return False, None
    
    def get_reatime_data_by_name(self, tag_name):
        """根据测点名称取单个测点的实时数据"""
        self.__check_tag_name(tag_name)
        return self.__get_reatime_data_by_name(tag_name)
        
    def __get_reatime_data_by_name(self, tag_name):
        """根据测点名称取单个测点的实时数据"""
        state, tag_id = self.__get_tag_id_by_name(tag_name)
        if state:
            return self.__get_reatime_data_by_id(tag_id)
        else:
            return False, None
    
    def get_reatime_data_by_name_current(self, tag_name):
        """根据测点名称取单个测点的实时数据，时间总是当前时间。"""
        self.__check_tag_name(tag_name)
        return self.__get_reatime_data_by_name_current(tag_name)
        
    def __get_reatime_data_by_name_current(self, tag_name):
        """根据测点名称取单个测点的实时数据"""
        state, tag_id = self.__get_tag_id_by_name(tag_name)
        if state:
            return self.__get_reatime_data_by_id_current(tag_id)
        else:
            return False, None

    def write_reatime_data_by_id(self, tag_id, tag_value):
        """根据测点id写单个测点的实时数据"""
        self.__check_tag_id(tag_id)
        if isinstance(tag_value, bool):
            tag_value = int(tag_value)
        return self.__write_reatime_data_by_id(tag_id, tag_value)

    def __write_reatime_data_by_id(self, tag_id, tag_value):
        """根据测点id写单个测点的实时数据"""
        try:
            record = _RecordStruct()
            record.id = tag_id
            
            current_time = datetime.datetime.now()
            record.time.year = current_time.year % 100
            record.time.month = current_time.month
            record.time.day = current_time.day
            record.time.hour = current_time.hour
            record.time.minute = current_time.minute
            record.time.second = current_time.second
            record.time.millisecond = 0
            
            record.value.value_union.fval = tag_value
            record.value.value_type = 0
            
            record.quality = 0

            state = self._syncbase_api.sync_WriteRealData(self._hsyncbase, ctypes.byref(record))
            if state:
                return True
            else:
                return False
        except Exception as e:
            print(repr(e))
            return False
    
    def write_reatime_data_by_name(self, tag_name, tag_value):
        """根据测点名称写单个测点的实时数据"""
        self.__check_tag_name(tag_name)
        return self.__write_reatime_data_by_name(tag_name, tag_value)
        
    def __write_reatime_data_by_name(self, tag_name, tag_value):
        """根据测点名称写单个测点的实时数据"""
        state, tag_id = self.__get_tag_id_by_name(tag_name)
        if state:
            return self.__write_reatime_data_by_id(tag_id, tag_value)
        else:
            return False

    def write_batch_realtime_data_by_id(self, tag_ids, tag_values):
        """根据测点id写批量测点的实时数据"""
        self.__check_int_list(tag_ids)
        self.__check_list(tag_values)
        if len(tag_ids) != len(set(tag_ids)):
            raise ValueError('测点列表中存在重复id。')
        if len(tag_ids) != len(tag_values):
            raise ValueError('测点列表与值列表长度不一致。')
        return self.__write_batch_realtime_data_by_id(tag_ids, tag_values)
    
    def __write_batch_realtime_data_by_id(self, tag_ids, tag_values):
        """根据测点id写批量测点的实时数据"""
        try:
            tag_count = len(tag_ids)
            records = (_RecordStruct * tag_count)()
            current_time = datetime.datetime.now()
            for i in range(tag_count):
                record = records[i]
                record.id = tag_ids[i]
                record.time.year = current_time.year % 100
                record.time.month = current_time.month
                record.time.day = current_time.day
                record.time.hour = current_time.hour
                record.time.minute = current_time.minute
                record.time.second = current_time.second
                record.time.millisecond = 0                
                record.value.value_union.fval = tag_values[i]
                record.value.value_type = 0                
                record.quality = 0
            state = self._syncbase_api.sync_WriteBatchRealData(self._hsyncbase, ctypes.byref(records), 
                                                               ctypes.c_int(tag_count))
            if state:
                return True
            else:
                return False
        except Exception as e:
            print(repr(e))
            return False

    def write_batch_realtime_data_by_name(self, tag_names, tag_values):
        """根据测点名称写批量测点的实时数据"""
        self.__check_str_list(tag_names)
        self.__check_list(tag_values)
        if len(tag_names) != len(set(tag_names)):
            raise ValueError('测点列表中存在重复名称。')
        if len(tag_names) != len(tag_values):
            raise ValueError('测点列表与值列表长度不一致。')
        tag_ids = []
        for tag_name in tag_names:
            state, tag_id = self.__get_tag_id_by_name(tag_name)
            if state:
                tag_ids.append(tag_id)
        if len(tag_ids) != len(tag_names):
            raise ValueError('测点名称列表中部分测点不存在。')
        return self.__write_batch_realtime_data_by_id(tag_ids, tag_values)

    def __check_list(self, data):
        if not isinstance(data, list):
            raise TypeError('输入参数应该是列表。')

    def __check_int_list(self, data):
        self.__check_list(data)
        for item in data:
            if not isinstance(item, int):
                raise TypeError('输入列表中不全是整数。')
    
    def __check_str_list(self, data):
        self.__check_list(data)
        for item in data:
            if not isinstance(item, str):
                raise TypeError('输入列表中不全是字符串。')
        
    def get_batch_realtime_data_by_id(self, tag_ids):
        """根据测点id取批量测点的实时数据；若是数据回放，则时间为回放时间。"""
        self.__check_list(tag_ids)
        return self.__get_batch_realtime_data_by_id_common(tag_ids, 0)
            
    def get_batch_realtime_data_by_id_current(self, tag_ids):
        """根据测点id取批量测点的实时数据，时间总是当前时间。"""
        self.__check_list(tag_ids)
        return self.__get_batch_realtime_data_by_id_common(tag_ids, 1)        
    
    def __get_batch_realtime_data_by_id_common(self, tag_ids, time_type):
        """根据测点id取批量测点的实时数据，时间根据time_type确定。
        Args:
            tag_ids: 测点id列表。
            time_type: 时间类型，0表示取实时时间或回放时间，由SyncBase刷新时间确定；1表示只取当前时间。
        Returns:
            以测点id为索引的测点值记录字典。
        """
        tag_ids = set(tag_ids)
        tag_count = len(tag_ids)
        ids = (ctypes.c_int * tag_count)(*tag_ids)
        values = (_ValueStruct * tag_count)()
        qualities = (ctypes.c_byte * tag_count)()
        success_count = self._syncbase_api.sync_ReadBatchRealData(
                self._hsyncbase, 
                ctypes.byref(ids), 
                ctypes.byref(values), 
                ctypes.byref(qualities), 
                tag_count)
        if success_count > 0:
            if time_type == 0:
                state, record = self.__get_reatime_data_by_id(ids[0])
                if state:
                    server_time = record.time
            elif time_type == 1:
                state, server_time = self.get_server_time()
            else:
                state = False
            
            if state:
                result = {}
                for i in range(success_count):
                    result[ids[i]] = Record(ids[i], server_time, values[i].value, qualities[i])
                return True, result

        return False, None
    
    def get_batch_realtime_data_by_name(self, tag_names):
        """根据测点名称取批量测点的实时数据；若是数据回放，则时间为回放时间。"""
        self.__check_list(tag_names)
        return self.__get_batch_realtime_data_by_name_common(tag_names, 0)

    def get_batch_realtime_data_by_name_current(self, tag_names):
        """根据测点名称取批量测点的实时数据，时间总是当前时间。"""
        self.__check_list(tag_names)
        return self.__get_batch_realtime_data_by_name_common(tag_names, 1)
    
    def __get_batch_realtime_data_by_name_common(self, tag_names, time_type):
        """根据测点名称取批量测点的实时数据，时间根据time_type确定
        Args:
            tag_names: 测点名称列表。
            time_type: 时间类型，0表示取实时时间或回放时间，由SyncBase刷新时间确定；1表示只取当前时间。
        Returns:
            以测点名称为索引的测点值记录字典。
        """
        ids = {}
        for tag_name in tag_names:
            state, tag_id = self.__get_tag_id_by_name(tag_name)
            if state:
                ids[tag_id] = tag_name
        if len(ids) > 0:
            state, result_ids = self.__get_batch_realtime_data_by_id_common(ids.keys(), time_type)
            if state:
                result_names = {ids[key] : result_ids[key] for key in result_ids}
                return True, result_names
        
        return False, None
        
    def get_history_data_by_id(self, tag_id, start_time, end_time, period):
        """根据测点id取单个测点的历史数据"""
        self.__check_tag_id(tag_id)
        return self.__get_history_data_by_id(tag_id, start_time, end_time, period)

    def __get_history_data_by_id(self, tag_id, start_time, end_time, period):
        """根据测点id取单个测点的历史数据"""
        hdata = ctypes.c_void_p()
        s_time = _InputTimeStruct.get_from_datetime(start_time)
        e_time = _InputTimeStruct.get_from_datetime(end_time)
        state = self._syncbase_api.sync_OpenHisQuery(self._hsyncbase, tag_id, 
                                                     s_time, e_time, period, 
                                                     ctypes.byref(hdata))
        
        if state:
            try:
                records = {}
                record_struct = _RecordStruct()
                read_state = self._syncbase_api.sync_ReadHisData(hdata, ctypes.byref(record_struct))
                while read_state > 0:
                    record = record_struct.to_record()
                    records[record.time] = record
                    read_state = self._syncbase_api.sync_ReadHisData(hdata, ctypes.byref(record_struct))                
                return True, records
            except Exception as e:
                print(repr(e))
                return False, None
            finally:
                self._syncbase_api.sync_CloseHisQuery(ctypes.byref(hdata))
        else:
            return False, None
        
    def get_history_data_by_name(self, tag_name, start_time, end_time, period):
        """根据测点名称取单个测点的历史数据"""
        self.__check_tag_name(tag_name)
        return self.__get_history_data_by_name(tag_name, start_time, end_time, period)

    def __get_history_data_by_name(self, tag_name, start_time, end_time, period):
        """根据测点名称取单个测点的历史数据"""
        state, tag_id = self.__get_tag_id_by_name(tag_name)
        if state:
            return self.__get_history_data_by_id(tag_id, start_time, end_time, period)
        else:
            return False, None

    def get_batch_history_data_by_id(self, tag_ids, start_time, end_time, period):
        """根据测点id取批量测点的历史数据"""
        self.__check_int_list(tag_ids)
        return self.__get_batch_history_data_by_id(tag_ids, start_time, end_time, period)

    def __get_batch_history_data_by_id(self, tag_ids, start_time, end_time, period):
        """根据测点id取批量测点的历史数据"""
        tag_ids = set(tag_ids)
        if len(tag_ids) > 0:
            results = {}
            for tag_id in tag_ids:
                state, records = self.__get_history_data_by_id(tag_id, start_time, end_time, period)
                if state:
                    results[tag_id] = records
            return True, results
        else:
            return False, None
        
    def get_batch_history_data_by_name(self, tag_names, start_time, end_time, period):
        """根据测点名称取批量测点的历史数据"""
        self.__check_str_list(tag_names)
        return self.__get_batch_history_data_by_name(tag_names, start_time, end_time, period)

    def __get_batch_history_data_by_name(self, tag_names, start_time, end_time, period):
        """根据测点名称取批量测点的历史数据"""
        tag_names = set(tag_names)
        if len(tag_names) > 0:
            results = {}
            for tag_name in tag_names:
                state, records = self.__get_history_data_by_name(tag_name, start_time, end_time, period)
                if state:
                    results[tag_name] = records
            return True, results
        else:
            return False, None

    def _to_data_frame(self, data_dict):
        frame = pd.DataFrame(data_dict)
        row_count = frame.index.size
        for column in frame.columns:
            for i in range(row_count):
                frame[column][i] = frame[column][i].value
        return frame.astype('float64')
    
    def get_data_frame_by_id(self, tag_ids, start_time, end_time, period):
        """根据测点获取由历史数据组成的DataFrame对象"""
        state, his_data = self.get_batch_history_data_by_id(tag_ids, start_time, end_time, period)
        if state:
            frame = self._to_data_frame(his_data)
            return True, frame
        else:
            return False, None
   
    def get_data_frame_by_name(self, tag_names, start_time, end_time, period):
        """根据测点名称获取由历史数据组成的DataFrame对象"""
        state, his_data = self.get_batch_history_data_by_name(tag_names, start_time, end_time, period)
        if state:
            frame = self._to_data_frame(his_data)
            return True, frame
        else:
            return False, None
    
    def get_tag_info_by_id(self, tag_id):
        """根据测点id获取测点信息"""
        self.__check_tag_id(tag_id)
        return self.__get_tag_info_by_id(tag_id)

    def __get_tag_info_by_id(self, tag_id):
        """根据测点id获取测点信息"""
        taginfo_struct = _TagInfoStruct()
        state = self._syncbase_api.sync_ReadTagParById(self._hsyncbase, tag_id, ctypes.byref(taginfo_struct))
        if state:
            return True, taginfo_struct.to_tag_info()
        else:
            return False, None
            
    def get_server_time(self):
        """取服务器当前时间"""
        server_time_raw = ctypes.c_int()
        state = self._syncbase_api.sync_GetServerTime(self._hsyncbase, ctypes.byref(server_time_raw))
        if state:
            return True, datetime.datetime.fromtimestamp(server_time_raw.value)
        else:
            return False, None
    
    def get_tag_id_by_name(self, tag_name):
        """根据测点名称取测点id"""
        self.__check_tag_name(tag_name)
        return self.__get_tag_id_by_name(tag_name)

    def __get_tag_id_by_name(self, tag_name):
        """根据测点名称取测点id"""
        tag_name = str.encode(tag_name)
        tag_id = self._syncbase_api.sync_GetTagIdByName(self._hsyncbase, tag_name)
        if tag_id >= 0:
            return True, tag_id
        else:
            return False, None
    
    def __check_tag_name(self, tag_name):
        if not isinstance(tag_name, str):
            raise TypeError('测点名称应该为字符串。')
            
    def __check_tag_id(self, tag_id):
        if (not isinstance(tag_id, int)) or tag_id < 0:
            raise TypeError('测点id应该为非负整数。')
    
    def __del__(self):
        """析构函数"""
        if (self._hsyncbase):
            self.close()
            self._syncbase_api.sync_DestoryDB(self._hsyncbase)
    
