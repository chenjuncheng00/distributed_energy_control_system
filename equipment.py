import math
import numpy as np
import tensorflow as tf

class Centrifugal_Chiller():
    """类：离心式冷水机；螺杆式冷水机组、离心式热泵、水源热泵、地源热泵的制冷工况同样适用"""

    def __init__(self, cooling_power_rated, load_min, frequency_scaling, wp_chilled_water, wp_cooling_water, gc):
        """类的初始化"""
        # 制冷功率出力，额定值
        self.cooling_power_rated = cooling_power_rated
        # 离心式冷水机最低运行负荷率
        self.load_min = load_min
        # 离心式冷水机是否变频
        self.frequency_scaling = frequency_scaling
        # 离心式冷水机采用的冷冻水泵
        self.wp_chilled_water = wp_chilled_water
        # 离心式冷水机采用的冷却水泵
        self.wp_cooling_water = wp_cooling_water
        # 离心式冷水机额定冷冻水供回水温差
        self.chilled_water_temperature_difference_rated = gc.chilled_water_temperature_difference_rated
        # 离心式冷水机额定冷却水供回水温差
        self.cooling_water_temperature_difference_rated = gc.cooling_water_temperature_difference_rated
        # 离心式冷水机COP神经网络模型
        self.model_centrifugal_chiller_cop_1 = gc.model_centrifugal_chiller_cop_1 # 离心式冷水机负荷率范围：50%~100%
        self.model_centrifugal_chiller_cop_2 = gc.model_centrifugal_chiller_cop_2 # 离心式冷水机负荷率范围：10%~50%

    def chilled_water_flow_rated(self):
        # 如果冷冻水泵定频，始终等于最大流量
        chilled_water_flow_rated = self.cooling_power_rated * 3600 / 1000 / 4.2 / self.chilled_water_temperature_difference_rated
        return chilled_water_flow_rated

    def cooling_water_flow_rated(self):
        # 计算冷冻水额定流量，为冷冻水额定流量基的1.18倍
        cooling_water_flow_rated = 1.18 * self.cooling_power_rated * 3600 / 1000 / 4.2 / self.chilled_water_temperature_difference_rated
        return cooling_water_flow_rated

    def cooling_water_flow(self, load_ratio):
        """冷却水流量，某一负荷率下"""
        # 如果冷却水泵为变频
        if self.wp_cooling_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化，冷却水随负荷率变化
            if load_ratio >= 0.4:
                ans =self.cooling_water_flow_rated() * load_ratio
            else:
                # 如果负荷率小于40%，则等于35%的流量，不再减少
                ans = self.cooling_water_flow_rated() * 0.35
        else:
            # 如果冷却水泵定频，始终等于额定流量
            ans = self.cooling_water_flow_rated()
        # 返回结果
        return ans

    def chilled_water_flow(self, load_ratio):
        """冷冻水流量，某一负荷率下"""
        # 如果冷冻水泵为变频
        if self.wp_chilled_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化
            if load_ratio >= 0.4:
                ans = load_ratio * self.chilled_water_flow_rated()
            else:
                # 如果负荷率小于40%，则等于32%的流量，不再减少
                ans = 0.32 * self.chilled_water_flow_rated()
        else:
            # 如果冷冻水泵定频，始终等于最大流量
            ans= self.chilled_water_flow_rated()
        #返回结果
        return ans

    def cooling_water_temperature(self, load_ratio):
        """离心式冷水机冷却水出口水温"""
        # 100%负荷时是37℃
        # 如果冷却水泵为变频
        if self.wp_cooling_water.frequency_scaling == True:
            if load_ratio <= 0.5:
                ans = 425 * math.pow(load_ratio, 4) - 555*  math.pow(load_ratio, 3) + 224.75 * math.pow(load_ratio, 2) -20.55 * load_ratio +20.24
            else:
                ans = 27.343 * load_ratio + 9.6495
        # 如果冷却水泵为定频
        else:
            if load_ratio <= 0.5:
                ans = 4.64 * load_ratio +18.404
            else:
                ans = 32.571 * load_ratio +4.3881

        # 返回计算结果
        return ans

    def centrifugal_chiller_cop(self, load_ratio, chilled_water_temperature, cooling_water_temperature):
        # 如果设备负荷率大于等于0.5
        if load_ratio >= 0.5:
            # 输入
            x1 = (load_ratio - 0.5) / (1 - 0.5)
            x2 = (chilled_water_temperature - 5) / (12 - 5)
            x3 = (cooling_water_temperature - 17.51) / (39.7 - 17.51)
            X_1 = np.array([x1, x2, x3], dtype='float32')
            X = np.mat(X_1)
            # 加载训练好的神经网络模型
            ans = self.model_centrifugal_chiller_cop_1.predict(X)
            # 计算预测结果
            cop = ans[0][0] * (8.522 - 5.025) + 5.025
        # 如果设备负荷率小于0.5
        else:
            # 输入
            x1 = (load_ratio - 0.1) / (0.5 - 0.1)
            x2 = (chilled_water_temperature - 5) / (12 - 5)
            x3 = (cooling_water_temperature - 15.55) / (23.35 - 15.55)
            X_1 = np.array([x1, x2, x3], dtype='float32')
            X = np.mat(X_1)
            # 加载训练好的神经网络模型
            ans = self.model_centrifugal_chiller_cop_2.predict(X)
            # 计算预测结果
            cop = ans[0][0] * (8.522 - 3.959) + 3.959
        # 返回结果
        return cop

    def centrifugal_chiller_cooling_water_pump_head_min(self, cooling_water_flow):
        # 离心式冷水机组冷却水泵最低扬程需求量计算（仅针对变频水泵的计算）
        # 针对单台冷却水泵进行计算，变频泵在不同的流量比例（当前流量与最大流量比例）情况下，的最低扬程需求，从而反算出可以运行的最低频率
        # ooling_water_flow_rated = self.cooling_water_flow_rated()
        # cooling_water_flow_proportion = cooling_water_flow / cooling_water_flow_rated  # 离心式冷水机冷却水比例
        # water_pump_head_min = 1.835 * (15.076 * math.pow(cooling_water_flow_proportion, 2) - 0.0258 * cooling_water_flow_proportion + 2.57)
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def centrifugal_chiller_chilled_water_pump_head_min(self, chilled_water_flow):
        # 目前无冷冻水泵扬程随流量变化数据，暂时按照冷却水流量的公式放大1.1875倍
        # chilled_water_flow_rated = self.chilled_water_flow_rated()
        # chilled_water_flow_proportion = chilled_water_flow / chilled_water_flow_rated # 离心式冷水机冷冻水比例
        # water_pump_head_min = 1.835 * (15.076 * math.pow(chilled_water_flow_proportion, 2) - 0.0258 * chilled_water_flow_proportion + 2.57) * 1.1875
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, cooling_water_flow, chilled_water_flow):
        """辅助设备耗电功率计算"""
        # 冷却水泵耗电功率，某一负荷率下
        if self.wp_cooling_water.frequency_scaling == False:
            #如果是定频水泵，频率永远保持50Hz（定频水泵的扬程都是满足要求的，不再计算扬程）
            cooling_pump_power = self.wp_cooling_water.pump_performance_data(cooling_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算冷却水流量额定值
            cooling_water_flow_rated = self.cooling_water_flow_rated()
            # 从这个点开始寻找频率合适的值
            wp_frequency_start_cooling_water = (cooling_water_flow/cooling_water_flow_rated) * 50
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_cooling_water = self.wp_cooling_water.pump_performance_data(cooling_water_flow, wp_frequency_start_cooling_water)[0]
            # 冷却水泵扬程在当前流量下最低需求值
            cooling_water_pump_head_min = self.centrifugal_chiller_cooling_water_pump_head_min(cooling_water_flow)
            if wp_pump_head_start_cooling_water >= cooling_water_pump_head_min:
                wp_frequency_cooling_water = wp_frequency_start_cooling_water
                # 计算当前频率、流量情况下水泵功率
                cooling_pump_power = self.wp_cooling_water.pump_performance_data(cooling_water_flow, wp_frequency_cooling_water)[1]
            else:
                # 因为冷冻水和冷却水系统的流量比等于频率比，所以可以算出来一个在满足最低扬程需求情况下的最低频率值，也就是最低流量值
                # 水泵频率初始值
                wp_frequency_cooling_water = wp_frequency_start_cooling_water
                # 计算当前频率、流量情况下水泵功率
                cooling_pump_power = self.wp_cooling_water.pump_performance_data(cooling_water_flow, wp_frequency_cooling_water)[1]
                while wp_frequency_cooling_water <= 50: # 最大50Hz
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    cooling_water_flow = (wp_frequency_cooling_water / 50) * cooling_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_a = self.wp_cooling_water.pump_performance_data(cooling_water_flow, wp_frequency_cooling_water)[0]
                    if wp_pump_head_a >= cooling_water_pump_head_min:
                        # 计算当前频率、流量情况下水泵功率
                        cooling_pump_power = self.wp_cooling_water.pump_performance_data(cooling_water_flow, wp_frequency_cooling_water)[1]
                        break
                    else:
                        wp_frequency_cooling_water += 1
        # 冷冻水泵计算
        if self.wp_chilled_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            chilled_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算冷冻水泵额定值
            chilled_water_flow_rated = self.chilled_water_flow_rated()
            wp_frequency_start_chilled_water = (chilled_water_flow / chilled_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_chilled_water = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_start_chilled_water)[0]
            # 冷冻水泵扬程最小值需求量
            chilled_water_pump_head_min = self.centrifugal_chiller_chilled_water_pump_head_min(chilled_water_flow)
            if wp_pump_head_start_chilled_water >= chilled_water_pump_head_min:
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                chilled_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
            else:
                # 因为冷冻水和冷却水系统的流量比等于频率比，所以可以算出来一个在满足最低扬程需求情况下的最低频率值，也就是最低流量值
                # 水泵频率初始值
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                # 计算当前频率、流量情况下水泵功率
                chilled_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                while wp_frequency_chilled_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    chilled_water_flow = (wp_frequency_chilled_water / 50) * chilled_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[0]
                    if wp_pump_head_b >= chilled_water_pump_head_min:
                        # 计算当前频率、流量情况下水泵功率
                        chilled_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                        break
                    else:
                        wp_frequency_chilled_water += 1
        # 冷却塔风机耗电功率，某一负荷率下，风机为定频，功率保持不变
        cooling_tower_fan_power = 20
        # 返回总辅助设备耗电功率，某一负荷率下
        return cooling_pump_power + chilled_pump_power + cooling_tower_fan_power

    def centrifugal_chiller_power_consumption(self, load_ratio, centrifugal_chiller_cop):
        """离心式冷水机本身耗电功率，某一负荷率下"""
        return load_ratio * self.cooling_power_rated/ centrifugal_chiller_cop

class Centrifugal_Heat_Pump():
    """类：离心式热泵机组；水源热泵、地源热泵的制热工况同样适用"""

    def __init__(self, heating_power_rated, load_min, frequency_scaling, wp_heating_water, wp_heat_source_water, gc):
        """类的初始化"""
        # 制热功率出力，额定值
        self.heating_power_rated = heating_power_rated
        # 离心式热泵机组最低运行负荷率
        self.load_min = load_min
        # 离心式热泵机组是否变频
        self.frequency_scaling = frequency_scaling
        # 离心式热泵机组采用的采暖水泵
        self.wp_heating_water = wp_heating_water
        # 离心式热泵机组采用的低温热源水泵
        self.wp_heat_source_water = wp_heat_source_water
        # 离心式热泵机组额定采暖水供回水温差
        self.heating_water_temperature_difference_rated = gc.heating_water_temperature_difference_rated
        # 离心式热泵机组额定低温热源水供回水温差
        self.heat_source_water_temperature_difference_rated = gc.heat_source_water_temperature_difference_rated
        # 离心式热泵机组制热COP神经网络模型
        # self.model_centrifugal_heat_pump_cop_1 = gc.model_centrifugal_heat_pump_cop_cop_1  # 离心式热泵机组负荷率范围：50%~100%
        # self.model_centrifugal_heat_pump_cop_2 = gc.model_centrifugal_heat_pump_cop_cop_2  # 离心式热泵机组负荷率范围：10%~50%

    def centrifugal_heat_pump_cop(self, load_ratio, heating_water_temperature, heat_source_water_temperature):
        # 离心式热泵机组制热COP
        cop = 5.8
        return cop

    def heating_water_flow_rated(self):
        # 如果采暖水泵定频，始终等于最大流量
        heating_water_flow_rated = self.heating_power_rated * 3600 / 1000 / 4.2 / self.heating_water_temperature_difference_rated
        return heating_water_flow_rated

    def heat_source_water_flow_rated(self):
        # 计算低温热源水额定流量，低温热源水的功率+电功率=制热输出功率
        # 计算满负荷时候的制热COP
        cop = self.centrifugal_heat_pump_cop(1, 55, 25)
        # 计算满负荷时候的电负荷功率
        electric_power_consumption_rated = self.heating_power_rated / cop
        # 计算满负荷时候的低温热源水功率
        heat_source_water_power_rated = self.heating_power_rated - electric_power_consumption_rated
        # 计算满负荷时候的低温热源水额定流量
        heat_source_water_flow_rated = heat_source_water_power_rated * 3600 / 1000 / 4.2 / self.heat_source_water_temperature_difference_rated
        return heat_source_water_flow_rated

    def heating_water_flow(self, load_ratio):
        """采暖水流量，某一负荷率情况下"""
        # 如果采暖水泵为变频
        if self.wp_heating_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化，采暖水流量随负荷率变化
            if load_ratio >= 0.4:
                ans = self.heating_water_flow_rated() * load_ratio
            else:
                # 如果负荷率小于40%，则等于35%的流量，不再减少
                ans = self.heating_water_flow_rated() * 0.35
        else:
            # 如果采暖水泵定频，始终等于额定流量
            ans = self.heating_water_flow_rated()
            # 返回结果
        return ans

    def heat_source_water_flow(self, load_ratio):
        """采暖低温热源水流量，某一负荷率情况下"""
        # 如果采暖低温热源水泵为变频
        if self.wp_heat_source_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化，采暖低温热源水流量随负荷率变化
            if load_ratio >= 0.4:
                ans = self.heat_source_water_flow_rated() * load_ratio
            else:
                # 如果负荷率小于40%，则等于35%的流量，不再减少
                ans = self.heat_source_water_flow_rated() * 0.35
        else:
            # 如果采暖低温热源水泵定频，始终等于额定流量
            ans = self.heat_source_water_flow_rated()
            # 返回结果
        return ans

    def heat_source_water_temperature(self, load_ratio):
        """离心式热泵机组低温热源水出口水温"""
        # 100%负荷时是
        # 如果低温热源水泵为变频
        if self.wp_heat_source_water.frequency_scaling == True:
            ans = 10
        # 如果低温热源水泵为定频
        else:
            ans = 10

        # 返回计算结果
        return ans

    def centrifugal_heat_pump_heat_source_water_pump_head_min(self, heat_source_water_flow):
        # 离心式热泵机组低温热源水泵最低扬程需求量计算（仅针对变频水泵的计算）
        # 针对单台低温热源水泵进行计算，变频泵在不同的流量比例（当前流量与最大流量比例）情况下，的最低要成需求，从而反算出可以运行的最低频率
        # heat_source_water_flow_rated = self.heat_source_water_flow_rated()
        # heat_source_water_flow_proportion = heat_source_water_flow / heat_source_water_flow_rated  # 离心式热泵机组低温热源水比例
        # water_pump_head_min = 1.835 * (15.076 * math.pow(heat_source_water_flow_proportion, 2) - 0.0258 * heat_source_water_flow_proportion + 2.57)
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def centrifugal_heat_pump_heating_water_pump_head_min(self, heating_water_flow):
        # 离心式热泵机组采暖水泵最低扬程需求量计算（仅针对变频水泵的计算），暂时按照低温热源水流量的公式放大1.1875倍
        # heating_water_flow_rated = self.heating_water_flow_rated()
        # heating_water_flow_proportion = heating_water_flow / heating_water_flow_rated
        # water_pump_head_min = 1.835 * (15.076 * math.pow(heating_water_flow_proportion, 2) - 0.0258 * heating_water_flow_proportion + 2.57) * 1.1875
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, heat_source_water_flow, heating_water_flow):
        """辅助设备耗电功率计算"""
        # 低温热源水泵耗电功率，某一负荷率下
        if self.wp_heat_source_water.frequency_scaling == False:
            #如果是定频水泵，频率永远保持50Hz（定频水泵的扬程都是满足要求的，不再计算扬程）
            heat_source_water_pump_power = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算低温热源水流量额定值
            heat_source_water_flow_rated = self.heat_source_water_flow_rated()
            wp_frequency_start_heat_source_water = (heat_source_water_flow/heat_source_water_flow_rated) * 50 # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_heat_source_water = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, wp_frequency_start_heat_source_water)[0]
            # 低温热源水泵扬程在当前流量下最低需求值
            heat_source_water_pump_head_min = self.centrifugal_heat_pump_heat_source_water_pump_head_min(heat_source_water_flow)
            if wp_pump_head_start_heat_source_water >= heat_source_water_pump_head_min:
                wp_frequency_heat_source_water = wp_frequency_start_heat_source_water
                # 计算当前频率、流量情况下水泵功率
                heat_source_water_pump_power = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, wp_frequency_heat_source_water)[1]
            else:
                # 初始值
                wp_frequency_heat_source_water = wp_frequency_start_heat_source_water
                # 计算当前频率、流量情况下水泵功率
                heat_source_water_pump_power = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, wp_frequency_heat_source_water)[1]
                while wp_frequency_heat_source_water <= 50: # 最大50Hz
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    heat_source_water_flow = (wp_frequency_heat_source_water / 50) * heat_source_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_a = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, wp_frequency_heat_source_water)[0]
                    if wp_pump_head_a >= heat_source_water_pump_head_min:
                        # 计算当前频率、流量情况下水泵功率
                        heat_source_water_pump_power = self.wp_heat_source_water.pump_performance_data(heat_source_water_flow, wp_frequency_heat_source_water)[1]
                        break
                    else:
                        wp_frequency_heat_source_water += 1
        # 采暖水泵计算
        if self.wp_heating_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算采暖水泵额定值
            heating_water_flow_rated = self.heating_water_flow_rated()
            wp_frequency_start_heating_water = (heating_water_flow / heating_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_heating_water = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_start_heating_water)[0]
            # 采暖水泵扬程最小值需求量
            heating_water_pump_head_min = self.centrifugal_heat_pump_heating_water_pump_head_min(heating_water_flow)
            if wp_pump_head_start_heating_water >= heating_water_pump_head_min:
                wp_frequency_heating_water = wp_frequency_start_heating_water
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
            else:
                # 初始值
                wp_frequency_heating_water = wp_frequency_start_heating_water
                # 计算当前频率、流量情况下水泵功率
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                while wp_frequency_heating_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    heating_water_flow = (wp_frequency_heating_water / 50) * heating_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[0]
                    if wp_pump_head_b >= heating_water_pump_head_min:
                        heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                        break
                    else:
                        wp_frequency_heating_water += 1

        # 返回总辅助设备耗电功率，某一负荷率下
        return heat_source_water_pump_power + heating_water_pump_power

    def centrifugal_heat_pump_power_consumption(self, load_ratio, centrifugal_heat_pump_cop):
        """离心式热泵机组本身耗电功率，某一负荷率下"""
        return load_ratio * self.heating_power_rated / centrifugal_heat_pump_cop


