import pyautogui as pag
import keyboard
import time


dateDic = {'date1': None,'date2':None,'ticketingBtn':None}
_2F = {9: None,10:None,11:None,12:None,13:None,14:None,15:None,16:None,17:None,18:None}
_3F = {27: None, 28: None, 29: None, 30: None, 31: None, 32: None, 33: None, 34: None, 35: None, 36: None}

def findXY():
    position = pag.position()
    xy = [position.x, position.y]
    time.sleep(0.3)
    return xy

def findColor():
    xy = pag.position()
    img = pag.screenshot()
    print(img.getpixel(xy))   
    print(xy) 

def fill_dict(preDic, dictionary, loc):
    all_values_not_none = all(value is not None for value in preDic.values())
    if all_values_not_none:
        for key, value in dictionary.items():
            if value is None:
                dictionary[key] = loc
                break

while _3F[36] is None:
    if keyboard.is_pressed("F4"): #좌표 찾기
        loc = findXY()
        for key, value in dateDic.items():
            if value is None:
                dateDic[key] = loc
                break
        # _2F 채우기
        fill_dict(dateDic,_2F, loc)
        # _3F 채우기
        fill_dict(_2F,_3F, loc)

    if keyboard.is_pressed("F3"):
        findColor()
        break

######################################33
with open('position.txt', 'w') as f:
    for name,xy in dateDic.items():
        f.write(f'{name}:{xy} ')
    f.write('\n')
    for name,xy in _2F.items():
        f.write(f'{name}:{xy} ')
    f.write('\n')
    for name,xy in _3F.items():
        f.write(f'{name}:{xy} ')