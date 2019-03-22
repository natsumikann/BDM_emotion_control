# -*- coding: utf-8 -*-
import pygame.mixer
import time
musicmode = 0
# メイン
def main():
    if friendship == 90 and musicmode == 0:
        musicmode = 1
        pygame.mixer.init(frequency = 44100)    # 初期設定
        pygame.mixer.music.load("hana.mp3")     # 音楽ファイルの読み込み
        pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
        time.sleep(100)                         # 音楽の再生時間
        pygame.mixer.music.stop()               # 再生の終了
        musicmode = 0
if __name__ == '__main__':
    main()
