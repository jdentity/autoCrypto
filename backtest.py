import pyupbit
import numpy as np

COIN_NAME = "KRW-BTC"
TESTING_DAY = 30
K_VALUE = 0.5

# OHLCV(open, high, low, close, volume) 시가, 고가, 저가, 종가, 거래량
df = pyupbit.get_ohlcv(COIN_NAME, count=TESTING_DAY)
df['range'] = (df['high'] - df['low']) * K_VALUE
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")