import pyautogui as pag
import keyboard

while True:
    if keyboard.is_pressed("F3"):
    #print(pag.size())
        date = [1847, 616]
        date2 = [1863, 678]
        ticketingBtn = [1855,858]
        pag.click(date2[0],date2[1])
        pag.click(ticketingBtn[0],ticketingBtn[1])

        #가격선택
        nextBtn = [1479, 1107]
        while True:
            if pag.pixelMatchesColor(nextBtn[0],nextBtn[1],(204,204,204)):
                break
        selectBox =[1193,416]
        one = [1164,539]
        pag.click(selectBox[0],selectBox[1])
        pag.click(one[0],one[1])
        next = [1580,1105]
        pag.click(x=1580,y=1105,interval=0.2)

        #결제페이지
        payPageNextBtn = [1612,1165]
        while pag.pixelMatchesColor(payPageNextBtn[0],payPageNextBtn[1],(204,204,204)):
            break
        print('카드사를 선택합니다.')
        pag.press("space", interval=0.5)
        cardCompany=[757,285]
        KB = [683, 642]
        payOption = [743,366]
        payInFull = [689,492]
        checkbox1 = [237, 641]
        checkbox2 = [231, 865]
        pag.click(cardCompany[0],cardCompany[1], interval=0.1)
        pag.click(KB[0],KB[1])
        pag.click(payOption[0],payOption[1], interval=0.1)
        pag.click(payInFull[0],payInFull[1])
        pag.click(checkbox1[0],checkbox1[1])
        pag.click(checkbox2[0],checkbox2[1])
        while True:
            if not pag.pixelMatchesColor(payPageNextBtn[0],payPageNextBtn[1],(204,204,204)):
                pag.click(payPageNextBtn[0],payPageNextBtn[1])
                break
# #글자 타이핑 
# pag.typewrite("글자")
# #키보드 누르기
# pag.press('tab')