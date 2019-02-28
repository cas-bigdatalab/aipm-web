# from django.urls import path
from django.conf.urls import url

from .views import face_similarity, face_in_photo, plate_recognition, dogorcat, mandarin_asr, sentiment

urlpatterns = [
    url(r'face/similarity/$', face_similarity),
    url(r'face/in_photo/$', face_in_photo),
    url(r'plate/$', plate_recognition),
    url(r'classify/dogorcat/$', dogorcat),
    url(r'asr/$', mandarin_asr),
    url(r'sentiment/classifier',sentiment)
]
