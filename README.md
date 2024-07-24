# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya Jaya Institut ingin mendeteksi siswa yang mungkin akan melakukan dropout. Dengan mendeteksi siswa yang mungkin akan melakukan dropout, institusi pendidikan ini dapat memberikan bimbingan khusus kepada siswa tersebut sehingga dapat mencegah terjadinya dropout.

### Cakupan Proyek
Proyek ini akan membahas mengenai bagaimana mendeteksi siswa yang mungkin akan melakukan dropout. Proyek ini akan membahas mengenai:
- Analisis data siswa yang dropout dan tidak dropout
- Pembuatan model machine learning untuk mendeteksi siswa yang mungkin akan melakukan dropout
- Pembuatan business dashboard untuk memantau perkembangan siswa

### Persiapan

Sumber data: [Dicoding: Students Performance]https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:
1. Buat folder baru untuk menyimpan proyek. Misalnya, dengan nama `student`.
2. Buka terminal atau PowerShell.
3. Arahkan ke folder yang telah dibuat dengan menjalankan perintah berikut. Contoh: `cd student`.
4. Di terminal, buat virtual environment dengan conda menggunakan perintah berikut.
    ```
     conda create --name attrition python=3.9.19
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate student
    ```
4. Install semua library yang dibutuhkan menggunakan perintah berikut.
    ```
    pip install -r requirements.txt
    ```
    atau
    ```
    pip install joblib==1.3.2 matplotlib==3.8.2 scikit_learn==1.2.2 streamlit==1.24.1 numpy==1.25.1 pandas==2.0.3 seaborn==0.12.2 SQLAlchemy==2.0.31
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```

## Business Dashboard
Business dashboard adalah salah satu cara untuk memantau perkembangan siswa. Dashboard ini akan menampilkan informasi mengenai:
- Peminjam Uang, Penerima Beasiswa, dan Biaya Sekolah Naik dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai peminjam uang, penerima beasiswa, dan biaya sekolah naik dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap peminjam uang, penerima beasiswa, dan biaya sekolah. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki peminjam uang yang lebih tinggi, penerima beasiswa yang lebih rendah, dan biaya sekolah yang lebih rendah dibandingkan dengan siswa yang tidak dropout.
- Rata-rata Nilai Siswa dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai rata-rata nilai siswa dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap rata-rata nilai siswa. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki rata-rata nilai yang lebih rendah dibandingkan dengan siswa yang tidak dropout.
- Rata-rata Unit Kurikulum Siswa yang diambil dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai rata-rata unit kurikulum siswa dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap rata-rata unit kurikulum siswa. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki rata-rata unit kurikulum yang lebih tinggi dibandingkan dengan siswa yang tidak dropout.
- Rata-rata Unit Kurikulum Siswa yang diterima dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai rata-rata unit kurikulum siswa yang diterima dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap rata-rata unit kurikulum siswa yang diterima. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki rata-rata unit kurikulum yang diterima yang lebih tinggi dibandingkan dengan siswa yang tidak dropout.
- Rata-rata Umur Siswa dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai rata-rata umur siswa dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap rata-rata umur siswa. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki rata-rata umur yang lebih tinggi dibandingkan dengan siswa yang tidak dropout.
- Rata-rata Passing Grade Siswa dari Status Siswa
    Dashboard ini akan menampilkan informasi mengenai rata-rata passing grade siswa dari status siswa. Hal ini akan membantu institusi pendidikan untuk mengetahui bagaimana status siswa berpengaruh terhadap rata-rata passing grade siswa. Seperti yang terdapat pada gambar tersebut, terlihat bahwa siswa yang dropout memiliki rata-rata passing grade yang lebih rendah dibandingkan dengan siswa yang tidak dropout.

## Menjalankan Sistem Machine Learning
Sistem machine learning ini akan membantu institusi pendidikan untuk mendeteksi siswa yang mungkin akan melakukan dropout. Sistem ini akan menggunakan model machine learning yang telah dibuat sebelumnya. Sistem ini akan menerima input berupa data siswa dan akan memberikan output berupa prediksi apakah siswa tersebut akan melakukan dropout atau tidak.

Untuk menjalankan streamlit, jalankan perintah berikut.
    ```
    streamlit run app.py
    ```

Contoh data yang digunakan:
| Kolom | Nilai |
| --- | --- |
|Admission_grade | 117 |
|Age_at_enrollment | 18 |
|Application_mode | 17 |
|Application_order | 1 |
|Curricular_units_1st_sem_approved | 5 |
|Curricular_units_1st_sem_enrolled | 6 |
|Curricular_units_1st_sem_evaluations | 10 |
|Curricular_units_1st_sem_grade | 10 |
|Curricular_units_1st_sem_without_evaluations | 1 |
|Curricular_units_2nd_sem_approved | 5 |
|Curricular_units_2nd_sem_enrolled | 6 |
|Curricular_units_2nd_sem_evaluations | 9 |
|Curricular_units_2nd_sem_grade | 12.2 |
|Curricular_units_2nd_sem_without_evaluations | 0 |
|Daytime_evening_attendance | 1 |
|Debtor | 0 |
|Displaced | 1 |
|Gender | 0 |
|Marital_status | 1 |
|Mothers_qualification | 37 |
|Previous_qualification_grade | 120 |
|Scholarship_holder | 1 |
|Tuition_fees_up_to_date | 1 |
| --- | --- |

Berikut link untuk menjalankan sistem machine learning: [Jaya-Jaya Institute](https://ghifarullah19-jaya-jaya-institute.streamlit.app/)

## Conclusion
Berdasarkan hasil analisis data yang telah dilakukan, ditemukan bahwa terdapat beberapa faktor yang mempengaruhi siswa untuk melakukan dropout. Faktor-faktor tersebut antara lain adalah peminjam uang, penerima beasiswa, biaya sekolah, rata-rata nilai, rata-rata unit kurikulum, umur, dan passing grade. Oleh karena itu, institusi pendidikan dapat memberikan bimbingan khusus kepada siswa yang memiliki faktor-faktor tersebut sehingga dapat mencegah terjadinya dropout.

### Rekomendasi Action Items
Berdasarkan hasil analisis data yang telah dilakukan, terdapat beberapa action items yang dapat dilakukan oleh institusi pendidikan. Action items tersebut antara lain adalah:
- Mengkaji ulang peminjam uang, penerima beasiswa, dan biaya sekolah dari siswa yang dropout
- Memberikan bimbingan khusus kepada siswa yang memiliki faktor-faktor yang mempengaruhi siswa untuk melakukan dropout
- Memonitor perkembangan siswa secara berkala
- Membuat program-program yang dapat membantu siswa untuk tidak melakukan dropout
