[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cRgiVn_y)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15152894&assignment_repo_type=AssignmentRepo)
# Live Code 8 - Set 1

---

## Assignment Objectives

*Live Code 8* ini dibuat guna mengevaluasi konsep NoSQL pada pembelajaran Phase 2 sebagai berikut:

- Mampu memahami konsep NoSQL.

- Mampu memasukkan data ke dalam tools NoSQL (Elasticsearch).

- Mampu membuat visualisasi data dengan Kibana.

---
## Dataset Description

Dataset : `survey-stack-overflow-2022.pkl`

| Column | Description |
| --- | --- |
| `ResponseID` | ID seorang responden |
| `Age` | Rentang usia responden |
| `RemoteWork` | Tempat kerja responden (`Remote`, `Offline`, `Hybrid`) |
| `CodingActivities` | Jenis aktivitas ngoding diluar kerja |
| `Education` | Tingkat pendidikan |
| `YearsCode` | Jumlah tahun seseorang sudah mulai ngoding (termasuk saat fase belajar ngoding, misal: belajar di Universitas, seminar, dll) |
| `YearsCodePro` | Jumlah tahun seseorang menjadi developer profesional (tidak termasuk fase belajar ngoding) |
| `DevType` | Jenis pekerjaan responden |
| `OrgSize` | Ukuran perusahaan dimana responden bekerja |
| `Country` | Negara tempat tinggal responden |
| `ProgrammingLanguage` | Jenis bahasa pemrograman yang dipakai di tempat kerja |
| `Database` | Jenis database yang dipakai di tempat kerja |
| `Platform` | Jenis cloud platform yang dipakai di tempat kerja |
| `WebFramework` | Jenis web framework yang dipakai di tempat kerja |
| `OtherFramework` | Jenis framework lain yang juga dipakai di tempat kerja |
| `ToolsTech` | Jenis developer tools yang digunakan untuk proses compiling, building dan testing |
| `CollabTools` | Jenis Collaborative Work Management tools yang dipakai |
| `OfficeTools` | Jenis communication tools yang digunakan untuk saling berinteraksi |
| `AIOpinion` | Opini responden tentang kegunaan tools AI dalam mendukung pekerjaannya |
| `Industry` | Jenis industri dimana responden bekerja |
| `AnnualSalary` | Gaji tahunan (USD) |

---

## Problems

Kasus : Seorang investor ingin membuat perusahaan yang bergerak dibidang IT. Ia ingin membuat perusahaan dibidang Travel Online dengan nama Berlian Travel. Namun, karena minimnya pengetahuan dari investor tersebut, ia menghubungi Anda selaku temannya yang memiliki kemampuan dibidang IT. Bantulah teman Anda ini dengan menjawab pertanyaannya dalam bentuk sebuah report/dashboard. Anda akan menggunakan dataset survey Stack Overflow 2022 sehingga jawaban/rekomendasi yang Anda berikan mendekati kenyataan yang ada.

1. Untuk membuat sebuah perusahaan IT, maka diperlukan platform untuk menampung code, data, konfigurasi, dll. Buatlah visualisasi yang menggambarkan **Top 7 `Platform` terpopuler** yang paling sering dipakai menggunakan Vertical Bar !

2. Platform Berlian Travel membutuhkan database yang dapat dihandalkan mengingat model bisnisnya yang menarik dan akan menyimpan banyak sekali file seperti gambar, video, audio, data user, data transaksi, dll. Buatlah visualisasi semacam `Wordcloud` untuk menampilkan **Top 30 `Database`** terpopuler yang sering dipakai.

3. Berlian Travel rencananya akan ditampilkan via web browser saja. Berikan **rekomendasi mengenai `WebFramework`** apa saja yang sering dipakai **di masing-masing Top 7 `Platform`** yang Anda dapatkan dari soal nomor 1. *Hint: Anda dapat menggunakan `Heatmap` dengan sumbu-x adalah `Platform` dan sumbu-y adalah `WebFramework`.*

4. Untuk mengurangi biaya sewa kantor, sang investor menginginkan bahwa tim IT dapat bekerja dari rumah. Berikan rekomendasi dengan menggunakan `Pie Chart` terhadap **Top 10 `OfficeTools`** yang harus dipakai oleh tim IT jika mereka bekerja secara `Remote`.

5. Untuk tim Back-End, berikan rekomendasi berupa `Horizontal Bar` mengenai **`ProgrammingLanguage` apa yang harus dikuasai**. Anda bisa menggunakan column `DevType`, kemudian memfilter terlebih dahulu posisi `back-end` ATAU `full-stack` sebelum melakukan visualisasi.

