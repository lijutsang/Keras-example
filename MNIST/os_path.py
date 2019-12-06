#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2019/10/30 09:48:24
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''

# here put the import code

import os

print('***获取当前目录***')
path = os.path.abspath(os.path.dirname(__file__))
print(os.getcwd())
print(path)
print(type(path))

print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))