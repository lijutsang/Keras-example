#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

ncc_path ='C:\\mPythonFile\\python\\packs\\ncc'
os.system(ncc_path + "\\ncc\\ncc --version\n")
#os.system("C:\\mPythonFile\\python\\packs\\ncc\\ncc\\ncc --help\n")
os.system(ncc_path + "\\ncc\\ncc " + ncc_path + "\\model\\mymodel.tflite "+ ncc_path + "\\model\\my.kmodel "+"-i tflite -o k210model --dataset "+ ncc_path + "\\test")
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

ncc_path ='C:\\mPythonFile\\python\\packs\\ncc'
if os.system(ncc_path + "\\ncc\\ncc " + ncc_path + "\\model\\mymodel.tflite "+ ncc_path + "\\model\\my4.kmodel " + "-i tflite -o k210model --dataset " + ncc_path + "\\test") == 0:
    print("\n转换模型成功!")
if os.system(ncc_path + "\\ncc\\ncc --version") == 0:
    print("\nncc版本!")
    
'''



