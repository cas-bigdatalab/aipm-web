# from django.urls import path
from django.conf.urls import url

from .views import face_similarity, plate_recognition,dogorcat

urlpatterns = [
    url(r'face/similarity/$', face_similarity),
    url(r'plate/$', plate_recognition),
    url(r'classify/dogorcat$', dogorcat)
]