class Air_Source_Heat_Pump_Cold():
    """类：空气源热泵制冷工况；风冷螺杆式热泵的制冷工况同样适用"""

    def __init__(self, cooling_power_rated, load_min, frequency_scaling, wp_chilled_water, gc):
        """类的初始化"""
        # 制冷功率出力，额定值
        self.cooling_power_rated = cooling_power_rated
        # 空气源热泵制冷最低运行负荷率
        self.load_min = load_min
        # 空气源热泵制冷是否变频
        self.frequency_scaling = frequency_scaling
        # 空气源热泵制冷采用的冷冻水泵
        self.wp_chilled_water = wp_chilled_water
        # 空气源热泵制冷额定冷冻水供回水温差
        self.chilled_water_temperature_difference_rated = gc.chilled_water_temperature_difference_rated
        # 空气源热泵制冷COP神经网络模型
        # self.model_centrifugal_chiller_cop_1 = gc.model_centrifugal_chiller_cop_1  # 离心式冷水机负荷率范围：50%~100%
        # self.model_centrifugal_chiller_cop_2 = gc.model_centrifugal_chiller_cop_2  # 离心式冷水机负荷率范围：10%~50%

    def chilled_water_flow_rated(self):
        # 如果冷冻水泵定频，始终等于最大流量
        chilled_water_flow_rated = self.cooling_power_rated * 3600 / 1000 / 4.2 / self.chilled_water_temperature_difference_rated
        return chilled_water_flow_rated

    def chilled_water_flow(self, load_ratio):
        """冷冻水流量，某一负荷率下"""
        # 如果冷冻水泵为变频
        if self.wp_chilled_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化
            if load_ratio >= 0.4:
                ans = load_ratio * self.chilled_water_flow_rated()
            else:
                # 如果负荷率小于40%，则等于32%的流量，不再减少
                ans = 0.32 * self.chilled_water_flow_rated()
        else:
            # 如果冷冻水泵定频，始终等于最大流量
            ans= self.chilled_water_flow_rated()
        #返回结果
        return ans

    def air_source_heat_pump_cold_cop(self, load_ratio, chilled_water_temperature, environment_temperature):
        cop = 3.32
        # 返回结果
        return cop

    def air_source_heat_pump_cold_chilled_water_pump_head_min(self, chilled_water_flow):
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, chilled_water_flow):
        """辅助设备耗电功率计算"""
        # 冷冻水泵计算
        if self.wp_chilled_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算冷冻水泵额定值
            chilled_water_flow_rated = self.chilled_water_flow_rated()
            wp_frequency_start_chilled_water = (chilled_water_flow / chilled_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_chilled_water = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_start_chilled_water)[0]
            # 冷冻水泵扬程最小值需求量
            chilled_water_pump_head_min = self.air_source_heat_pump_cold_chilled_water_pump_head_min(chilled_water_flow)
            if wp_pump_head_start_chilled_water >= chilled_water_pump_head_min:
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
            else:
                # 初始值
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                while wp_frequency_chilled_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    chilled_water_flow = (wp_frequency_chilled_water / 50) * chilled_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[0]
                    if wp_pump_head_b >= chilled_water_pump_head_min:
                        chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                        break
                    else:
                        wp_frequency_chilled_water += 1
        # 冷却风机耗电功率，某一负荷率下，风机为定频，功率保持不变
        cooling_fan_power = 20
        # 返回总辅助设备耗电功率，某一负荷率下
        return chilled_water_pump_power + cooling_fan_power

    def air_source_heat_pump_cold_power_consumption(self, load_ratio, air_source_heat_pump_cold_cop):
        """空气源热泵制冷工况本身耗电功率，某一负荷率下"""
        return load_ratio * self.cooling_power_rated/ air_source_heat_pump_cold_cop

