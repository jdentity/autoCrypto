import time
import pyupbit
import datetime
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ACCESS_KEY = os.getenv('UPBIT_ACCESS_KEY')          # 본인 값으로 변경
SECRET_KEY = os.getenv('UPBIT_SECRET_KEY')          # 본인 값으로 변경

K_VALUE = 0.2               # K 변수값
KRW_TICKER = "KRW-ETH"      # KRW-코인 티커
TICKER = "ETH"              # 코인 티커

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

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(KRW_TICKER) #9:00
        end_time = start_time + datetime.timedelta(days=1) #9:00 + 1일

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price(KRW_TICKER, K_VALUE)
            current_price = get_current_price(KRW_TICKER)
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order(KRW_TICKER, krw*0.9995)
        else:
            blc = get_balance(TICKER)
            if blc > 5000/get_current_price(KRW_TICKER):
                upbit.sell_market_order(KRW_TICKER, blc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)