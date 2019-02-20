import os
import sys
import io
from django.conf import settings
asrPath=os.path.join(settings.BASE_DIR,"service/tools/ASR/")
sys.path.append(os.path.abspath(asrPath)) 
from SpeechModel251 import ModelSpeech
from LanguageModel import ModelLanguage
import keras

modelpath = os.path.join(asrPath,"model_speech/")
datapath = os.path.join(asrPath,"tempAudio.wav")
print(datapath)
def load_data(req_file: "UploadedFile", mode="RGB")->"numpy.array or None":
    
    fbytes = req_file.read()
    
    try:
        data = []
        #im = io.BytesIO(fbytes)
        with open(datapath,"wb+") as wavfile:
            wavfile.write(fbytes)
        
    except Exception as err:
        print(err)

    return None


def asr_mandarin(req_file:"UploadedFile"):
    load_data(req_file)
    keras.backend.clear_session()
    ms = ModelSpeech(datapath)
    ms.LoadModel(modelpath + 'speech_model251_e_0_step_12000.model')

    r = ms.RecognizeSpeech_FromFile(datapath)

    ml = ModelLanguage('model_language')
    ml.LoadModel()
    str_pinyin = r
    r = ml.SpeechToText(str_pinyin)
    return r
















