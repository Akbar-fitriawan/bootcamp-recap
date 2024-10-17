[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2mQiAgBn)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14914493&assignment_repo_type=AssignmentRepo)
# Live Code 5 - Set 1

---

## Assignment Objectives

*Live Code 5* ini dibuat guna mengevaluasi konsep Ensemble Learning sebagai berikut:

- Mampu memahami konsep ensemble learning dengan Decision Tree dan Random Forest.

- Mampu mempersiapkan data untuk digunakan dalam model Decision Tree dan Random Forest.

- Mampu mengimplementasikan Decision Tree dan Random Forest untuk membuat prediksi.

---

## Dataset Desciription

Dataset Name : `heart-attack-possibility.csv`

Description : Dataset ini berisi data rekam medis beberapa orang baik yang terkena serangan jantung maupun bukan disuatu rumah sakit.

| Column | Description |
| --- | --- |
| `age` | Age of the patient (in years) |
| `sex` | Sex of the patient |
| `cp` | Chest Pain Type <br><br> `0` = Typical angina <br> `1` = Atypical angina <br> `2` = Non-anginal pain <br> `3` = Asymptomatic |
| `trestbps` | Resting blood pressure (in mm Hg on admission to the hospital |
| `chol` | Serum cholesterol (in mg/dl) |
| `fbs` | Is fasting blood sugar > 120 mg/dl ? <br><br> `1` = Yes <br> `0` = No |
| `restecg` | Resting electrocardiographic results <br><br> `0` = Normal <br> `1` = Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) <br> `2` = Showing probable or definite left ventricular hypertrophy by Estes' criteria |
| `thalach` | Maximum heart rate achieved  |
| `exang` | Exercise induced angina <br><br> `1` = Yes <br> `0` = No |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | The Slope of the Peak Exercise ST Segment |
| `ca` | Number of Major Vessels (0-3) Colored by Flourosopy |
| `thal` | Thallium Stress Test Result  |
| `target` | Diagnosis of Heart Disease <br><br> `1` : Heart attack = Yes <br> `0` : Heart attack = No |

---

## Problems

Anda adalah seorang Data Scientist disebuah rumah sakit disuatu kota besar. Karena tingginya jumlah pasien yang datang setiap hari ke rumah sakit tersebut dan mengeluh adanya rasa sakit di area jantung, manajemen rumah sakit memutuskan untuk meminta Anda untuk membuat sebuah program untuk mendeteksi kemungkinan seseorang terkena penyakit jantung atau tidak. Hal ini bertujuan untuk mengefisienkan waktu seorang dokter jantung sehingga pasien yang ia temui memang kemungkinan besar dapat terkena penyakit jantung.

Buatlah model Machine Learning untuk memprediksi kemungkinan seseorang terkena serangan jantung menggunakan dataset yang disediakan. Dataset terlampir pada repository dan jawablah pertanyaan dibawah ini.

***Note : Anda diwajibkan untuk menjawab pertanyaan-pertanyaan dibawah ini. Namun, Anda juga dipersilakan untuk melakukan Exploratory Data Analysis (EDA) dan analisa model lainnya pada bagian Model Evaluation diluar pertanyaan yang diminta.***

### Lakukan pada bagian Exploratory Data Analysis (EDA)
1. Berdasarkan informasi dari [PennMedicine](https://www.pennmedicine.org/updates/blogs/heart-and-vascular-blog/2015/february/protecting-your-heart-what-is-a-healthy-cholesterol-level-for-you), dibawah ini adalah kategori mengenal tingkat kolesterol seseorang.
   * `healthy` : < 200
   
   * `at risk` : 200 - 240
   
   * `dangerous` : ≥ 240
   
   Berapa jumlah data masing-masing kategori berdasarkan tingkat kolesterol dari dataset yang diberikan dan buatlah visualisasinya ! (Hint : Anda dapat menggunakan kolom `chol` untuk melakukannya)

2. Lakukan perbandingan antara jumlah denyut nadi maksimal seseorang yang pernah terekam dengan jumlah denyut nadi maksimal yang seharusnya dengan panduan dibawah ini :
   * Data mengenai jumlah denyut nadi maksimal seseorang yang pernah terekam dapat menggunakan kolom `thalach`.
   
   * Data mengenai jumlah denyut nadi maksimal yang seharusnya, dapat mengikut langkah-langkah dibawah ini : 
     
     + Formula : `220 - usia seseorang`.
     
     + Buat kolom baru berdasarkan formula diatas mengenai jumlah denyut nadi maksimal yang seharusnya.
     
     + Beri nama kolom ini dengan `max_heart_rate`.
     
     + *Note : kolom baru (`max_heart_rate`) ini tidak perlu diikutsertakan dalam pembentukan model*
   
   * Bandingkan antara `thalach` dan `max_heart_rate` dengan kemungkinan seseorang terkena serangan jantung. Lakukan analisa terhadap hasil ini !

### Lakukan pada bagian Model Evaluation
1. Analisa hasil prediksi dengan langkah-langkah dibawah ini : 
   * Lakukan prediksi pada train-set.
   
   * Ambil data yang tergolong False Negative.
   
   * Jelaskan ciri-ciri dari pasien yang tergolong False Negative ini !

2. Analisa hasil prediksi dengan langkah-langkah dibawah ini : 
   * Lakukan prediksi pada test-set.
   
   * Ambil data yang tergolong False Negative.
   
   * Jelaskan ciri-ciri dari pasien yang tergolong False Negative ini !
   
   * Berikan analisa dan pernyataan apakah ciri-ciri yang Anda dapatkan sama dengan ciri-ciri pada poin 1 diatas !

3. Apa kelebihan dan kelemahan model yang Anda buat untuk kasus ini ?

---

## Instruction

*Live Code 5* dikerjakan dalam format ***notebook (.ipynb)*** dengan beberapa **kriteria wajib** dibawah ini:
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

- Simpan assignment pada sesi ini dengan nama `P1LC5_Set_1_<nama-students>.ipynb` misal `P1LC5_Set_1_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria| Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 35 pts |
| Decision Tree | Mengimplementasikan Decision Tree dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Random Forest | Mengimplementasikan Random Forest dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Hyperparameter Tuning | Mengimplementasikan Hyperparameter Tuning dengan Scikit-Learn | 20 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru terhadap model yang terbaik dari keseluruhan proses modeling | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

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
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 37 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

```
Total Points : 167
```

---
## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 5 menjadi 0.**
