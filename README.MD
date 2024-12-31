# Analisis Data Penjualan dan Pembelian Sembako

## Tujuan
Dokumentasi ini menjelaskan langkah-langkah pengerjaan proyek analisis data penjualan dan pembelian sembako, meliputi proses ETL, cara menjawab pertanyaan bisnis, serta alat yang digunakan.

---

## Proses ETL
### 1. **Extract**
- Dataset diunduh dari [Kaggle](https://www.kaggle.com/datasets/bejopamungkas/transaksi-pembelian-penjualan-sembako).
- Dataset berbentuk file CSV dibaca menggunakan Python dengan library **pandas**.
- Pemeriksaan struktur data dilakukan untuk memastikan dataset siap diolah, termasuk mengecek kolom, tipe data, dan kemungkinan data yang hilang.

### 2. **Transform**
- Data dibersihkan dari nilai kosong dan duplikasi menggunakan Python.
- Kolom tanggal diformat menjadi tipe datetime untuk memudahkan analisis waktu.

### 3. **Load**
- Database PostgreSQL disiapkan dengan membuat tabel sesuai struktur dataset.
- Dataset diimpor ke PostgreSQL menggunakan library **SQLAlchemy** untuk koneksi Python ke database.
- Query SQL diuji untuk memastikan data berhasil dimasukkan dengan benar.

---

## Cara Menjawab Pertanyaan Bisnis

1. **Bagaimana tren penjualan di toko, dan apa yang mempengaruhinya?**  
   - Query SQL dibuat untuk menghitung total penjualan bulanan dan kemudian membuat visualisasi pada Looker Studio untuk melihat tren.  
   - Faktor yang memengaruhi tren dievaluasi berdasarkan musim atau waktu tertentu dengan membandingkan bulan.  

2. **Berapa total pendapatan setiap bulan?**  
   - Query SQL menghitung total pendapatan dengan formula `SUM(nominal)` per bulan.  
   - Hasil divisualisasikan menggunakan diagram batang.  

3. **Siapa pembeli dengan pembelian terbanyak?**  
   - Query SQL mengidentifikasi pelanggan dengan nilai pembelian tertinggi menggunakan `GROUP BY` dan `ORDER BY`.  
   - Hasil divisualisasikan dengan grafik batang.  

4. **Pada hari apa dalam seminggu terjadi transaksi terbanyak?**  
   - Tanggal transaksi diubah menjadi nama hari.  
   - Frekuensi transaksi dihitung untuk setiap hari dalam seminggu, dan hasilnya ditampilkan menggunakan bar chart.  

---

## Alat yang Digunakan dan Alasan Pemilihannya

1. **Python**  
   - **Pandas**: Untuk membaca dan membersihkan dataset.  
   - **SQLAlchemy**: Untuk memuat data ke PostgreSQL.  

2. **PostgreSQL**  
   - Dipilih karena mendukung analisis data skala besar dan fleksibel dengan query SQL yang kompleks.  

3. **Looker Studio**  
   - Digunakan untuk membuat dashboard visualisasi interaktif agar memudahkan pengambilan keputusan.  

4. **VS Code**  
   - Untuk pengembangan kode dan manajemen proyek karena mendukung banyak ekstensi yang membantu produktivitas.  

---

## Struktur Direktori

```
data/  
  ├── raw/  
  └── cleaned/  
scripts/  
  ├── data_cleaning.py  
  └── etl_postgres.py  
sql/  
  └── insight_query.sql  
visualization/  
  ├── 1_report.jpg  
  ├── 2_insight_rec.jpg  
docs/  
  └── README.md  
```

---  
Dokumentasi ini diharapkan memudahkan evaluasi proyek serta reproduksi hasil analisis oleh pihak lain.
