from config import channel_link
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import traceback
import telethon
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerUser



async def joinner(channel, bot_client):
    join = await bot_client(JoinChannelRequest(channel)) 
    return join

async def runner(user, bot_client):
    try:
        invite = await bot_client(InviteToChannelRequest(
            channel_link,
            [user]
        ))
        username = user.username
        print(f"RunningMan added {username}")

    except telethon.errors.rpcerrorlist.UserIdInvalidError:
          user = InputPeerUser(user.id, user.access_hash)
          invite = await bot_client(InviteToChannelRequest(
            channel_link,
            [user]
        ))


        # await bot_client(AddChatUserRequest(
        #     channel_link,
        #     user,
        #     fwd_limit=10  # Allow the user to see the 10 last messages
        # ))

    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")

