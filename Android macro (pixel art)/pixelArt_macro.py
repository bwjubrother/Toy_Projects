from ppadb.client import Client
import cv2, time
import numpy as np

SKIP_PIXELS = 9
TARGET_COLOR = [139, 139, 139]

palette = [
    [105, 1700],
    [320, 1700],
    [530, 1700],
    [750, 1700],
    [950, 1700],
    [105, 1900],
    [320, 1900],
    [530, 1900],
    [750, 1900],
    [950, 1900],

]

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

    '''
    # 캡쳐한 이미지 보기
    img = cv2.resize(img, dsize=None, fx=0.3, fy=0.3)
    cv2.imshow('img', img)
    if cv2.waitKey(0) == ord('q'):
        exit()
    '''

    return img

page = 0

while True:
    for i, p in enumerate(palette):
        print('[*] Painting color %d...' % (page * 10 + i + 1))
        device.input_tap(p[0], p[1])

        img = take_screenshot()

        for y in range(300, img.shape[0] - 900, 9):
            for x in range(47, img.shape[1] - 47, 9):
                pixel = img[y, x]

                if np.array_equal(pixel, TARGET_COLOR):
                    tap_x = x + 10
                    tap_y = y + 10

                    print('TAP (%d, %d)' % (tap_x, tap_y))
                    device.input_tap(tap_x, tap_y)

                    img = take_screenshot()

    device.input_swipe(1000, 1800, 500, 1800, 300)
    page += 1

