import schedule
import pygame
import time
import requests
import urllib.request
import os


f = open(os.path.dirname(__file__)+"/kakaokey.txt", 'r')
SECRET_KEY =f.readline()
f.close()
SECRET_KEY



url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
request = urllib.request.Request(url)
request.add_header('Host','kakaoi-newtone-openapi.kakao.com')
request.add_header('Content-Type','application/xml')
request.add_header('Authorization',f'KakaoAK {SECRET_KEY}')


#+++++++++++++++++++==firebase db++++++++++++++++++++++++++++++++++++++++


def medicine():
    VoiceName = 'WOMAN_DIALOG_BRIGHT'
    text3 = "할머니! 약 드실 시간이에요. 오늘도 건강한 하루 되세요."
    data = "<speak><voice name='" + VoiceName + "'>" + text3 + "</voice></speak>"
    response = urllib.request.urlopen(request, data = data.encode('utf-8'))

    writeFile=open('medicine_time.mp3','wb')
    writeFile.write(response.read())
    writeFile.close()
    # 음성 출력
    pygame.mixer.init()
    pygame.mixer.music.load("medicine_time.mp3")
    pygame.mixer.music.play()
    time.sleep(7) # 문장이 5초 이상 될 것같은 경우 sleep 시간 조절.
    pygame.mixer.quit()
    