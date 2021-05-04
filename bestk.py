import pyupbit
import numpy as np

COIN_NAME = "KRW-BTC"
TESTING_DAY = 90

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv(COIN_NAME, count=TESTING_DAY)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.05, 1.0, 0.05):
    ror = get_ror(k)
    print("%.2f %f" % (k, ror))