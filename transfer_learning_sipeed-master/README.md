# transfer_learning_sipeed 迁移学习 k210
# h5 ---> tflite ---> kmodel
## 环境
win10 ubuntu18.04测试转换kmodel成功

numpy                    1.17.2
Keras                    2.3.1
tensorflow               1.14.0
...

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

### 测试h5模型 test.py
```
model = models.load_model(dir_path +'/my_model/my_model.h5')
def test():
    preprocessed_image = prepare_image(dir_path +'\\santa.jpg')
    predictions_santa = model.predict(preprocessed_image) 
    print("image is Santa") 
    print(predictions_santa[0][1]*100,"%") 
    print("is Uno") 
    print(predictions_santa[0][0]*100,"%")                       
    preprocessed_image = prepare_image(dir_path +'\\uno.jpg') 
    predictions_uno = model.predict(preprocessed_image) 
    print("Santa") 
    print(predictions_uno[0][1]*100,"%") 
    print("Uno") 
    print(predictions_uno[0][0]*100,"%")
```

Link to the full tutorial https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
Create your own custom image classifier with transfer learning in Keras, convert the trained model to .kmodel format and run it on Sipeed board (can be any board, Bit/Dock or Go) using Micropython or Arduino IDE.
