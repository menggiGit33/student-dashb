# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

- Membuat Dashbord yang andal dan mudah dimengerti oleh pihak Admin 
- Membuat Model Machine Learning untuk prediksi data siswa

### Cakupan Proyek

- Proyek ini menggunakan Jupyter Notebook untuk proses pengolahan data 
- Tableau untuk Visualisasi Dashboard
- Streamlit Cloud untuk Deploy Environment Machine Learning

### Persiapan

Sumber data: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

```
   conda create --name dashboard python=3.9
   conda activate main-ds
   pip install -r requirements.txt
```

## Business Dashboard

Dashboard ini menunjang admin untuk memonitor variabel yang sangat memepengaruhi Dropout Rate Siswa. dalam Dashboard ini tersedia jumlah siswa, persentase siswa dropoutserta masih banyak lagi dan juga dalam dashboard ini dilengkapi dengan berbagai macam visualisasi yang mempermudah pihak admin untuk melakukan analisis secara statistikal. (https://public.tableau.com/app/profile/althaf.yudhistira/viz/Book1_17466738700550/Dashboard1?publish=yes)
## Menjalankan Sistem Machine Learning
Untuk Program prediksi status mahasiswa menggunakan algoritma machine learning berupa Random Forest dengan akurasi sebesar 87% sehingga dapat dikatakan cukup andal untuk melakukan proses klasifikasi. klasifikasi dibagi menjadi 2 kelas yaitu kelas dropout dan enrolled. dapat diakses pada link berikut (https://student-dashb-kukbywfasb7ubwv7akjkzq.streamlit.app)
```
   streamlit run app.py
```

## Conclusion

Siswa berhenti sekolah dapat dipengaruhi beberapa faktor seperti : 
1. Nilai semester 2
2. Nilai semester 1
3. Pembayaran UKT
4. Nilai awal masuk kuliah
5. Nilai sebelum masuk kuliah         
6. Cicilan
7. Pekerjaan Ayah
8. Pekerjaan Ibu                   
9. Umur saat masuk kuliah
10. Pemegang beasiswa

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan Kampus guna menyelesaikan permasalahan atau mencapai target mereka.

- untuk menangani variabel yang berhubungan dengan pembayaran UKT, diharapkan kampus dapat memberi keringanan ataupun menggunakan skema lain yang lebih menguntungkan kedua belah pihak.

- untuk variabel yang berkaitan dengan nilai siswa, diharapkan mahasiswa yang memiliki nilai dibawah rata-rata harap diberi perhatian lebih dan kampus harus memberi dukungan entah dalam bentuk bimbingan intensif terkait mata kuliah yang membebani siswa

- memperbanyak beasiswa, menurut data yang tersedia pemegang beasiswa cenderung berkesempatan kecil untuk dropout
