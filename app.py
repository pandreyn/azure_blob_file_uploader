import os
import time
import uuid
import json

from utils import savetostorage, generateFile

def save_by_timer(params):
    u = uuid.uuid1()
    number_of_files = int(params.number_of_files)
    interval_in_sec = int(params.interval_in_sec)
    
    if os.path.isfile(params.config_file):
        with open(params.config_file, 'r') as f:
            config = json.load(f)
    else:
        config = {'account_name': os.environ['ACCOUNT_NAME'], 
                    'account_key': os.environ['ACCOUNT_KEY'], 
                    'container_name': os.environ['CONTAINER_NAME']}

    if ('account_name' not in config) or ('account_key' not in config) or ('container_name' not in config):
        print('you should set ACCOUNT_NAME and ACCOUNT_KEY and CONTAINER_NAME') 
        return

    for i in range(number_of_files):
        file_name = '{}_{}.json'.format(str(u), str(i + 1).zfill(3))
        file_body = generateFile.generate_file()
        savetostorage.upload_file(file_name, file_body, config)
        print("Uploaded file: {}, waiting for {} seconds...".format(file_name, interval_in_sec))
        time.sleep(interval_in_sec)

    print()
    print("Upload completed")

# Main method.
if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-n", "--number_of_files", dest="number_of_files",
                        required=True,
                        help="set number of files to generate")
    parser.add_argument("-c", "--config_file", dest="config_file",
                        default="config.json",
                        help="path to the config file")
    parser.add_argument("-w", "--wait", dest="interval_in_sec", default=60.0,
                        help="How many seconds to wait between files generating (default = 1 min)")

    args = parser.parse_args()
    
    save_by_timer(args)