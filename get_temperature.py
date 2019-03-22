import Adafruit_DHT as DHT

def get_value():
    SENSOR_TYPE = DHT.DHT22
    DHT_GPIO = 4
    h,t = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)
    return t

