#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   install.py
@Time    :   2019/10/22 17:37:24
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''

import os
def getTxt():
        txt = open("C:\\Users\\AOC\\Desktop\\mpython\\python\\packs\\AIDEMO_1\\libs.txt","r").read()
        for dd in ",":
                txt=txt.replace(dd," ")
        return txt
kusTxt=getTxt()
words= kusTxt.split()
for word in words:
        os.system("pip install --index-url https://pypi.douban.com/simple "+word)
        #os.system("pip install --no-index --find-links=C:\\Users\\AOC\\Desktop\\mpython\\python\\packs\\AIDEMO_1 "+word)
        print("成功安装")