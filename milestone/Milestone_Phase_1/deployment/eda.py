import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
# Memanggil data csv 
    df= pd.read_csv(r'Car_Insurance_Claim.csv')

# menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn phik matrix
    st.title('Distribusi Claims or NO')
    image = Image.open('distclaim.png')
    st.image(image, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        claim_percentage = 31.3
        no_claim_percentage = 68.7
        st.caption(f'Dari plot di atas {claim_percentage:.1f}% orang yang mengajukan claim dan {no_claim_percentage:.1f}% yang tidak mengajukan claim, target prediksi imbalnced atau tidak seimbang sehingga harus penyasuaian parameter atau metode lain untuk mengatasinya.')


#menampilakn phik matrix
    st.title('Visualisasi Age Vs Outcome')
    image = Image.open('age.png')
    st.image(image, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):

        st.caption('lorem ipsum')


#menampilakn phik matrix
    st.title('Visualisasi Drive experience Vs Outcome')
    image = Image.open('expdrive.png')
    st.image(image, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):

        st.caption('lorem upsum')