class Air_Source_Heat_Pump_Heat():
    """类：空气源热泵制热工况；风冷螺杆式热泵的制热工况同样适用"""

    def __init__(self, heating_power_rated, load_min, frequency_scaling, wp_heating_water, gc):
        """类的初始化"""
        # 制热功率出力，额定值
        self.heating_power_rated = heating_power_rated
        # 空气源热泵机组制热最低运行负荷率
        self.load_min = load_min
        # 空气源热泵机组制热是否变频
        self.frequency_scaling = frequency_scaling
        # 空气源热泵机组制热采用的采暖水泵
        self.wp_heating_water = wp_heating_water
        # 空气源热泵机组制热额定采暖水供回水温差
        self.heating_water_temperature_difference_rated = gc.heating_water_temperature_difference_rated
        # 离心式热泵机组制热COP神经网络模型
        # self.model_centrifugal_heat_pump_cop_1 = gc.model_centrifugal_heat_pump_cop_cop_1  # 离心式热泵机组负荷率范围：50%~100%
        # self.model_centrifugal_heat_pump_cop_2 = gc.model_centrifugal_heat_pump_cop_cop_2  # 离心式热泵机组负荷率范围：10%~50%

    def heating_water_flow_rated(self):
        # 如果采暖水泵定频，始终等于最大流量
        heating_water_flow_rated = self.heating_power_rated * 3600 / 1000 / 4.2 / self.heating_water_temperature_difference_rated
        return heating_water_flow_rated

    def heating_water_flow(self, load_ratio):
        """采暖水流量，某一负荷率情况下"""
        # 如果采暖水泵为变频
        if self.wp_heating_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化，采暖水流量随负荷率变化
            if load_ratio >= 0.4:
                ans = self.heating_water_flow_rated() * load_ratio
            else:
                # 如果负荷率小于40%，则等于35%的流量，不再减少
                ans = self.heating_water_flow_rated() * 0.35
        else:
            # 如果采暖水泵定频，始终等于额定流量
            ans = self.heating_water_flow_rated()
            # 返回结果
        return ans

    def air_source_heat_pump_heat_cop(self, load_ratio, heating_water_temperature, environment_temperature):
        # 空气源热泵机组制热COP
        cop = 3.3
        return cop

    def air_source_heat_pump_heat_heating_water_pump_head_min(self, heating_water_flow):
        # 空气源热泵机组制热采暖水泵最低扬程需求量计算（仅针对变频水泵的计算）
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, heating_water_flow):
        """辅助设备耗电功率计算"""
        # 采暖水泵计算
        if self.wp_heating_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算采暖水泵额定值
            heating_water_flow_rated = self.heating_water_flow_rated()
            wp_frequency_start_heating_water = (heating_water_flow / heating_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_heating_water = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_start_heating_water)[0]
            # 采暖水泵扬程最小值需求量
            heating_water_pump_head_min = self.air_source_heat_pump_heat_heating_water_pump_head_min(heating_water_flow)
            if wp_pump_head_start_heating_water >= heating_water_pump_head_min:
                wp_frequency_heating_water = wp_frequency_start_heating_water
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
            else:
                # 初始值
                wp_frequency_heating_water = wp_frequency_start_heating_water
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                while wp_frequency_heating_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    heating_water_flow = (wp_frequency_heating_water / 50) * heating_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[0]
                    if wp_pump_head_b >= heating_water_pump_head_min:
                        heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                        break
                    else:
                        wp_frequency_heating_water += 1
        # 风机耗电功率，某一负荷率下，风机为定频，功率保持不变
        heating_fan_power = 20

        # 返回总辅助设备耗电功率，某一负荷率下
        return heating_water_pump_power + heating_fan_power

    def air_source_heat_pump_heat_power_consumption(self, load_ratio, air_source_heat_pump_heat_cop):
        """空气源热泵机组制热本身耗电功率，某一负荷率下"""
        return load_ratio * self.heating_power_rated / air_source_heat_pump_heat_cop


