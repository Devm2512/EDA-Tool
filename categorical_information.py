import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def counting_information(dataframe, column):
    
    print("\033[1mColumn Name: \033[0m", column)
    print("\033[1mTotal Unique Count: \033[0m",len(dataframe[column].unique()))
    print("\033[1mThe Mode for the Column is: \033[0m", dataframe[column].mode())
    print("\033[1mUnique Values: \033[0m", dataframe[column].unique())
    print("\033[1mValue Counts: \033[0m",dataframe[column].value_counts())

    
def plot_countplot(dataframe, column):
    
    if len(dataframe[column].unique()) > 15:
        print("Too Many Categories")
    
    elif len(dataframe[column].unique()) > 5:
        plt.title(f"Distribution of {column}")
        sns.barplot(x = dataframe[column].value_counts().index.to_list(), y = list(dataframe[column].value_counts()))
        plt.xticks(rotation = 90)
        plt.show()

    elif len(dataframe[column].unique()) > 1:
        plt.title(f"Distribution of {column}")  
        plt.pie(labels= dataframe[column].value_counts().index.to_list(), x = list(dataframe[column].value_counts()), autopct= "%1.1f%%")
        plt.show()
        
    print("")
    print("------------------------************************--------------------------------")
    print("")