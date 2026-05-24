import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def counting_information(dataframe, column):

    Unique_count = len(dataframe[column].unique())
    Mode = dataframe[column].mode()
    Value_counts = dataframe[column].value_counts()

    return Unique_count, Mode, Value_counts
                       

def plot_countplot(dataframe, column):

    unique_count = dataframe[column].unique()
    
    if len(unique_count) > 15:
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
        return None
    
    plt.tight_layout()
    return fig
        
    print("")
    print("------------------------************************--------------------------------")
    print("")

    return plot
