import os
import pandas as pd


def create_csv(RAW_DATA_PATH="..\\data\\raw"):
    """ Create CSV file out of text files stored in various folder
    """

    SUB_FOLDERS = list(
        os.walk(RAW_DATA_PATH + "\\EMG_data_for_gestures-master"))[1:]

    FILE_PATHS = []
    for SUB_FOLDER in SUB_FOLDERS:
        for FILE in SUB_FOLDER[2]:
            FILE_PATHS.append(SUB_FOLDER[0] + "\\" + FILE)

    DATAFRAMES = []
    for FILE_PATH in FILE_PATHS:
        df = pd.read_csv(FILE_PATH, delimiter='\t')
        DATAFRAMES.append(df)
    Final_df = pd.concat(DATAFRAMES)

    return Final_df


if __name__ == '__main__':
    create_csv()
