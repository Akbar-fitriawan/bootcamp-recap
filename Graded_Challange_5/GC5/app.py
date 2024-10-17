import pandas as pd 
import numpy as np
import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])
if page == 'Home Page':
    # Judul halaman
    st.title('Selamat Datang di Graded Challange 5')
    st.write('Nama  :   Akbar Fitriawan')
    st.write('Batch :   FTDS-HCK 14')
    st.divider()
    st.header('Objective')
    # Deskripsi singkat tentang proyek
    st.write("""
    Proyek ini bertujuan untuk memprediksi apakah customer akan membayar Credit card di bulan depan?.
    Kami menggunakan model Machine Learning untuk memprediksi hasil dan mengklasifikasikan data baru.
    """)
    st.header('Models')
    st.write('-', 'Logistic Regression')
    st.write('-', 'SVM Classifier')
    st.write('-', 'K-Nearest Neighbor (KNN)')
    st.divider()
    st.header('Metric Score')
    df = pd.read_csv('metric_score.csv',index_col=0)
    st.dataframe(df)
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    models.run()

