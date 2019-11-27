# transfer_learning_sipeed 迁移学习 k210
# h5 ---> tflite ---> kmodel
win10 ubuntu18.04测试转换kmodel成功

教程：https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
## 训练
```
python mbnet_kers.py 
```
## keras *.h5模型 ---> tensorflow *.tflite模型
```
tflite_convert  --output_file=model.tflite \   --keras_model_file=my_model.h5
```
## 转换kmodel
```
ncc compile ./my_model/mymodel.tflite ./my_model/my.kmodel -i tflite -o kmodel -t k210 --dataset ./images
```
Link to the full tutorial https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
Create your own custom image classifier with transfer learning in Keras, convert the trained model to .kmodel format and run it on Sipeed board (can be any board, Bit/Dock or Go) using Micropython or Arduino IDE.
