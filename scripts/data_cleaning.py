import pandas as pd

#Membaca data csv
data_pemasukan = pd.read_csv('data/raw/pemasukan barang.csv')
data_penjualan = pd.read_csv('data/raw/penjualan barang.csv')

# Menghapus kolom yang tidak diperlukan
data_pemasukan = data_pemasukan.drop(columns=['Unnamed: 0'])
data_penjualan = data_penjualan.drop(columns=['Unnamed: 0'])

# Membersihkan nilai string
data_pemasukan['nama.barang'] = data_pemasukan['nama.barang'].str.strip()
data_penjualan['nama.barang'] = data_penjualan['nama.barang'].str.strip()
data_penjualan['nama.pembeli'] = data_penjualan['nama.pembeli'].str.strip()

# Mengonversi kolom tanggal ke datetime 
if 'tanggal' in data_pemasukan.columns:
    data_pemasukan['tanggal'] = pd.to_datetime(data_pemasukan['tanggal'], errors='coerce')
if 'tanggal' in data_penjualan.columns:
    data_penjualan['tanggal'] = pd.to_datetime(data_penjualan['tanggal'], errors='coerce')


# Mengonversi kolom numerik ke tipe float
data_pemasukan['kuantum'] = pd.to_numeric(data_pemasukan['kuantum'], errors='coerce')
data_penjualan['kuantum'] = pd.to_numeric(data_penjualan['kuantum'], errors='coerce')
data_penjualan['nominal'] = pd.to_numeric(data_penjualan['nominal'], errors='coerce')

# Menghapus baris dan kolom yang mengandung nilai NaN
data_pemasukan = data_pemasukan.dropna()
data_pemasukan = data_pemasukan.dropna(axis=1)
data_penjualan = data_penjualan.dropna()
data_penjualan = data_penjualan.dropna(axis=1)

# Menghapus data duplikat
data_pemasukan = data_pemasukan.drop_duplicates()
data_penjualan = data_penjualan.drop_duplicates()

# Menyimpan data yang telah dibersihkan
data_pemasukan.to_csv('data/cleaned/pemasukan_cleaned.csv', index=False)
data_penjualan.to_csv('data/cleaned/penjualan_cleaned.csv', index=False)