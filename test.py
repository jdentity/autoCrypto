import os
import pyupbit
from dotenv import load_dotenv

load_dotenv(verbose=True)

ACCESS_KEY = os.getenv('UPBIT_ACCESS_KEY')          # 본인 값으로 변경
SECRET_KEY = os.getenv('UPBIT_SECRET_KEY')          # 본인 값으로 변경
upbit = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
