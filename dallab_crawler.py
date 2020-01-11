import requests
import json
import telegram
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

# .env에서 값 가져오기
load_dotenv()
bot_token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telegram.Bot(token=bot_token)


def get_latest_event():
    url = 'https://festa.io/api/v1/organizations/528/events?page=1&pageSize=1&order=eventId'
    data = requests.get(url)
    events = json.loads(data.text)
    return events['rows'][0]


current_eventId = get_latest_event()['eventId']  # 실행시점 가장 큰 eventId 저장


def check_new_event():
    global current_eventId  # current_eventId를 global변수로 사용

    latest_event = get_latest_event()
    latest_eventId = latest_event['eventId']  # 반복 실행되면서 가장 큰 eventId 저장

    if (latest_eventId > current_eventId):  # 새로운 이벤트가 만들어지면 실행
        event_name = latest_event['name']
        event_url = 'https://festa.io/events/'+str(latest_eventId)
        # 원하는 message형태를 만듦
        message = event_name+'의 티켓이 오픈되었습니다.\n바로가기 : '+event_url
        bot.send_message(chat_id=chat_id, text=message)
        current_eventId = latest_eventId  # current_eventId를 업데이트


sched = BlockingScheduler()
sched.add_job(check_new_event, 'interval', seconds=30)
sched.start()
