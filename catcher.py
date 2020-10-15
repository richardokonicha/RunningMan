from itertools import islice
from runner import runner
from datetime import datetime, timedelta, timezone
import time
import random
from config import db
from telethon.tl.types import ChannelParticipantsAdmins

users = []


async def catcher(group, out_group, bot_client, index):
    max_add = 50
    number = 0
    offset = 0
    group_admin = await bot_client.get_participants(group, filter=ChannelParticipantsAdmins)
    async for user in bot_client.iter_participants(group):
        if index > offset:
            offset = offset + 1
            pass
        else:
            user_legible = check_status(user, group_admin)
            if user_legible:
                run = await runner(user, out_group, bot_client)
                number += 1
                time.sleep(random.randint(1, 3))

                if number >= max_add:
                    print(f"Reached {max_add} cooling down")
                    cooldown = datetime.now() + timedelta(minutes=30)
                    break
                if run == "Flooded":
                    print(f"Reached max capacity Flooded")
                    break
            else:
                pass
    index = index + number
    db.update({'index': index})
    return index


async def groupGetter(group, bot_client):
    group = await bot_client.get_entity(group)
    return group


def check_status(user, group_admin):
    "This checks to see that the user entity meets all the criteria before being added"
    if user.bot:
        return False
    if user in group_admin:
        return False
    if user.deleted:
        return False
    if user.status.was_online < datetime.now(timezone.utc) - timedelta(days=150):
        # check if user was online in last 5 months
        return False
    else:
        return True
