import pyautogui as pag
import keyboard
import re
import time

#위치값 저장
with open('position.txt', 'r') as f:
    contents = f.read()
content_list = contents.split("\n")
dateDic = {}
_2F = {}
_3F = {}
dic_list = [dateDic, _2F, _3F]
idx = 0
for content in content_list:
    matches = re.findall(r'(\w+):\[(\d+), (\d+)\]', content)
    for match in matches:
        key = match[0]
        value = [int(match[1]), int(match[2])]
        dic_list[idx][key] = value
    idx+=1
################ 티케팅 코드 ###############
def clicker(xy):
    pag.click(xy[0],xy[1])

def checkChair():
    
while True:
    if keyboard.is_pressed("F3"): #실행
        print(pag.size())
        #날짜 선택
        clicker(dateDic['date2'])
        clicker(dateDic['ticketingBtn'])
        time.sleep(0.2)
        #좌석 선택
        nextBtn=[1643, 1263]
        while True:
            if pag.pixelMatchesColor(nextBtn[0],nextBtn[1],(204,204,204)):
                break
        clicker((dic_list[1]['12']))

