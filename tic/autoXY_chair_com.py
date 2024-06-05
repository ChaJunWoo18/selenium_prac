import pyautogui as pag
import keyboard
import time

_2F = {10:[],11:[],12:[]}

def findXY():
    position = pag.position()
    xy = [position.x, position.y]
    time.sleep(0.3)
    return xy

# _2F 10,11,12 좌석 좌표 채우기
while True:
    if keyboard.is_pressed("F4"): #좌표 찾기
        loc = findXY()
        _2F[10].append(loc)
    if keyboard.is_pressed("F8"): #좌표 찾기
        loc = findXY()
        _2F[11].append(loc)
    if keyboard.is_pressed("F9"): #좌표 찾기
        loc = findXY()
        _2F[12].append(loc)
    if keyboard.is_pressed("F3"):
        break


######################################33
with open('chair.txt', 'a') as f:
    for name,xy in _2F.items():
        f.write(f'{name}:{xy} ')
        f.write("\n")