import streamlit as st
import pandas as pd
import numpy as np

# page
import eda
import prediction

page = st.sidebar.radio(label="Navigation", options=['Home Page', 'Exploratory Data Analysis', 'Prediction'])
st.sidebar.divider()


if page == "Home Page":
    st.header("Welcome Page")
    st.write('')
    st.write('Introduction')
    st.write("Name\t: Akbar Fitriawan")
    st.write("Batch\t: hacktiv8-15")

    st.write('Tujuan Milestone    : ')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('lorem ipsum')

    with st.expander("Problem Statement"):
            st.caption('lorem ipsum')

    with st.expander("Kesimpulan"):
        st.caption('lorem ipsum')
elif page == 'Exploratory Data Analysis':
    eda.run()
else:
     prediction.run()



