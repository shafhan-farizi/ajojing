# Kelompok Ajojing

Repositori ini merupakan bagian dari pengerjaan tugas mata kuliah **Exploratory Data Analysis (EDA)**. Proyek ini berfokus pada eksplorasi, pemeriksaan kualitas, pembersihan, dan analisis dataset penjualan supermarket menggunakan Python.

## 1. Anggota Tim

1. **Shafhan Farizi** (0110223019)
2. **Abdul Aziz Alfarizi** (0110225057)
3. **Ziqri Akbar Ashari** (0110225120)
4. **Muhammad Rijal Jiddan** (0110221246)

## 2. Tujuan Proyek

Proyek ini bertujuan untuk melakukan eksplorasi dan analisis terhadap data transaksi penjualan supermarket. Proses pengerjaan meliputi pemeriksaan kualitas data, identifikasi nilai kosong dan data yang tidak konsisten, pembersihan data, analisis statistik deskriptif, serta eksplorasi hubungan antarvariabel.

Selain itu, proyek ini menerapkan prinsip pengelolaan data yang bertanggung jawab melalui dokumentasi kamus data, identifikasi atribut yang berpotensi mengandung informasi pribadi, serta penerapan teknik penyamaran pada kolom tertentu.

Hasil analisis diharapkan dapat memberikan gambaran mengenai pola transaksi, karakteristik pelanggan, kategori produk, dan pendapatan penjualan.

## 3. Pertanyaan Analisis

### Pertanyaan Payung

Bagaimana pola penjualan dan sebaran pendapatan pada dataset Supermarket Sales selama periode Januari–Maret 2019?

### Pertanyaan Turunan

1. Kategori produk (*Product Line*) apa yang menghasilkan total pendapatan kotor (*Gross Income*) terbesar di Cabang A selama kuartal pertama tahun 2019?

   **Kolom:** `Product line`, `gross income`, `Branch`, `Date`.

2. Bagaimana perbandingan total volume penjualan barang (*Quantity*) berdasarkan tipe pelanggan (*Customer Type*) dan gender?

   **Kolom:** `Quantity`, `Customer type`, `Gender`.

3. Bagaimana tren total penjualan (*Sales*) harian di Cabang A sepanjang periode Januari–Maret 2019?

   **Kolom:** `Date`, `Sales`, `Branch`.

4. Metode pembayaran (*Payment*) apa yang paling sering digunakan pelanggan untuk melakukan transaksi?

   **Kolom:** `Payment`.

## 4. Sumber dan Provenans Data

Dataset yang digunakan dalam proyek ini merupakan data sekunder yang diperoleh dari platform Kaggle.

| Informasi | Keterangan |
|---|---|
| Nama dataset | Supermarket Sales |
| Sumber | Kaggle |
| Kontributor | Fares Ashraf |
| Tautan dataset | https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales |
| Tanggal pengambilan | Kamis, 1 Oktober 2026 |
| Lisensi | Apache 2.0 (sesuai pencatatan sumber pada pengerjaan tugas) |
| Format data | CSV |
| Jumlah data | 1.000 baris dan 17 kolom |

**Kalimat sitasi untuk laporan:**

Data sekunder mengenai transaksi penjualan ritel yang dianalisis dalam laporan ini bersumber dari dataset publik 'Supermarket Sales' yang diunggah oleh kontributor Fares Ashraf di platform Kaggle dan didistribusikan di bawah lisensi Apache 2.0.

## 5. Struktur Direktori Proyek

Berikut merupakan struktur direktori repositori Kelompok Ajojing:

```text
ajojing/
│
├── README.md
├── requirements.txt
├── data_dictionary.md
├── AI_usage_log.md
│
├── data/
│   ├── raw/
│   │   └── SuperMarket Analysis.csv
│   │
│   └── processed/
│       └── SuperMarket Analysis_cleaned.csv
│
├── notebooks/
│   ├── 01_quality.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_univariate.ipynb
│   ├── 04_multivariate.ipynb
│   └── 05_advanced.ipynb
│
├── knime/
│   └── workflow.knwf
│
└── reports/
    └── figures/
```

### Keterangan Direktori dan File

