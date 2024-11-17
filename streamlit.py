# prompt: use streamlit to create an interactive dashboard
pip install matplotlib

#!pip install streamlit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import streamlit as st

# Load the data
data = pd.read_csv('/content/drive/My Drive/IBES.csv')

st.title("Interactive Data Exploration Dashboard")
st.markdown("""
## Introduction
Welcome to the EPS Forecasting Dashboard! This tool is designed to assist financial analysts and investors by providing detailed visual analysis of Earnings Per Share (EPS) forecasting accuracy. By examining historical forecast data against actual outcomes, we aim to uncover patterns and insights that help in making informed investment decisions.
""")

# Sidebar for user selections
st.sidebar.header("Select Options")
selected_columns = st.sidebar.multiselect("Select Columns for Analysis", data.columns)

# Visualization options
st.sidebar.header("Visualization Options")
plot_type = st.sidebar.radio("Choose Plot Type", ['Histogram', 'Box Plot', 'Scatter Plot', 'Heatmap'])

st.header("Data Exploration")

# Based on user selection of plot type, show the corresponding plot
if plot_type == 'Histogram':
    if not selected_columns:
        st.write("Please select at least one column from the sidebar to view the plots.")
    else:
        for column in selected_columns:
            if pd.api.types.is_numeric_dtype(data[column]):
                st.subheader(f"Histogram of {column}")
                fig, ax = plt.subplots()
                ax.hist(data[column], bins=20)
                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')
                st.pyplot(fig)

elif plot_type == 'Box Plot':
    for column in selected_columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            st.subheader(f"Box Plot of {column}")
            fig, ax = plt.subplots()
            ax.boxplot(data[column])
            ax.set_ylabel(column)
            st.pyplot(fig)

elif plot_type == 'Scatter Plot':
    if len(selected_columns) > 1:  # Checking if there are at least two columns selected for scatter plot
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=selected_columns[0], y=selected_columns[1], ax=ax)
        ax.set_xlabel(selected_columns[0])
        ax.set_ylabel(selected_columns[1])
        st.pyplot(fig)

elif plot_type == 'Heatmap':
    if len(selected_columns) > 0:
        numeric_cols = [col for col in selected_columns if pd.api.types.is_numeric_dtype(data[col])]
        if numeric_cols:
            st.subheader
