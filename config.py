from dotenv import load_dotenv
import os
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
from telethon.sync import TelegramClient
import telebot

import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
load_dotenv()

token = os.getenv("token")
heroku_url = os.getenv("heroku_url")
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
debug = (os.getenv("DEBUG") == 'True')
in_group = os.getenv("in_group")
out_group = os.getenv("out_group")
session_strings = os.getenv("session_strings")
session_strings = session_strings.split(",")

jobstores = {
    # 'default': MongoDBJobStore(client=client, database="test", HOST="realmcluster-shard-00-02.yjlnu.mongodb.net"),
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    # 'default': ThreadPoolExecutor(20),
    # 'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    # 'coalesce': False,
    'max_instances': 3,
    'misfire_grace_time': 259200
}
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    # timezone=utc
)
scheduler.start()

bot = telebot.TeleBot(
    token,
    threaded=True
)

start_markup = telebot.types.InlineKeyboardMarkup()
start_button = telebot.types.InlineKeyboardButton(
    text="Start campaign ✅", callback_data="start_campaign")
start_markup.add(start_button)
