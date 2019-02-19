from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from .forms import FaceForm, PlateForm, BinClassifyForm
from .tools.face import compute_face_similarity
from .tools.lpr import recognize_plate_number
from .tools.classify import bin_dogorcat
# Create your views here.


@csrf_exempt
def face_similarity(request):
    """
    计算两张图片中的人脸相似度
    """
    if request.method =="POST":
        dic = {"res":True, "value":-1, "error":""}
        form1 = FaceForm(data=request.POST, files=request.FILES)
        if not form1.is_valid():
            dic["res"] = False
            dic["error"] = "form is not valid"
        else:
            req_file1 = form1.cleaned_data['image1']
            req_file2 = form1.cleaned_data['image2']
            sim = compute_face_similarity(req_file1,req_file2)
            if sim != None:
                dic['value'] = sim

        return JsonResponse(dic)

    
    form1 = FaceForm()

    return render(request, 'face_sim.html', {'form': form1})


@csrf_exempt
def plate_recognition(request):
    """
    车牌号码识别
    """
    if request.method == "POST":
        dic = {"res": True, "value": "", "error": ""}
        form1 = PlateForm(data=request.POST, files=request.FILES)
        if not form1.is_valid():
            dic["res"] = False
            dic["error"] = "form is not valid"
        else:
            req_file1 = form1.cleaned_data['image1']
            res = recognize_plate_number(req_file1)
            dic["value"] = res

        return JsonResponse(dic)

    form1 = PlateForm()

    return render(request, 'plate.html', {'form': form1})

@csrf_exempt

def dogorcat(request):
    """
    猫狗图像分类
    """
    if request.method == "POST":
        dic = {"res": True, "value":"", "error":""}
        form1 = BinClassifyForm(data=request.POST, files=request.FILES)
        if not form1.is_valid():
            dic["res"] = False
            dic["error"] = "form is not valid"
        else:
            req_file1 = form1.cleaned_data['image1']
            res = bin_dogorcat(req_file1)
            dic["value"] = res

        return JsonResponse(dic)

    form1 = BinClassifyForm()

    return render(request, 'binaryClassify.html', {'form': form1})


            
