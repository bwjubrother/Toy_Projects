import pyupbit

### 모든 암호화폐 목록
# print(pyupbit.get_tickers())
# print(len(pyupbit.get_tickers()))


### 원화시장 암호화폐 목록
# print(pyupbit.get_tickers(fiat="KRW"))
# print(len(pyupbit.get_tickers(fiat="KRW")))


### 암호화폐 현재가 조회 (최대 100개)
# print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]))


### 시가/고가/저가/종가/거래량을 DataFrame으로 반환 (9시 기준)
'''
*PARAMETERS
count : 이전 영업일수, default 200, max 200)
interval : "조회 단위", day/minute1/minute3/minute5/minute10/minute15/minute30/minute60/minute240/week/month
to : to 파라미터에 입력된 이전 단위(interval)까지의 데이터, ex) "20201010"
'''
# df = pyupbit.get_ohlcv("KRW-BTC", count=100)
# print(df.tail())

'''
### 1000개의 데이터 받아오기
import pandas as pd
import time

date = None
dfs = [ ]

for i in range(5):
    df = pyupbit.get_ohlcv("KRW-BTC", to=date)
    dfs.append(df)

    date = df.index[0]
    time.sleep(0.1)

df = pd.concat(dfs).sort_index()
print(len(df))
'''


### get_orderbook : 매수/매도 호가 정보를 조회
# print(pyupbit.get_orderbook(tickers="KRW-BTC"))


### 로그인
access = "4116937irIHcqjE3ksYR0dfVdri4iTakvxE589zH"          # 본인 값으로 변경
secret = "dKWhdtjm6mc0lNSxFDUsdi5gx1zSpoWxDLxCe4dz"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


## 잔고 조회
# print(upbit.get_balance("KRW-XRP"))
# print(upbit.get_balance("KRW"))
balances = upbit.get_balances()
for i in balances:
    print(i)


### 매수 (예 비트코인)
# print(upbit.buy_limit_order("KRW-BTC", 613, 10))


### 매도 (예 비트코인)
# print(upbit.sell_limit_order("KRW-BTC", 600, 20))


### 시장가 매수 / 매도 (예 리플)
# print(upbit.buy_market_order("KRW-XRP", 10000))
# print(upbit.sell_market_order("KRW-XRP", 30))


### 미체결 주문 조회
# upbit.get_order("KRW-LTC")


### 체결 주문 조회
# print(upbit.get_order("KRW-LTC", state="done"))


### 주문 취소
# print(upbit.cancel_order('50e184b3-9b4f-4bb0-9c03-30318e3ff10a'))


### 웹소켓으로 실시간 현재가, 호가, 체결 정보
'''
from pyupbit import WebSocketManager

if __name__ == "__main__":
    wm = WebSocketManager("ticker", ["KRW-BTC"])
    for i in range(10):
        data = wm.get()
        print(data)
    wm.terminate()
'''


### PyQT 이용
'''
from pyupbit import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import time


class Worker(QThread):
    recv = pyqtSignal(str)
    def run(self):
        # create websocket
        wm = WebSocketManager("ticker", ["KRW-BTC"])
        while True:
            data = wm.get()
            self.recv.emit(data['content']['closePrice'])


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("BTC", self)
        label.move(20, 20)

        self.price = QLabel("-", self)
        self.price.move(80, 20)
        self.price.resize(60, 20)

        button = QPushButton("Run", self)
        button.move(20, 50)
        button.clicked.connect(self.click_btn)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)

    @pyqtSlot(str)
    def receive_msg(self, msg):
        print(msg)
        self.price.setText(msg)

    def click_btn(self):
       self.th.start()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   ex.show()
   app.exec_()
'''


