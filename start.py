from config import bot, start_markup, scheduler
import re
import telebot
from runningman import client_master, itachi, run_client_master
from config import session_strings
import asyncio
import datetime

@bot.message_handler(commands=["start", "Start"])
def start(message):
    userid = message.from_user.id
    # get user object
    text = """
Welcome back
or front 😏 I don't really know the difference.

I am the Runnning Man so
Lets get your campaign started
    """
    bot.send_chat_action(userid, action='typing')
    bot.send_message(userid, text=text, reply_markup=start_markup)



@bot.callback_query_handler(func=lambda call: call.data == "start_campaign")
def join_channel(call):
    user_id = call.from_user.id
    message_id = call.message.message_id
    # run_client_master()

    # from rq import Queue
    # from worker import conn
    # q = Queue(connection=conn)
    # result = q.enqueue(run_client_master)


    job = scheduler.add_job(run_client_master, 'date', run_date=datetime.datetime.now() + datetime.timedelta(seconds=5))
    pass
