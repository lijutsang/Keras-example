#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   opencv_face.py
@Time    :   2019/12/10 09:48:05
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''

# here put the import code
'''
利用OpenCV实现人脸检测
使用OpenCV之前，要先安装OpenCV库，在命令行中输入“pip install opencv-python”
OpenCV开源库中，haarcascade_frontalface_alt.xml是人脸的哈尔特征迭代
分类器模型，detectMultiScale( )是多个尺度检测人脸算法的函数。实现过程的
代码如下：
'''
from PIL import Image
import cv2
import numpy
import os
dir_path = os.path.abspath(os.path.dirname(__file__))
def detect(frame):
    cascPath = dir_path + "/model/haarcascade_frontalface_default.xml"
    print(cascPath)
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.15,minNeighbors=10)
    print("Found {0} facse!".format(len(faces)))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

frame = cv2.imread(dir_path + "/test.jpg")
detect(frame)
cv2.imshow("face found",frame)
cv2.imwrite(dir_path + '/test_detected.jpg',frame)
cv2.waitKey(0)
