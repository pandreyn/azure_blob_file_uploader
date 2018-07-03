import datetime
import json
import time
from random import randint

from azure.storage.blob import BlockBlobService


def generate_file():
   
    temp = randint(1, 100)
    dt = datetime.datetime.now().isoformat()
    ts = time.time()
    data = {"temperature": temp, "date": dt, "timestamp": ts}
    return json.dumps(data)
