import requests
import urllib
import time
import json
import string
import random
import hashlib
import base64
import openai
import os


class Robot:

    def qingyunke(self, msg):
        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(
            urllib.parse.quote(msg))
        html = requests.get(url)
        return html.json()["content"]

    def xiaobing(self, msg):
        uid = '5175429989'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
        source = '209678993'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
        SUB = '_2A25JAHJRDeRhGeBL6FUY8C7IyziIHXVqdOSZrDV_PUNbm9AGLXP4kW9NRw6OUikg6zuJuocOXnE8Y2LiNFSlyuxQ'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
        url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
        data = {'text': msg, 'uid': uid, 'source': source}
        headers = {
            'cookie': 'SUB=' + SUB,
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'https://api.weibo.com/chat/'
        }
        response = requests.post(url_send, data=data, headers=headers).json()
        sendMsg = response['text']
        time.sleep(1)

        while True:
            url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(
                uid, source)
            response = requests.get(url_get, headers=headers).json()
            getMsg = response['direct_messages'][0]['text']
            if sendMsg == getMsg:
                time.sleep(1)
            else:
                return getMsg

    def tuling(self, msg):
        index = 0
        while True:
            api_key = [
                "618bd2a9b7c6414ebbda21585f0d0752",  # 提供一下我的
            ]
            url = 'http://openapi.tuling123.com/openapi/api/v2'
            data = {
                "perception": {
                    "inputText": {
                        "text": msg
                    },
                },
                "userInfo": {
                    "apiKey": api_key[index],
                    "userId": "1"
                }
            }
            datas = json.dumps(data)
            html = requests.post(url, datas).json()
            if html['intent']['code'] == 4003:
                print(">> 次数用完")
                index += 1
                if index == len(api_key):
                    return None
                else:
                    print(">> 换key重试:", index)
                    time.sleep(1)
                    continue
            break
        return html['results'][0]['values']['text']

    def GPT(self, msg):
        # ip:172.104.73.40
        os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
        os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"
        # Set up the OpenAI API client
        openai.api_key = "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"

        # Set up the model and prompt
        # model_engine = "text-davinci-003"
        model_engine = "gpt-3.5-turbo"

        # Generate a response
        completion = openai.Completion.create(
            model=model_engine,
            prompt=msg,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        return response


if __name__ == '__main__':
    msg = "你好"
    print("原话：你好")  # 原话：你好

    robot = Robot()
    # print(robot.qingyunke(msg))
    # print(robot.tuling(msg))
    # print(robot.xiaobing(msg))  # (不想登微博了，自行测试吧！)
    print(robot.GPT(msg))
