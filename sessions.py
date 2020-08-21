from telethon.sync import TelegramClient
import datetime
from config import sessionString, api_id, api_hash

sessionList = sessionString.split(",")


class Session:
    # converts session string into client and stores cooldown timer
    def __init__(self, sessionItem):
        self.session = sessionItem
        self.client = TelegramClient(StringSession(sessionString), api_id, api_hash)
        self.flood = False
        self.cooldown = datetime.datetime.now()
        self.owner = str()

sessionsObjects = []
for string in sessionString:
    sessionObject = Session(string)
    sessionsObjects.append(sessionObject)

print(Session)
print(sessionsObjects)

