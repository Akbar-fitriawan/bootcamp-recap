[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_n4074K4)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14981332&assignment_repo_type=AssignmentRepo)
# Live Code 6 - Set 2

---

## Assignment Objectives

*Live Code 6* ini dibuat guna mengevaluasi konsep Unsupervised Learning sebagai berikut:

- Mampu memahami konsep Unsupervsied Learning dengan KMeans.

- Mampu mempersiapkan data untuk digunakan saat training dengan algoritma KMeans.

- Mampu mengimplementasikan KMeans untuk membuat prediksi.

---

## Dataset Desciription

Dataset Name : `humanitarian-aid.csv`

Dataset Description : This dataset contains indicators related to the well-being level of the population in a country.

| Column | Description |
| --- | --- |
| `country` | Name of the country |
| `child_mortality` | Death of children under 5 years of age per 1000 live births |
| `exports` | Export of goods and services. Given as percentage of the Total GDP |
| `health` | Total health spending as percentage of Total GDP |
| `imports` | Imports of goods and services. Given as percentage of the Total GDP |
| `income` | Net income per person |
| `inflation` | The measurement of the annual growth rate of the Total GDP |
| `life_expectancy` | The average number of years a new born child would live if the current mortality patterns remain the same |
| `total_fertility` | The number of children that would be born to each woman if the current age-fertility rates remain the same |
| `gdpp` | The GDP per capita. Calculated as the Total GDP divided by the total population. |

---

## Problems

Sebuah lembaga LSM berkomitmen untuk memerangi kemiskinan dan menyediakan fasilitas dan bantuan dasar bagi masyarakat di negara-negara kurang mampu. Baru-baru ini, mereka telah mampu mengumpulkan dana sekitar $ 10 juta. CEO LSM tersebut perlu memutuskan bagaimana menggunakan uang ini secara strategis dan efektif. Isu signifikan yang muncul saat membuat keputusan ini adalah terkait dengan pemilihan negara mana yang paling membutuhkan bantuan.

Buatlah model machine learning Unsupervised Learning dengan menggunakan KMeans untuk mengelompokkan negara-negara tersebut. **Nyatakan secara jelas negara mana yang Anda rekomendasikan kepada sang CEO di bagian Kesimpulan.**

*Dataset terlampir pada repository*

---

## Instruction

*Live Code 6* dikerjakan dalam format ***notebook (.ipynb)*** dengan beberapa **kriteria wajib** dibawah ini:
1. Machine Learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan objective yang ingin dicapai.

   2. Import Libraries
      > Cell pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset yang diberikan dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
       > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam data untuk membuat model. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.

   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

5. **Disarankan mengerjakan menggunakan Google Colab**.
    > Segala jenis problem yang muncul akibat masalah yang dialami komputer student saat Live Code karena menggunakan Jupyter Notebook seperti laptop blue screen, laptop freeze, dll, menjadi tanggung jawab student.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1LC6_Set_2_<nama-students>.ipynb` misal `P1LC6_Set_2_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (normalisasi, scaling, dll) | 35 pts |
| PCA | Mampu melakukan reduksi dimensi dengan menggunakan PCA | 10 pts |
| KMeans | Mampu melakukan training data dengan algoritma KMeans | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berjalan dan berfungsi dengan sempurna | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

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

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Mampu melakukan evaluasi model untuk menentukan nilai `K` / jumlah cluster | 15 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Hint : 

Setelah jumlah cluster yang optimal terbentuk, silakan lakukan beberapa hal dibawah ini : 
1. Visualisasikan dalam ruang 2D.
2. Lakukan eksplorasi terhadap masing-masing cluster sehingga ciri khas setiap cluster dapat diketahui.
3. Narasikan negara mana yang Anda rekomendasikan.
```
---

```
Total Points : 125
```

---

## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 6 menjadi 0.**
