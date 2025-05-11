# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Proyek ini mengangkat sebuah studi kasus mengenai sebuah institusi di bidang pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Intitut ini bernama Jaya jaya yang telah mencetak banyak lulusan dengan reputasi yang sangat baik. Walaupun berhasil mendapat reputasi yang baik, masih terdapat siswa yang tidak dapat menyelesaikan pendidikannya atau bisa dibilang *Dropout*.
Intitusi ini membutuhkan bantuan untuk mengidentifikasi apa penyebab mahasiswanya hingga harus *dropout*. Dengan ditemukannya penyebab masalah tersebut diharapkan dapat diambil keputusan yang cepat dan tepat untuk mengurangi jumlah mahasiswa yang *dropout*

### Permasalahan Bisnis

Institut Jaya Jaya mengalami masalahbesar karena jumlah mahasiswa yang tidak dapat menyelesaikan studinya lumayan tinggi. Kondisi ini dapat berdampak pada reputasi baik institusi ini.

### Cakupan Proyek

Berikut beberapa cakupan proyek ini:

1. Apa saja faktor yang mempengaruhi tingkat *dropout* pada institus jaya Jaya.

### Persiapan

Sumber data: "[https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv]"

Setup environment:

1. Buat virtual environment
   `python -m venv env`

2. Aktifkan environment
   `env\Scripts\activate`

3. Install semua library dari file `requirement.txt`
   `pip install -r requirements.txt`

4. Jalankan skripnya
   `python <nama file>.py`

## Business Dashboard

![Bayun Kurniawan - Dashboard](https://github.com/user-attachments/assets/33ea3b22-ac09-41f2-a5a2-1f1e9b2a4bb8)
Dashboard tersebut menampilkan beberapa fitur yang ada dalam data tersebut mulai dari jumlah keseluruhan mahasiswa, jumlah pemegang beasiswa, sampai asal mulai mahasiswa tersebut.

## Conclusion

Data pada proyek ini memiliki jumlah 4424 data tanpa ada data yang mmemiliki 'missing value".
Datanya berisi 37 fitur dengan rincian:
- 1 data dengan tipe data objek dengan fitur `Status`
- 36 data lainnya dengan tipe data numerik

Selanjutnya saya membuat grafik untuk melihat jumlah mahasiswa berdasarkan `Status` nya, didpatkan data sebagai berikut:

| Status    | Jumlah | Persentase (%) |
|-----------|--------|----------------|
| Graduate  | 2209   | 49.93%         |
| Dropout   | 1421   | 32.12%         |
| Enrolled  | 794    | 17.95%         |
| **Total** | **4424** | **100.00%**  |

Berdasakan data di atas dapat dilihat, jumlah mahasiswa yang berstatus *dropout* ada 32,12% dengan jumlah 1421 dari jumalh 4424 siswa. 

Selanjutnya saya membuat fitur baru bernama `status_label` yang berasal dari fitur 'Status` dengan mengubah tipenya menjadi numerik. Status `Dropout` saya ubah menjadi angka 0, `Enrolled` saya ubah menjadi angka 1 dan `Graduate` saya ubah menjadi 2. Setelah itu saya tentukan nilai korelasi dari semua fitur yang ada terhadap fitur `status_label` yang baru saya buat. 
Saat dilakukan uji korelasi adidapatkan nilai sebagai berikut

| Fitur                                     | Korelasi  |
|-------------------------------------------|-----------|
| Curricular_units_2nd_sem_approved         | 0.624157  |
| Curricular_units_2nd_sem_grade            | 0.566827  |
| Curricular_units_1st_sem_approved         | 0.529123  |
| Curricular_units_1st_sem_grade            | 0.485207  |
| Tuition_fees_up_to_date                   | 0.409827  |
| Scholarship_holder                        | 0.297595  |
| Curricular_units_2nd_sem_enrolled         | 0.175847  |
| Curricular_units_1st_sem_enrolled         | 0.155974  |
| Admission_grade                           | 0.120889  |
| Displaced                                 | 0.113986  |
| Previous_qualification_grade              | 0.103764  |
| Curricular_units_2nd_sem_evaluations      | 0.092721  |
| Application_order                         | 0.089791  |
| Daytime_evening_attendance                | 0.075107  |
| Curricular_units_2nd_sem_credited         | 0.054004  |
| Curricular_units_1st_sem_credited         | 0.048150  |
| Curricular_units_1st_sem_evaluations      | 0.044362  |
| GDP                                       | 0.044135  |
| Course                                    | 0.034219  |

| Application_mode                          | -0.221747 |
| Gender                                    | -0.229270 |
| Debtor                                    | -0.240999 |
| Age_at_enrollment                         | -0.243438 |

Dikarenakan nilai pada fitur `status_label` maka bisa disimpulkan nilai dengan korelasi positif cenderung berbanding lurus dengan status `Graduate` yang bernilai 2 dan korelasi negatif cenderung berbanding lurus dengan status `Dropout` yang bernilai 0.

Dari nilai korelasi tersebut ada 4 fitur yang paling berpengaruh terhadap status `Dropout` nya mahasiswa mulai dari `Application_mode`, `Gender`, `Debtor` dan juga `Age_at_Enrollment`. 4 fitur ini dapat dipertimbangkan untuk mencegah terjadinya *dropout* dikemudian hari.

### Rekomendasi Action Items
Berdasarkan pada pengerjaan yang sudah saya lakukan, rekomendasi action yang bisa dilakukan oleh Jaya Jaya institut adalah:
1. Membantu pinjaman kepada mahasiswa untuk biaya kuliah atau menambah kuota beasiswa untuk mahasiswa yang membutuhkan
2. Monitoring lebih awal terhadap mahasiswa terutama yang memiliki 4 kriteria di atas 
