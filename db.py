import datetime
from mongoengine import *
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('db_host')

connect('monitor_db', host=db_host)


class FetchGroup(DynamicDocument):
    # title = StringField(max_length=200, required=True)
    # date_modified = DateTimeField(default=datetime.datetime.utcnow)
    # order_id = IntField(unique=True)
    # phone = IntField(unique=True)
    # product_id = IntField()
    # expire = DateTimeField()
    pass


class FetchSession(DynamicDocument):
    pass