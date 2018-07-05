import datetime
import json
import time
from random import randint

from azure.storage.blob import BlockBlobService


def generate_file_test():
   
    temp = randint(1, 100)
    dt = datetime.datetime.now().isoformat()
    ts = time.time()
    data = {"temperature": temp, "date": dt, "timestamp": ts}
    return json.dumps(data)

# sample JSON
# {
# 	"CreationTimeUtc": "2018-07-03T13:59:47.0000000Z",
#   "EventProcessedUtcTime":"2018-07-03T18:59:49.3049402Z",
# 	"resLevel": "1",
# 	"pressure": "2",
# 	"resTemper": "3"
# 	"IoTHub": {
# 		"ConnectionDeviceId": "MyPythonDevice",
# 	}
# }

def generate_file():
    devices = ["MyPythonDevice"]
    devices.extend(list("Device{}".format(x + 1) for x in range(9)))

    temp = randint(1, 100)
    dt = datetime.datetime.utcnow().isoformat()
    ts = time.time()
    randIdx = randint(1, len(devices) - 1)
    device = devices[randIdx]

    iotHub = {"ConnectionDeviceId": device}
    data = {"CreationTimeUtc": dt,
            "EventProcessedUtcTime": dt,
            "resLevel": "1",
            "pressure": "1",
            "resTemper": temp,
            "timestamp": ts,
            "IoTHub": iotHub }
        
    return json.dumps(data)
