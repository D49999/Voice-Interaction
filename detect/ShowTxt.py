import speech_recognition as sr  # pyaudio SpeechRecognition模块
from aip import AipSpeech
import win32com.client as win
import time

APP_ID = '31346648'
API_KEY = 'tmVOENUGY2nrn723zeZhIaXl'
SECRET_KEY = 'uEPF2wk3jOXePPssleSd9heBofVye9dD'  # 这三个输入你自己的接口账号密钥哈，我就不放了，有需要可以找我要

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
speak = win.Dispatch("SAPI.SpVoice")


def rec(rate=16000):  # 从系统麦克风拾取音频数据，采样率为 16000
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        speak.Speak('您好，请问您要去几楼？')
        print("您好，请问您要去几楼？")  # 这里会打印please say something，提示你说话进行录音
        time.sleep(0.1)
        audio = r.listen(source)

    with open("recording.wav",
              "wb") as f:  # 把采集到的音频数据以 wav 格式保存在当前目录下的recording.wav 文件
        f.write(audio.get_wav_data())
    return 1


rec()  # 运行rec函数，录制音频


def listen():
    with open('recording.wav',
              'rb') as f:  # 将录制好的音频文件recording.wav上传至百度语音的服务，返回识别后的文本结果并输出。
        audio_data = f.read()

    results = client.asr(
        audio_data,
        'wav',
        16000,
        {
            'dev_pid':
            1537,  # 这里的results是一个字典，文本内容在Key名字为result对应的值，这里我恶补了一点字典的知识
        })
    if 'result' in results:
        print('已发送去' + results['result'][0] + '的指令')
        print(
            "正在前往的楼层是:" + results['result'][0]
        )  # results['result']这个是输出Key名字为result对应的值，也就是我们要的文本，至于后面[0]有什么用我还没搞明白，
        speak.Speak('电梯运行中，正在前往' + results['result'][0])
        return results['result'][0]
    else:
        print("出现错误，错误代码：", results['err_no'])  # 不存在result就返回错误代码err_no


listen()  # 运行listen函数，将录音转成文字
