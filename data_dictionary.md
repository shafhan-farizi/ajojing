# Data Dictionary — SuperMarket Analysis

## 1. Informasi Dataset

| Atribut | Keterangan |
|---|---|
| Nama dataset | SuperMarket Analysis |
| Sumber | Kaggle — [Supermarket Sales](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales) |
| Jumlah baris | 1.000 |
| Jumlah kolom | 17 |
| Periode data | Januari–Maret 2019 (berdasarkan konteks tugas) |
| Format data | CSV |
| Lisensi | Apache 2.0 (sesuai informasi sumber yang dicatat pada tugas) |

Dataset berisi catatan transaksi penjualan supermarket. Kamus data ini disusun berdasarkan struktur kolom, tipe data, dan hasil pemeriksaan awal (`df.info()` dan `df.dtypes`) yang diperoleh saat menjalankan notebook.

## 2. Kamus Data

Keterangan kategori privasi:
- **Pengenal langsung**: kolom yang berfungsi sebagai identitas atau nomor pengenal suatu catatan/transaksi.
- **Quasi-identifier**: informasi yang jika digabungkan dengan atribut lain berpotensi membantu membedakan suatu catatan atau kelompok.
- **Bukan data pribadi**: atribut transaksi atau produk yang tidak secara langsung mengidentifikasi pelanggan dalam dataset ini.

| No. | Nama Kolom | Tipe Data | Deskripsi | Kategori Data Pribadi | Tindakan Penanganan |
|---:|---|---|---|---|---|
| 1 | `Invoice ID` | object | Nomor unik yang digunakan untuk mengidentifikasi transaksi atau faktur penjualan. | Pengenal langsung | Hash |
| 2 | `Branch` | object | Kode cabang supermarket tempat transaksi dilakukan, misalnya A, B, atau C. | Quasi-identifier | Pertahankan |
| 3 | `City` | object | Kota tempat cabang supermarket berada. | Quasi-identifier | Pertahankan |
| 4 | `Customer type` | object | Jenis pelanggan berdasarkan status keanggotaan, seperti Member atau Normal. | Quasi-identifier | Pertahankan |
| 5 | `Gender` | object | Kategori gender pelanggan sebagaimana tercatat pada dataset. | Quasi-identifier | Pertahankan |
| 6 | `Product line` | object | Kategori atau kelompok produk yang dibeli pelanggan. | Bukan data pribadi | Pertahankan |
| 7 | `Unit price` | float64 | Harga satu unit produk. | Bukan data pribadi | Pertahankan |
| 8 | `Quantity` | int64 | Jumlah unit produk yang dibeli dalam satu transaksi. | Bukan data pribadi | Pertahankan |
| 9 | `Tax 5%` | float64 | Nilai pajak sebesar 5% yang tercatat pada transaksi. | Bukan data pribadi | Pertahankan |
| 10 | `Sales` | float64 | Nilai penjualan yang tercatat untuk transaksi. | Bukan data pribadi | Pertahankan |
| 11 | `Date` | object | Tanggal ketika transaksi dilakukan. Pada dataset sumber, kolom ini tersimpan sebagai teks dan dapat dikonversi menjadi tipe tanggal saat analisis. | Quasi-identifier | Pertahankan |
| 12 | `Time` | object | Waktu ketika transaksi dilakukan. Kolom ini tersimpan sebagai teks. | Quasi-identifier | Pertahankan |
| 13 | `Payment` | object | Metode pembayaran yang digunakan pelanggan, misalnya Cash, Credit card, atau Ewallet. | Bukan data pribadi | Pertahankan |
| 14 | `cogs` | float64 | Cost of Goods Sold, yaitu biaya pokok barang yang terjual pada transaksi. | Bukan data pribadi | Pertahankan |
| 15 | `gross margin percentage` | float64 | Persentase margin kotor yang tercatat pada transaksi. | Bukan data pribadi | Pertahankan |
| 16 | `gross income` | float64 | Pendapatan kotor yang diperoleh dari transaksi. | Bukan data pribadi | Pertahankan |
| 17 | `Rating` | float64 | Nilai penilaian atau kepuasan pelanggan terhadap pengalaman berbelanja. | Bukan data pribadi | Pertahankan |

## 3. Ringkasan Pemeriksaan Awal

Berdasarkan hasil pemeriksaan dataset yang dicatat pada notebook:

- Dataset memiliki **1.000 baris** dan **17 kolom**.
- Seluruh kolom memiliki **1.000 nilai terisi**; tidak ditemukan nilai kosong pada pemeriksaan awal.
- Terdapat **9 kolom** bertipe `object`, **7 kolom** bertipe `float64`, dan **1 kolom** bertipe `int64`.
- Kolom `Date` dan `Time` masih terbaca sebagai `object`, sehingga perlu dikonversi jika analisis membutuhkan operasi tanggal atau waktu.
- Tidak ada kolom yang diberi tindakan `hapus` berdasarkan pemetaan penanganan yang digunakan pada tugas.
- Kolom `Invoice ID` diberi tindakan `hash`, sedangkan kolom lainnya dipertahankan.

## 4. Penjelasan Tindakan Penanganan

| Tindakan | Penerapan pada Dataset | Tujuan |
|---|---|---|
| Hash | `Invoice ID` | Menyamarkan nilai pengenal transaksi dengan fungsi SHA-256 dan mengambil 12 karakter awal hasil hash. |
| Pertahankan | Seluruh kolom selain `Invoice ID` | Mempertahankan atribut yang diperlukan untuk analisis sesuai klasifikasi pada tugas. |
| Hapus | Tidak ada | Tidak ada kolom yang ditetapkan untuk dihapus dalam pemetaan saat ini. |

---
Dokumen ini dibuat untuk mendokumentasikan struktur kolom, makna atribut, klasifikasi data pribadi, dan tindakan penanganan pada dataset proyek tim.
