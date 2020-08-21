from telethon.sync import TelegramClient
from config import api_hash, api_id, group
from runner import runner
from catcher import catcher
import time 
import datetime
import random


bot_client = TelegramClient('anon', api_id, api_hash)
bot_client.start()
catch = bot_client.loop.run_until_complete(
    catcher(group, bot_client))


def whistle(bot_client, catch):
    # iterates over 50 users per session caught calls the runner func for each user
    number = 0
    time.sleep(5)
    for user in catch:
        bot_client.loop.run_until_complete(
            runner(user, bot_client))
        number += 1
        if number >= 50:
            print("Reached 50 cooling down")
            flood = True
            floodtime = datetime.datetime.now() + datetime.timedelta(minutes=30)
            break
        time.sleep(random.randint(10, 15))
    print(f"Added {number}")


whistle(bot_client, catch)