class Natural_Gas_Boiler_heat():
    """类：天然气锅炉，供采暖负荷"""

    def __init__(self, heating_power_rated, load_min, wp_heating_water, gc):
        """类的初始化"""
        # 制热功率出力，最大值
        self.heating_power_rated = heating_power_rated
        # 锅炉最低运行负荷率
        self.load_min = load_min
        # 天然气锅炉采用的采暖水泵
        self.wp_heating_water = wp_heating_water
        # 采暖水供回水额定温差
        self.heating_water_temperature_difference_rated = gc.heating_water_temperature_difference_rated
        # 天然气热值
        self.natural_gas_calorific_value = gc.natural_gas_calorific_value

    def heating_water_temperature_difference(self, load_ratio):
        """采暖水供回水温差"""
        # 如果采暖水泵是变频水泵
        if self.wp_heating_water.frequency_scaling == True:
            # 热水流量比例下限
            heating_water_flow_min = 0.5
            # 负荷率大于等于50%，温差不变
            if load_ratio >= 0.5:
                ans = self.heating_water_temperature_difference_rated
            # 负荷率低于50%，温差下降
            else:
                if load_ratio > 0:
                    ans = load_ratio * self.heating_water_temperature_difference_rated / heating_water_flow_min
                else:
                    ans = self.heating_water_temperature_difference_rated
        # 如果采暖水泵是定频水泵，则温差随负荷率变化
        else:
            if load_ratio > 0:
                ans = load_ratio * self.heating_water_temperature_difference_rated
            else:
                ans = self.heating_water_temperature_difference_rated
        return ans

    def heating_water_flow_rated(self):
        # 天然气热水锅炉采暖水额定流量
        ans = self.heating_power_rated * 3600 / 1000 / 4.2 / self.heating_water_temperature_difference_rated
        return ans

    def heating_water_flow(self, load_ratio, heating_water_temperature_difference):
        # 采暖水流量，某一负荷率下
        return load_ratio * self.heating_power_rated * 3600 / 1000 / 4.2 / heating_water_temperature_difference

    def boiler_efficiency(self, load_ratio):
        # 如果锅炉负荷率大于等于35%
        if load_ratio >= 0.35:
            eff = -0.3686 * math.pow(load_ratio, 4) + 0.7877 * math.pow(load_ratio, 3) - 0.6808 * math.pow(load_ratio, 2) + 0.251 * load_ratio + 0.9474
        else:
            eff = - 0.1333 * math.pow(load_ratio, 3) - 4.56 * math.pow(load_ratio, 2) + 3.0723 * load_ratio + 0.469
        return eff

    def natural_gas_boiler_heating_water_pump_head_min(self, heating_water_flow):
        # 天然气热水锅炉采暖水泵最低扬程需求量计算（仅针对变频水泵的计算）
        # 针对单台采暖水泵进行计算，变频泵在不同的流量比例（当前流量与最大流量比例）情况下，的最低要成需求，从而反算出可以运行的最低频率
        # heating_water_flow_rated = self.heating_water_flow_rated()
        # heating_water_flow_proportion = heating_water_flow / heating_water_flow_rated  # 天然气热水锅炉采暖水比例
        # 缺少数据，暂时采用与离心式冷水机组一样的扬程性能曲线
        # water_pump_head_min = 1.835 * (15.076 * math.pow(heating_water_flow_proportion, 2) - 0.0258 * heating_water_flow_proportion + 2.57)
        # 模型不全，采用定值
        water_pump_head_min = 5
        # 返回计算结果
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, heating_water_flow):
        """辅助设备耗电功率计算"""
        # 采暖水泵耗电功率，某一负荷率下
        if self.wp_heating_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远保持50Hz（定频水泵的扬程都是满足要求的，不再计算扬程）
            heating_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算采暖水流量额定值
            heating_water_flow_rated = self.heating_water_flow_rated()
            wp_frequency_start_heating_water = (heating_water_flow / heating_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_heating_water = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_start_heating_water)[0]
            # 采暖水泵扬程在当前流量下最低需求值
            heating_water_pump_head_min = self.natural_gas_boiler_heating_water_pump_head_min(heating_water_flow)
            if wp_pump_head_start_heating_water >= heating_water_pump_head_min:
                wp_frequency_heating_water = wp_frequency_start_heating_water
                # 计算当前频率、流量情况下水泵功率
                heating_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
            else:
                # 初始值
                wp_frequency_heating_water = wp_frequency_start_heating_water
                # 计算当前频率、流量情况下水泵功率
                heating_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                while wp_frequency_heating_water <= 50:  # 最大50Hz
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    heating_water_flow = (wp_frequency_heating_water / 50) * heating_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_a = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[0]
                    if wp_pump_head_a >= heating_water_pump_head_min:
                        # 计算当前频率、流量情况下水泵功率
                        heating_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                        break
                    else:
                        wp_frequency_heating_water += 1

        # 返回总辅助设备耗电功率，某一负荷率下,两个12分别3500kW锅炉为燃气设备和风机耗电（均为定频）
        return (12 + 12) + heating_pump_power

    def natural_gas_consumption(self, load_ratio, boiler_efficiency):
        """锅炉设备天然气消耗量，某一负荷率下"""
        heating_power = load_ratio * self.heating_power_rated
        # 计算结果为m3/h
        return heating_power * 3600 / self.natural_gas_calorific_value / boiler_efficiency


