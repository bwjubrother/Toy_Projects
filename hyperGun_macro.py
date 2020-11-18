from ppadb.client import Client
import cv2, time
import numpy as np

TARGET_COLOR = [65, 225, 71] # B G R

client = Client(host='127.0.0.1', port=5037)

devices = client.devices()

if len(devices) == 0:
    print('연결된 기기가 없습니다.')
    exit()

device = devices[0]

def take_screenshot():
    img_byte = device.screencap()
    img = cv2.imdecode(np.frombuffer(img_byte, np.uint8), flags=-1)
    if img.all() != None:
        img = img[:, :, :3]

    return img

print('Game start')

while True:
    img = take_screenshot()

    for y in range(0, 700, 9):
        for x in range(900, 1100, 9):
            pixel = img[y, x]

            if np.array_equal(pixel, TARGET_COLOR):
                device.input_tap(500, 500)
                print('hit left')
    
    for y in range(0, 700, 9):
        for x in range(1100, 1300, 9):
            pixel = img[y, x]

            if np.array_equal(pixel, TARGET_COLOR):
                device.input_tap(1500, 500)
                print('hit right')

# Target Range                
# X : 900 1100 1300
# Y : 0 700