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

##########의자 정보 가져오기#################
with open('chair.txt', 'r') as file:
    lines = file.readlines()
chair = {}
# 필요한 값을 추출하여 딕셔너리에 저장
for line in lines:
    # 각 줄이 "번호:값" 형태인지 확인
    if ':' in line:
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        
        # 문자열 형태의 좌표 리스트를 파싱
        value = value.replace('[[', '').replace(']]', '').replace('], [', '];[')
        coords = value.split(';')
        coords = [list(map(int, coord.replace('[', '').replace(']', '').split(','))) for coord in coords]
        
        # 딕셔너리에 저장
        chair[int(key)] = coords

################ 티케팅 코드 ###############
def clicker(xy):
    pag.click(xy[0],xy[1])

def checkChair(chairNum):
    for c in chair[chairNum]:
        clicker(c)

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
        #좌표 클릭하기
        checkChair(10)