# 如要正常使用本程序，需要导入以下几个第三方程序库
# numpy,tensorflow

import random
import time
from project_load import load_predict_function as lpf
from equipment_optimization_function import equipment_optimization_function as eof
from global_constant import Global_Constant

# 执行程序
if __name__ == '__main__':

    # 实例化一个全局常量类
    gc = Global_Constant()

    # 供冷时出水温度
    chilled_water_temperature = 7
    # 供热时出水温度
    heating_water_temperature = 55
    # 空气源热泵在作为一级低温热源制热时的出水温度
    ashp_heat_source_water_temperature = 25

    while True:
        # 负荷预测的输入参数
        environment_temperature = random.randint(11, 38)
        environment_humidity = random.randint(8, 29)
        sun_radiation = random.randint(0, 1260)
        personnel_density = random.randint(0, 1)
        cold_load_1 = random.randint(0, 140)
        cold_load_24 = random.randint(0, 140)
        heat_load_1 = 0
        heat_load_24 = 0
        # 运行负荷预测程序
        cold_load_now = lpf(environment_temperature, environment_humidity, sun_radiation, personnel_density,
                            cold_load_1, cold_load_24, heat_load_1, heat_load_24, gc)[1]
        heat_load_now = lpf(environment_temperature, environment_humidity, sun_radiation, personnel_density,
                            cold_load_1, cold_load_24, heat_load_1, heat_load_24, gc)[2]
        hot_water_prediction = 1000
        electricity_prediction = 3000

        print(cold_load_now)

        # 运行设备优化计算程序
        eof(cold_load_now, heat_load_now, hot_water_prediction, electricity_prediction, environment_temperature,
            chilled_water_temperature, heating_water_temperature, ashp_heat_source_water_temperature, gc)

        # 10分钟计算一次
        time.sleep(5)

