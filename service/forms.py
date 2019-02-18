from django import forms

class FaceForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")
    image2 = forms.FileField(label="FaceImage2")


# class FaceForm(forms.Form):
#     image1 = forms.CharField(max_length=200, label="url of image1")
#     image2 = forms.CharField(max_length=200, label="url of image2")


class PlateForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")
