import requests
import json

def response(input_text):
    dialogue_url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=634f436833326d46654a316b5635473936307739594253335258565955584333452e754658596150497632"
    payload = {
      "utt": input_text,
      "context": "",
      "nickname": "ゆい",
      "nickname_y": "ゆい",
      "sex": "女",
      "bloodtype": "A",
      "birthdateY": "1997",
      "birthdateM": "2",
      "birthdateD": "14",
      "age": "21",
      "constellations": "蟹座",
      "place": "東京",
      "mode": "dialog",
    }
    r = requests.post(dialogue_url, data=json.dumps(payload))
    return r.json()['utt']
