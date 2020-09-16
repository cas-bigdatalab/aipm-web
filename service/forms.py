from django import forms

class FaceFeatureForm(forms.Form):
    image = forms.FileField(label="FaceImage")

class FaceForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")
    image2 = forms.FileField(label="FaceImage2")

class FaceInPhotoForm(forms.Form):
    image1 = forms.FileField(label="FaceImage")
    image2 = forms.FileField(label="PhotoImage")


class PlateForm(forms.Form):
    image1 = forms.FileField(label="FaceImage1")


class BinClassifyForm(forms.Form):
    image1 = forms.FileField(label="Image")


class ASRForm(forms.Form):
    audio1 =forms.FileField(label="Audio")


class SentimentForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class TextSegmentForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)
