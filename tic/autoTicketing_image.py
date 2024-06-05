#이미지티케팅의 경우 성능이 많이 떨어짐
import pyautogui as pag
import keyboard
import re
import time
from PIL import Image
from colorCheck_com import get_matching_color_coordinates
#12:[945, 952]

#위치값 저장
with open('position.txt', 'r') as f:
    contents = f.read()
content_list = contents.split("\n")
dateDic = {}
_2F = {}
dic_list = [dateDic, _2F]
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

# 특정 색상 설정
target_color1 = (72, 36, 232) 
target_color2 = (57, 201, 227)

#width, height구하기
top_left = [504, 628]
bottom_right = [1006, 1026]
width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]

# 원하는 위치와 크기 설정 (예: (x, y, width, height))
region = (top_left[0], top_left[1], width, height) 

while True:
    if keyboard.is_pressed("F3"): #실행
        #print(pag.size())
        #날짜 선택
        clicker(dateDic['date2'])
        time.sleep(0.1)
        clicker(dateDic['ticketingBtn'])
        time.sleep(0.3)
        #좌석 선택
        nextBtn=[1643, 1263]
        while True:
            if pag.pixelMatchesColor(nextBtn[0],nextBtn[1],(204,204,204)):
                break
        clicker((dic_list[1]['10']))
        while True:
            if not pag.pixelMatchesColor(898,666,(0, 204, 255)):
                if pag.pixelMatchesColor(288,397,(244,244,244)):
                    break
        #화면 축소
        pag.click(1461, 1178, clicks=2)
        # 특정 영역 스크린샷
        screenshot = pag.screenshot(region=region)
        screenshot.save('screenshot.png')
        matching_coord = get_matching_color_coordinates(screenshot, target_color1, target_color2)
        time.sleep(1)
        print(matching_coord)
        pag.click(top_left[0] + matching_coord[0], top_left[1] + matching_coord[1])
