# 🐜 UNIB Navigator (ACO) - Pencarian Rute Terpendek dengan Ant Colony Optimization

Proyek ini adalah aplikasi pemetaan rute terpendek berbasis peta kampus **Universitas Bengkulu (UNIB)** yang menggunakan algoritma **Ant Colony Optimization (ACO)**. Aplikasi ini memungkinkan pengguna untuk mencari rute dari satu lokasi ke lokasi lainnya dalam area kampus UNIB, kemudian menampilkannya secara interaktif di browser dalam bentuk peta.

---

## 📌 Fitur Utama

- 📍 Input nama lokasi asal dan tujuan (contoh: *Rektorat UNIB* ke *Fakultas Teknik*)
- 🐜 Menggunakan ACO untuk pencarian rute alternatif selain Dijkstra
- 📏 Estimasi jarak tempuh & waktu perjalanan untuk:
  - 🚶 Jalan kaki
  - 🏍 Motor
  - 🚗 Mobil
- 🗺 Visualisasi rute interaktif dalam file HTML
- 🧠 Simulasi koloni semut (ACO) yang memperbarui jalur berdasarkan feromon

---

## 🛠 Teknologi yang Digunakan

- **Python 3.x**
- [OSMnx](https://github.com/gboeing/osmnx)
- [NetworkX](https://networkx.org/)
- [Folium](https://python-visualization.github.io/folium/)
- [Geopy](https://geopy.readthedocs.io/)
- Web browser untuk membuka hasil peta

---

## 🚀 Cara Menjalankan

1. **Instal dependensi terlebih dahulu** (jika belum):
```bash
pip install osmnx networkx folium geopy
```

2. **Jalankan program:**
```bash
python unib_pathfinder_aco.py
```

3. **Input nama lokasi asal dan tujuan**, misalnya:
```
Tentukan lokasi awal (contoh: Gedung Rektorat): Rektorat UNIB
Tentukan lokasi tujuan (contoh: Fakultas Teknik): Fakultas Teknik
```

4. **Hasil akan tersimpan sebagai file HTML dan langsung terbuka di browser:**
```
Peta disimpan sebagai 'unib_navigation_aco.html'
contoh map dan estimasi waktu :
```
![Cuplikan layar 2025-04-08 085410](https://github.com/user-attachments/assets/196a1f59-084e-41c0-9688-eb06b018d85f)
![Cuplikan layar 2025-04-08 085815](https://github.com/user-attachments/assets/13bdf621-bfce-43f4-8185-e38c66fd5409)
---

## 💡 Contoh Lokasi yang Bisa Digunakan

Berikut beberapa nama tempat yang bisa dimasukkan sebagai input:

- Rektorat UNIB
- Fakultas Teknik
- Fakultas Pertanian
- Fakultas Ekonomi
- Perpustakaan UNIB
- Masjid Al-Muqaddimah UNIB
- Gerbang UNIB
- Gedung Kuliah Bersama (GKB)
- Asrama Mahasiswa
- dan lain lain yang terlihat di map dan disesuaikan dengan ejaan di map tersebut

> ⚠️ Tips: Tambahkan kata “UNIB” atau “Bengkulu” untuk hasil geocoding yang lebih akurat.

---

## 📷 Tampilan Output

- File HTML: `unib_navigation_aco.html`
- Elemen visual:
  - Jalur terpendek berwarna biru
  - Marker titik asal (hijau) & tujuan (merah)
  - Panel info di kiri bawah:
    - Nama lokasi
    - Jarak (meter)
    - Estimasi waktu untuk 3 moda transportasi
    - Waktu eksekusi (di terminal)

---

## 🧠 Tentang Algoritma ACO

ACO (Ant Colony Optimization) adalah algoritma inspirasi dari perilaku semut dalam menemukan rute terpendek ke sumber makanan. Semut-semut virtual akan menjelajahi graf jalan kampus, meninggalkan feromon pada jalur yang lebih baik, hingga akhirnya menemukan rute terbaik.

---

## ⏱ Estimasi Kecepatan Transportasi

| Moda Transportasi | Kecepatan Rata-rata | Simbol |
|-------------------|---------------------|--------|
| Jalan Kaki        | 1.4 m/s (~5 km/jam) | 🚶     |
| Motor             | 8.33 m/s (~30 km/jam) | 🏍    |
| Mobil             | 11.11 m/s (~40 km/jam) | 🚗    |

---

## 📌 Catatan

- Pastikan koneksi internet aktif saat pertama kali menjalankan (untuk ambil data OSM).
- Area graf dibatasi hanya untuk Universitas Bengkulu.
- ACO bersifat heuristik, jadi hasil bisa berbeda tiap eksekusi (tergantung random semut).

---

## 🤝 Kontribusi

Jika ingin menambahkan fitur baru seperti:
- Drag marker langsung di peta
- Visualisasi langkah semut (ACO)

Silakan fork dan pull request!

---

## 🧭 Selamat menjelajah UNIB secara digital! 🌐
