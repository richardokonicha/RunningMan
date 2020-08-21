from telethon.sync import TelegramClient
from telethon.sessions import StringSession

import datetime
import time
from config import sessionString, api_id, api_hash
from runner import runner
import random


sessionString=["1BJWap1sBuxVAQiLBVM1CaYhIBUJ3GaEDD5bdXj3gCFpuUaNGXBmwWKQfRsXOmjZAHzDcLXzUohw2A0X203XxCH2I8JZsPuRmkrMvstAJidx40OGm1-RJZWXHoMsigLVMnkisY5o22a2iYgmrjsl_e0hb6TodNkTcvk9xpfkQZxwCJoKTEJuOHumeSCvx1cs_scq_tMOv3UUF8xKtYNLMFWRDtmjuP1rBiM6W2h9vZU0eLFDb_-mAGQv-yXtqnBQ7b3yqq3dLlD7-Q4gsO4WeXnHprVy5UGw8I5fA69-otTKy8mV16Bps0N3VAoiA79AHy63T18cBCRSZJ1dQsFnpBLqOObYFsPc=","1BJWap1wBu2KUNs72uH17ooCoaMHg8kfagmf2q-Vk9EsJh3DLEFXbRKw0fsFf9LcUt4z5keiF1ack2imGf5iHIMJFimjkas3472COmgMRRX3cdy2LAIHFHFP76RICquy9ieT2UtDmyvCjRZo6sg8CMQ0q5o4W3uqt9jmdPD7OXsHSGmb91wq8zXyfOqRcFo_aKMY3omlHDfDWPR8GujO5CRDs3yddC0GfUqncMsg5ag8Pp7BRY72pSAR8-xGh33hHtg0kR6T4n4uXVmDjIzDz2sHTOL_8QHESYi1933FGmshv6jMjOpfac-SwpVE4dL39y_hM9Cb7IARgBur9Jmmt2p1J3AKtCsc="]


sessionList = sessionString.split(",")

class Session:
    # converts session string into client and stores cooldown timer
    def __init__(self, StringSess):
        # self.session = sessionItem
        self.client = TelegramClient(StringSess, api_id, api_hash)
        self.flood = False
        self.cooldown = datetime.datetime.now()
        self.owner = str()

    def __repr__(self):
        return f"Session {self.owner} "

    def whistle(self, catch):
    # iterates over 50 users per session caught calls the runner func for each user
        number = 0
        time.sleep(5)
        for user in catch:
            self.client.loop.run_until_complete(
                runner(user, self.client))
            number += 1
            if number >= 50:
                print("Reached 50 cooling down")
                self.flood = True
                self.cooldown = datetime.datetime.now() + datetime.timedelta(minutes=30)
                break
            time.sleep(random.randint(10, 15))
        print(f"Added {number} cooling down for {self.cooldown}")
        return number





# async def c():
#     group = await sessionsObjects[0].client.get_entity("me")
#     return group



# sessionsObjects[0].client.start()
# sessionsObjects[0].client.loop.run_until_complete(c())


# print(sessionsObjects)



