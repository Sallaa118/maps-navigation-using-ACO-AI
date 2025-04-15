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
## 📷 Analisis Program dari Output

- Melakukan 10 kali percobaan berhasil dari dekanat teknik ke 10 lokasi berbeda
![Cuplikan layar 2025-04-15 000335](https://github.com/user-attachments/assets/7704ae91-f6e2-4f76-a202-c5ae438a1c95)
![Cuplikan layar 2025-04-15 000255](https://github.com/user-attachments/assets/0241aefd-9110-4162-93e9-9833c2d1782e)
![Cuplikan layar 2025-04-15 000138](https://github.com/user-attachments/assets/d245bab0-68c1-4652-96f4-f3d987cc9a8b)
![Cuplikan layar 2025-04-15 000042](https://github.com/user-attachments/assets/e726f130-fd63-4f8f-887b-3ee42ae52837)
![Cuplikan layar 2025-04-14 235950](https://github.com/user-attachments/assets/7cad9475-47ce-4d64-8aaa-028f42e3d2f6)
![Cuplikan layar 2025-04-15 001846](https://github.com/user-attachments/assets/144aa892-94e8-480e-97d7-5e16a8bc9240)
![Cuplikan layar 2025-04-15 001805](https://github.com/user-attachments/assets/88bcb97c-92ab-4cce-a41b-fba44ad2eabb)
![Cuplikan layar 2025-04-15 001356](https://github.com/user-attachments/assets/1846f9e8-8259-48e1-90d7-e5876a8a05df)
![Cuplikan layar 2025-04-15 000717](https://github.com/user-attachments/assets/5fee661c-4b58-492c-b77d-5c8ac8b45ce5)
![Cuplikan layar 2025-04-15 000534](https://github.com/user-attachments/assets/fc9090a6-c347-4396-838c-af11d3c5df15)

Dari 10 lokasi yang dituju dan ditampilkan di atas, merupakan hasil dari rute yang berhasil ditemukan
Namun ada beberapa rute yang tidak bisa/ belum bisa diakses dari lokasi awal yaitu dekanat teknik ke lokasi tujuan, yaitu sekitaran unib depan

- Melakukan 10 kali percobaan berhasil dari dekanat teknik ke laboratorium tanah untuk melihat perbedaan jalur yang dihasilkan
![Cuplikan layar 2025-04-15 001846](https://github.com/user-attachments/assets/a258ba45-9828-45d4-82e1-704bca68533f)
![Cuplikan layar 2025-04-15 001916](https://github.com/user-attachments/assets/468f35c8-2398-427b-b294-548d6c07f1bb)
![Cuplikan layar 2025-04-15 001955](https://github.com/user-attachments/assets/5e74441d-6d5f-4a8f-b074-167f96852c3e)
![Cuplikan layar 2025-04-15 002114](https://github.com/user-attachments/assets/ff91e0b8-76c6-413e-bc21-d3c2e7eb5f15)
![Cuplikan layar 2025-04-15 002144](https://github.com/user-attachments/assets/0b7ddc0b-4aaa-44e2-b6d5-97ef2be40547)
![Cuplikan layar 2025-04-15 002221](https://github.com/user-attachments/assets/bce57fa2-4002-409a-8d85-3e29e1de179c)
![Cuplikan layar 2025-04-15 002243](https://github.com/user-attachments/assets/ce0927ae-73d1-436d-9fd8-63a443863b09)
![Cuplikan layar 2025-04-15 002331](https://github.com/user-attachments/assets/b805a398-d150-4206-ad13-a25e2effd6c8)
![Cuplikan layar 2025-04-15 002458](https://github.com/user-attachments/assets/72d559f0-a94d-4f4a-95f8-3ae4426eda36)
![Cuplikan layar 2025-04-15 002621](https://github.com/user-attachments/assets/9732cd5b-86bf-4385-8f9a-56ddf5a61e4d)

Dari 10 kali percobaan berhasil tersebut, terdapat 9 kali percobaan yang gagal menemukan rute sehingga total percobaan yaitu 19 kali percobaan
Kemudian terlihat dari gambar bahwa setiap percobaan menghasilkan rute yang berbeda beda sehingga menampilkan jalur yang berbeda dan menjadi shortest path yang lebih baik

- Analisis lain
  - Terdapat empat kasus yang kami temukan jika lokasi awal dan tujuan sudah ditemukan:
    - rute ditemukan, yaitu map akan langsung ditampilkan dan shortest path ditemukan oleh ant colony
    - rute tidak ditemukan, yaitu ant colony tidak menemukan rute dari lokasi awal ke lokasi tujuan
    - rute di percobaan sebelumnya ditemukan namun di percobaan selanjutnya tidak ditemukan
    - rute di percobaan sebelumnya tidak ditemukan namun di percobaan selanjutnya ditemukan
  - Estimasi waktu yang dibutuhkan program untuk dijalankan dari awal memuat peta hingga menampilkan peta
    - rata rata yang dibutuhkan untuk menjalankan program yaitu sekitar 12 detik
    - penginputan lokasi dari user juga berkontribusi dalam estimasi waktu dijalankannya program

---
## 🧠 Tentang Algoritma ACO

ACO (Ant Colony Optimization) adalah algoritma inspirasi dari perilaku semut dalam menemukan rute terpendek ke sumber makanan. Semut-semut virtual akan menjelajahi graf jalan kampus, meninggalkan feromon pada jalur yang lebih baik, hingga akhirnya menemukan rute terbaik.
Tiap percobaan yang sama akan menghasilkan jalur yang berbeda beda karena feromon yang dihasilkan semut akan selalu diperbarui, sehingga semakin banyak percobaan yang dilakukan maka akan semakin baik shortest path yang ditemukan.

### Kekurangan dari program yang dibuat
- untuk output yang dihasilkan masih belum bisa diterapkan constraint seperti
  - perbedaan 2 jalur atau 1 jalur yang ada di dunia nyata
  - jika ada typo dalam penginputan lokasi maka program tidak bisa menemukan lokasi
- masih ada lokasi yang tidak bisa dicari rute ataupun lokasinya
- titik yang dihasilkan oleh output tidak selalu tepat pada gedung/node nya
- perlu dilakukan percobaan berkali kali agar semut dapat menemukan rute ataupun shortest path yang sesuai dengan jalur
- tipe jalur yang diambil dari OSM yaitu untuk pejalan kaki sehingga belum bisa menampilkan jalur dengan mode transportasi lainnya
  

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
