import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


# Load your dataset
@st.cache_data
def load_data():
    data = pd.read_csv("P1G5_Set_1_akbar_fitriawan.csv")
    return data

def run():
    data = load_data()

    # Title of the web app
    st.title('Exploratory Data Analysis with Streamlit')

    # Display the dataset
    st.subheader('Dataset')
    st.write(data.head())

    # EDA Section
    st.subheader('Exploratory Data Analysis')

    # Summary Statistics
    st.write('Summary Statistics:')
    st.write(data.describe())

    # Data Visualization
    st.subheader('Data Visualization')



    # Correlation Matrix
    st.write('Correlation Matrix:')
    with open('list_cat_cols.pkl', 'rb') as file3:
        list_cat_cols = pickle.load(file3)

    with open('list_num_cols.pkl', 'rb') as file4:
        list_num_cols = pickle.load(file4)


    corr_matrixCat = data[['default_payment_next_month']+list_cat_cols].corr()
    st.write(sns.heatmap(corr_matrixCat, annot=True).figure)

    corr_matrixNum = data[['default_payment_next_month']+list_num_cols].corr()
    st.write(sns.heatmap(corr_matrixNum, annot=True).figure)


if __name__ == '__main__':
    run()