class Natural_Gas_Boiler_hot_water():
    """类：天然气锅炉，供生活热水负荷"""

    def __init__(self, heating_power_rated, load_min, wp_hot_water, gc):
        """类的初始化"""
        # 制热功率（生活热水）出力，最大值
        self.heating_power_rated = heating_power_rated
        # 锅炉最低运行负荷率
        self.load_min = load_min
        # 天然气锅炉采用的生活热水水泵
        self.wp_hot_water = wp_hot_water
        # 生活热水供回水额定温差
        self.hot_water_temperature_difference_rated = gc.hot_water_temperature_difference_rated
        # 天然气热值
        self.natural_gas_calorific_value = gc.natural_gas_calorific_value

    def hot_water_flow_rated(self):
        # 天然气热水锅炉采暖水额定流量
        ans = self.heating_power_rated * 3600 / 1000 / 4.2 / self.hot_water_temperature_difference_rated
        return ans

    def hot_water_flow(self):
        # 生活热水流量，定频水泵，在不同负荷率下，流量不变
        return self.heating_power_rated * 3600 / 1000 / 4.2 / self.hot_water_temperature_difference_rated

    def boiler_efficiency(self, load_ratio):
        # 如果锅炉负荷率大于等于35%
        if load_ratio >= 0.35:
            eff = -0.3686 * math.pow(load_ratio, 4) + 0.7877 * math.pow(load_ratio, 3) - 0.6808 * math.pow(load_ratio, 2) + 0.251 * load_ratio + 0.9474
        else:
            eff = - 0.1333 * math.pow(load_ratio, 3) - 4.56 * math.pow(load_ratio, 2) + 3.0723 * load_ratio + 0.469
        return eff

    def auxiliary_equipment_power_consumption(self, hot_water_flow):
        """辅助设备耗电功率计算"""
        # 采暖水泵耗电功率，某一负荷率下
        heating_pump_power = self.wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
        # 返回总辅助设备耗电功率，某一负荷率下,两个12分别3500kW锅炉为燃气设备和风机耗电（均为定频）
        return (12 + 12) + heating_pump_power

    def natural_gas_consumption(self, load_ratio, boiler_efficiency):
        """锅炉设备天然气消耗量，某一负荷率下"""
        heating_power = load_ratio * self.heating_power_rated
        # 计算结果为m3/h
        return heating_power * 3600 / self.natural_gas_calorific_value / boiler_efficiency


class Internal_Combustion_Engine():
    """类：内燃发电机"""

    def __init__(self, electricity_power_rated, gc, load_min):
        """类的初始化"""
        # 发电功率，额定值
        self.electricity_power_rated = electricity_power_rated
        self.natural_gas_calorific_value = gc.natural_gas_calorific_value
        # 内燃机最低运行负荷率
        self.load_min = load_min

    def electricity_power_efficiency(self, load_ratio):
        # 内燃机发电效率
        electricity_power_eff = -0.104 * math.pow(load_ratio, 2) + 0.226 * load_ratio + 0.293
        return electricity_power_eff

    def total_heat_input(self, load_ratio, electricity_power_efficiency):
        # 内燃机热量总输入功率，某一负荷率下
        return load_ratio * self.electricity_power_rated / electricity_power_efficiency

    def residual_heat_efficiency(self, load_ratio):
        # 内燃机余热利用效率
        residual_heat_efficiency = 0.04 * math.pow(load_ratio, 2) - 0.118 * load_ratio + 0.542
        return residual_heat_efficiency

    def residual_heat_power(self, total_heat_input, residual_heat_efficiency):
        # 内燃机余热利用功率，某一负荷率下
        return total_heat_input * residual_heat_efficiency

    def natural_gas_consumption(self, total_heat_input):
        # 内燃机天然气消耗量，某一负荷率下，单位m3/h
        return total_heat_input * 3600 / self.natural_gas_calorific_value

    def auxiliary_equipment_power_consumption(self, load_ratio):
        # 内燃机辅助设备耗电功率，均为定频泵和风机，功率不变
        return 4 + 1.5 + 28.5 + 7.5 + 2.5 * 2


