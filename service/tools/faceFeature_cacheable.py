import os
import numpy as np
import sys
import time
import dlib
from PIL import Image
from django.conf import settings
import cv2
from .image import load_image_from_request_file
import hashlib

MODEL_DIR = os.path.join(settings.BASE_DIR, "ai_models/dlib")

detector = dlib.get_frontal_face_detector()

sp = dlib.shape_predictor(os.path.join(
    MODEL_DIR, "shape_predictor_68_face_landmarks.dat"))
face_rec = dlib.face_recognition_model_v1(os.path.join(
    MODEL_DIR, "dlib_face_recognition_resnet_model_v1.dat"))

cache_dict = dict()

def extract_faces_feature(img: np.array) -> np.array:
    """
    识别出图片中所有的人脸并抽取出128维的特征数据
    """
    data = []
    if img.shape[0] * img.shape[1] > 500000:  # 图像太大，进行压缩
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # 检测人脸，抽取特征数据
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        rec = dlib.rectangle(d.left(), d.top(), d.right(), d.bottom())
        shape = sp(img, rec)  # 获取landmark
        # 使用resNet获取128维的人脸特征向量
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        data.append(face_descriptor)
    return np.array(data)

def getFaceFeatures(face_req_file: "UploadedFile") -> np.array:

    face_img_array = load_image_from_request_file(face_req_file)
    md5hash = hashlib.md5(face_img_array)
    md5 = md5hash.hexdigest()
    facesFeatures = ""
    if md5 in cache_dict :
        facesFeatures = cache_dict.get(md5)
    else:
        extracted_facesFeatures = extract_faces_feature(face_img_array)
        cache_dict[md5] = extracted_facesFeatures
        facesFeatures = extracted_facesFeatures

    return facesFeatures