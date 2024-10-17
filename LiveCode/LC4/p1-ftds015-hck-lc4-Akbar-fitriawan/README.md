[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/BAr8c996)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14829424&assignment_repo_type=AssignmentRepo)
# Live Code 4 - Set 3

---

## Assignment Objectives

*Live Code 4* ini dibuat guna mengevaluasi konsep Regression sebagai berikut:

- Mampu memahami konsep regression dengan Linear Regression.

- Mampu mempersiapkan data untuk digunakan dalam model Linear Regression.

- Mampu mengimplementasikan Linear Regression untuk membuat prediksi.

---

## Dataset Desciription

Dataset : `car-price-prediction.csv`

Description : Dataset ini berisi harga penjualan mobil bekas.

| Column | Description |
| --- | --- |
| brand | Merek mobil |
| model | Model mobil |
| year | Tahun pembelian |
| price | Harga penjualan (GBP) |
| transmission | Jenis gearbox |
| mileage | Jarak tempuh (KM) |
| fuelType | Jenis bahan bakar |
| tax | Pajak setiap tahun |
| mpg | Konsumsi bahan bakar (Miles per gallon) |
| engineSize | Ukuran mesin (litres) |

---

## Problems

Anda adalah seorang Data Scientist yang hendak ingin membeli mobil bekas. Dikarenakan kriteria mobil idaman Anda belum ada iklan penjualannya, Andapun tidak tahu berapa estimasi harga yang harus Anda keluarkan untuk membeli mobilnya. Anda memutuskan untuk memprediksi estimasi harga sang mobil idaman dengan cara membuat model Machine Learning berdasarkan data penjualan mobil bekas yang tersedia di Internet.

Buatlah model Linear Regression untuk memprediksi harga mobil bekas menggunakan dataset yang disediakan. Dataset terlampir pada repository dan jawablah pertanyaan dibawah ini.

***Note : Anda diwajibkan untuk menjawab pertanyaan-pertanyaan dibawah ini. Namun, Anda juga dipersilakan untuk melakukan Exploratory Data Analysis (EDA) dan analisa model lainnya pada bagian Model Evaluation diluar pertanyaan yang diminta.***

### Lakukan pada bagian Exploratory Data Analysis (EDA)
1. Informasi yang diberikan dibawah ini adalah jenis mobil bekas berdasarkan konsumsi bahan bakar berbanding dengan jarak.
   * `super efficient` : `mpg` ≥ 60
   
   * `efficient` : 50 ≤ `mpg` < 60
   
   * `decent` : 35 ≤ `mpg` < 50
   
   * `standard` : 25 ≤ `mpg` < 35
   
   * `not efficient` : `mpg` < 25
  
   Buatlah bar plot yang menampilkan besarnya masing-masing jenis diatas dan urutkan dari jumlah jenis terbanyak hingga terkecil.

### Lakukan pada bagian Model Analysis
1. Analisa hasil prediksi dengan langkah-langkah dibawah ini : 
   1. Lakukan prediksi pada test-set. 
   
   2. Dari keseluruhan test-set yang diprediksi, berapa nilai minimum dan nilai maksimum yang diprediksi oleh model. 
   
   3. Bandingkan nilai minimum dan nilai maksimum dari keseluruhan hasil prediksi dengan nilai minimum dan nilai maksimum yang sebenarnya dari keseluruhan test-set.
   
   4. Analisa dan narasikan hasil ini.
 
2. Apakah model Anda cenderung menghasilkan harga prediksi yang lebih rendah ataukah cenderung menghasilkan harga prediksi yang lebih tinggi dari harga sebenarnya baik dari train-set maupun test-set ? Buktikan hal ini dengan sebuah eksplorasi.

---

## Instruction

*Live Code 4* dikerjakan dalam format ***notebook (.ipynb)*** dengan beberapa **kriteria wajib** dibawah ini:

1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1LC4_Set_3_<nama-students>.ipynb` misal `P1LC4_Set_3_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria| Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 35 pts |
| Linear Regression | Mengimplementasikan Linear Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata dengan Baik| Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas dan lengkap terkait masalah dan latar belakang masalah yang akan diselesaikan.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
7. Tidak adanya typo.
```

### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 25 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 10 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

```
Total Points : 115
```

---
## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 4 menjadi 0.**
