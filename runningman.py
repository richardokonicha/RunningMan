from telethon.sync import TelegramClient
from config import api_hash, api_id
from telethon.sessions import StringSession
from catcher import groupGetter, catcher
from telethon.tl.functions.channels import JoinChannelRequest
import os
import datetime
import random
from config import session_strings, index_value
import asyncio
from config import db


async def itachi(bot_client, index):
    me = await bot_client.get_me()
    # joins and returns group entity
    print(me.username)
    group = await groupGetter(in_group, bot_client)
    participants = await catcher(group, out_group, bot_client, index)
    return participants


def client_master(list: session_strings, workfunc, index):
    # loops thru all string session and performs action till until_complete,is_standalone func
    for string in session_strings:
        string_object = StringSession(string)
        # loop = asyncio.new_event_loop()
        bot_client = TelegramClient(string_object, api_id, api_hash)
        bot_client.connect()
        index = bot_client.loop.run_until_complete(workfunc(bot_client, index))
        bot_client.disconnect()
    print(f"ADDED {index}")

# index = 300
# client_master(session_strings, itachi, index)


def run_client_master():
    print("Which ")

    try:
        from config import in_group as ing, out_group as oug
        global in_group
        global out_group
        in_group = input(
            u"\u001b[34mGetting new users from (Group Link):") or ing
        out_group = input(
            u"\u001b[32mAdding new users to (Group Link):") or oug

        db_index = db.all()
        db_index = db_index[-1]["index"]

        index = int(
            input(f"\u001b[37mStarting point (default number: {db_index})") or db_index)
    except ValueError:
        return print("index is a number")
    except TypeError:
        return print("Invalid group info")
        # index = index_value

    client_master(session_strings, itachi, index)
    print("Running client master")


run_client_master()
