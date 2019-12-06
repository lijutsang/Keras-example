#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   img.py
@Time    :   2019/10/29 16:40:14
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''

# here put the import code
'''
def main():
    global img
    img = cv2.imread('C:/Users/AOC/Desktop/liju-work/MNIST/5.png')  # 手写数字图像所在位置
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转换图像为单通道(灰度图)
    resize_img = cv2.resize(img, (28,28)) # 调整图像尺寸为28*28
    ret, thresh_img = cv2.threshold(resize_img,127,255,cv2.THRESH_BINARY) # 二值化
    cv2.imshow('result', thresh_img)
    cv2.imwrite('C:/Users/AOC/Desktop/liju-work/MNIST/5_1.png', thresh_img)  # 预处理后图像保存位置
    cv2.imshow('image', img)
    cv2.waitKey(0)

'''
import numpy as np
from PIL import Image 

def Image_PreProcessing():
    # 待处理图片存储路径	
    img = Image.open('./picture/5.png')
    #转换为灰度图
    gray = img.convert('L')
    gray.show()
    #转换为二值图
    img = gray.convert('1')
    arr = np.array(img)
    print(arr)
	# Resize图片大小，入口参数为一个tuple，新的图片大小
    imBackground = img.resize((28,28))
	#处理后的图片的存储路径，以及存储格式
    imBackground.save('./picture/5_2.png','PNG')
    #img.save('./picture/5_1.png','PNG')
    #img.show()
    imBackground.show()

if __name__ == "__main__":
	Image_PreProcessing()

