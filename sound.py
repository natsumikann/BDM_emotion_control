import wave
import numpy as np
from statistics import mean

def big():
    wav = wave.open("./voice.wav")
    wav.rewind()
    wavdata = wav.readframes(wav.getnframes())
    wavdata = np.frombuffer(wavdata,'int16')
    print(wavdata)
    print(max(wavdata))
    if max(wavdata) > 100:
        return True
    else:
        return False

if __name__=="__main__":
    big()
