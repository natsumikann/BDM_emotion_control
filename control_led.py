import wiringpi as pi,time
import time
import info
#start


if __name__ == "__main__":
    #jikannde ugokashitai

    data = info.get_info_arr()
    temp = int(float(data[0]))
    moist = int(data[1])
    friend = int(data[2])

    #debug
    print(data)
    
    #temperature
    temperature_high = 0
    temperature_low = 0
    if temp > 15:
        temperature_high = int((temp-15)/(35-15)*100)
    elif temp < 10:
        temperature_low = int((10-temp)/(10-(-10))*100)
    
    #humidity
    humidity_high = 0
    humidity_low = 0
    if moist > 800:
        humidity_high = int((moist-800)/(1200-800)*100)
    elif moist < 600:
        humidity_low = int((600-moist)/600*100)
    
    #friendship
    friendship = 0
    if friend < 50:
        friendship = int((50-friend)/50*100) # friendship upper limit
    
    ## LED
    
    pi.wiringPiSetupGpio()
    pi.pinMode(22,0)
    pi.pinMode(17,0)
    pi.pinMode(27,0)
    
    pi.softPwmCreate(22, 0, 100)
    pi.softPwmCreate(17, 0, 100)
    pi.softPwmCreate(27, 0, 100)   
    
    #red 22
    pi.softPwmWrite(22, max([temperature_high, temperature_low]))
    #green 17
    pi.softPwmWrite(17, friendship)
    #blue 27
    pi.softPwmWrite(27, max([humidity_high, humidity_low]))
    """
    pi.pinMode( LED_PIN, pi.OUTPUT)
    pi.softPwmCreate(LED_PIN, 0, 100)

    if Color == 0:
        value = temperature_high
    if Color == 1:
        value = temperature_low
    if Color == 2:
        value = friendship
    if Color == 3:
        value = humidity_high
    if Color == 4:
        value = humidity_low

    if Color == 0 and Color == 1 and Color == 3 and Color == 4 and Color == 5:
        pi.softPwmWrite(LED_PIN,value)
        time.sleep(5)

        pi.digitalWrite( LED_PIN, pi.LOW )

    if Color == 2:
        start_time = time.time() + 5
        pi.softPwmWrite(LED_PIN,value)
        time.sleep(5)

        while True:
            pi.digitalWrite(LED_PIN,value)
            time.sleep(0.5)
            pi.digitalWrite(LED_PIN,0)
            time.sleep(0.5)
            if (time.time() - start_time > 5):
                break
    """