class Lithium_Bromide_Cold():
    """类：溴化锂，制冷季"""

    def __init__(self, residual_heat_power, wp_chilled_water, wp_cooling_water, wp_hot_water, gc):
        """类的初始化"""
        # 余热利用功率，某一负荷率下，从内燃机类中导入
        self.residual_heat_power = residual_heat_power
        # 溴化锂采用的冷冻水泵
        self.wp_chilled_water = wp_chilled_water
        # 溴化锂采用的生活热水水泵
        self.wp_hot_water = wp_hot_water
        # 溴化锂采用的冷却水泵
        self.wp_cooling_water = wp_cooling_water
        # 冷却水供回水额定温差
        self.cooling_water_temperature_difference_rated = gc.cooling_water_temperature_difference_rated
        # 冷冻水供回水额定温差
        self.chilled_water_temperature_difference_rated = gc.chilled_water_temperature_difference_rated
        # 生活热水供回水额定温差
        self.hot_water_temperature_difference_rated = gc.hot_water_temperature_difference_rated

    def cooling_cop(self, load_ratio):
        # 溴化锂制冷COP
        # 冷COP随设备负荷率的变化情况
        cooling_cop = 0.08 * math.pow(load_ratio, 2) - 0.32 * load_ratio + 1.29
        return cooling_cop

    def heating_cop(self, load_ratio):
        # 溴化锂制热COP
        # 热COP随设备负荷率的变化情况
        heating_cop = 0.016 * math.pow(load_ratio, 2) - 0.044 * load_ratio + 0.988
        return heating_cop

    def hot_water_residual_heat_consumption(self, hot_water_load, heating_cop):
        # 溴化锂生活热水消耗的内燃机余热量计算
        return hot_water_load / heating_cop

    def cooling_power(self, cooling_cop, hot_water_residual_heat_consumption):
        # 溴化锂制冷出力，某一负荷率下
        return (self.residual_heat_power - hot_water_residual_heat_consumption) * cooling_cop

    def chilled_water_temperature_difference(self, load_ratio):
        """冷冻水供回水温差"""
        # 冷冻水泵为变频
        if self.wp_chilled_water.frequency_scaling == True:
            # 溴化锂冷冻水变频泵，温差始终等于额定值
            ans = self.chilled_water_temperature_difference_rated
        # 冷冻水泵为定频，温差随负荷率变化
        else:
            # 冷冻水流量不变，但温差变
            ans = (0.32 * math.pow(load_ratio, 2) - 0.08 * load_ratio + 0.76)* self.chilled_water_temperature_difference_rated
        # 返回结果
        return ans

    def cooling_water_temperature_difference(self, load_ratio):
        """冷却水供回水温差"""
        # 冷却水泵为变频
        if self.wp_cooling_water == True:
            # 溴化锂冷却水变频泵，温差始终等于额定值
            ans = self.cooling_water_temperature_difference_rated
        # 冷却水泵为定频，温差随负荷率变化
        else:
            # 冷却水流量不变，但温差变
            ans = (0.544 * math.pow(load_ratio, 2) - 0.312 * load_ratio + 0.768) * self.cooling_water_temperature_difference_rated
        # 返回结果
        return ans

    def hot_water_temperature_difference(self, load_ratio):
        """生活热水供回水温差"""
        # 生活热水泵为变频
        if self.wp_hot_water == True:
            # 溴化锂生活热水变频泵，温差始终等于额定值
            ans = self.hot_water_temperature_difference_rated
        # 生活热水泵为定频，温差随负荷率变化
        else:
            # 生活热水流量不变，但温差变，目前采用与采暖一样的模型曲线
            ans = (0.8 * math.pow(load_ratio, 2) - 0.6 * load_ratio + 0.8) * self.hot_water_temperature_difference_rated
        # 返回结果
        return ans

    def cooling_water_flow(self, load_ratio, residual_heat_cooling_ratio):
        """冷却水流量，某一负荷率下"""
        # 冷却水额定流量
        cooling_water_flow_rated = 305 * residual_heat_cooling_ratio
        # 如果冷却水泵为变频
        if self.wp_cooling_water.frequency_scaling == True:
            # 溴化锂冷冻水变频泵最低负荷60%，流量按下列规律变化
            ans = cooling_water_flow_rated * (0.7082 * math.pow(load_ratio, 2) - 0.5574 * load_ratio + 0.8492)
        else:
            # 如果冷却水泵定频，始终等于额定流量
            ans = cooling_water_flow_rated
        # 返回结果
        return ans

    def chilled_water_flow(self, load_ratio, residual_heat_cooling_ratio):
        """冷冻水流量，某一负荷率下"""
        # 冷冻水流量额定值，根据余热中用于制冷的比例进行折算
        chilled_water_flow_rated = 155 * residual_heat_cooling_ratio
        # 如果冷冻水泵为变频
        if self.wp_chilled_water.frequency_scaling == True:
            # 溴化锂冷冻水泵为变频泵，流量按下列规律变化
            ans = chilled_water_flow_rated*(0.4129 * math.pow(load_ratio, 2) - 0.2323 * load_ratio + 0.8194)
        else:
            # 如果冷冻水泵定频，始终等于额定流量
            ans = chilled_water_flow_rated
        # 返回结果
        return ans

    def hot_water_flow(self, hot_water_load, hot_water_temperature_difference):
        # 生活热水流量计算
        return hot_water_load * 3600 / 1000 / 4.2 / hot_water_temperature_difference

    def auxiliary_equipment_power_consumption_cooling(self, cooling_water_flow, chilled_water_flow):
        """溴化锂设备制冷时辅助设备耗电"""
        # 溴化锂制冷辅助设备耗电功率，某一负荷率下
        # 冷却水泵耗电功率，某一负荷率下
        cooling_pump_power = self.wp_cooling_water.pump_performance_data(cooling_water_flow, 50)[1]
        # 冷冻水泵耗电功率，某一负荷率下
        chilled_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, 50)[1]
        # 冷却塔风机耗电功率，某一负荷率下，风机为定频，功率保持不变
        cooling_tower_fan_power = 12
        # 返回总辅助设备耗电功率，某一负荷率下
        return cooling_pump_power + chilled_pump_power + cooling_tower_fan_power

    def auxiliary_equipment_power_consumption_hot_water(self, hot_water_flow):
        """计算生活热水辅机设备耗电量"""
        # 冷却水泵耗电功率，某一负荷率下
        hot_water_pump_power = self.wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
        # 返回总辅助设备耗电功率，某一负荷率下
        return hot_water_pump_power


class Lithium_Bromide_Heat():
    """类：溴化锂，制热季"""

    def __init__(self, residual_heat_power, wp_heating_water, wp_hot_water, gc):
        """类的初始化"""
        # 余热利用功率，某一负荷率下，从内燃机类中导入
        self.residual_heat_power = residual_heat_power
        # 溴化锂采用的采暖水泵
        self.wp_heating_water = wp_heating_water
        # 溴化锂采用的生活热水水泵
        self.wp_hot_water = wp_hot_water
        # 采暖水供回水额定温差
        self.heating_water_temperature_difference_rated = gc.heating_water_temperature_difference_rated
        # 生活热水供回水额定温差
        self.hot_water_temperature_difference_rated = gc.hot_water_temperature_difference_rated

    def heating_cop(self, load_ratio):
        # 溴化锂制热COP
        # 热COP随设备负荷率的变化情况
        heating_cop = 0.016 * math.pow(load_ratio, 2) - 0.044 * load_ratio + 0.988
        return heating_cop

    def hot_water_residual_heat_consumption(self, hot_water_load, heating_cop):
        # 溴化锂生活热水消耗的内燃机余热量计算
        return hot_water_load / heating_cop

    def heating_power(self, heating_cop, hot_water_residual_heat_consumption):
        # 溴化锂制热出力，某一负荷率下
        return (self.residual_heat_power - hot_water_residual_heat_consumption) * heating_cop

    def heating_water_temperature_difference(self, load_ratio):
        """采暖水供回水温差"""
        # 采暖水泵为变频
        if self.wp_heating_water == True:
            # 溴化锂采暖水变频泵，温差始终等于额定值
            ans = self.heating_water_temperature_difference_rated
        # 采暖水泵为定频，温差随负荷率变化
        else:
            # 采暖水流量不变，但温差变
            ans = (0.8 * math.pow(load_ratio, 2) - 0.6 * load_ratio + 0.8) * self.heating_water_temperature_difference_rated
        # 返回结果
        return ans

    def hot_water_temperature_difference(self, load_ratio):
        """生活热水供回水温差"""
        # 生活热水泵为变频
        if self.wp_hot_water == True:
            # 溴化锂生活热水变频泵，温差始终等于额定值
            ans = self.hot_water_temperature_difference_rated
        # 生活热水泵为定频，温差随负荷率变化
        else:
            # 生活热水流量不变，但温差变，目前采用与采暖一样的模型曲线
            ans = (0.8 * math.pow(load_ratio, 2) - 0.6 * load_ratio + 0.8) * self.hot_water_temperature_difference_rated
        # 返回结果
        return ans

    def heating_water_flow(self, load_ratio, residual_heat_heating_ratio):
        """采暖水流量，某一负荷率下"""
        # 采暖水额定流量
        heating_water_flow_rated = 73 * residual_heat_heating_ratio
        # 如果采暖水泵为变频
        if self.wp_heating_water.frequency_scaling == True:
            # 溴化锂采暖水泵为变频，流量按下列规律变化
            ans = heating_water_flow_rated * (0.8767 * math.pow(load_ratio, 2) - 0.7123 * load_ratio + 0.8356)
        else:
            # 如果采暖水泵定频，始终等于额定流量
            ans = heating_water_flow_rated
        # 返回结果
        return ans

    def hot_water_flow(self, hot_water_load, hot_water_temperature_difference):
        # 生活热水流量计算
        return hot_water_load * 3600 / 1000 / 4.2 / hot_water_temperature_difference

    def auxiliary_equipment_power_consumption_heating(self, heating_water_flow):
        # 溴化锂制热辅助设备耗电功率，某一负荷率下
        # 冷却水泵耗电功率，某一负荷率下
        heating_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, 50)[1]
        # 返回总辅助设备耗电功率，某一负荷率下
        return heating_pump_power

    def auxiliary_equipment_power_consumption_hot_water(self, hot_water_flow):
        """计算生活热水辅机设备耗电量"""
        # 冷却水泵耗电功率，某一负荷率下
        hot_water_pump_power = self.wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
        # 返回总辅助设备耗电功率，某一负荷率下
        return hot_water_pump_power


