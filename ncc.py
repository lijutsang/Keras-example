#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

ncc_path ='C:\\mPythonFile\\python\\packs\\ncc'
os.system(ncc_path + "\\ncc\\ncc --version\n")
#os.system("C:\\mPythonFile\\python\\packs\\ncc\\ncc\\ncc --help\n")
os.system(ncc_path + "\\ncc\\ncc " + ncc_path + "\\model\\mymodel.tflite "+ ncc_path + "\\model\\my.kmodel "+"-i tflite -o k210model --dataset "+ ncc_path + "\\test")
'''
model_path = 'C:\\mPythonFile\\python\\packs\\ncc\\model'
ncc_path ='C:\\mPythonFile\\python\\packs\\ncc\\ncc\\ncc'
tflite_path = 'C:\\mPythonFile\\python\\packs\\ncc\\model\\mymodel.tflite'
kmodel_path = 'C:\\mPythonFile\\python\\packs\\ncc\\model\\test.kmodel'
data = 'C:\\mPythonFile\\python\\packs\\ncc\\test'

convert_kmodel = "{ncc} {tflite} {kmodel} -i tflite -o k210model --dataset {data}".format(ncc=ncc_path,tflite=tflite_path,kmodel=kmodel_path,data=data)

if os.system(convert_kmodel) == 0:
    print("\n转换模型成功!")
    
'''

