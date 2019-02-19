import os
import dlib
import io
import numpy as np
import cv2
from django.conf import settings
from .image import load_image_from_request_file
import PIL.Image

MODEL_DIR = os.path.join(settings.BASE_DIR, "ai_models/dlib")  # dlib库使用的相关model文件目录
import numpy as np
import sys
from keras.models import load_model
import keras



def load_data(req_file: "UploadedFile", mode="RGB")->"numpy.array or None":
    
    fbytes = req_file.read()
    try:
        data = []
        im = PIL.Image.open(io.BytesIO(fbytes))
        image = cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR)
        #image = cv2.imread(io.BytesIO(fbytes))
        image = cv2.resize(image, (Width, Height))
        image = np.array(image).reshape(Width, Height, 3)
        data.append(image)
        data = np.array(data, dtype="float") / 255.0
        return data
    except Exception as err:
        print(err)

    return None


def bin_dogorcat(req_file:"UploadedFile"):
    global Width, Height
    Width = 224
    Height = 224    
    X_test = load_data(req_file)
    keras.backend.clear_session()
    model = load_model(os.path.join(MODEL_DIR, "DogVsCat.h5"))
    ans = model.predict(X_test)

    if ans[0][0]>ans[0][1]:
        return "cat"
    else:
        return "dog"
