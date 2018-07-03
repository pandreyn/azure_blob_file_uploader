import datetime
import json
import time
from random import randint

from azure.storage.blob import BlockBlobService


def upload_file(file_name, file_body, config):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name = config['account_name'], account_key = config['account_key'])
        container_name = config['container_name']

        # Upload
        block_blob_service.create_blob_from_text(container_name, file_name, file_body)

        # # List the blobs in the container
        # print("\nList blobs in the container")
        # generator = block_blob_service.list_blobs(container_name)
        # for blob in generator:
        #     print("\t Blob name: " + blob.name)

    except Exception as e:
        print(e)
