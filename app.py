import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from main import data_reading
from numeric_information import (Describing_numeric_column, calculate_skew_and_plot_kdeplot, outlier_detection,missing_value_calculation,whether_to_impute_missing_values, missing_value_treatment)
from categorical_information import counting_information, plot_countplot

st.set_page_config(page_title="EDA Tool", layout = "wide", page_icon="📊")

st.title("EDA TOOL for Data Analysis")

uploaded_file = st.file_uploader("Upload Your csv File", type = ["csv"])

if uploaded_file is None:
    st.info("👆 Please upload a CSV file to get started.")
    st.stop()

@st.cache_data
def load_data(uploaded_file):

    return data_reading(file = uploaded_file)

dataframe = load_data(uploaded_file)
st.success(f"✅ File uploaded successfully! **{uploaded_file.name}**")









st.sidebar.title("📊 EDA Tool")
st.sidebar.markdown("---")

menu_options = st.sidebar.selectbox("Select options",["DataFrame","Columns"])

# DataFrame Information

if menu_options == "DataFrame":

    st.title("DataFrame Information")
    st.subheader("🔷 Shape of DataFrame")
    col1, col2 = st.columns(2)
    col1.metric("Rows", dataframe.shape[0])
    col2.metric("Columns", dataframe.shape[1])

    # Column Info

    st.subheader("🔷 Column Information")
    info_df = pd.DataFrame({
        "Column":dataframe.columns,
        "Datatype": dataframe.dtypes.values,
        "Non-null Count": dataframe.count().values,
        "Null count": dataframe.isna().sum().values,
        "Null Percentage": (dataframe.isna().sum().values/ len(dataframe)*100).round(2)
    })
    st.dataframe(info_df, use_container_width=True)


    #Sample Rows
    st.subheader("🔷 Sample Rows")
    sample_number = st.number_input("Enter number of sample rows", min_value = 1, max_value= len(dataframe), value = 5)
    if st.button("show sample"):
        st.dataframe(dataframe.sample(sample_number), use_container_width= True)


# Section 2 Column Information

elif menu_options == "Columns":

    st.title("Column Analysis")
    column = st.selectbox("Select Column", dataframe.columns)

    numeric_dtype = ["int64", "float64", "int32","float32"]
    categorical_dtype = ["object"]

    if dataframe[column].dtype in numeric_dtype:
        st.markdown("🔢 Numeric Column")

        # Basic Description
        st.subheader("📌 Basic Description")
        mean, std_dev = Describing_numeric_column(dataframe, column)
        st.dataframe(dataframe[column].describe().to_frame(), use_container_width= True)
        c1, c2, c3 = st.columns(3)
        c1.metric("Mean", f"{mean:.4f}")
        c2.metric("Median", f"{dataframe[column].median():.4f}")
        c3.metric("Std Dev", f"{std_dev:.4f}")

        st.markdown("-----------")

        # Outlier Detection
        st.subheader("📌 Outlier Detection")
        if st.button("Detect Outlier"):

            st.session_state.detected = True

        if st.session_state.get("detected", False):
            skew  = dataframe[column].skew()

            q1, q2, q3, iqr, lower_bound, upper_bound, new_df = outlier_detection(dataframe, column, skew, mean, std_dev)

            if q1 == 0.0 and iqr == 0.0:
                st.info("💡 Normal distribution detected. Outliers calculated using **Z-Score Method (3 Std Dev)**.")
                c1, c2 = st.columns(2)
                c1.metric("Lower Bound", f"{lower_bound:.4f}")
                c2.metric("Upper Bound", f"{upper_bound:.4f}")

            else:          
                c11, c12, c13 = st.columns(3)
                c21, c22, c23 = st.columns(3)

                c11.metric("Q1", f"{q1:.4f}")
                c12.metric("Q2", f"{q2:.4f}")
                c13.metric("Q3", f"{q3:.4f}")
                c21.metric("IQR", f"{iqr:.4f}")
                c22.metric("Lower Bound", f"{lower_bound:.4f}")
                c23.metric("Upper Bound", f"{upper_bound:.4f}")

                if st.checkbox("View Updated Dataframe"):
                    st.title("Updated DataFrame")
                    st.dataframe(new_df)

        st.markdown("---------")

        # Missing Value Analysis
        st.subheader("📌 Missing Value Analysis")
        null_value,null_value_percentage, message = missing_value_calculation(dataframe, column)

        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("Null Value", null_value)
        mc2.metric("Null Value Percentage", null_value_percentage)
        mc3.metric("Verdict", message)

        # Missing Value Imputation
        st.title("Data Cleaning Dashboard")

        # Component to select the column you want to check
        # column = st.selectbox("Select Column to Analyze", dataframe.columns)

        # Step 1: Check for missing values dynamically
        missing_count = dataframe[column].isna().sum()

        if missing_count > 0:
            # Inform the user beautifully
            st.warning(f"⚠️ '{column}' has {missing_count} missing values.")
            
            # Capture the user's decision using a radio toggle
            choice = st.radio(
                "Do you wish to impute these Missing Values?",
                options=["No", "Yes"],
                index=0  # Defaults to "No"
            )
            
            # Step 2: Trigger execution only when they click the button
            if st.button("Apply Decision"):
                result_msg = whether_to_impute_missing_values(dataframe, column, choice)
                
                # Display feedback based on the outcome
                if "Success" in result_msg:
                    st.success(result_msg)
                    st.dataframe(dataframe) # Show updated dataframe
                else:
                    st.info(result_msg)

        else:
            st.success(f"✅ '{column}' is perfectly clean! No missing values found.")

    elif dataframe[column].dtype in categorical_dtype:

        st.markdown("Categorical Data Type")

        # Basic Description

        st.subheader("Basic Description")
        unique_count, mode, value_counts = counting_information(dataframe, column)

        c1, c2,c3 = st.columns(3)

        c1.metric("Unqiue Values", f"{unique_count}")
        c3.metric("Mode", f"{value_counts[0]}")
        c2.metric("Mode Value", f"{value_counts.index[0]}")
        st.dataframe(value_counts.to_frame(), use_container_width= True)

        st.markdown("-----------")


        # Plotting Countplot

        st.subheader("Distribution of Column")
        graph = plot_countplot(dataframe, column)
        if graph:
            st.pyplot(graph)


