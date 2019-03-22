TEMPERATURE_WORD_LIST = ["温度", "気温", "寒い", "暑い", "冷える"]
MOISTURE_WORD_LIST = ["水", "みず", "湿度", "じめじめ", "ジメジメ", "乾", "湿", "カラカラ"]

import response_temperature
import response_moisture
import response_friendship
import info

def response(input_text):
    res = ""
    for word in TEMPERATURE_WORD_LIST:
        if word in input_text:
            res = response_temperature.response()
            info.add_friendship(5)
    for word in MOISTURE_WORD_LIST:
        if word in input_text:
            res = response_moisture.response()
            info.add_friendship(5)
    if res == "":
        res = response_friendship.response(input_text)
        # TODO change info.friendship value here
        info.add_friendship(5)
    return res
