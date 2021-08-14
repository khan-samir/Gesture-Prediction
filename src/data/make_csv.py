import os
import datetime
import pandas as pd
import download_data

# importing config file
import sys
sys.path.insert(0, "./src/config")
from config import read_params


def create_csv():
    """ Create CSV file out of text files stored in various folder
    """
    config = read_params()
    download_data.main()

    sub_folders = list(
        os.walk(config['data']['raw'] + "\\EMG_data_for_gestures-master"))[1:]

    file_paths = []
    for sub_folder in sub_folders:
        for FILE in sub_folder[2]:
            file_paths.append(sub_folder[0] + "\\" + FILE)

    dataframes = []
    for file_path in file_paths:
        df = pd.read_csv(file_path, delimiter='\t')
        dataframes.append(df)
    final_df = pd.concat(dataframes)

    datetime_ = datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")
    final_df.to_csv(f"{config['data']['interim']}\\gesture-prediction-{datetime_}.csv", index=False)

    return final_df


if __name__ == '__main__':
    create_csv()
