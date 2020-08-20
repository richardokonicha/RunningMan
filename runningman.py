from telethon.sync import TelegramClient
from config import api_hash, api_id, group
from runner import runner
from catcher import catcher
import time 

# bot_client = TelegramClient(
#     StringSession(sessionString), api_id, api_hash)


bot_client = TelegramClient('anon', api_id, api_hash)
bot_client.start()
catch = bot_client.loop.run_until_complete(
    catcher(group, bot_client))

time.sleep(5)
for user in catch:
    # username  ="clynezino"
    # bot_client = TelegramClient('anon', api_id, api_hash)
    # bot_client.start()
    bot_client.loop.run_until_complete(
        runner(user, bot_client))
    time.sleep(10)
