import datetime
import json
import time
from random import randint

from azure.storage.blob import BlockBlobService


def upload_file(file_name, config):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name = config['account_name'], account_key = config['account_key'])
        container_name ='test-container'

        temp = randint(1, 100)
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts = time.time()
        data = {"temperature": temp, "date": dt, "timestamp": ts}
        json_text = json.dumps(data)

        # Upload
        block_blob_service.create_blob_from_text(container_name, file_name, json_text)

        # # List the blobs in the container
        # print("\nList blobs in the container")
        # generator = block_blob_service.list_blobs(container_name)
        # for blob in generator:
        #     print("\t Blob name: " + blob.name)

    except Exception as e:
        print(e)
