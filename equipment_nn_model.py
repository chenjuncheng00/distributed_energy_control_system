import tensorflow as tf
import numpy as np
import matplotlib as plt

def load_data_water_pump_model(file_name):
    #导入数据
    # 获取训练用的输入(训练样本的输入x，有两个输入)；和训练用的输出（训练样本的输出y，有两个输出）
    # 读取txt文件
    f = open(file_name)  # 打开文件
    trainx_data = [] # 训练用的输入矩阵
    trainy_data =[] # 训练用的输出矩阵
    for line in f.readlines():
        trainx_tmp = [] # 读取的训练输入过程量
        trainy_tmp = [] # 读取的训练输出过程量
        lines = line.strip().split("\t") # 根据制表符将一行分开，按照行存入列表lines中；\t：制表符（一个tab键距离）
        for i in range(len(lines) - 2): # len函数，获取字符长度，i从0开始，因此len(lines)=4,一共有4列。range函数的范围为[)，包含最小值但是不包含最大值
            trainx_tmp.append(float(lines[i]))# 获取x值；float(lines[i]):第1列和第2列
        for i in range(len(lines)-2, len(lines)):
            trainy_tmp.append(float(lines[i])) # 获取y值；如果是扬程，float(lines[-2]):第3列；如果是功率，float(lines[-1]):第4列
        trainx_data.append(trainx_tmp) # 文件的第1列和第2例，有2个输入
        trainy_data.append(trainy_tmp) # 文件的第3列和第4例，有2个输出
    f.close()  # 关闭文件
    # 返回计算结果
    return np.mat(trainx_data), np.mat(trainy_data)

def load_data_centrifugal_chiller_cop_model(file_name):
    """读取离心式冷水机神经网络训练数据"""
    f = open(file_name)  # 打开文件
    trainx_data = []  # 训练用的输入矩阵
    trainy_data = []  # 训练用的输出矩阵
    for line in f.readlines():
        trainx_tmp = []  # 读取的训练输入过程量
        trainy_tmp = []  # 读取的训练输出过程量
        lines = line.strip().split("\t")  # 根据制表符将一行分开，按照行存入列表lines中；\t：制表符（一个tab键距离）
        for i in range(len(lines) - 1):  # len函数，获取字符长度，i从0开始，因此len(lines)=4,一共有4列。range函数的范围为[)，包含最小值但是不包含最大值
            trainx_tmp.append(float(lines[i]))  # 获取x值；float(lines[i]):第1列、第2列和第3列
        for i in range(len(lines) - 1, len(lines)):
            trainy_tmp.append(float(lines[i]))  # 获取y值，第4列
        trainx_data.append(trainx_tmp)  # 文件的第1列、第2例和第3列，有3个输入
        trainy_data.append(trainy_tmp)  # 文件的第4例，有1个输出
    f.close()  # 关闭文件
    # 返回计算结果
    return np.mat(trainx_data), np.mat(trainy_data)

def train_water_pump_model():
    """水泵的神经网络模型"""
    # 导入训练数据
    # 340t/h水泵
    (x_train, y_train) = load_data_water_pump_model("./water_pump_model/wp_340t/wp_340t_data.txt")
    # 600t/h水泵
    #(x_train, y_train) = load_data_water_pump_model("./water_pump_model/wp_600t/wp_600t_data.txt")
    # 710t/h水泵
    #(x_train, y_train) = load_data_water_pump_model("./water_pump_model/wp_710t/wp_710t_data.txt")

    # 构建模型
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(50, input_shape=(2,)), # Dense:建立全连接神经网络，第一层是输入层，2个输入，50个输出
        tf.keras.layers.Dense(50, activation='sigmoid'), # 第二层采用径向基函数，50个神经元
        tf.keras.layers.Dense(2) # 第三层输出层，2个输出
    ])
    # 配置模型
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),# 梯度下降法
                  loss='mean_squared_error',
                  metrics=['mse'])
    model.summary()
    # 训练
    model.fit(x_train, y_train, batch_size=2, epochs=50)
    # 预测
    x_test = np.mat([0.488888889, 0.246575342])
    y_test = np.mat([0.292433102, 0.106844533])
    err = model.evaluate(x_test, y_test)# 预测值和实际值的差值
    result = model.predict(x_test)#预测值
    print(err)
    print(result)

    # 保存训练好的模型
    # 340t/h水泵
    # model.save('./water_pump_model/wp_340t/wp_340t_model.h5')
    # 600t/h水泵
    # model.save('./water_pump_model/wp_600t/wp_600t_model.h5')
    # 710t/h水泵
    # model.save('./water_pump_model/wp_710t/wp_710t_model.h5')

    #加载模型
    # model = tf.keras.models.load_model('path_to_my_model.h5')

def train_centrifugal_chiller_cop_model():
    """离心式冷水机神经网络模型"""
    # 导入训练数据
    (x_train, y_train) = load_data_centrifugal_chiller_cop_model("./centrifugal_chiller_cop_model/centrifugal_chiller_cop_data_0.5_to_1.txt")
    # (x_train, y_train) = load_data_centrifugal_chiller_cop_model("./centrifugal_chiller_cop_model/centrifugal_chiller_cop_data_0.1_to_0.5.txt")

    # 构建模型
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(50, input_shape=(3,)),  # Dense:建立全连接神经网络，第一层是输入层，3个输入，50个输出
        tf.keras.layers.Dense(50, activation='sigmoid'),  # 第二层采用径向基函数，50个神经元
        tf.keras.layers.Dense(1)  # 第三层输出层，1个输出
    ])
    # 配置模型
    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),  # 梯度下降法
                  loss='mean_squared_error',
                  metrics=['mse'])
    model.summary()
    # 训练
    model.fit(x_train, y_train, batch_size=2, epochs=50)
    # 预测
    x_test = np.mat([1, 0.285714286, 0.11212708])
    result = model.predict(x_test)  # 预测值
    print(result)

    # 保存训练好的模型
    # model.save('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.5_to_1.h5')
    # model.save('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.1_to_0.5.h5')


def model_test():
    # model = tf.keras.models.load_model('./water_pump_model/natural_gas_boiler_heating_water_pump/natural_gas_boiler_heating_water_pump_model.h5')
    (x_test, y_test) = load_data_centrifugal_chiller_cop_model("./centrifugal_chiller_cop_model/centrifugal_chiller_cop_data_0.5_to_1.txt")
    # (x_test, y_test) = load_data_centrifugal_chiller_cop_model("./centrifugal_chiller_cop_model/centrifugal_chiller_cop_data_0.1_to_0.5.txt")

    model = tf.keras.models.load_model('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.5_to_1.h5')
    # model = tf.keras.models.load_model('./centrifugal_chiller_cop_model/centrifugal_chiller_cop_model_0.1_to_0.5.h5')


    y_pre = model.predict(x_test)

    print(y_pre)


# train_water_pump_model()
# train_centrifugal_chiller_cop_model()
# model_test()


