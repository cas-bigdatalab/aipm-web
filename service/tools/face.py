# import sys
import os
# import json
import dlib
import numpy as np
# import PIL.Image
# import PIL.ImageFile
import cv2
# import io
from django.conf import settings

from .image import load_image_from_request_file

MODEL_DIR = os.path.join(settings.BASE_DIR, "ai_models/dlib")  # dlib库使用的相关model文件目录




# 使用cnn进行人脸识别（没有gpu会比较慢）
# cnn_detector = dlib.cnn_face_detection_model_v1(
#     os.path.join(MODEL_DIR, "mmod_human_face_detector.dat"))
# # 使用传统的HOG特征+级联分类的方法 进行人脸识别
detector = dlib.get_frontal_face_detector()

sp = dlib.shape_predictor(os.path.join(
    MODEL_DIR, "shape_predictor_68_face_landmarks.dat"))
face_rec = dlib.face_recognition_model_v1(os.path.join(
    MODEL_DIR, "dlib_face_recognition_resnet_model_v1.dat"))

def extract_faces_feature(img:np.array)->np.array:
    """
    识别出图片中所有的人脸并抽取出128维的特征数据
    """
    data = []
    if img.shape[0]*img.shape[1] > 500000:  # 图像太大，进行压缩
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
   

def compute_distance_of_features(feature1:np.array,feature2:np.array):
    """
    计算人脸相似度
    """
    if feature1.shape != feature2.shape and feature1.shape[0]!=1:
        return -1
    temp = feature1[0] - feature2[0]
    e = np.linalg.norm(temp, axis=0, keepdims=True)  # 计算欧式距离
    return 1-e[0]


def compute_face_similarity(req_file1:"UploadedFile", req_file2:"UploadedFile")->float:
    img1_array = load_image_from_request_file(req_file1)
    img2_array = load_image_from_request_file(req_file2)

    img1_faces = extract_faces_feature(img1_array)
    img2_faces = extract_faces_feature(img2_array)
    if len(img1_faces) == 0 or len(img2_faces) == 0:
        return 0
    return compute_distance_of_features(img1_faces, img2_faces)
