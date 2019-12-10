#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dlib_test.py
@Time    :   2019/12/10 10:12:45
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''
import os
import dlib
import numpy as np
import cv2
dir_path = os.path.abspath(os.path.dirname(__file__))

def detect(frame):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(dir_path + '/shape_predictor_68_face_landmarks.dat')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 人脸数
    rects = detector(gray, 0)
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(frame,rects[i]).parts()])
        for idx, point in enumerate(landmarks):
            # 68点的坐标
            pos = (point[0, 0], point[0, 1])
            cv2.circle(frame, pos, 1, color=(0, 255, 0))

frame = cv2.imread(dir_path + "/test.jpg")
detect(frame)
cv2.imshow("face found",frame)
cv2.imwrite(dir_path + '/test_landmark_detected.jpg',frame)
cv2.waitKey(0)