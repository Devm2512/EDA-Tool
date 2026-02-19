import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def calculate_skew_and_plot_kdeplot(dataframe, column):

    # Computing Skew
    skew_values = dataframe[column].skew()
    print(f"\033[1mThe Skew for the column is: \033[0m", skew_values)

    if abs(skew_values) <= 0.5:
        print("\033[1mAlmost Normal Distribution\033[0m]")
    elif abs(skew_values) > 0.5 and abs(skew_values) <= 1:
        print("Moderately Skewed But can be \033[1maccepted as Normal Distrubiton\033[0m]")
    else:
        print("\033[1mHighly Skewed Distribution\033[0m")

    # Calculating the kdeplot
    plt.title(f"The distribution of {column}")
    sns.kdeplot(data = dataframe, x = column, color= "green")
    plt.grid()
    plt.xlabel(f"{column}")
    plt.ylabel("Probability Density")
    plt.show()

    return skew_values



def outlier_detection(dataframe, column, skew_value, mean, std_dev):
    
    if skew_value <= 1:
        Lower_Bound = mean - 3 *std_dev
        Upper_Bound = mean + 3 *std_dev

        print(Lower_Bound, Upper_Bound)
        print("\033[1mTotal Outliers Detected: \033[0m",dataframe[(dataframe[column] < Lower_Bound) | (dataframe[column] > Upper_Bound)].shape[0])


    elif skew_value > 1:

        # Computing the quatiles
        Q1 = np.quantile(dataframe[column],0.25)
        Q2 = np.quantile(dataframe[column],0.5)
        Q3 = np.quantile(dataframe[column],0.75)

        print(f"\033[1mThe 25th Percentile of the {column} is : \033[0m", Q1)
        print(f"\033[1mThe 50th Percentile of the {column} is : \033[0m", Q2)
        print(f"\033[1mThe 75th Percentile of the {column} is : \033[0m", Q3)

        # Computing the IQR --> Interquartile Range

        IQR = Q3 - Q1

        print(f"\033[1mThe Interquartile Range of the {column} is : \033[0m", IQR)

        # computing the lower Bound and Upper Bound

        Lower_Bound = Q1 - (1.5 * IQR)
        Upper_Bound = Q3 + (1.5 * IQR)

        print(f"\033[1mThe Lower_Bound of the {column} is : \033[0m", Lower_Bound)
        print(f"\033[1mThe Upper_Bound of the {column} is : \033[0m", Upper_Bound)

        print("\033[1mTotal Outliers Detected: \033[0m",dataframe[dataframe[column] > Upper_Bound].shape[0])


    # new_df = dataframe[dataframe[column] < Upper_Bound]
    # return Q1, Q2, Q3, IQR, Lower_Bound, Upper_Bound, new_df


def Describing_numeric_column(dataframe,column):
    print(column)
    print(f"\033[1mThe Average of column is: \033[0m", dataframe[column].mean())
    print(f"\033[1mThe Median Value for the column is: \033[0m", dataframe[column].median())
    print(f"\033[1mThe Maximum Value in the Column is: \033[0m", dataframe[column].max())
    print(f"\033[1mThe Minimum Value in the Column is: \033[0m", dataframe[column].min())
    print(f"\033[1mThe Standard Deviation for the Column is: \033[0m", np.std(dataframe[column]))

    return dataframe[column].mean(), np.std(dataframe[column])



def numeric_information(dataframe, column):

    mean, std_dev = Describing_numeric_column(dataframe, column)
    skew = calculate_skew_and_plot_kdeplot(dataframe, column)
    outlier_detection(dataframe, column, skew, mean, std_dev)
    missing_value_calculation(dataframe, column)

    treat_missing_value = input("Do you wish to impute the Missing Values?")
    if treat_missing_value.lower() == "yes":
        missing_value_treatment(dataframe, column) 
    else:
        print("no missing values imputed") 

    return mean, std_dev, skew



# - Provides basic information about the main / imp columns
def counting_information(dataframe, column):
    
    print("\033[1mColumn Name: \033[0m", column)
    print("\033[1mTotal Unique Count: \033[0m",len(dataframe[column].unique()))
    print("\033[1mThe Mode for the Column is: \033[0m", dataframe[column].mode())
    print("\033[1mUnique Values: \033[0m", dataframe[column].unique())
    print("\033[1mNull Values in the data: \033[0m", dataframe[column].isnull().sum())
    print("\033[1mValue Counts: \033[0m",dataframe[column].value_counts())
    
  
    if len(dataframe[column].unique()) > 15:
        pass
    
    elif len(dataframe[column].unique()) > 5:
        plt.title(f"Distribution of {column}")
        sns.barplot(x = dataframe[column].value_counts().index.to_list(), y = list(dataframe[column].value_counts()))
        plt.xticks(rotation = 90)
        # plt.annotate()
        plt.show()

    elif len(dataframe[column].unique()) > 1:
        plt.title(f"Distribution of {column}")  
        plt.pie(labels= dataframe[column].value_counts().index.to_list(), x = list(dataframe[column].value_counts()), autopct= "%1.1f%%")
        plt.show()
        # plt.title(f"Distribution of {column}")
    
        
        
    print("")
    print("------------------------************************--------------------------------")
    print("")



# Missing Value calculation
def missing_value_calculation(dataframe, column):

    null_values = dataframe[column].isna().sum()
    null_values_percentage = null_values / dataframe[column].shape[0]

    if null_values_percentage == 0.0:
        print("No Null Values Detected")
    elif null_values_percentage <= 10.0:
        print(f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mImputation \033[0m")
    elif null_values_percentage <=35.0:
        print(f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mImputation Possible\033[0m")
    else:
        print(f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mDrop the Column\033[0m")
    # print(null_values, null_values_percentage)


def missing_value_treatment(dataframe, column):

    Imputation_methods = ["Mean","Median","Mode","Constant","Missing_Category"]
    
    print("Available Imputation methods are ", Imputation_methods)
    select_imputation_method = input("Enter the Imputation Method: ")
    
    # Mean Imputation
    if select_imputation_method.lower() == "mean":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
    
    # Median Imputation
    elif select_imputation_method.lower() == "median":
        dataframe[column] = dataframe[column].fillna(dataframe[column].median())
    
    # Mode imputation
    elif select_imputation_method.lower() == "mode":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode())
    
    # Constant Imputation
    elif select_imputation_method.lower() == "constant":
        constant = int(input("Enter the constant value for imputation: "))
        dataframe[column] = dataframe[column].fillna(constant)
    
    # Missing Category Imputation
    elif select_imputation_method.lower() == "missing":
        dataframe[column] = dataframe[column].fillna("Missing")
