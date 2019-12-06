#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mnist.py
@Time    :   2019/10/21 12:27:13
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''
#openCV视觉库
from cv2 import cv2 
import os
#python标准图像处理库
from PIL import Image 
import warnings 
warnings.filterwarnings('ignore')
import tensorflow as tf 
#MNIST数据
from tensorflow.examples.tutorials.mnist import input_data 
#可用来存储和处理大型矩阵 
import numpy as np 

global img
#isTrain = True 训练模型，isTrain = False 加载模型预测手写数字
isTrain = False
#设置mnist路径
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
batch_size = 100 

#设置占位符，尺寸为样本输入和输出的尺寸
X_holder = tf.placeholder(tf.float32,name="x")
y_holder = tf.placeholder(tf.float32,name="y")
X_images = tf.reshape(X_holder, [-1, 28, 28, 1])

#convolutional layer 设置第一个卷积层和池化层
conv1_Weights = tf.get_variable(name="v1",initializer=tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
conv1_biases = tf.get_variable(name="v2",initializer=tf.constant(0.1, shape=[32]))
conv1_conv2d = tf.nn.conv2d(X_images, conv1_Weights, strides=[1, 1, 1, 1], padding='SAME') + conv1_biases
conv1_activated = tf.nn.relu(conv1_conv2d)
conv1_pooled = tf.nn.max_pool(conv1_activated, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
#convolutional layer 2 
#设置第二个卷积层和池化层
conv2_Weights = tf.get_variable(name="v3",initializer=tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
conv2_biases = tf.get_variable(name="v4",initializer=tf.constant(0.1, shape=[64]))
conv2_conv2d = tf.nn.conv2d(conv1_pooled, conv2_Weights, strides=[1, 1, 1, 1], padding='SAME') + conv2_biases
conv2_activated = tf.nn.relu(conv2_conv2d)
conv2_pooled = tf.nn.max_pool(conv2_activated, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
#full connected layer 1
#设置第一个全连接层
connect1_flat = tf.reshape(conv2_pooled, [-1, 7 * 7 * 64])
connect1_Weights = tf.get_variable(name="v5",initializer=tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1))
connect1_biases = tf.get_variable(name="v6",initializer=tf.constant(0.1, shape=[1024]))
connect1_Wx_plus_b = tf.add(tf.matmul(connect1_flat, connect1_Weights), connect1_biases)
connect1_activated = tf.nn.relu(connect1_Wx_plus_b)

keep_prob=tf.placeholder(tf.float32)
#full connected layer 2
#设置第二个全连接层
connect2_Weights = tf.get_variable(name="v7",initializer=tf.truncated_normal([1024, 10], stddev=0.1))
connect2_biases = tf.get_variable(name="v8",initializer=tf.constant(0.1, shape=[10]))
connect2_Wx_plus_b = tf.add(tf.matmul(connect1_activated, connect2_Weights), connect2_biases)
predict_y = tf.nn.softmax(connect2_Wx_plus_b)

#loss and train损失和训练 ，建立loss function，为交叉熵
loss = tf.reduce_mean(-tf.reduce_sum(y_holder * tf.log(predict_y), 1))
#配置Adam优化器，学习速率为1e-4
optimizer = tf.train.AdamOptimizer(0.0001)
train = optimizer.minimize(loss)
'''
对于神经网络模型，重要是其中的W、b这两个参数。
开始神经网络模型训练之前，这两个变量需要初始化。
tf.global_variables_initializer实例化tensorflow中的Operation对象。
调用tf.Session方法实例化会话对象；
调用tf.Session对象的run方法做变量初始化。
'''
#初始化模型
init = tf.global_variables_initializer()
session = tf.compat.v1.Session()
session.run(init)
#saver = tf.train.Saver()
saver = tf.compat.v1.train.Saver()

if isTrain:
    #训练模型和保存模型
    for step in range(10001):
        train_images, train_labels = mnist.train.next_batch(200)
        session.run(train, feed_dict={X_holder:train_images, y_holder:train_labels})
    
        if step % 100 == 0:
            #建立正确率计算表达式
            correct_prediction = tf.equal(tf.argmax(predict_y, 1), tf.argmax(y_holder, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            test_images, test_labels = mnist.test.next_batch(2000)
            train_accuracy = session.run(accuracy, feed_dict={X_holder:train_images, y_holder:train_labels})
            test_accuracy = session.run(accuracy, feed_dict={X_holder:test_images, y_holder:test_labels})
            print('step:%d 训练正确率:%.4f 测试正确率:%.4f' %(step, train_accuracy, test_accuracy))
        
    save_path = saver.save(session, 'C:/Users/AOC/Desktop/liju-work/MNIST/save_model/mnist_cnn')
    print('Save to path:', save_path)
    print('MNIST模型保存路径:', save_path)
else:
    #加载模型
    #ckpt = tf.train.get_checkpoint_state('C:/Users/AOC/Desktop/liju-work/MNIST/save_model')
    saver.restore(session, "./save_model/mnist_cnn")

    correct_prediction = tf.equal(tf.argmax(predict_y, 1), tf.argmax(y_holder, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print('load model successful')
    print('模型加载成功！！！')
    train_images, train_labels = mnist.train.next_batch(5000)
    test_images, test_labels = mnist.test.next_batch(5000)
    train_accuracy = session.run(accuracy, feed_dict={X_holder:train_images, y_holder:train_labels})
    test_accuracy = session.run(accuracy, feed_dict={X_holder:test_images, y_holder:test_labels})
    print('MNIST模型训练 正确率:%.4f 测试正确率:%.4f' %(train_accuracy, test_accuracy))


    im = Image.open('./picture/test.png')
    data = list(im.getdata())
    result = [(255-x)*1.0/255.0 for x in data] 
    #print(result)

    img = cv2.imread('./picture/3.png')  # 手写数字图像所在位置
    cv2.namedWindow('image')
    cv2.imshow('image', img)

    #预测自己的手写数字
    prediction = tf.argmax(predict_y,1)
    predint = prediction.eval(feed_dict={X_holder: [result],keep_prob: 1.0}, session=session)
    print("recognize result: %d" %predint[0])
    print("手写数字识别结果: %d" %predint[0])
    cv2.waitKey(0)
