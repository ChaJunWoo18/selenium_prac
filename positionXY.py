import pyautogui as pag
import keyboard
import time

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

while True:
    if keyboard.is_pressed("F3"):
        print(findXY())
    if keyboard.is_pressed("F4"):
        findColor()