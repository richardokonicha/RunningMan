from itertools import islice
from runner import runner
import datetime
import time
import random
from config import db

users = []


async def catcher(group, out_group, bot_client, index):
    max_add = 50
    number = 0
    offset = 0
    async for user in bot_client.iter_participants(group):
        if index > offset:
            offset = offset + 1
            pass
        else:
            run = await runner(user, out_group, bot_client)
            number += 1
            time.sleep(random.randint(1, 5))

            if number >= max_add:
                print(f"Reached {max_add} cooling down")
                cooldown = datetime.datetime.now() + datetime.timedelta(minutes=30)
                break
            if run == "Flooded":
                print(f"Reached max capacity Flooded")
                break

    index = index + number
    db.update({'index': index})

    return index


async def groupGetter(group, bot_client):
    group = await bot_client.get_entity(group)
    return group