class Lithium_Bromide_Transition():
    """类：溴化锂，过渡季"""

    def __init__(self, residual_heat_power, wp_hot_water, gc):
        """类的初始化"""
        # 余热利用功率，某一负荷率下，从内燃机类中导入
        self.residual_heat_power = residual_heat_power
        # 溴化锂采用的生活热水水泵
        self.wp_hot_water = wp_hot_water
        # 生活热水供回水额定温差
        self.hot_water_temperature_difference_rated = gc.hot_water_temperature_difference_rated

    def heating_cop(self, load_ratio):
        # 溴化锂制热COP
        # 热COP随设备负荷率的变化情况
        heating_cop = 0.016 * math.pow(load_ratio, 2) - 0.044 * load_ratio + 0.988
        return heating_cop

    def hot_water_residual_heat_consumption(self, hot_water_load, heating_cop):
        # 溴化锂生活热水消耗的内燃机余热量计算
        return hot_water_load / heating_cop

    def residual_heat_remaining(self, hot_water_residual_heat_consumption):
        # 溴化锂制生活热水后，还没有用完的余热量
        return self.residual_heat_power - hot_water_residual_heat_consumption

    def hot_water_temperature_difference(self, load_ratio):
        """生活热水供回水温差"""
        # 生活热水泵为变频
        if self.wp_hot_water == True:
            # 溴化锂生活热水变频泵，温差始终等于额定值
            ans = self.hot_water_temperature_difference_rated
        # 生活热水泵为定频，温差随负荷率变化
        else:
            # 生活热水流量不变，但温差变，目前采用与采暖一样的模型曲线
            ans = (0.8 * math.pow(load_ratio, 2) - 0.6 * load_ratio + 0.8) * self.hot_water_temperature_difference_rated
        # 返回结果
        return ans

    def hot_water_flow(self, hot_water_load, hot_water_temperature_difference):
        # 生活热水流量计算
        return hot_water_load * 3600 / 1000 / 4.2 / hot_water_temperature_difference

    def auxiliary_equipment_power_consumption_hot_water(self, hot_water_flow):
        """计算生活热水辅机设备耗电量"""
        # 冷却水泵耗电功率，某一负荷率下
        hot_water_pump_power = self.wp_hot_water.pump_performance_data(hot_water_flow, 50)[1]
        # 返回总辅助设备耗电功率，某一负荷率下
        return hot_water_pump_power


class Energy_Storage_Equipment_Cold():
    """类：蓄能装置的制冷工况，适用于蓄能水罐和冰蓄冷装置"""

    def __init__(self, cooling_power_rated, load_min, cooling_storage_rated, wp_chilled_water, gc):
        """类的初始化"""
        # 制冷功率出力，额定值（单位kW)
        self.cooling_power_rated = cooling_power_rated
        # 蓄能装置制冷最低运行负荷率
        self.load_min = load_min
        # 蓄能装置的蓄冷量，额定值（单位是kWh）
        self.cooling_storage_rated = cooling_storage_rated
        # 蓄能装置采用的冷冻水泵
        self.wp_chilled_water = wp_chilled_water
        # 蓄能装置制冷蓄冷额定冷冻水供回水温差
        self.cooling_storage_water_temperature_difference_rated = gc.cooling_storage_water_temperature_difference_rated

    def chilled_water_flow_rated(self):
        # 如果冷冻水泵定频，始终等于最大流量
        chilled_water_flow_rated = self.cooling_power_rated * 3600 / 1000 / 4.2 / self.cooling_storage_water_temperature_difference_rated
        return chilled_water_flow_rated

    def chilled_water_flow(self, load_ratio):
        """冷冻水流量，某一负荷率下"""
        # 如果冷冻水泵为变频
        if self.wp_chilled_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化
            if load_ratio >= 0.4:
                ans = load_ratio * self.chilled_water_flow_rated()
            else:
                # 如果负荷率小于40%，则等于32%的流量，不再减少
                ans = 0.32 * self.chilled_water_flow_rated()
        else:
            # 如果冷冻水泵定频，始终等于最大流量
            ans= self.chilled_water_flow_rated()
        #返回结果
        return ans

    def cooling_storage_residual(self, cooling_consume_sum):
        # 蓄能水罐目前剩余的蓄冷量，输入的变量为冷负荷消耗量（单位小时内的功率值），供冷工况为正值，蓄冷工况为负值，输入的均为累计值
        return self.cooling_storage_rated - cooling_consume_sum

    def energy_storage_equipment_cold_chilled_water_pump_head_min(self, chilled_water_flow):
        water_pump_head_min = 5
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, chilled_water_flow):
        """辅助设备耗电功率计算"""
        # 冷冻水泵计算
        if self.wp_chilled_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算冷冻水泵额定值
            chilled_water_flow_rated = self.chilled_water_flow_rated()
            wp_frequency_start_chilled_water = (chilled_water_flow / chilled_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_chilled_water = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_start_chilled_water)[0]
            # 冷冻水泵扬程最小值需求量
            chilled_water_pump_head_min = self.energy_storage_equipment_cold_chilled_water_pump_head_min(chilled_water_flow)
            if wp_pump_head_start_chilled_water >= chilled_water_pump_head_min:
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
            else:
                # 初始值
                wp_frequency_chilled_water = wp_frequency_start_chilled_water
                chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                while wp_frequency_chilled_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    chilled_water_flow = (wp_frequency_chilled_water / 50) * chilled_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[0]
                    if wp_pump_head_b >= chilled_water_pump_head_min:
                        chilled_water_pump_power = self.wp_chilled_water.pump_performance_data(chilled_water_flow, wp_frequency_chilled_water)[1]
                        break
                    else:
                        wp_frequency_chilled_water += 1

        # 返回总辅助设备耗电功率，某一负荷率下
        return chilled_water_pump_power


