import info
def response():
    res = ""
    if int(info.get_info_arr()[1]) < 300:
      res = "乾燥しています"
    elif int(info.get_info_arr()[1]) > 800:
      res = "水が多すぎます"
    else:
      res = "ちょうどいいです"
    return res
