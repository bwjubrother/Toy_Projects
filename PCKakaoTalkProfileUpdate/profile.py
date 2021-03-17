import pyautogui as pg
import time
import keyboard

# 좌표 객체 얻기 
# while True:
#     position = pg.position()
#     print(position)

while True:
    ## 프로필 업데이트 된 사람 찾기
    dot_location = pg.locateOnScreen('dot.png')
    if keyboard.is_pressed('F3'):
        break
    if dot_location == None:
        pg.moveTo(1664, 508)
        pg.click()
        pg.scroll(-500)
    else:
        profile_x = dot_location.left + 15
        profile_y = dot_location.top + 15
        ## 프로필 클릭
        pg.moveTo(profile_x, profile_y)
        pg.click()

        ## 1374, 828 프로필 사진 클릭
        pg.moveTo(1374, 828)
        pg.click()
        time.sleep(3)
exit()