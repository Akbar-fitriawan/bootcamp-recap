import streamlit as st
from PIL import Image

# page
from st_app import app
from st_recomendation import alpha
from st_filterRecomendation import beta

# Buka gambar menggunakan PIL
pil_image = Image.open("logo.png")

# Menambahkan menu navigasi di sidebar
menu = st.sidebar.selectbox("Menu", ["Halaman Utama", "Recomendation System", "Another Recomender Alpha", "Another Recomender Beta"])
st.sidebar.divider()

st.sidebar.markdown("## Contributor")
st.sidebar.markdown("""
Albert Novanto Pratama Jayadi | [Github](https://github.com/albertn15)  
M. Arindra Jehan Putrandadira | [Github](https://github.com/arindrajehan)  
Titan Russo | [Github](https://github.com/TRusso03)  
Akbar Fitriawan | [Github](https://github.com/Akbar-fitriawan)""")

# Menampilkan halaman berdasarkan pilihan menu
if menu == "Halaman Utama":
    st.markdown("<h1 style='text-align: center;'>FeastFinder</h1>", unsafe_allow_html=True)
    st.image(pil_image, width=440, use_column_width=True)
    st.write('')

    st.markdown("""
    ## Selamat datang di FeastFinder

    FeastFinder adalah platform yang menyediakan solusi cerdas untuk pencarian restoran yang sesuai dengan preferensi Anda.

    Dengan menggunakan teknologi terkini dan algoritma cosine similarity, kami menyajikan sistem rekomendasi restoran yang didukung oleh proses feature engineering menggunakan text preprocessing dari NLTK dan TfidfVectorizer.

    Cara kerjanya sederhana namun efektif: Anda memberikan informasi tentang jenis makanan yang Anda sukai dan memberikan ulasan tentang pengalaman makan Anda sebelumnya. Dari sana, kami menggunakan informasi ini untuk menciptakan deskripsi yang unik dan membandingkannya dengan basis data restoran kami. Melalui proses perbandingan, kami mengidentifikasi restoran yang paling cocok dengan preferensi Anda.
    """)
    st.write('')

    st.markdown("""
                ## Fitur utama 
    "Pencarian Spesifik" dalam FeastFinder memungkinkan pengguna untuk dengan cepat menemukan restoran yang sesuai dengan keinginan mereka. Dengan kemampuan untuk mencari berdasarkan kategori spesifik seperti jenis masakan, lokasi, rentang harga dan suasana, pengguna dapat dengan mudah mengkustomisasi pencarian mereka. FeastFinder menyajikan hasil pencarian yang relevan dan menyertakan pemetaan lokasi restoran untuk memudahkan pengguna dalam pengambilan keputusan. Dengan fitur ini, pengguna dapat dengan mudah menemukan tempat makan yang tepat sesuai dengan preferensi mereka tanpa harus melalui pencarian yang memakan waktu.""")

    st.markdown("""
        ## GitHub Repository
        Untuk melihat kode sumber dan berkontribusi pada pengembangan aplikasi kami, kunjungi repository GitHub kami di [link ini](https://example.com). Kami menyambut kontribusi dari komunitas untuk membuat aplikasi ini semakin baik.""")


elif menu == "Recomendation System":
    app()
elif menu == "Another Recomender Alpha":
    alpha()
else:
    beta()
