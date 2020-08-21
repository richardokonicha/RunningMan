

users = []

class Users:
    def __init__(self, userid, access_hash, username):
        self.userid = userid
        self.access_hash = access_hash
        self.username = username


async def catcher(group, bot_client):
    # group = await bot_client.get_entity(group)
    # await bot_client(JoinChannelRequest(group))
    participants = await bot_client.get_participants(group)
    return participants

async def groupGetter(group, bot_client):
    group = await bot_client.get_entity(group)
    return group

