import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def counting_information(dataframe, column):
    
    # print("\033[1mColumn Name: \033[0m", column)
    print("\033[1mTotal Unique Count: \033[0m",len(dataframe[column].unique()))
    print("\033[1mThe Mode for the Column is: \033[0m", dataframe[column].mode())
    # print("\033[1mUnique Values: \033[0m", dataframe[column].unique())
    print("\033[1mValue Counts: \033[0m",dataframe[column].value_counts())

    Unique_count = len(dataframe[column].unique())
    Mode = dataframe[column].mode()
    Value_counts = dataframe[column].value_counts()

    return Unique_count, Mode, Value_counts
                       

def plot_countplot(dataframe, column):

    unique_count = dataframe[column].unique()
    
    if len(unique_count) > 15:
        print("Too Many Categories")
        return None
    
    fig,ax = plt.subplots(figsize = (5,3))
    
    if len(unique_count) > 5:
        plot = sns.barplot(x = dataframe[column].value_counts().index.to_list(), y = list(dataframe[column].value_counts()), ax = ax)
        plt.xticks(rotation = 90)
        plt.title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        for i, value in enumerate(dataframe[column].value_counts().values):
            ax.text(
                i,
                value,
                str(value),
                ha='center',
                va='bottom',
                fontsize=9
            )



    elif len(unique_count) > 1:
        fig, ax = plt.subplots(figsize=(4, 4))

        counts = dataframe[column].value_counts()

        ax.pie(
            counts.values,
            labels=counts.index,
            autopct="%1.1f%%"
        )

        ax.set_title(f"Distribution of {column}")

    else:
        print("Not enough Categories to plot")
        return None
    
    plt.tight_layout()
    return fig
        
    print("")
    print("------------------------************************--------------------------------")
    print("")

    return plot
