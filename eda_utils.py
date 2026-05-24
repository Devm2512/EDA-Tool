import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numeric_information import Describing_numeric_column, calculate_skew_and_plot_kdeplot,outlier_detection,missing_value_calculation, whether_to_impute_missing_values
from categorical_information import counting_information, plot_countplot


def basic_info_dataframe(dataframe):

    shape = dataframe.shape
    column_and_its_information = dataframe.info()
    
    sample_number = int(input("Enter the sample count to be viewed: "))
    sample_rows = dataframe.sample(sample_number)



    return shape, column_and_its_information, sample_rows


def rec_fuction(dataframe):

    # basic_info_dataframe(dataframe)
    column = input("Enter the column name from the above list: ")

    return column


def numeric_information(dataframe, column):

    while True:
            
        try:
            choice = numeric_information_selection(dataframe, column)

            if choice == 1:
                basic_info_dataframe(dataframe)

            
            elif choice == 2:
                mean, std_dev = Describing_numeric_column(dataframe, column)
                return mean, std_dev
            
            elif choice == 3:
                skew = calculate_skew_and_plot_kdeplot(dataframe, column)
                return skew
            
            elif choice == 4:
                mean, std_dev = Describing_numeric_column(dataframe, column)
                skew = calculate_skew_and_plot_kdeplot(dataframe, column)
                outlier_detection(dataframe, column, skew, mean, std_dev)
            
            elif choice == 5:
                missing_value_calculation(dataframe, column)
            
            elif choice == 6:
                whether_to_impute_missing_values(dataframe, column)

            else:
                print("Invalid Selection")

        
        except ValueError:

            print("Please Enter a Valid Number")


def categorical_information(dataframe, column):

    basic_info_dataframe(dataframe)
    counting_information(dataframe, column)
    plot_countplot(dataframe, column)
    missing_value_calculation(dataframe, column)
    whether_to_impute_missing_values(dataframe, column)
