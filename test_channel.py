# from telethon.tl.functions.channels import GetParticipantsRequest
# from telethon.tl.types import ChannelParticipantsSearch
# from time import sleep
from config import api_hash, api_id
# from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# # from telethon import TelegramClient

# from telethon.tl.functions.channels import GetParticipantsRequest

# from telethon.tl.types import ChannelParticipantsRecent
# from telethon.tl.types import InputChannel
# from telethon.tl.types import ChannelAdminLogEventsFilter

from telethon.tl.types import ChannelParticipantsAdmins


# # string_ = ""
# # string_object = StringSession()
# bot_client = TelegramClient("ds", api_id, api_hash)


# async def get_channel_users():

#     # async for dialog in bot_client.iter_dialogs():
#     #     print(dialog.name, 'has ID', dialog.id)

#     #     group_admin = await bot_client.get_participants(dialog, filter=ChannelParticipantsAdmins)

#     channel = await bot_client.get_entity(
#         'https://t.me/forexliontrading')


# bot_client.session.report_errors = False
# bot_client.connect()
# index = bot_client.loop.run_until_complete(
#     get_channel_users())

# # channel = client(ResolveUsernameRequest('channelusername')) # Your channel username

# # user = client(ResolveUsernameRequest('admin'))  # Your channel admin username
# # admins = [InputUserSelf(), InputUser(
# #     user.users[0].id, user.users[0].access_hash)]  # admins
# # admins = []  # No need admins for join and leave and invite filters

# # filter = None  # All events
# # filter = ChannelAdminLogEventsFilter(
# #     True, False, False, False, True, True, True, True, True, True, True, True, True, True)
# # cont = 0
# # list = [0, 100, 200, 300]
# # for num in list:
# #     result = client(GetParticipantsRequest(InputChannel(
# #         channel.chats[0].id, channel.chats[0].access_hash), filter, num, 100))
# #     for _user in result.users:
# #         print(str(_user.id) + ';' + str(_user.username) + ';' +
# #               str(_user.first_name) + ';' + str(_user.last_name))
# # with open(''.join(['users/', str(_user.id)]), 'w') as f:
# #     f.write(str(_user.id))

from telethon.tl.custom.button import Button
from telethon import TelegramClient
from utils import string_

string_object = StringSession(string_)
client = TelegramClient(string_object, api_id, api_hash)

admins = []


async def main():
    me = await client.get_me()
    username = me.username
    print(username)
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

        if dialog.is_group:
            group_admin = await client.get_participants(dialog, filter=ChannelParticipantsAdmins)
            for i in group_admin:
                # admins.append(i)
                text = """
            <a href='https://extractor.netlify.app'>Get this software now </a>https://extractor.netlify.app 
            limited offer"""
                await client.send_message(i, text, file='C:/Users/Richard Okonicha/Pictures/Design/Extract.png', parse_mode='html')
with client:
    client.loop.run_until_complete(main())
