import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def Describing_numeric_column(dataframe,column):
    
    try:
        mean = dataframe[column].mean()
        stad_dev = np.std(dataframe[column])

        return mean, stad_dev
    
    except KeyError:
        print(f"The Mentioned Column {column} does not exist in the Dataframe")

    except Exception as e:
        print(f"Unexcepted Error Occured: {e}")

    finally:
        print(f"The Numeric Column Described.")



def calculate_skew_and_plot_kdeplot(dataframe, column):

    try:
        # Computing Skew
        skew_values = dataframe[column].skew()
        if abs(skew_values) <= 0.5:
            print("\033[1mAlmost Normal Distribution\033[0m")
        
        elif abs(skew_values) > 0.5 and abs(skew_values) <= 1:
            print("Moderately Skewed But can be \033[1maccepted as Normal Distrubiton\033[0m")
        
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
    
    except NameError:
        print(f"The Column {column} Does Not Exist in the DataFrame.")

    except Exception as e:
        print(f"Unexpected Error Occured: {e}")

    finally:
        print(f"The Numeric Column Described.")

        

# CENTRAL FUNCTION
def missing_value_calculation(dataframe, column):

    try:
        null_values = dataframe[column].isna().sum()
        null_values_percentage = round((null_values / dataframe[column].shape[0])*100,2)

        if null_values_percentage == 0.0:
            Message = "No Null Values Detected"
        elif null_values_percentage <= 10.0:
            Message = f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mImputation \033[0m"
        elif null_values_percentage <=35.0:
            Message = f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mImputation Possible\033[0m"
        else:
            Message = f"{null_values_percentage} percent null values detected. Suggested Treatment: \033[1mDrop the Column\033[0m"

    except NameError:
        print(f"The Column {column} Does Not Exist in the DataFrame.")
    except Exception as e:
        print(f"Unexpected Error Occured: {e}")

    finally:
        print(f"The Numeric Column Described.")
    
    return null_values, null_values_percentage, Message


def whether_to_impute_missing_values(dataframe, column, impute_choice):

    try:
        if dataframe[column].isna().sum() >= 1:
            if impute_choice == "Yes":
                # Call your treatment function (make sure it modifies the df or returns it)
                missing_value_treatment(dataframe, column) 
                return "Success: Missing Values Imputed!"
            else:
                return "Info: Missing Values Treatment Skipped by User."
        else:
            return "Info: No Missing Values Found."
            
    except KeyError:
        return f"Error: The Column '{column}' Does Not Exist."
    except Exception as e:
        return f"Unexpected Error: {e}"
    


# CENTRAL FUNCTION --> add a check to identify whether the column is categorical or numeric and then provide the corresponsing missing value imputatio methods
def missing_value_treatment(dataframe, column):

    Imputation_methods = ["Drop","Mean","Median","Mode","Constant","Missing_Category"]
    
    # Dropping Missing Values
    print("Available Imputation methods are ", Imputation_methods)
    select_imputation_method = input("Enter the Imputation Method: ")
    
    # Dropping Missing Values
    if select_imputation_method.lower() == "drop":
        dataframe[column] = dataframe[column].dropna()
        print("Missig Values Dropped")

    # Mean Imputation
    elif select_imputation_method.lower() == "mean":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
        print("Imputation Complete")
    
    # Median Imputation
    elif select_imputation_method.lower() == "median":
        dataframe[column] = dataframe[column].fillna(dataframe[column].median())
        print("Imputation Complete")
    
    # Mode imputation
    elif select_imputation_method.lower() == "mode":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode())
        print("Imputation Complete")
    
    # Constant Imputation
    elif select_imputation_method.lower() == "constant":
        constant = int(input("Enter the constant value for imputation: "))
        dataframe[column] = dataframe[column].fillna(constant)
        print("Imputation Complete")
    
    # Missing Category Imputation
    elif select_imputation_method.lower() == "missing":
        dataframe[column] = dataframe[column].fillna("Missing")
        print("Imputation Complete")


def outlier_detection(dataframe, column, skew_value, mean, std_dev):
    
    if skew_value <= 1:
        Lower_Bound = mean - 3 *std_dev
        Upper_Bound = mean + 3 *std_dev

        print(Lower_Bound, Upper_Bound)
        print("\033[1mTotal Outliers Detected: \033[0m",dataframe[(dataframe[column] < Lower_Bound) | (dataframe[column] > Upper_Bound)].shape[0])

        Q1, Q2, Q3, IQR = 0.0, 0.0, 0.0, 0.0
        new_df = dataframe[(dataframe[column] >= Lower_Bound) & (dataframe[column] <= Upper_Bound)]
        return 0.0, 0.0, 0.0, 0.0, Lower_Bound, Upper_Bound, new_df



    else:
        
        # Computing the quatiles
        Q1 = np.nanquantile(dataframe[column],0.25)
        Q2 = np.nanquantile(dataframe[column],0.5)
        Q3 = np.nanquantile(dataframe[column],0.75)

        IQR = Q3 - Q1

        Lower_Bound = Q1 - (1.5 * IQR)
        Upper_Bound = Q3 + (1.5 * IQR)



        new_df = dataframe[(dataframe[column] >= Lower_Bound) & (dataframe[column] <= Upper_Bound)]
    return Q1, Q2, Q3, IQR, Lower_Bound, Upper_Bound, new_df