6. Baik Back-End Developer maupun Front-End Developer, terkadang memiliki beberapa tools yang mirip yang dapat digunakan oleh keduanya. Karena perusahaan ini baru akan berdiri, hal ini akan membuat biaya hiring lebih efisien jika seorang Back-End Developer dapat mengoperasikan tools-tools yang sering dipakai Front-End Developer, begitu juga sebaliknya. Berikan rekomendasi dalam bentuk `Wordcloud` mengenai **Top 50 `ToolsTech` yang dapat dipakai oleh seorang `DevType` yang berposisi sebagai `Developer`**.

7. Sang investor ingin pegawainya memiliki tingkat pendidikan `Bachelor` atau `Master` atau `Associate_degree`. **Carilah gaji minimal, rata-rata, dan maksimal** berdasarkan tingkat pendidikan yang baru disebutkan di masing-masing rentang umur.

---
## Instruction

Berikut ini adalah langkah-langkah yang harus dilakukan : 

1. Download dataset dari [link](https://drive.google.com/file/d/1BiFVXvj4AmoPWTBWFB1neSshqFQiyst-/view?usp=sharing) berikut. **Dataset ini tidak perlu anda upload ke GitHub.**

2. Buat script Python yang digunakan untuk memasukkan dataset ke dalam Elasticsearch. Beri nama file ini dengan format `P2LC8_<nama-student>.ipynb`. Contoh : `P2LC8_raka_ardhi.ipynb`.

3. Proses memasukkan data ke Elasticsearch akan memakan waktu karena jumlah data yang dimasukkan adalah **89.183 document**. Pastikan sebelum Anda memulai visualisasi, cek jumlah document yang sudah dimasukkan haruslah berjumlah 89.183. Silakan tunggu beberapa saat jika script Python sudah selesai memasukkan data namun di Elasticsearch data belum terbaca 89.183.

4. Jika proses memasukkan data masih belum selesai dalam kurun waktu 1 jam, Anda dapat memulai untuk membuat visualisasi dengan menggunakan data yang sudah ada terlebih dahulu. Namun, pastikan bahwa sebelum jawaban final dikumpulkan, ubah time window menjadi `Last 3 hours` untuk memastikan bahwa report yang dibuat menggunakan keseluruhan data. Contoh : ![plot](update-time.png)

5. Untuk pembuatan dashboard, di beberapa browser, terdapat kemungkinan tidak semua data tertampil efek rendering font yang kurang maksimal oleh browser tersebut. Gunakan browser yang berbeda jika disuatu browser datanya tidak tertampil.

6. Buatlah dashboard dengan Kibana sesuai dengan problem dengan ketentuan :
   - Terdapat 7 plot visualisasi sesuai dengan problem.
   - Tambahkan 1 visualisasi dibagian atas berupa `Markdown` yang berisi Identitas student.
   - Total visualisasi : 7 visualisasi + 1 visualisasi Markdown mengenai indetitas = 8 visualiasi.

7. Screenshot setiap plot pada Dashboard.
   - Buat sebuah folder bernama `images`.
   - Masukkan semua screenshot ke dalam folder tersebut.
   - Screenshot juga bagian mengenai Identitas.

---

## Assignment Submission

- Push Assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.

- Contoh bentuk repository :
  ```
  P2-LC8-Set-1/raka-ardhi
  |
  ├── P2LC8_raka_ardhi.ipynb
  ├── README.md
  ├── update-time.png
  ├── /images
      ├── introduction & objective.png
      ├── plot 01.png
      ├── plot 02.png
      ├── plot 03.png
      ├── plot 04.png
      ├── plot 05.png
      ├── plot 06.png
      └── plot 07.png
  ```

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Data Ingestion | Mampu memasukkan data ke dalam Elasticsearch menggunakan Python | 4 pts |
| Data Visualization | Mampu membuat 7 visualisasi dengan menggunakan Kibana | Soal 1 & 2 : 4 pts / visualisasi <br> Soal 3 & 4 : 6 pts / visualisasi <br> Soal 5 & 6 : 7 pts / visualisasi <br> Soal 7 : 8 pts |

### Clarity

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Clarity | Kejelasan visualisasi yang ditampilkan | 1 pts / visualisasi |

```
Untuk mendukung kejelasan visualisasi yang telah Anda buat, Anda dapat :
1. Menambahkan grid
2. Mengubah warna sehingga lebih bervariasi
3. Menambahkan legend
4. dll
```

---

```
Total Points : 53
```

---
## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 8 menjadi 0.**
