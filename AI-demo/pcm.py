#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pcm.py
@Time    :   2019/12/10 12:02:28
@Author  :   LiJu Tsang
@Version :   1.0
@Contact :   zengliju60@gmail.com,957790617@qq.com
@Desc    :   None
'''
from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '16007034'
API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def change_to_mp3(content='请输入要转换的文字内容，这是默认测试内容',turn=1,mp3_name='test'):
    result  = client.synthesis(content, 'zh', 1, {
        'vol': 5,'per':0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
        if turn:
            os.system("ffmpeg -y  -i auido.mp3  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s.pcm"%(mp3_name))
            #os.system("ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s"%(wav_file,pcm_file))


def audio_test():
    APP_ID = '16007034'
    API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
    SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    with open('test.pcm','rb') as f:
        file_pcm = f.read()

    res = client.asr(file_pcm,'pcm',16000,{
    'dev_pid':1537,
    })

    print(res)
    print('百度识别结果：{}'.format(res['result'][0]))
change_to_mp3('今天天气真好，我们去学习吧!')
audio_test()










import speech_recognition as sr

def rec1(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())


import pyaudio
import wave
input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "音频存储位置"              # 输入文件的path
in_path = input_filepath + input_filename

def get_audio(filepath):
    aa = str(input("是否开始录音？   （是/否）"))
    if aa == str("是") :
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*10, "开始录音：请在5秒内输入语音")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    elif aa == str("否"):
        exit()
    else:
        print("无效输入，请重新选择")
        get_audio(in_path)

# 联合上一篇博客代码使用，就注释掉下面，单独使用就不注释
#get_audio(in_path)

#rec1()