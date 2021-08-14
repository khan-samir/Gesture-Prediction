import os
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from src.config.config import read_params


def download_and_unzip():
    config = read_params()
    http_response = urlopen(config['data']['url'])
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=config['data']['raw'])


def main():
    config = read_params()
    if not os.path.isdir(config['data']['raw'] + "\\EMG_data_for_gestures-master"):
        download_and_unzip()
    if not os.path.isdir(config['data']['external']):
        os.mkdir(config['data']['external'])
    if not os.path.isdir(config['data']['interim']):
        os.mkdir(config['data']['interim'])
    if not os.path.isdir(config['data']['processed']):
        os.mkdir(config['data']['processed'])


if __name__ == '__main__':
    main()
