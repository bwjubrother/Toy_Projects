import pyupbit
from pyupbit import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


### 로그인
access = "4116937irIHcqjE3ksYR0dfVdri4iTakvxE589zH"
secret = "dKWhdtjm6mc0lNSxFDUsdi5gx1zSpoWxDLxCe4dz"
upbit = pyupbit.Upbit(access, secret)


# balances = upbit.get_balances()
# for i in balances:
#     print(i)


class Worker(QThread):

    def run(self, ticker):
        # create websocket
        wm = WebSocketManager("ticker", [ticker])
        while True:
            data = wm.get()
            print(data)




if __name__ == '__main__':
    balances = upbit.get_balances()
    for balance in balances:
        ticker = balance['currency']
        th = Worker()
        th.run(ticker)
    th.start()