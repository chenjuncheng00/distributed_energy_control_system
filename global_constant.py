import tensorflow as tf

class Global_Constant():
    def __init__(self):
        # 设置历史数据读取间隔（单位秒）
        self.period = 1 * 60
        # 环境温度
        self.environment_temperature = 30
        # 整个项目的建筑面积
        self.area = 189000
        # 允许的最大冷负荷
        self.cold_load_max = 28000
        # 允许的最大热负荷
        self.heat_load_max = 14000
        # 允许的最大生活热水负荷
        self.hot_water_load_max = 4500
        # 烟气热水型溴化锂设备在制冷季是否供生活热水
        self.lb_hot_water_switch_cooling_season = False
        # 烟气热水型溴化锂设备在采暖季是否供生活热水
        self.lb_hot_water_switch_heating_season = False
        # 供冷时出水温度
        self.chilled_water_temperature = 7
        # 供热时出水温度
        self.heating_water_temperature = 55
        # 空气源热泵在作为一级低温热源制热时的出水温度
        self.ashp_heat_source_water_temperature = 25
        # 冷冻水额定供回水温差
        self.chilled_water_temperature_difference_rated = 5
        # 冷却水额定供回水温差
        self.cooling_water_temperature_difference_rated = 5
        # 采暖水额定供回水温差
        self.heating_water_temperature_difference_rated = 5
        # 离心式热泵低温热源水额定供回水温差
        self.heat_source_water_temperature_difference_rated = 5
        # 生活热水出水温度额定值
        self.hot_water_temperature = 85
        # 生活热水额定供回水温差
        self.hot_water_temperature_difference_rated = 20
        # 蓄冷装置蓄冷供冷时的冷冻水供回水温差
        self.cooling_storage_water_temperature_difference_rated = 5
        # 蓄热装置蓄热供热时的采暖水供回水温差
        self.heating_storage_water_temperature_difference_rated = 5
        # 冷却水补水率
        self.cooling_water_supply_rate = 0.015
        # 闭式循环补水率
        self.closed_loop_supply_rate = 0.0015
        # 低温热源水补水率
        self.heat_source_water_supply_rate = 0.015
        # 天然气热值，kj/m3
        self.natural_gas_calorific_value = 34000
        # 售冷单价
        self.cooling_price = 0.495
        # 售热单价
        self.heating_price = 0.65
        # 生活热水单价
        self.hot_water_price = 0.65
        # 售电电价
        self.sale_electricity_price = 0.65
        # 天然气单价
        self.natural_gas_price = 2.6
        # 补水单价
        self.water_price = 5
        # 购电单价
        self.buy_electricity_price = 0.6707
        # 项目负荷误差容错系数
        self.project_load_error = 50
        # 蓄冷蓄热负荷误差容错系数
        self.ese_load_error = 5
        # 设备负荷率误差容错系数
        self.load_ratio_error_coefficient = 0.005
        # 溴化锂设备供应冷热的一些常量
        # 溴化锂1、2的生活热水负荷最大值
        self.lb1_hot_water_max = 1600
        self.lb2_hot_water_max = 1600
        # 溴化锂1、2的冷负荷最大值
        self.lb1_cold_max = 1750
        self.lb2_cold_max = 1750
        # 溴化锂1、2的热负荷最大值
        self.lb1_heat_max = 1600
        self.lb2_heat_max = 1600
        # 溴化锂设备生活热水计算步长
        self.lb1_hot_water_step = 50
        self.lb2_hot_water_step = 50
        # 制冷季的开始月份和日期
        self.cooling_season_start_date = "05-15"
        # 制冷季的结束月份和日期
        self.cooling_season_end_date = "10-15"
        # 采暖季的开始月份和日期
        self.heating_season_start_date = "11-15"
        # 采暖季的结束月份和日期
        self.heating_season_end_date = "03-15"
        # 非谷电时间段列表(用与蓄冷蓄热策略计算)
        self.hour_ese_out = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        # 程序计算周期（一小时计算几次），用于蓄冷蓄热计算
        self.hour_num_of_calculations = 1
        # 神经网络负荷预测模型
        self.cold_load_model = tf.keras.models.load_model('./load_forecast_model/cold_load_forecast_model.h5')
        self.heat_load_model = tf.keras.models.load_model('./load_forecast_model/heat_load_forecast_model.h5')
        # 离心式冷水机COP神经网络模型
        self.model_centrifugal_chiller_cop_1 = tf.keras.models.load_model('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.5_to_1.h5')
        self.model_centrifugal_chiller_cop_2 = tf.keras.models.load_model('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.1_to_0.5.h5')
        # 水泵功率和扬程神经网络模型
        self.model_wp_710t = tf.keras.models.load_model('./water_pump_model/wp_710t/wp_710t_model.h5')
        self.model_wp_600t = tf.keras.models.load_model('./water_pump_model/wp_600t/wp_600t_model.h5')
        self.model_wp_340t = tf.keras.models.load_model('./water_pump_model/wp_340t/wp_340t_model.h5')
