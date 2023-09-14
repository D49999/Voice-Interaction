import speech_recognition as sr
from aip import AipSpeech
import json
import pygame
import os
import openai

# 填写代理地址
os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"

# api:gpt-3.5
openai.api_key = "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"

APP_ID = '31346648'
API_KEY = 'tmVOENUGY2nrn723zeZhIaXl'
SECRET_KEY = 'uEPF2wk3jOXePPssleSd9heBofVye9dD'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


class ChatGPT:

    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": "一个具有导航、迎宾等功能的迎宾机器人"}]
        self.filename = "./user_messages.json"

    def ask_gpt(self):
        # q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
        rsp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                           messages=self.messages)
        return rsp.get("choices")[0]["message"]["content"]

    def writeTojson(self):
        try:
            # 判断文件是否存在
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    # 创建文件
                    pass
            # 读取
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}
            # 追加
            msgs.update({self.user: self.messages})
            # 写入
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(msgs, f)
        except Exception as e:
            print(f"错误代码：{e}")


# 录音
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("请提问：")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

    return 1


# 将录制好的音频文件recording.wav上传至百度语音的服务，返回识别后的文本结果并输出。
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    results = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537,
    })
    if 'result' in results:
        print("you said: " + results['result'][0])
        return results['result'][0]
    else:
        print("出现错误，错误代码：", results['err_no'])


# 语音合成
def speak(text=""):
    result = client.synthesis(text, 'zh', 1, {
        'spd': 4,
        'vol': 5,
        'per': 3,
    })

    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)


# 播放音频
def play():
    pygame.mixer.init(
    )  # 初始化混音器模块（pygame库的通用做法，每一个模块在使用时都要初始化pygame.init()为初始化所有的pygame模块，可以使用它也可以单初始化这一个模块）
    pygame.mixer.music.load(
        "C:/Users/DDMonkey/Desktop/STUDY/Python/Pworkplce/VoiceInteraction/audio.mp3"
    )  # 加载音乐 ######大坑，注意这里需要使用绝对路径（就是不是默认当前路径，我恶补一下绝对路径和相对路径）
    pygame.mixer.music.set_volume(0.5)  # 设置音量大小0~1的浮点数
    pygame.mixer.music.play()  # 播放音频
    while pygame.mixer.music.get_busy():  # 在音频播放未完成之前不退出程序
        pass
    pygame.mixer.music.unload()  # 停止加载音频


def main():

    user = 'User'
    chat = ChatGPT(user)

    # 循环
    while 1:
        # 限制对话次数
        if len(chat.messages) >= 11:
            print("******************************")
            print("*********强制重置对话**********")
            print("******************************")
            # 写入之前信息
            chat.writeTojson()
            user = "User"
            chat = ChatGPT(user)

        rec()  # 提问→保存录音文件：recording.wav
        text = listen()  # 调用百度Ai的api，自动打开录音文件recording.wav进行识别,返回识别的文字存到text
        if '结束程序' in text:  # 这里我设置了一个结束语，说“结束程序”的时候就结束，你也可以改掉
            print("*********退出程序**********")
            # 写入之前信息
            chat.writeTojson()
            break

        # text_1 = robot(text)  # 将text中的文字发送给机器人，返回机器人的回复存到text_1
        # speak(text_1)  # 将text_1中机器人的回复用语音输出，保存为audio.mp3文件
        # play()  # 播放audio.mp3文件

        # 提问-回答-记录
        chat.messages.append({"role": "user", "content": text})
        answer = chat.ask_gpt()
        print(f"【ChatGPT】{answer}")
        speak(answer)  # 将text_1中机器人的回复用语音输出，保存为audio.mp3文件
        play()  # 播放audio.mp3文件
        chat.messages.append({"role": "assistant", "content": answer})

        # # 提问
        # q = input(f"【{chat.user}】")

        # # 逻辑判断
        # if q == "0":
        #     print("*********退出程序**********")
        #     # 写入之前信息
        #     chat.writeTojson()
        #     break
        # elif q == "1":
        #     print("**************************")
        #     print("*********重置对话**********")
        #     print("**************************")
        #     # 写入之前信息
        #     chat.writeTojson()
        #     user = input("请输入用户名称: ")
        #     chat = ChatGPT(user)
        #     continue


if __name__ == "__main__":
    main()

# # # TulingBot
# TURING_KEY = "******"
# URL = "http://openapi.tuling123.com/openapi/api/v2"
# HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}

# def robot(text=""):
#     data = {
#         "reqType": 0,
#         "perception": {
#             "inputText": {
#                 "text": ""
#             },
#             "selfInfo": {
#                 "location": {
#                     "city": "广州",
#                     "street": "大学城"
#                 }
#             }
#         },
#         "userInfo": {
#             "apiKey": '1dde879fa943438e9**********',
#             "userId": "123"
#         }
#     }

#     data["perception"]["inputText"]["text"] = text
#     response = requests.request("post", URL, json=data, headers=HEADERS)
#     response_dict = json.loads(response.text)

#     result = response_dict["results"][0]["values"]["text"]
#     print("the AI said: " + result)
#     return result
