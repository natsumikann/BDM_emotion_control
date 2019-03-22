#!/bin/bash

# python3 init_led.py
while :
do
  sudo rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 voice.wav trim 0 3
  python3 main.py
  python3 control_led.py
done

python3 stop_led.py
