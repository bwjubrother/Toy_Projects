import time
import pyupbit
import datetime
import requests

access = "YOUR-UPBIT-ACCESS-KEY"
secret = "YOUR-UPBIT-SECRET-KEY"
myToken = "YOUR-SLACK-TOKEN-KEY"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(coin):
    """해당 코인 잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_balances_profits(now):
    """내 잔고와 수익률 조회"""
    balances = upbit.get_balances()
    message = '현재 시간: ' + str(now) + '\n'
    for b in balances:
        if b['currency'] == 'KRW':
            message += '보유 현금: ' + str(round(float(b['balance']), 0)) + '\n'
        else:
            ticker = 'KRW-' + b['currency']
            current_price = int(get_current_price(ticker))
            profit = (current_price - int(b['avg_buy_price'])) / int(b['avg_buy_price'])
            profit = round(profit*100, 2)
            message += b['currency'] + ": 수익률 " + str(profit) + " 현재가 " + str(format(current_price,',')) + " 매수단가 " + str(format(int(b['avg_buy_price']), ',')) + "\n"
    return message


def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#btc", "autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        """30분 마다 잔고 수익률 메세지"""
        if now.minute % 30 == 0 and now.second % 60 == 0:
            message = get_balances_profits(now)
            post_message(myToken,"#btc", message)

        '''
        """변동성 돌파 전략 자동 매수, 매도"""
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    post_message(myToken,"#btc", "BTC buy : " +str(buy_result))
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#btc", "BTC buy : " +str(sell_result))
        '''


        time.sleep(0.5)
        
        
    except Exception as e:
        print(e)
        post_message(myToken,"#btc", e)
        time.sleep(1)