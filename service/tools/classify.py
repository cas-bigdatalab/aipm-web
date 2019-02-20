import os
import dlib
import io
from django.conf import settings
from .image import load_image_from_request_file
import PIL.Image
import keras

MODEL_DIR = os.path.join(settings.BASE_DIR, "ai_models/dlib")  

from keras.models import model_from_yaml
from keras.optimizers import Adam
from keras.preprocessing import image
import numpy as np
from keras.applications.resnet50 import preprocess_input

image_size = (150, 150)


def load_data(req_file: "UploadedFile", mode="RGB")->"numpy.array or None":
    
    tempImage="./temp.jpg"
    fbytes = req_file.read()
    try:
        data = []
        im = PIL.Image.open(io.BytesIO(fbytes))
        im.save(tempImage)
        return tempImage
    except Exception as err:
        print(err)

    return None

def bin_dogorcat(req_file:"UploadedFile"):

    keras.backend.clear_session()
    with open(os.path.join(MODEL_DIR,'cat_dog.yaml')) as yamlfile:
        loaded_model_yaml = yamlfile.read()
    model = model_from_yaml(loaded_model_yaml)
    model.load_weights(os.path.join(MODEL_DIR,'cat_dog.h5'))

    sgd = Adam(lr=0.0003)
    model.compile(loss='categorical_crossentropy',optimizer=sgd, metrics=['accuracy'])

    images = []
    tempImage=load_data(req_file)
    img = image.load_img(tempImage, target_size=image_size)
    img_array = image.img_to_array(img)

    x = np.expand_dims(img_array, axis=0)
    x = preprocess_input(x)
    result = model.predict_classes(x,verbose=0)
    
    os.remove(tempImage)

    if result[0]==0:
        return "cat"
    if result[0]==1:
        return "dog"
    else:
        return "other"
