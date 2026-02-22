import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numeric_information import Describing_numeric_column, calculate_skew_and_plot_kdeplot,outlier_detection,missing_value_calculation, whether_to_impute_missing_values
from categorical_information import counting_information, plot_countplot


def basic_info_dataframe(dataframe):

    shape = dataframe.shape
    print("The shape of the dataframe is: ", shape)

    column_and_its_information = dataframe.info()
    print("The columnwise information about the dataframe is: ", column_and_its_information)
    
    sample_number = int(input("Enter the sample count to be viewed: "))
    sample_rows = dataframe.sample(sample_number)
    print("Sample Rows from the dataframe are: ", sample_rows)


    return shape, column_and_its_information, sample_rows


def numeric_information(dataframe, column):

    basic_info_dataframe(dataframe)
    mean, std_dev = Describing_numeric_column(dataframe, column)
    skew = calculate_skew_and_plot_kdeplot(dataframe, column)
    outlier_detection(dataframe, column, skew, mean, std_dev)
    missing_value_calculation(dataframe, column)
    whether_to_impute_missing_values(dataframe, column)
    

    return mean, std_dev, skew


def categorical_information(dataframe, column):

    basic_info_dataframe(dataframe)
    counting_information(dataframe, column)
    plot_countplot(dataframe, column)
    missing_value_calculation(dataframe, column)
    whether_to_impute_missing_values(dataframe, column)
