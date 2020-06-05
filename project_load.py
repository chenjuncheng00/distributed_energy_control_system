import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import datetime
import write_to_database as wtd
from global_constant import Global_Constant

def load_predict():
    """冷热电负荷预测，并写入数据库"""

    # 实例化一个全局常量类
    gc = Global_Constant()

    # 设置时间格式
    format_pattern = "%m-%d"
    # 获取当前的时间
    now_1 = str(datetime.datetime.now().strftime(format_pattern))
    now = datetime.datetime.strptime(now_1, format_pattern)
    # 负荷情况
    electricity_load_result = electricity_load(gc)
    hot_water_load_result = hot_water_load(gc)
    # 根据时间判断，当前是制冷季、采暖季还是过渡季
    cooling_season_start_date = datetime.datetime.strptime(gc.cooling_season_start_date, format_pattern)
    cooling_season_end_date = datetime.datetime.strptime(gc.cooling_season_end_date, format_pattern)
    heating_season_start_date = datetime.datetime.strptime(gc.heating_season_start_date, format_pattern)
    heating_season_end_date = datetime.datetime.strptime(gc.heating_season_end_date, format_pattern)
    if now >= cooling_season_start_date and now <= cooling_season_end_date:
        cold_load_result = cold_load(gc)
        heat_load_result = 0
    elif now >= heating_season_start_date or now <= heating_season_end_date:
        cold_load_result = 0
        heat_load_result = heat_load(gc)
    else:
        cold_load_result = 0
        heat_load_result = 0
    # 将负荷值写入数据库
    cold_heat_prediction = max(cold_load_result, heat_load_result)
    hot_water_prediction = hot_water_load_result
    electricity_prediction = electricity_load_result
    wtd.write_to_database_prediction(cold_heat_prediction, hot_water_prediction, electricity_prediction)


def cold_load(gc):
    # 项目冷负荷
    # 载入神经网络模型
    cold_load_model = gc.cold_load_model
    # 神经网络模型输入参数，归一化处理
    # 室外干球温度
    environment_temperature = (35-10.8)/(38.6-10.8)
    # 室外环境湿度
    environment_humidity = (25-7.43)/(29.6-7.43)
    # 太阳辐射强度
    sun_radiation = (600-0)/(1261.37-0)
    # 人员密度
    personnel_density = 0.35
    # 上一个时刻的冷负荷(w/㎡)
    cold_load_1 = (63-0)/(148-0)
    # 24个时刻之前的冷负荷
    cold_load_24 = (33-0)/(148-0)
    # 神经网络输入矩阵
    X_cold_load_model = np.mat([environment_temperature, environment_humidity, sun_radiation, personnel_density, cold_load_1, cold_load_24])
    # 预测输入结果
    Y_cold_load_model = (cold_load_model.predict(X_cold_load_model))*(148-0) + 0
    # 最终结果（单位kW）
    cold_load_result = gc.area * Y_cold_load_model/1000
    # 返回结果
    return cold_load_result[0][0]


def heat_load(gc):
    # 项目热负荷
    # 载入神经网络模型
    heat_load_model = gc.heat_load_model
    # 神经网络模型输入参数，归一化处理
    # 室外干球温度
    environment_temperature = (10 - (-4.3)) / (29.4 - (-4.3))
    # 室外环境湿度
    environment_humidity = (10 - 1.55) / (15.57 - 1.55)
    # 太阳辐射强度
    sun_radiation = (600 - 0) / (1007.33 - 0)
    # 人员密度
    personnel_density = 0.55
    # 上一个时刻的热负荷(w/㎡)
    heat_load_1 = (22.81 - 0) / (61.345 - 0)
    # 24个时刻之前的热负荷
    heat_load_24 = (8.89 - 0) / (61.345 - 0)
    # 神经网络输入矩阵
    X_heat_load_model = np.mat([environment_temperature, environment_humidity, sun_radiation, personnel_density, heat_load_1, heat_load_24])
    # 预测输入结果
    Y_heat_load_model = (heat_load_model.predict(X_heat_load_model)) * (61.345 - 0) + 0
    # 最终结果（单位kW）
    heat_load_result = gc.area * Y_heat_load_model / 1000
    # 返回结果
    return heat_load_result[0][0]


def hot_water_load(gc):
    # 项目生活热水负荷
    return 0

def electricity_load(gc):
    # 项目电负荷
    return 3000


