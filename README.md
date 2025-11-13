
# 🛒 Aplikasi Kasir dan Inventaris Sederhana

**Proyek Latihan Python Tingkat Dasar: Fungsi**

Aplikasi konsol sederhana ini dikembangkan sebagai latihan untuk memperkuat pemahaman tentang fungsi Python (`def`), parameter, nilai kembali (`return`), dan *default arguments* dalam skenario kasus nyata (Sistem Kasir).

## 🚀 Fitur Utama

Proyek ini menyediakan empat fungsi inti untuk mengelola transaksi:

1.  **`cek_ketersediaan()`:** Memastikan stok barang cukup sebelum transaksi.
2.  **`hitung_biaya_item()`:** Menghitung total harga sebelum diskon.
3.  **`terapkan_diskon()`:** Menerapkan diskon, dengan diskon standar 5% (*menggunakan *default argument**\*).
4.  **`proses_pembelian()`:** Menggabungkan ketiga fungsi di atas dan memperbarui stok inventaris.

## 🛠️ Persyaratan

  * Python 3.x

## 📁 Struktur Data

Inventaris toko disimpan dalam struktur data **Dictionary** (Kamus) Python.

```python
inventaris_toko = {
    "Nama_Barang": {
        "stok": 15,        # Jumlah unit yang tersedia (Integer)
        "harga": 8500000.0 # Harga per unit (Float)
    }
    # ... item lainnya
}
```

## 💻 Cara Menjalankan

1.  Pastikan Anda memiliki Python terinstal.

2.  Salin semua kode fungsi dan skenario pengujian ke dalam satu *file* Python (misalnya, `kasir.py`).

3.  Jalankan *file* dari terminal Anda:

    ```bash
    python kasir.py
    ```

## 💡 Contoh Skenario Pengujian

Kode yang Anda buat akan diuji dengan skenario berikut:

### 1\. Transaksi

  * **Pembelian 1:** 2 unit "Keyboard Mekanik"
  * **Pembelian 2:** 10 unit "Mouse Wireless"

### 2\. Hasil (Output Diharapkan)

Setelah kedua transaksi, Anda akan melihat total harga akhir untuk setiap pembelian dan stok inventaris yang telah diperbarui.

```
Total harga akhir setelah diskon: [Hasil Perhitungan]
Stok [Nama Barang] sisa: [Sisa Stok]
```

## 📝 Catatan Pengembang

Tujuan utama dari latihan ini adalah untuk memahami konsep **Single Responsibility Principle** dalam fungsi: setiap fungsi melakukan satu hal, dan fungsi utama (`proses_pembelian`) mengorkestrasi fungsi-fungsi kecil tersebut. Ini adalah kunci untuk kode yang bersih dan mudah diuji