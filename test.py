# import pyautogui as pag

# while True:
#     x, y = pag.position()
#     print('x: %s, y: %s' % (x, y))

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('00:00', end='\r')
    
countdown(90)
exit()