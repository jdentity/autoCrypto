# autoCrypto
automated cryptocurrency trading by python

## Ubuntu server command
- server time setting at Korean : sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
- package update : sudo apt update
- pip3 install : sudo apt install python3-pip
- pyupbit install : pip3 install pyupbit
- background run : nohup python3 bitcoinAutoTrade.py > output.log &
- check running process : ps ax | grep .py
- kill process : kill -9 PID

source : https://github.com/youtube-jocoding/pyupbit-autotrade