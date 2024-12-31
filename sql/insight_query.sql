-- Total pendapatan setiap bulan
SELECT 
    DATE_TRUNC('month', tanggal) AS bulan, 
    SUM(nominal) AS total_pendapatan
FROM penjualan
GROUP BY 1
ORDER BY 1;

-- Hari dengan transaksi terbanyak
SELECT 
    TO_CHAR(tanggal, 'Day') AS hari, 
    COUNT(*) AS jumlah_transaksi
FROM penjualan
GROUP BY 1
ORDER BY jumlah_transaksi DESC;

-- Pelanggan dengan pembelian terbanyak
SELECT 
    "nama.pembeli" AS pelanggan, 
    SUM(nominal) AS total_belanja
FROM penjualan
GROUP BY pelanggan
ORDER BY total_belanja DESC
LIMIT 10;

-- Tren penjualan berdasarkan barang
SELECT 
    "nama.barang" AS barang, 
    DATE_TRUNC('month', tanggal) AS bulan, 
    SUM(nominal) AS total_terjual
FROM penjualan
GROUP BY barang, bulan
ORDER BY barang, bulan;

-- Kontribusi Produk terhadap Pendapatan
SELECT 
    "nama.barang" AS barang, 
    SUM(nominal) AS total_pendapatan, 
    (SUM(nominal) * 100.0 / (SELECT SUM(nominal) FROM penjualan)) AS kontribusi_persen
FROM penjualan
GROUP BY barang
ORDER BY total_pendapatan DESC;

-- Pelanggan yang Paling Sering Kembali
SELECT 
    "nama.pembeli" AS pelanggan, 
    COUNT(DISTINCT DATE(tanggal)) AS hari_kunjungan
FROM penjualan
GROUP BY pelanggan
ORDER BY hari_kunjungan DESC
LIMIT 10;

