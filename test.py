import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def load_data_model_test(file_name):
    """神经网络负荷预测模型数据读取，冷负荷"""
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


def train_model_test():
    """负荷预测的神经网络模型"""
    # 导入训练数据
    # 冷负荷模型训练数据
    (x_train, y_train) = load_data_model_test("./load_forecast_model/1_train.txt")

    # 构建模型
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(40, input_shape=(16,)), # Dense:建立全连接神经网络，第一层是输入层，6个输入，50个输出
        tf.keras.layers.Dense(40, activation='sigmoid'), # 第二层采用径向基函数，50个神经元
        tf.keras.layers.Dense(1) # 第三层输出层，1个输出
    ])
    # 配置模型
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),# 梯度下降法
                  loss='mean_squared_error',
                  metrics=['mse'])
    model.summary()
    # 训练
    model.fit(x_train, y_train, batch_size=5, epochs=50)

    # 保存训练好的模型
    # model.save('./load_forecast_model/1_model.h5')

    #批量预测
    # 输入
    file_name = "./load_forecast_model/1_test.txt"
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

#train_model_test()



