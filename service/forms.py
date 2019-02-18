from django import forms

class FaceForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")
    image2 = forms.FileField(label="FaceImage2")


class FaceInPhotoForm(forms.Form):
    image1 = forms.FileField(label="FaceImage")
    image2 = forms.FileField(label="PhotoImage")


class PlateForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")
