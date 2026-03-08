import pandas as pd
from menu import Menu


def data_reading():

    dataframe = pd.read_csv("C:/Users/dewan/Downloads/data_science/EDA Project/df_selected_cols.csv")

    return dataframe


if __name__ == "__main__":

    dataframe = data_reading()

    menu = Menu(dataframe)

    menu.start()
