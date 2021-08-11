import os
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

global_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00481/EMG_data_for_gestures-master.zip"


def download_and_unzip(url=global_url, extract_to=".\\data\\raw"):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)


def main():
    if not os.path.isdir(".\\data\\raw\\EMG_data_for_gestures-master"):
        download_and_unzip()
    if not os.path.isdir(".\\data\\external"):
        os.mkdir(".\\data\\external")
    if not os.path.isdir(".\\data\\interim"):
        os.mkdir(".\\data\\interim")
    if not os.path.isdir(".\\data\\processed"):
        os.mkdir(".\\data\\processed")


if __name__ == '__main__':
    main()
