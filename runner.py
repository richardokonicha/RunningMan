from config import channel_link
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import traceback

# user = await bot_client.get_entity(username)

async def runner(user, bot_client):
    try: 
        invite = await bot_client(InviteToChannelRequest(
            channel_link,
            [user]
        ))
        username = user.username
        print(f"RunningMan added {username}")
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")