| File/Folder | Fungsi |
|---|---|
| `README.md` | Dokumentasi utama proyek. |
| `requirements.txt` | Daftar pustaka Python yang diperlukan. |
| `data_dictionary.md` | Kamus data yang menjelaskan atribut, tipe data, kategori data pribadi, dan tindakan penanganan. |
| `AI_usage_log.md` | Catatan penggunaan AI generatif selama pengerjaan proyek. |
| `data/raw/` | Menyimpan dataset asli yang tidak boleh diubah. |
| `data/processed/` | Menyimpan dataset yang telah melalui proses pembersihan dan penanganan data. |
| `notebooks/` | Menyimpan notebook untuk setiap tahapan analisis. |
| `knime/` | Menyimpan workflow analisis menggunakan KNIME. |
| `reports/figures/` | Menyimpan grafik dan visualisasi yang digunakan dalam laporan. |

## 6. Cara Menjalankan Proyek (Setup Lokal)

Ikuti langkah-langkah berikut untuk menjalankan notebook analisis di komputer lokal menggunakan Python dan VS Code.

### 6.1. Kloning Repositori

Buka terminal dan jalankan perintah berikut:

```bash
git clone https://github.com/shafhan-farizi/ajojing.git
cd ajojing
```

### 6.2. Instalasi Pustaka

Pastikan Python sudah terinstal. Selanjutnya, instal seluruh pustaka yang diperlukan melalui `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 6.3. Menyiapkan Dataset

Pastikan dataset tersedia di direktori `data/raw/` dengan nama file:

```text
SuperMarket Analysis.csv
```

Dataset asli harus dipertahankan dan tidak boleh dimodifikasi secara langsung. Seluruh proses pembersihan dilakukan terhadap salinan data dan hasilnya disimpan di direktori `data/processed/`.

### 6.4. Menjalankan Notebook

1. Buka folder repositori `ajojing` menggunakan VS Code.
2. Masuk ke direktori `notebooks/`.
3. Buka notebook `.ipynb` yang ingin dijalankan.
4. Pilih kernel Python yang sesuai.
5. Jalankan setiap sel kode secara berurutan atau gunakan fitur **Run All**.

Notebook dikerjakan secara bertahap sesuai urutan analisis, mulai dari pemeriksaan kualitas data hingga analisis lanjutan.

## 7. Pembagian Peran dan Tanggung Jawab Tim

Pembagian tugas dilakukan berdasarkan tahapan pengerjaan proyek Exploratory Data Analysis. Setiap anggota memiliki tanggung jawab masing-masing dan tetap berkoordinasi untuk memastikan seluruh proses analisis berjalan sesuai tujuan.

| Anggota | Peran | Tanggung Jawab |
|---|---|---|
| **Shafhan Farizi** | Koordinator / Ketua Tim | Mengkoordinasikan pengerjaan proyek, menentukan arah analisis, merumuskan pertanyaan analisis, mengawasi integrasi hasil pekerjaan, serta melakukan pemeriksaan akhir terhadap dokumentasi dan hasil proyek. |
| **Abdul Aziz Alfarizi** | Data Quality & Cleaning | Bertanggung jawab terhadap pemeriksaan kualitas dataset, identifikasi nilai kosong, duplikasi, inkonsistensi data, serta proses pembersihan dan validasi dataset. |
| **Ziqri Akbar Ashari** | Data Analysis & Visualization | Bertanggung jawab terhadap analisis statistik deskriptif, analisis univariat dan multivariat, eksplorasi hubungan antarvariabel, serta pembuatan visualisasi data. |
| **Muhammad Rijal Jiddan** | Data Privacy & Advanced Analysis | Bertanggung jawab terhadap penyusunan kamus data, identifikasi atribut yang berpotensi mengandung data pribadi, penerapan penanganan data, serta eksplorasi analisis lanjutan menggunakan Python dan KNIME. |

### Koordinasi Tim

Seluruh anggota bertanggung jawab untuk berkoordinasi, melakukan evaluasi terhadap hasil pekerjaan, dan membantu penyelesaian proyek sesuai kebutuhan. Koordinator bertugas memastikan setiap tahapan pengerjaan terintegrasi dengan baik sehingga menghasilkan dokumentasi dan analisis yang konsisten.

## 8. Dokumentasi dan Penggunaan AI

Dalam proses pengerjaan proyek, AI generatif digunakan sebagai alat bantu untuk memahami instruksi, mempelajari konsep analisis data, membantu penyusunan dan pemeriksaan kode Python, serta mendukung penyusunan dokumentasi.

Penggunaan AI dicatat secara transparan dalam file `AI_usage_log.md`. Hasil yang diberikan AI tetap perlu ditinjau dan disesuaikan dengan kebutuhan serta hasil aktual pengerjaan proyek.

Dokumentasi struktur atribut dan penanganan data dapat dilihat pada `data_dictionary.md`.

---

**Kelompok Ajojing**

Mata Kuliah: Exploratory Data Analysis