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
    index_former = index
    group_admin = await bot_client.get_participants(group, filter=ChannelParticipantsAdmins)
    async for user in bot_client.iter_participants(group):
        if index_former > offset:
            offset = offset + 1
            pass
        else:
            index = index + 1
            db.update({'index': index})

            user_legible = check_status(user, group_admin)
            if user_legible:
                run = await runner(user, out_group, bot_client)

                if run == "Good":
                    number += 1
                    time.sleep(random.randint(1, 5))

                if number >= max_add:
                    print(f"Reached {max_add} cooling down")
                    cooldown = datetime.now() + timedelta(minutes=30)
                    break
                if run == "Flooded":
                    print(f"Reached max capacity Flooded")
                    break
                if run == "NotAdmin":
                    print(f"Not an Admin")
                    break
            else:
                pass
    # index = index + number
    # db.update({'index': index})
    print(f"Added {number}")
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

    try:
        inactivity_date = datetime.now(timezone.utc) - timedelta(days=15)
        if user.status.was_online > inactivity_date:
            # check if user was online in last 5 months
            return True
        else:
            return False
    except AttributeError:
        if user.participant.date > inactivity_date:
            return True
        else:
            return False
