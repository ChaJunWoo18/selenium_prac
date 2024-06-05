from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
import seatGenerator

chair10 = seatGenerator.chair10()
chair11 = seatGenerator.chair11()
chair12 = seatGenerator.chair12()

chrome_options = Options()
chrome_options.add_experimental_option('detach',True) #실행 후 자동 종료 방지
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

ticketing_url = 'https://ticket.wemakeprice.com/product/3000011741'
wait = WebDriverWait(driver,15)
driver.get(ticketing_url)

def getElement(CSS_SELECTOR):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))

#로그인
loginMenu = getElement('#header > div.u-global-width > div.util-menu > a:nth-child(1)')
loginMenu.click()
loginId = getElement('#_loginId')
loginPw = getElement('#_loginPw')
loginBtn = getElement('#_userLogin')
loginId.send_keys('wnsdnxla@naver.com')
loginPw.send_keys('vmfhrmfoaj18!')
loginBtn.click()

# 원래 창의 핸들 저장
original_window = driver.current_window_handle

while True:
    #키보드를 누르면 실행 'F4'(F4누를 때까지 대기)
    if keyboard.is_pressed('F4'):
        break
#날짜 선택
dayChecker = getElement('#prodSdString')
print(dayChecker.text)
while dayChecker.text == '날짜를 선택해 주세요.':
    Sat = getElement('#calendarTicket > ul.time-list.list-change-event > li:nth-child(1) > a')
    Sun = getElement('#calendarTicket > ul.time-list.list-change-event > li:nth-child(2) > a')
    Sat.click()
    time.sleep(0.1)
dateBtn = getElement('#calendarTicket > button.btn.ticketing.seatReservation')
dateBtn.click()

# 새 창이 열릴 때까지 대기
wait.until(EC.number_of_windows_to_be(2))
# 새 창으로 전환
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
#좌석선택  #11,12 rgb : 57,201,227, 10 rgb : 72,36,232 , 구매불가 : (175,175,175)
non_target_color = "rgb(175, 175, 175)"
iframe = getElement("iframe[name='oneStopFrame']")
driver.switch_to.frame(iframe)
seat10 = getElement('#ez_eln5a64cy1 > tspan:nth-child(2)') 
seat11 =getElement('#ez_ewuwded0bn > tspan:nth-child(2)')
seat12 = getElement('#ez_e1iv6vhos4 > tspan:nth-child(2)')

seat_list = [seat10,seat11,seat12]
chair_list = [chair10, chair11, chair12]
#좌석 찾을때까지 반복
findSuc = True
seat_idx = 0
while findSuc: # 11 > 10 > 12
    if keyboard.is_pressed('F8'):
        driver.quit()
    seat_idx += 1
    if seat_idx==4:
        seat_idx =0
    seat_list[seat_idx].click()
    for i in range(len(chair_list[seat_idx])):
        for el in chair_list[seat_idx][i]:
            if keyboard.is_pressed('F9'):
                break
            c = getElement(el)
            style = c.get_attribute("style")
            color = style.split("fill: ")[1].split(";")[0]
            if color != non_target_color:
                c.click()
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                except Exception:
                    pass
                findSuc = False
                break
        if findSuc==False:
            break
    if findSuc:
        #홈으로 갑니다
        homeBtn = getElement('#oneStop-wrap > div.seat-container > div.seat-content > div.center-area > div.btn-map > button.btn-home')
        homeBtn.click()
#클릭성공
to2step = getElement('#nextTicketSelection')
time.sleep(0.2)
to2step.click()

#가격선택
selectBox = getElement('#partTicketType > tbody > tr:nth-child(2) > td > div > div > span')
selectBox.click()
time.sleep(0.3)
one = getElement('#partTicketType > tbody > tr:nth-child(2) > td > div > div > ul > li:nth-child(2)')
one.click()
to3step = getElement('#nextPayment')
time.sleep(0.2)
to3step.click()

#결제/수령방법
checkbox1 = getElement('#dForm > div > div.oneStop-content > div:nth-child(5) > div > ul > li:nth-child(1) > div.top-area > label')
checkbox2 = getElement('#dForm > div > div.oneStop-content > div:nth-child(5) > div > ul > li:nth-child(2) > div.top-area > label')
#수령방법은 선택해주지않습니다.
findAddrBtn = getElement('#part_delivery_info > table > tbody > tr:nth-child(3) > td > div:nth-child(1) > a')
findAddrBtn.click()

# 현재 창 핸들 저장
main_window = driver.current_window_handle
# 모든 창 핸들 가져오기
all_windows = driver.window_handles
# 새 창 핸들 찾기
for window in all_windows:
    if window != main_window and window != original_window:
        new_window = window
        break

driver.switch_to.window(new_window)
#주소
inputAddr = getElement('#postTxt1')
inputAddr.send_keys('덕소로 150')
btnAddr = getElement('#layer-pop-address > div > div > div.search-box > div > button')
btnAddr.click()
time.sleep(0.3)
selectAddr = getElement('#postResultUl1 > li > a')
selectAddr.click()
 
driver.switch_to.window(main_window)
iframe = getElement("iframe[name='oneStopFrame']")
driver.switch_to.frame(iframe)
addrDetail = getElement('#delivAddrDtl')
addrDetail.send_keys('108동 1902호')
#카드선택
cardCompany = getElement('#partPaymentCard > table > tbody > tr:nth-child(1) > td > div > div > span')
kb = getElement('#partPaymentCard > table > tbody > tr:nth-child(1) > td > div > div > ul > li:nth-child(6)')
cardCompany.click()
time.sleep(0.3)
kb.click()
halbu = getElement('#partPaymentCard > table > tbody > tr:nth-child(2) > td > div.select-w195 > div > span')
halbu.click()
time.sleep(0.3)
nohalbu = getElement('#partPaymentCard > table > tbody > tr:nth-child(2) > td > div.select-w195 > div > ul > li:nth-child(2)')
nohalbu.click()
#체크박스
checkbox1.click()
checkbox2.click()
toLastStepBtn = getElement('#btnFinalPayment')
time.sleep(0.2)
#toLastStepBtn.click()
