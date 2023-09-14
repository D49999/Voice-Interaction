from aip import AipSpeech

APP_ID = '31346648'
API_KEY = 'tmVOENUGY2nrn723zeZhIaXl'
SECRET_KEY = 'uEPF2wk3jOXePPssleSd9heBofVye9dD'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# result = client.synthesis('你好百度', 'zh', 1, {
#     'vol': 5,
# })

# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('audio.mp3', 'wb') as f:
#         f.write(result)
# print(result)


def speak(text=""):
    result = client.synthesis(
        text,
        'zh',
        1,
        {  # 这里的参数可以调zh表示中文
            'spd': 4,  # 语速
            'vol': 5,  # 音量
            'per': 4,  # 类型
        })
    if not isinstance(result, dict):
        print('3')
        with open(
                'audio.mp3', 'wb'
        ) as f:  # 保存为当前目录下mp3格式的音频：audio.mp3，不建议用wav格式，wav格式后面我用的是pagame播放无法识别
            f.write(result)
            f.close
    print(result)


speak('你好小度')  # 运行speak函数,把机器人回复的文字转换成语音
