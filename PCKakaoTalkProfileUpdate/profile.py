import pyautogui as pg
import time
import keyboard

# 좌표 객체 얻기 
# while True:
#     position = pg.position()
#     print(position)

print('*******************************************************')
print('\n')
print('안녕하세요 카톡 프로필 바뀐 사람 모아보기 프로그램입니다.')
print('* 카톡은 PC화면의 오른쪽 아래 모서리에 위치시켜 주세요.')
print('* 친구목록을 최상단에 위치시켜 주세요.')
print('\n')
print('----------------------------------------------------')
print('위치하셨다면 "F3"을 눌러 프로그램을 실행시켜 주세요.')
print('프로그램 종료는 ESC를 눌러주세요.')

while True:
    if keyboard.is_pressed('F3'):
        cnt = 0
        while True:
            if keyboard.is_pressed('esc'):
                print('프로필 갱신한 사람: ' + cnt + '명을 확인했습니다.')
                time.sleep(3)
                exit()
            ## 프로필 업데이트 된 사람 찾기
            dot_location = pg.locateOnScreen('dot.png')
            if dot_location == None:
                pg.moveTo(1664, 508)
                pg.click()
                pg.scroll(-500)
            else:
                cnt += 1
                profile_x = dot_location.left + 15
                profile_y = dot_location.top + 15
                ## 프로필 클릭
                pg.moveTo(profile_x, profile_y)
                pg.click()

                ## 1374, 828 프로필 사진 클릭
                pg.moveTo(1374, 828)
                pg.click()
                time.sleep(3)
        
    elif keyboard.is_pressed('esc'):
        exit()
