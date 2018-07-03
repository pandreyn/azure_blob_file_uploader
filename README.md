# azure_blob_file_uploader

This tool generates json files with simple structure and uploads them to azure storage.

## Installation:
1. install python
2. clone repo
3. cd to repo folder
4. install virtual env:
```
python -m venv venv
virtualenv venv
```
5. activate virtual env (on Windows run `venv\Scripts\activate`)
6. run `pip install -r requirements.txt`

## Usage:
Run `python app.py` whith needed arguments

1. Commandline arguments:
```
usage: app.py [-h] -n NUMBER_OF_FILES [-c CONFIG_FILE] [-w INTERVAL_IN_SEC]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_FILES, --number_of_files NUMBER_OF_FILES
                        set number of files to generate
  -c CONFIG_FILE, --config_file CONFIG_FILE
                        path to the config file
  -w INTERVAL_IN_SEC, --wait INTERVAL_IN_SEC
                        How many seconds to wait between files generating
                        (default = 1 min)
```

2. config file is a simple json file with two arguments:
```
{
    "account_name": "xxx",
    "account_key": "yyy"
    "container_name": "zzz"
}
```

Where `account_name` is the storage account name and `account_key` is access key of that storage account.
If you do not want to use config file, you can set `account_name` and `account_key` through env variables: `ACCOUNT_NAME` and `ACCOUNT_KEY` respectively.

For windows:
```
set ACCOUNT_NAME=xxx
set ACCOUNT_KEY=yyy
set CONTAINER_NAME=zzz
```
