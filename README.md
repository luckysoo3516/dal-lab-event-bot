# 달랩 이벤트 알리미
source : [https://festa.io/hosts/528](https://festa.io/hosts/528)

## EC2 - ubuntu 18.04 세팅
```bash
sudo apt-get update
sudo apt install python3-pip
```

## 모듈 설치
```python
pip3 install requests
pip3 install bs4
pip3 install apscheduler
pip3 install python-telegram-bot
pip3 install python-dotenv
```

## git clone
```git
cd ~
git clone https://github.com/luckysoo3516/dal-lab-event-bot.git
```

## Write `.env` file
```bash
TOKEN = <Your Bot Token Id>
CHAT_ID = <Your Chat Id>
```

## Background로 실행
```bash
nohup python3 dallab_crawler.py &
```