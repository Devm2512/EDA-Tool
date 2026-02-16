import pandas as pd
from eda_utils import numeric_information,counting_information

dataframe = pd.read_csv("Enter the path of your CSV File Here")
print("The available columns are: ", dataframe.columns)

column = input("Enter the column name from the above list: ")

def statistics_for_each_columns(dataframe, column):

    datatype = ["int32", "int64", "float32", "float64"]
    
    # for i in dataframe.columns:

    if dataframe[column].dtype in datatype:
        numeric_information(dataframe, column)
        print("")
        print("----------------------------------****************************************------------------------------------------")
        print("")
    else:
        counting_information(dataframe,column)
        print("")
        print("----------------------------------****************************************------------------------------------------")
        print("")
            

if __name__ == "__main__":
    statistics_for_each_columns(dataframe, column)