class Energy_Storage_Equipment_Heat():
    """类：蓄能装置的制热工况"""

    def __init__(self, heating_power_rated, load_min, heating_storage_rated, wp_heating_water, gc):
        """类的初始化"""
        # 制热功率出力，额定值
        self.heating_power_rated = heating_power_rated
        # 蓄能装置制热最低运行负荷率
        self.load_min = load_min
        # 蓄能装置的蓄热量，额定值（单位是kWh）
        self.heating_storage_rated = heating_storage_rated
        # 蓄能装置采用的采暖水泵
        self.wp_heating_water = wp_heating_water
        # 蓄能装置制热蓄热额定采暖水供回水温差
        self.heating_storage_water_temperature_difference_rated = gc.heating_storage_water_temperature_difference_rated

    def heating_water_flow_rated(self):
        # 如果采暖水泵定频，始终等于最大流量
        heating_water_flow_rated = self.heating_power_rated * 3600 / 1000 / 4.2 / self.heating_storage_water_temperature_difference_rated
        return heating_water_flow_rated

    def heating_water_flow(self, load_ratio):
        """采暖水流量，某一负荷率下"""
        # 如果采暖水泵为变频
        if self.wp_heating_water.frequency_scaling == True:
            # 如果负荷率大于等于40%，则随负荷率均匀变化
            if load_ratio >= 0.4:
                ans = load_ratio * self.heating_water_flow_rated()
            else:
                # 如果负荷率小于40%，则等于32%的流量，不再减少
                ans = 0.32 * self.heating_water_flow_rated()
        else:
            # 如果冷冻水泵定频，始终等于最大流量
            ans= self.heating_water_flow_rated()
        #返回结果
        return ans

    def heating_storage_residual(self, heating_consume_sum):
        # 蓄能水罐目前剩余的蓄热量，输入的变量为热负荷消耗量（单位小时内的功率值），供热工况为正值，蓄热工况为负值，输入的均为累计值
        return self.heating_storage_rated - heating_consume_sum

    def energy_storage_equipment_heat_heating_water_pump_head_min(self, heating_water_flow):
        water_pump_head_min = 5
        return water_pump_head_min

    def auxiliary_equipment_power_consumption(self, heating_water_flow):
        """辅助设备耗电功率计算"""
        # 采暖水泵计算
        if self.wp_heating_water.frequency_scaling == False:
            # 如果是定频水泵，频率永远50Hz，（定频水泵的扬程都是满足要求的，不再计算扬程）
            heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, 50)[1]
        else:
            # 如果是变频水泵，频率变化，寻找满足要求最小需求时的频率
            # 计算采暖水泵额定值
            heating_water_flow_rated = self.heating_water_flow_rated()
            wp_frequency_start_heating_water = (heating_water_flow / heating_water_flow_rated) * 50  # 从这个点开始寻找频率合适的值
            # 计算当前流量下，变频水泵的扬程
            wp_pump_head_start_heating_water = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_start_heating_water)[0]
            # 采暖水泵扬程最小值需求量
            heating_water_pump_head_min = self.energy_storage_equipment_heat_heating_water_pump_head_min(heating_water_flow)
            if wp_pump_head_start_heating_water >= heating_water_pump_head_min:
                wp_frequency_heating_water = wp_frequency_start_heating_water
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
            else:
                # 初始值
                wp_frequency_heating_water = wp_frequency_start_heating_water
                heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                while wp_frequency_heating_water <= 50:
                    # 频率改变后，流量也会改变（流量与频率成正比）
                    heating_water_flow = (wp_frequency_heating_water / 50) * heating_water_flow_rated
                    # 重新计算此时的扬程
                    wp_pump_head_b = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[0]
                    if wp_pump_head_b >= heating_water_pump_head_min:
                        heating_water_pump_power = self.wp_heating_water.pump_performance_data(heating_water_flow, wp_frequency_heating_water)[1]
                        break
                    else:
                        wp_frequency_heating_water += 1

        # 返回总辅助设备耗电功率，某一负荷率下
        return heating_water_pump_power


class Water_Pump():
    """类：各种水泵"""

    def __init__(self, water_flow_rated, frequency_scaling, pump_head_rated, gc):
        # 水泵额定流量
        self.water_flow_rated = water_flow_rated
        # 水泵额定扬程
        self.pump_head_rated = pump_head_rated
        # 额定功率(理论计算结果，效率按照0.8考虑)
        self.power_consumption_rated = 2.73 * self.water_flow_rated * self.pump_head_rated / 0.8 / 1000
        # 水泵是否变频
        self.frequency_scaling = frequency_scaling
        # 水泵神经网络模型
        self.model_wp_710t = gc.model_wp_710t
        self.model_wp_600t = gc.model_wp_600t
        self.model_wp_340t = gc.model_wp_340t

    def pump_performance_data(self, water_flow, frequency):
        """各种泵的性能数据计算：扬程、耗电功率"""
        # 清空已有的tf模型
        tf.keras.backend.clear_session()
        # 从训练好的神经网络中计算水泵的的耗电功率

        if self.water_flow_rated == 710:
            """710t/h水泵"""
            # 直接使用训练好的神经网络参数进行矩阵运算
            # 输入
            x1 = (frequency - 5) / (50 - 5)
            x2 = (water_flow - 50) / (800 - 50)
            X_1 = np.array([x1, x2], dtype='float32')
            X = np.mat(X_1)
            # 加载训练好的神经网络模型（离心式冷水机冷却水泵）
            ans = self.model_wp_710t.predict(X)
            # 计算预测结果
            pump_head = ans[0][0] * (34.98-0.28) + 0.28
            power_consumption = ans[0][1] * (77.65 - 0.0603) + 0.0603

        elif self.water_flow_rated == 600:
            """600t/h水泵"""

            # 直接使用训练好的神经网络参数进行矩阵运算
            # 输入
            x1 = (frequency - 5) / (50 - 5)
            x2 = (water_flow - 40) / (650 - 40)
            X_1 = np.array([x1, x2], dtype='float32')
            X = np.mat(X_1)
            # 加载训练好的神经网络模型（离心式冷水机冷冻水泵）
            ans = self.model_wp_600t.predict(X)
            # 计算预测结果
            pump_head = ans[0][0] * (42.39 - 0.4) + 0.4
            power_consumption = ans[0][1] * (79.64 - 0.0652) + 0.0652

        elif self.water_flow_rated == 330:
            """340t/h水泵"""

            # 直接使用训练好的神经网络参数进行矩阵运算
            # 输入
            x1 = (frequency - 5) / (50 - 5)
            x2 = (water_flow - 10) / (375 - 10)
            X_1 = np.array([x1, x2], dtype='float32')
            X = np.mat(X_1)
            # 加载训练好的神经网络模型（天然气采暖锅炉采暖水泵）
            ans = self.model_wp_340t.predict(X)
            # 计算预测结果
            pump_head = ans[0][0] * (39.8125 - 0.0246) + 0.0246
            power_consumption = ans[0][1] * (45.165 - 0.0205) + 0.0205

        else:
            """其它的水泵没有模型训练数据"""
            """其余的水泵根据额定流量，额定扬程，采用理论计算公式进行计算，效率全部按照0.8考虑"""
            # 现在的转速比等于现在的流量与额定流量之比
            speed_ratio = water_flow / self.water_flow_rated
            # 根据相似原理，现在的扬程与额定扬程的关系是转速比的平方
            pump_head = math.pow(speed_ratio, 2) * self.pump_head_rated
            # 根据相似原理，现在的功率与额定功率的关系是转速比的三次方
            power_consumption = math.pow(speed_ratio, 3) * self.power_consumption_rated

        return pump_head, power_consumption
