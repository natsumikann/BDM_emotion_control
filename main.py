# coding:utf-8
import requests
import json
import os
import response
import info
import wave
import sound

if __name__ == '__main__':
    info.init()
    path = "voice.wav"
    recognition_url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY=YOUR_API_KEY"
    dialogue_url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=YOUR_API_KEY"

    # speech recognition
    files = {"a": open(path, "rb"), "v": "on"}
    r = requests.post(recognition_url, files = files)
    print(r.json()['text'])
    # talk
    # TODO if volume is high enough do this
    if (sound.big()==True):
        os.system("jsay "+response.response(r.json()['text']))
        #print(response.response(r.json()['text']))
