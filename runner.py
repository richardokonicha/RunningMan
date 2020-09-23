from config import out_group
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserNotMutualContactError
import traceback
from telethon.tl.functions.channels import JoinChannelRequest
import time, datetime, random

async def joinner(channel, bot_client):
    join = await bot_client(JoinChannelRequest(channel)) 
    return join

async def runner(user, bot_client):
    try:
        invite = await bot_client(InviteToChannelRequest(
            out_group,
            [user]
        ))
        username = user.username
        print(f"RunningMan added {username}")
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except UserNotMutualContactError:
        print("The user isn't a mutal contact")
    except:
        traceback.print_exc()
        print("Unexpected Error")
    return True