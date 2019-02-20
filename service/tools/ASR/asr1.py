#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SpeechModel251 import ModelSpeech
from LanguageModel import ModelLanguage
import sys
import jieba



modelpath = './model_speech/'
datapath = './data/'

ms = ModelSpeech(datapath)
ms.LoadModel(modelpath + 'speech_model251_e_0_step_12000.model')

r = ms.RecognizeSpeech_FromFile(datapath+'temp.wav')

#print('*[提示] 语音识别结果：\n',r)

ml = ModelLanguage('model_language')
ml.LoadModel()
str_pinyin = r
r = ml.SpeechToText(str_pinyin)
print(r)


#print('语音转文字结果：\n',r)
#print('Full Mode:'+'/'.join(words_list))
















