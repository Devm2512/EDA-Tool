# import streamlit as st
# import pandas as pd
# import numpy as np
# from eda_utils import basic_info_dataframe
# from main import data_reading




# st.title("Exploratory Data Analysis Tool")

# st.sidebar.title("Menu")

# L = ["DataFrame", "Columns"]

# menu_option = st.sidebar.selectbox("", L)

# if menu_option == "DataFrame":

#     dataframe = data_reading()
#     shape, column_and_its_information, sample_rows = basic_info_dataframe(dataframe)


import streamlit as st
import pandas as pd
import numpy as np
from main import data_reading

st.title("Exploratory Data Analysis Tool")

st.sidebar.title("Menu")

menu_list = ["DataFrame", "Columns"]

menu_option = st.sidebar.selectbox("Select Option", menu_list)

# Load dataframe
dataframe = data_reading()

# ---------------- DATAFRAME INFORMATION ---------------- #

if menu_option == "DataFrame":

    st.header("DataFrame Information")

    st.subheader("Shape of DataFrame")
    st.write(dataframe.shape)

    st.subheader("Column Information")
    buffer = dataframe.info(buf=None)

    # Better way to show dataframe info
    info_df = pd.DataFrame({
        "Column": dataframe.columns,
        "Datatype": dataframe.dtypes,
        "Non-Null Count": dataframe.count()
    })

    st.dataframe(info_df)

    st.subheader("Sample Rows")

    sample_number = st.number_input(
        "Enter number of sample rows",
        min_value=1,
        max_value=len(dataframe),
        value=5
    )

    if st.button("Show Sample"):

        sample_rows = dataframe.sample(sample_number)
        st.dataframe(sample_rows)


# ---------------- COLUMN INFORMATION ---------------- #

elif menu_option == "Columns":

    st.header("Column Analysis")

    column = st.selectbox("Select Column", dataframe.columns)

    if dataframe[column].dtype in ["int64", "float64", "int32", "float32"]:

        st.subheader("Numeric Column Summary")

        st.write(dataframe[column].describe())

        st.write("Median:", dataframe[column].median())
        st.write("Mean:", dataframe[column].mean())
        st.write("Standard Deviation:", dataframe[column].std())

        st.subheader("Distribution Plot")

        st.line_chart(dataframe[column])

    else:

        st.subheader("Categorical Column Summary")

        st.write("Unique Values:", dataframe[column].nunique())

        st.write("Mode:", dataframe[column].mode())

        st.write("Value Counts")

        st.dataframe(dataframe[column].value_counts())