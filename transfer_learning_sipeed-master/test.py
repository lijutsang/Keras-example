import keras
import numpy as np
from keras.preprocessing import image
from keras import models
from keras.models import Model
from keras.applications import imagenet_utils
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
import os
dir_path = os.path.abspath(os.path.dirname(__file__))

mobile = keras.applications.mobilenet.MobileNet()
model = models.load_model(dir_path +'/my_model/my_model.h5')

def prepare_image(file):
    img_path = ''
    img = image.load_img(img_path + file, target_size=(128, 128))
    img_array = image.img_to_array(img)
    image.save_img(img_path + file, img_array)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
def my_prepare_image(file):
    img_path = ''
    img = image.load_img(img_path + file, target_size=(128, 128))
    img_array = image.img_to_array(img)
    image.save_img(img_path + file, img_array)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
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

def test_mobile():

    preprocessed_image = prepare_image(dir_path +'\\German_Shepherd.jpg')
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    print(results)

    preprocessed_image = prepare_image(dir_path +'\\santa.jpg')
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    print(results)

    preprocessed_image = prepare_image(dir_path +'\\uno.jpg')
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    print(results)

test()