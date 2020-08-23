from telethon.sync import TelegramClient
from config import api_hash, api_id, groupLink
from runner import runner, joinner
from catcher import catcher, groupGetter
import time 
import datetime
import random
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from db import FetchGroup, FetchSession


# sessionString = [
#     {"string":"1BJWap1sBuxVAQiLBVM1CaYhIBUJ3GaEDD5bdXj3gCFpuUaNGXBmwWKQfRsXOmjZAHzDcLXzUohw2A0X203XxCH2I8JZsPuRmkrMvstAJidx40OGm1-RJZWXHoMsigLVMnkisY5o22a2iYgmrjsl_e0hb6TodNkTcvk9xpfkQZxwCJoKTEJuOHumeSCvx1cs_scq_tMOv3UUF8xKtYNLMFWRDtmjuP1rBiM6W2h9vZU0eLFDb_-mAGQv-yXtqnBQ7b3yqq3dLlD7-Q4gsO4WeXnHprVy5UGw8I5fA69-otTKy8mV16Bps0N3VAoiA79AHy63T18cBCRSZJ1dQsFnpBLqOObYFsPc=", "index": 0},
#     {"string": "1BJWap1wBu2KUNs72uH17ooCoaMHg8kfagmf2q-Vk9EsJh3DLEFXbRKw0fsFf9LcUt4z5keiF1ack2imGf5iHIMJFimjkas3472COmgMRRX3cdy2LAIHFHFP76RICquy9ieT2UtDmyvCjRZo6sg8CMQ0q5o4W3uqt9jmdPD7OXsHSGmb91wq8zXyfOqRcFo_aKMY3omlHDfDWPR8GujO5CRDs3yddC0GfUqncMsg5ag8Pp7BRY72pSAR8-xGh33hHtg0kR6T4n4uXVmDjIzDz2sHTOL_8QHESYi1933FGmshv6jMjOpfac-SwpVE4dL39y_hM9Cb7IARgBur9Jmmt2p1J3AKtCsc=","index": 0},
#     {"string": "1BJWap1wBu2gfrjGz_C1d2vfy0yqB0OVkmqvxm_A8QOc4BDpPEqeFB4_jySYMBeWJfv_MBOz91-A4CHxQLVnNBWASXdbVrazuInOaj98TxzhPXMBCd1oHqGwXH2Q1vqIQH0g6F7Ni7r9LH-IP0-11tK5W11WJUIp6_Op_o4QUROymIaserhQFbMqxf_XMoRR4PvgK_E7kz0NsPwPlvFaGY5XiMQ4uLG222gYAvzSOiSfJsuIhdMW_Pwb3xaL2hV3FwGlvW9fGJXdR3VSIL_2qGY9L0fJGju90FlYlc4btpFeYH72g07sZ_P9aKb81tNUTbeKFU3hePtQ3ltQqYXKRKBjHdISOEDE=", "index": 0}
#     ]

sessionString = FetchSession.objects.all()

n = 0
max_add = 50



def whistle(bot_client, catch):
    # iterates over 50 users per session caught calls the runner func for each user
    number = 0
    time.sleep(5)
    for user in catch:
        me = bot_client.get_me()
        run = bot_client.loop.run_until_complete(
            runner(user, bot_client))
        number += 1
        if number >= max_add:
            print(f"Reached {max_add} cooling down")
            cooldown = datetime.datetime.now() + datetime.timedelta(minutes=30)
            break
        time.sleep(random.randint(10, 15))
    print(f"Added {number}")

    return {"Added": number, "cooldown": cooldown }


bot_client = TelegramClient('anon', api_id, api_hash)
bot_client.start()

group = bot_client.loop.run_until_complete(groupGetter(groupLink, bot_client))
catch = bot_client.loop.run_until_complete(
    catcher(group, bot_client))
fetch_group = FetchGroup.objects(group_id= group.id).first()
answer_index = fetch_group["index_remain"]


for SES in sessionString:
    print("--------------------")

    bot_client.disconnect()
    string = sessionString[n]["session"]
    bot_client = TelegramClient(StringSession(string), api_id, api_hash)
    bot_client.connect()
    bot_client.loop.run_until_complete(joinner(groupLink, bot_client))


    me = bot_client.get_me()
    print(f"{me.username}  is starting")
    catch = catch[answer_index: ]
    answer = whistle(bot_client, catch) 
    answer_index = answer["Added"] + answer_index
    n += 1
    me = bot_client.get_me()
    cooldown = answer["cooldown"]
   
    if not fetch_group:
        fetch_group = FetchGroup(group_id=group.id, group_link=groupLink, index_remain=answer_index)
        fetch_group.save()

    fetch_group.index_remain = answer_index
    fetch_group.save()


    fetch_session = FetchSession.objects(username= me.username).first()
    if not fetch_session:
        fetch_session = FetchSession(username=me.username, session=string, cooldown=cooldown)
        fetch_session.save()
    else:
        fetch_session.cooldown = cooldown
        fetch_session.save()
    print(f"{me.username} has taken a break")


