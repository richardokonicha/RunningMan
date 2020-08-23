for user in users:
    n += 1
    if n % 50 == 0:
    try:
        print ("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(60, 180))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue



sessionString = [
    {"string":"1BJWap1sBuxVAQiLBVM1CaYhIBUJ3GaEDD5bdXj3gCFpuUaNGXBmwWKQfRsXOmjZAHzDcLXzUohw2A0X203XxCH2I8JZsPuRmkrMvstAJidx40OGm1-RJZWXHoMsigLVMnkisY5o22a2iYgmrjsl_e0hb6TodNkTcvk9xpfkQZxwCJoKTEJuOHumeSCvx1cs_scq_tMOv3UUF8xKtYNLMFWRDtmjuP1rBiM6W2h9vZU0eLFDb_-mAGQv-yXtqnBQ7b3yqq3dLlD7-Q4gsO4WeXnHprVy5UGw8I5fA69-otTKy8mV16Bps0N3VAoiA79AHy63T18cBCRSZJ1dQsFnpBLqOObYFsPc=", "index": 0},
    {"string": "1BJWap1wBu2KUNs72uH17ooCoaMHg8kfagmf2q-Vk9EsJh3DLEFXbRKw0fsFf9LcUt4z5keiF1ack2imGf5iHIMJFimjkas3472COmgMRRX3cdy2LAIHFHFP76RICquy9ieT2UtDmyvCjRZo6sg8CMQ0q5o4W3uqt9jmdPD7OXsHSGmb91wq8zXyfOqRcFo_aKMY3omlHDfDWPR8GujO5CRDs3yddC0GfUqncMsg5ag8Pp7BRY72pSAR8-xGh33hHtg0kR6T4n4uXVmDjIzDz2sHTOL_8QHESYi1933FGmshv6jMjOpfac-SwpVE4dL39y_hM9Cb7IARgBur9Jmmt2p1J3AKtCsc=","index": 0},
    {"string": "1BJWap1wBu2gfrjGz_C1d2vfy0yqB0OVkmqvxm_A8QOc4BDpPEqeFB4_jySYMBeWJfv_MBOz91-A4CHxQLVnNBWASXdbVrazuInOaj98TxzhPXMBCd1oHqGwXH2Q1vqIQH0g6F7Ni7r9LH-IP0-11tK5W11WJUIp6_Op_o4QUROymIaserhQFbMqxf_XMoRR4PvgK_E7kz0NsPwPlvFaGY5XiMQ4uLG222gYAvzSOiSfJsuIhdMW_Pwb3xaL2hV3FwGlvW9fGJXdR3VSIL_2qGY9L0fJGju90FlYlc4btpFeYH72g07sZ_P9aKb81tNUTbeKFU3hePtQ3ltQqYXKRKBjHdISOEDE=", "index": 0}
    ]


# For normal chats
from telethon.tl.functions.messages import AddChatUserRequest

# Note that ``user_to_add`` is NOT the name of the parameter.
# It's the user you want to add (``user_id=user_to_add``).
await client(AddChatUserRequest(
    chat_id,
    user_to_add,
    fwd_limit=10  # Allow the user to see the 10 last messages
))

# For channels (which includes megagroups)
from telethon.tl.functions.channels import InviteToChannelRequest

await client(InviteToChannelRequest(
    channel,
    [users_to_add]
))


# for private groups
from telethon.tl.functions.messages import ImportChatInviteRequest
updates = await client(ImportChatInviteRequest('AAAAAEHbEkejzxUjAUCfYg'))