from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from config import api_hash, api_id
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ImportChatInviteRequest


from telethon import TelegramClient

from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser


string_ = "1BJWap1wBu2KUNs72uH17ooCoaMHg8kfagmf2q-Vk9EsJh3DLEFXbRKw0fsFf9LcUt4z5keiF1ack2imGf5iHIMJFimjkas3472COmgMRRX3cdy2LAIHFHFP76RICquy9ieT2UtDmyvCjRZo6sg8CMQ0q5o4W3uqt9jmdPD7OXsHSGmb91wq8zXyfOqRcFo_aKMY3omlHDfDWPR8GujO5CRDs3yddC0GfUqncMsg5ag8Pp7BRY72pSAR8-xGh33hHtg0kR6T4n4uXVmDjIzDz2sHTOL_8QHESYi1933FGmshv6jMjOpfac-SwpVE4dL39y_hM9Cb7IARgBur9Jmmt2p1J3AKtCsc="
# string_ = "1BJWap1wBu4f1BqThE8kAyBlv1ZhC_ChhULo15hBG-h_xAUQZ9doNIaQj1DcWVJ4IyxqecaJPxXtDg2KMTLElGy8DpqdAbbk6jiKwm_F56e5Oqf3G5ypubeCrufZAkN2RbICNDGVN3mte1soK_2nzPQkEWxgOyCHRpCe4BUv8iRG9mxB4xEW_KNHSOIw1_53adL9eWRzhUtjrgztB4_0viQVEhEenYwY7ubSneJwyTBmTpWTIbhe700NZ-sBtCwEwpBgJQo4WGZvmCxx_FPJf4ZHUr8_ZnJnBqqVVEY5Kgf7HWAwlo40yQnPH0j5OEiLxeGnPKvU61fOYKaOcpQPeFMU6IbjHWYU="
string_object = StringSession(string_)
bot_client = TelegramClient(string_object, api_id, api_hash)


def get_channel_users():

    offset = 0
    limit = 100
    all_participants = []
    # chann = bot_client(ImportChatInviteRequest('AAAAAEeiWcA0fQf1XACelA'))

    channel = bot_client.get_entity(
        'https://t.me/forexliontrading')

    filter = ChannelAdminLogEventsFilter(
        False, False, False, False, False, False, False, False, False, False, False, False, False, False)

    while True:
        # channel, ChannelParticipantsSearch(''),#  offset_date=last_date,
        participants = bot_client(GetParticipantsRequest(
            channel,
            offset=0,
            filter=filter,
            # offset_peer=IxnputPeerEmpty(),
            limit=200,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)


bot_client.session.report_errors = False
bot_client.connect()
# index = bot_client.loop.run_until_complete(
#     get_channel_users("https://t.me/joinchat/AAAAAEeiWcA0fQf1XACelA"))


get_channel_users()


# channel = client(ResolveUsernameRequest('channelusername')) # Your channel username

# user = client(ResolveUsernameRequest('admin'))  # Your channel admin username
# admins = [InputUserSelf(), InputUser(
#     user.users[0].id, user.users[0].access_hash)]  # admins
# admins = []  # No need admins for join and leave and invite filters

# filter = None  # All events
# filter = ChannelAdminLogEventsFilter(
#     True, False, False, False, True, True, True, True, True, True, True, True, True, True)
# cont = 0
# list = [0, 100, 200, 300]
# for num in list:
#     result = client(GetParticipantsRequest(InputChannel(
#         channel.chats[0].id, channel.chats[0].access_hash), filter, num, 100))
#     for _user in result.users:
#         print(str(_user.id) + ';' + str(_user.username) + ';' +
#               str(_user.first_name) + ';' + str(_user.last_name))
# with open(''.join(['users/', str(_user.id)]), 'w') as f:
#     f.write(str(_user.id))
