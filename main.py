import pandas as pd
from menu import Menu


def data_reading(file = None):

    if file is not None:
        dataframe = pd.read_csv(file)

    else:
        path = input("Select teh csv File")
        dataframe = pd.read_csv(path)

    return dataframe


if __name__ == "__main__":

    dataframe = data_reading()
