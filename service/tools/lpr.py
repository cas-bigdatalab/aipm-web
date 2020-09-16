####
# 车牌号码识别 License Plate Recognition
# by lzx 20190215
####

from hyperlpr import *
import cv2
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from .image import load_image_from_request_file

def recognize_plate_number(req_image_file: "UploadedFile") -> str :
    """
    根据上传的车牌图片,返回识别出的车牌号
    """
    img_array = load_image_from_request_file(req_image_file)
    # results格式：[["<车牌号>:str","<准确度>:numpy.float64","<车牌位置>：[x1,y1,x2,y2]"], [...], ...]
    results = HyperLPR_PlateRecogntion(img_array) 
    results = results[:1]
    print(results)
    if len(results) > 0:
        return results[0][0]
    else:
        return ""
    