def load_data_load_forecast_model(file_name):
    """神经网络负荷预测模型数据读取，冷热负荷"""
    # 获取训练用的输入(训练样本的输入x，有两个输入)；和训练用的输出（训练样本的输出y，有两个输出）
    # 读取txt文件
    f = open(file_name)  # 打开文件
    trainx_data = []  # 训练用的输入矩阵
    trainy_data = []  # 训练用的输出矩阵
    for line in f.readlines():
        trainx_tmp = []  # 读取的训练输入过程量
        trainy_tmp = []  # 读取的训练输出过程量
        lines = line.strip().split("\t")  # 根据制表符将一行分开，按照行存入列表lines中；\t：制表符（一个tab键距离）
        for i in range(len(lines) - 1):  # len函数，获取字符长度，i从0开始，因此len(lines)=7,一共有7列。range函数的范围为[)，包含最小值但是不包含最大值
            trainx_tmp.append(float(lines[i]))  # 获取x值；float(lines[i]):第1列到第6列
        for i in range(len(lines) - 1, len(lines)):
            trainy_tmp.append(float(lines[i]))  # 获取y值；float(lines[-2]):倒数第二列；如果是功率，float(lines[-1]):最后一列
        trainx_data.append(trainx_tmp)  # 文件的第1列和第2例，有6个输入
        trainy_data.append(trainy_tmp)  # 文件的第3列和第4例，有1个输出
    f.close()  # 关闭文件
    # 返回计算结果
    return np.mat(trainx_data), np.mat(trainy_data)


def train_load_forecast_model():
    """负荷预测的神经网络模型"""
    # 导入训练数据
    # 冷负荷模型训练数据
    #(x_train, y_train) = load_data_load_forecast_model("./load_forecast_model/cold_load_forecast_model_data_train.txt")
    # 热负荷模型训练数据
    (x_train, y_train) = load_data_load_forecast_model("./load_forecast_model/heat_load_forecast_model_data_train.txt")

    # 构建模型
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(80, input_shape=(6,)), # Dense:建立全连接神经网络，第一层是输入层，6个输入，50个输出
        tf.keras.layers.Dense(80, activation='sigmoid'), # 第二层采用径向基函数，50个神经元
        tf.keras.layers.Dense(1) # 第三层输出层，1个输出
    ])
    # 配置模型
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),# 梯度下降法
                  loss='mean_squared_error',
                  metrics=['mse'])
    model.summary()
    # 训练
    model.fit(x_train, y_train, batch_size=5, epochs=50)
    # 冷负荷模型预测
    # x_test = np.mat([0.548201499, 0.447000455, 0.093969255, 0.1, 0.380416971, 0.310639827])
    # y_test = np.mat([0.289704519])
    # 热负荷模型预测
    #x_test = np.mat([0.53115729, 0.15763196, 0.393277275, 1, 0.091419595, 0.050981397])
    #y_test = np.mat([0.056336826])

    #err = model.evaluate(x_test, y_test)# 预测值和实际值的差值
    #result = model.predict(x_test)#预测值
    #print(err)
    #print(result)

    # 保存训练好的冷负荷模型
    # model.save('./load_forecast_model/cold_load_forecast_model.h5')
    # 保存训练好的热负荷模型
    # model.save('./load_forecast_model/heat_load_forecast_model.h5')


def load_forecast_model_predict():
    """批量测试"""
    # 加载冷负荷预测模型
    # model = tf.keras.models.load_model('./load_forecast_model/cold_load_forecast_model.h5')
    # 冷负荷预测模型输入
    # file_name = "./load_forecast_model/cold_load_forecast_model_data_test.txt"

    # 加载热负荷预测模型
    model = tf.keras.models.load_model('./load_forecast_model/heat_load_forecast_model.h5')
    # 热负荷预测模型输入
    file_name = "./load_forecast_model/heat_load_forecast_model_data_test.txt"

    f = open(file_name)  # 打开文件
    testx_data = []  # 测试用的输入矩阵
    testy_data = []  # 测试用的输出矩阵
    for line in f.readlines():
        testx_tmp = []  # 读取的测试输入过程量
        testy_tmp = []  # 读取的训练输出过程量
        lines = line.strip().split("\t")  # 根据制表符将一行分开，按照行存入列表lines中；\t：制表符（一个tab键距离）
        for i in range(len(lines) - 1):  # len函数，获取字符长度，i从0开始，因此len(lines)=7,一共有7列。range函数的范围为[)，包含最小值但是不包含最大值
            testx_tmp.append(float(lines[i]))  # 获取x值；float(lines[i]):第1列到第6列
        for i in range(len(lines) - 1, len(lines)):
            testy_tmp.append(float(lines[i]))  # 获取y值；如果是扬程，float(lines[-2]):第3列；如果是功率，float(lines[-1]):第4列
        testx_data.append(testx_tmp)  # 文件的第1列到第6例，有6个输入
        testy_data.append(testy_tmp)  # 文件的第3列和第4例，有1个输出
    X = np.mat(testx_data)
    Y = np.mat(testy_data)
    # 加载训练好的神经网络模型
    ans = model.predict(X)
    # 计算预测结果
    plt.plot(ans)
    plt.plot(Y)
    plt.show()

    # print(ans)


# 执行程序
if __name__ == '__main__':
    load_predict()
