#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/11/27 17:37:31
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''

# here put the import code
'''
借助Python探索蛋糕价格的奥秘
借助Python中的sklearn模块来探索蛋糕尺寸和价格之间的关系，并以
蛋糕尺寸为 x 轴，价格为 y 轴，通过matplotlib模块绘制出拟合的图象。
'''
from sklearn import linear_model
import matplotlib.pyplot as plt
# 样本数据(Xi, Yi)，Xi是蛋糕尺寸，Yi是蛋糕价格
Xi = [[6], [8], [9], [10], [12]]
Yi = [[40], [56], [69], [77], [96]]
# 设置模型
model = linear_model.LinearRegression()
# 训练数据，并用训练得出的模型预测数据
model.fit(Xi,Yi)
y_plot = model.predict(Xi)
# 打印价格y和尺寸x的关系式
print("y=", model.coef_, "x+", model.intercept_)
print(model.score(Xi, Yi))
# 绘图
plt.scatter(Xi, Yi, color = 'red', label = "sample data", linewidth = 2)
plt.plot(Xi, y_plot, color = 'green', label = "regression data", linewidth = 2)
plt.legend(loc = 'lower right')
plt.show()
'''
以城市人口和GDP两个特征为例，借助Python实现对这些城市的聚类
分析，当前尝试的簇数（即聚类的数量）为3
聚类得到的图像如图2.4.10所示，横轴为归一化后的城市人口，纵轴为
归一化后的GDP。可以看出，如果将城市聚合为3类，得到的绿色点分别
代表上海、北京、广州、天津和重庆，聚类结果基本符合人们对一线城市
的认同。
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# X为31个城市的人口，Y为对应城市的GDP归一化后的数据
X = [0.401773527, 0.307890959, 0.306004227, 0.109150352, 0.07103838,
0.216502413, 0.22211249, 0.283614034, 0.427462553, 0.195391659,
0.216974096, 0.154119412, 0.186559398, 0.215155169, 0.202546498,
0.243818744, 0.245820448, 0.205182025, 0.256621985, 0.221617223,
0.049240738, 0.412398183, 0.118318687, 0.165027078, 0.015854439,
0.243190816, 0.095583575, 0.059927302, 0.054255316, 0.078968548,1]
Y = [0.910942504, 0.634714225, 0.210362455, 0.10488792, 0.112623919,
0.193764073, 0.210015029, 0.216533084, 1, 0.372729708, 0.401499717,
0.154549278, 0.231952915, 0.222664322, 0.219940984, 0.284801082,
0.422753042, 0.335550497, 0.693696824, 0.131425388, 0.044632018,
0.431895424, 0.112060017, 0.152600639, 0.015080566, 0.222053931,
0.080352678, 0.044294883, 0.057409067, 0.087263939, 0.629575583]
# 转化成数组
x1 = np.array(X)
x2 = np.array(Y)
XX = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
# 现在我们来用K均值聚类方法来做聚类，首先选择k=3，代码如下：
cluster = 4 # 聚类簇数
k = KMeans(n_clusters=cluster) # 构造聚类器
y_pred = k.fit_predict(XX) # 聚类
# 绘制聚类后的散点图
plt.scatter(x1, x2, c=y_pred)
plt.show()