from telethon.sync import TelegramClient
from config import api_hash, api_id
from telethon.sessions import StringSession
from catcher import groupGetter, catcher
from telethon.tl.functions.channels import JoinChannelRequest
import os
import datetime
import random
from config import in_group, session_strings

async def itachi(bot_client, index):
    me = await bot_client.get_me()
    # joins and returns group entity
    print(me.username)
    group = await groupGetter(in_group, bot_client)
    participants = await catcher(group, bot_client, index)
    return participants

def client_master(list: session_strings, workfunc, index):
    # loops thru all string session and performs action till until_complete,is_standalone func
    for string in session_strings:
        string_object = StringSession(string)
        bot_client = TelegramClient(string_object, api_id, api_hash)
        bot_client.connect()
        index = bot_client.loop.run_until_complete(workfunc(bot_client, index))
        bot_client.disconnect()
    print(f"ADDED {index}")

index = 200
client_master(session_strings, itachi, index)