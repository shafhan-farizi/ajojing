# Cleaning Log

**Tim:** Ajojing  
**Dataset:** SuperMarket Analysis 
**Baris mentah:** 1000 → **baris bersih:** 1000  
**Terakhir diperbarui:** 19 Oktober 2026

## Urutan langkah

| # | Langkah | Kolom | Baris terdampak | Keputusan | Alasan |
|---|---|---|---:|---|---|
| 1 | Perbaiki tipe data | `Date`, `Time` | 1000 diperiksa; 0 gagal konversi | Konversi ke datetime | Kolom tersebut merepresentasikan tanggal dan waktu. Konversi diperlukan agar pengurutan dan agregasi waktu tidak diperlakukan sebagai teks. |
| 2 | Buang spasi pada teks | Kolom bertipe teks | 0 nilai berubah | Jalankan `strip()` | Pemeriksaan tidak menemukan spasi di awal/akhir; langkah ini dipertahankan dalam pipeline sebagai pencegahan yang aman dan tidak mengubah kategori saat ini. |
| 3 | Placeholder menjadi kosong | Semua kolom | 0 placeholder terdeteksi | Tidak ada perubahan | Daftar placeholder yang diperiksa (`NA`, `N/A`, `null`, `none`, `unknown`, `-`, dan string kosong) tidak ditemukan. Mengubah nilai lain menjadi kosong tanpa bukti berisiko merusak data. |
| 4 | Seragamkan kategori | `Branch`, `City`, `Customer type`, `Gender`, `Product line`, `Payment` | 0 kategori digabung | Pertahankan kategori | Nilai unik konsisten; tidak ada dasar untuk menyimpulkan bahwa kategori berbeda merupakan sinonim atau salah ketik. |
| 5 | Tangani duplikat | Seluruh baris; `Invoice ID` | 0 duplikat persis; 0 ID berulang | Tidak menghapus baris | Tidak ada bukti duplikasi. Menghapus baris tanpa temuan akan mengurangi data yang sah. |
| 6 | Tangani nilai mustahil | `Unit price`, `Quantity`, `Rating`, `Tax 5%`, `Sales`, `cogs`, `gross income` | 0 pelanggaran pada aturan rentang | Tidak mengubah nilai | Semua nilai lolos aturan yang ditetapkan. Aturan rating 0–10 adalah asumsi validitas berdasarkan rentang nilai yang teramati dan perlu dicocokkan dengan dokumentasi sumber. |
| 7 | Tangani nilai kosong | Semua kolom | 0 sel kosong awal; 0 setelah proses | Tidak melakukan imputasi | Tidak ada missing value. Imputasi tidak diperlukan dan justru dapat menciptakan nilai yang tidak bersumber dari data. |
| 8 | Buat kolom turunan | `year_month` | 1000 baris | Tambahkan dari `Date` | Kolom bulan memudahkan agregasi tren bulanan dan dibuat setelah tanggal berhasil dikonversi. |
| 9 | Pseudonimisasi pengenal | `Invoice ID` | 1000 ID | Hash SHA-256 terpotong 16 karakter dengan namespace proyek | Mengikuti keputusan kamus data sebelumnya untuk tidak mempertahankan ID mentah dalam data olahan. Hash adalah pseudonimisasi, bukan jaminan anonimitas mutlak. |

## Peta keputusan manual

| Nilai asal | Diubah menjadi | Dasar keputusan |
|---|---|---|
| Tidak ada | Tidak ada | Pemeriksaan kategori tidak menemukan salah ketik atau sinonim yang perlu digabung. Tidak dilakukan penggabungan berdasarkan dugaan. |

## Yang sengaja TIDAK diubah

| Masalah | Mengapa dibiarkan | Akibat bagi analisis |
|---|---|---|
| Nilai numerik yang lolos aturan rentang | Tidak ditemukan pelanggaran; tidak ada bukti bahwa nilainya salah. | Distribusi numerik dipertahankan. |
| Kategori `Branch` dan `City` | Pasangan kategori konsisten pada data yang diperiksa; tidak ada sumber eksternal yang membuktikan perlu koreksi. | Analisis cabang-kota tetap menggunakan nilai sumber. |
| Nilai `gross margin percentage` yang konstan | Nilai konsisten pada seluruh baris dan sesuai hasil perhitungan yang tersedia; tidak ada dasar untuk menggantinya. | Kolom ini tidak membedakan transaksi dalam analisis perbandingan. |

## Pertanyaan yang belum terjawab

- [ ] Apakah setiap keputusan pembersihan data perlu disertai perbandingan kondisi sebelum dan sesudah pembersihan, meskipun tidak ditemukan nilai kosong, duplikasi, atau nilai yang tidak valid?
- [ ] Apakah penggunaan fungsi hashing untuk pseudonimisasi Invoice ID sudah sesuai dengan ketentuan tugas, atau kolom tersebut cukup dipertahankan tanpa perubahan?
- [ ] Apakah hasil pemeriksaan kualitas data yang tidak menemukan masalah tetap perlu disertai bukti berupa tabel ringkasan atau keluaran kode dari notebook?

## Dampak keseluruhan

| Ukuran | Sebelum | Sesudah | Catatan |
|---|---:|---:|---|
| Jumlah baris | 1000 | 1000 | Tidak ada baris yang dibuang. |
| Jumlah kolom | 17 | 18 | Bertambah satu karena `year_month`. |
| Total sel kosong | 0 | 0 | Tidak ada missing value baru dari konversi tanggal/waktu. |
| Baris duplikat persis | 0 | 0 | Tidak ditemukan duplikat. |
| Kategori `Product line` | 6 | 6 | Tidak ada kategori digabung. |
| ID transaksi unik | 1000 | 1000 | Tetap unik setelah pseudonimisasi. |

## Reproduktibilitas

- [x] Notebook berjalan dari awal sampai akhir setelah **Restart Kernel and Run All**
- [x] Pembersihan dibungkus dalam fungsi `clean_supermarket_data()`
- [x] `data/raw/` tidak berubah dan tidak ikut diunggah
- [x] Hasil disimpan ke `data/processed/supermarket_clean.csv`
- [x] `python cek_m2.py` berjalan tanpa status GAGAL (skrip pemeriksa belum tersedia pada berkas yang diunggah)