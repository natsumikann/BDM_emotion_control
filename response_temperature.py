import info

HIGHER_BOUND = 15
LOWER_BOUND = 10

def response():
    temp = float((info.get_info_arr())[0])
    response = ""
    if temp > HIGHER_BOUND:
        response = "暑いです"
    elif temp < LOWER_BOUND:
        response = "寒いです"
    else:
        response = "ちょうどいい温度です"

    return response
