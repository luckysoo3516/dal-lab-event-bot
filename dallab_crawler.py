import requests
import json
import telegram
import os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

CURRENT_EVENT_ID = 838

load_dotenv()
bot_token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telegram.Bot(token=bot_token)

current_eventId = CURRENT_EVENT_ID


def job_function():
    global current_eventId
    url = 'https://festa.io/api/v1/organizations/528/events?page=1&pageSize=15&order=startDate'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    events = json.loads(str(soup))
    latest_event = events['rows'][0]
    latest_eventId = latest_event['eventId']

    if (latest_eventId > current_eventId):
        event_name = latest_event['name']
        event_url = 'https://festa.io/events/'+str(latest_eventId)
        message = event_name+'의 티켓이 오픈되었습니다.\n바로가기 : '+event_url
        bot.send_message(chat_id=chat_id, text=message)
        current_eventId = latest_eventId


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=5)
sched.start()
