from dotenv import load_dotenv
import os
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# from pytz import utc
# from apscheduler.schedulers.blocking import BlockingScheduler
from telethon.sync import TelegramClient


import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
load_dotenv()


api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
sessionString = os.getenv("sessionString")
debug = (os.getenv("DEBUG") == 'True')
in_group = os.getenv("in_group")
out_group = os.getenv("out_group")





# jobstores = {
#     'default': MongoDBJobStore(client=client, database="test", HOST="realmcluster-shard-00-02.yjlnu.mongodb.net"),
#     # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }
# executors = {
#     # 'default': ThreadPoolExecutor(20),
#     # 'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     # 'coalesce': False,
#     'max_instances': 3,
#     'misfire_grace_time': 259200
# }
# scheduler = BackgroundScheduler(
#     jobstores=jobstores,
#     executors=executors,
#     job_defaults=job_defaults,
#     timezone=utc
# )
# scheduler.start()
