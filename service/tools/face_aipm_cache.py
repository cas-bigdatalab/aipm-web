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
   

def compute_distance_of_features(features1:np.array,features2:np.array):
    """
    计算特征之间的距离
    """
    if features1.shape[-1] != features2.shape[-1] or features1.shape[0] == 0:
        return None
    temp = features1 - features2
    e = np.linalg.norm(temp, axis=1)  # 计算欧式距离
    return e


def compute_face_similarity(req_file1:"UploadedFile", req_file2:"UploadedFile")->[]:
    # fake func, for performance only
    img1_array = load_image_from_request_file(req_file1)
    img2_array = load_image_from_request_file(req_file2)

    faceFeaturesDict = np.load("/home/aipm-web/service/tools/feature.npy", allow_pickle=True).item()
    feature1 = []
    feature2 = []
    for (file, feature) in faceFeaturesDict.items():
        feature1 = feature
        feature2 = feature

    return compute_distance_of_features(feature1, feature2)


def is_face_in_photo(face_req_file: "UploadedFile", photo_req_file: "UploadedFile") -> bool:
    """判断<face_req_file>图片中的人脸是否在<photo_req_file>图片中:
        如果存在相似度大于0.5 的，则认为是同一个人脸
    """
    face_img_array = load_image_from_request_file(face_req_file)
    photo_img_array = load_image_from_request_file(photo_req_file)

    faces = extract_faces_feature(face_img_array)
    photo_faces = extract_faces_feature(photo_img_array)
    if len(faces) == 0 or len(photo_faces) == 0:
        return False
    distances = compute_distance_of_features(faces[:1], photo_faces)
    similarities = 1-distances
    sim = max(similarities)
    if sim > 0.5:
        return True
    else:
        return False

