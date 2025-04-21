# 🐜 UNIB Navigator (ACO) - Pencarian Rute Terpendek dengan Ant Colony Optimization

Proyek ini adalah aplikasi pemetaan rute terpendek berbasis peta kampus **Universitas Bengkulu (UNIB)** yang menggunakan algoritma **Ant Colony Optimization (ACO)**. Aplikasi ini memungkinkan pengguna untuk mencari rute dari satu lokasi ke lokasi lainnya dalam area kampus UNIB, kemudian menampilkannya secara interaktif di browser dalam bentuk peta.

---

## 📌 Fitur Utama

- 📍 Input nama lokasi asal dan tujuan (contoh: *Rektorat UNIB* ke *Fakultas Teknik*)
- 🐜 Menggunakan ACO untuk pencarian rute alternatif
- 📏 Estimasi jarak tempuh & waktu perjalanan untuk:
  - 🚶 Jalan kaki
  - 🏍 Motor
  - 🚗 Mobil
- 📏 Akses Gerbang UNIB
- 🗺 Visualisasi rute interaktif dalam file HTML
- 🧠 Simulasi koloni semut (ACO) yang memperbarui jalur berdasarkan feromon

---

## 🛠 Teknologi yang Digunakan

- **Python 3.x**
- [OSMnx](https://github.com/gboeing/osmnx)
- [Folium](https://python-visualization.github.io/folium/)
- [Geopy](https://geopy.readthedocs.io/)
- Web browser untuk membuka hasil peta

---

## 🚀 Cara Menjalankan

1. **Instal dependensi terlebih dahulu** (jika belum):
```bash
pip install osmnx folium geopy
```

2. **Jalankan program:**
```bash
python aco_algorithm.py
```

3. **Input nama lokasi asal dan tujuan**, misalnya:
```
Tentukan lokasi awal (contoh: Gedung Rektorat): Rektorat
Tentukan lokasi tujuan (contoh: Fakultas Teknik): Dekanat Teknik
```

4. **Hasil akan tersimpan sebagai file HTML dan langsung terbuka di browser:**
```
Peta disimpan sebagai 'unib_navigation_aco.html'
contoh map dan estimasi waktu :
```
### 🗺️ Contoh Visualisasi Rute

<table style="width:100%; border-collapse: collapse; margin: 20px 0;">
  <!-- Baris Pertama -->
  <tr>
    <td style="padding: 10px; text-align: center; vertical-align: top;">
      <img src="https://github.com/user-attachments/assets/196a1f59-084e-41c0-9688-eb06b018d85f" 
           alt="Visualisasi Rute 1" 
           style="width: 90%; max-width: 400px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
      <p style="margin-top: 8px; font-size: 0.9em; color: #555; font-weight: 500;">Tampilan Peta Navigasi</p>
    </td>
  </tr>
  
  <!-- Baris Kedua -->
  <tr>
    <td style="padding: 10px; text-align: center; vertical-align: top;">
      <img src="https://github.com/user-attachments/assets/13bdf621-bfce-43f4-8185-e38c66fd5409" 
           alt="Visualisasi Rute 2" 
           style="width: 90%; max-width: 400px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
      <p style="margin-top: 8px; font-size: 0.9em; color: #555; font-weight: 500;">Detail Estimasi Waktu</p>
    </td>
  </tr>
</table>

---

## 📍 Daftar Lokasi yang Dapat Diakses

Berikut adalah daftar lokasi di Universitas Bengkulu yang dapat digunakan sebagai titik awal/tujuan:

<table style="width:100%; border-collapse: collapse;">
  <tr>
    <th style="width:25%; padding: 8px; text-align: left; border-bottom: 1px solid #ddd; background-color: #f2f2f2;">Nama Lokasi</th>
    <th style="width:25%; padding: 8px; text-align: left; border-bottom: 1px solid #ddd; background-color: #f2f2f2;">Nama Lokasi</th>
    <th style="width:25%; padding: 8px; text-align: left; border-bottom: 1px solid #ddd; background-color: #f2f2f2;">Nama Lokasi</th>
    <th style="width:25%; padding: 8px; text-align: left; border-bottom: 1px solid #ddd; background-color: #f2f2f2;">Nama Lokasi</th>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung Rektorat</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Masjid Baitul Hikmah</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Perpustakaan</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Masuk Kanan UNIB Belakang</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Masuk Kiri UNIB Belakang</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Masuk UNIB Depan</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GB 1</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GB 2</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GB 3 & 4</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GB 5</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">LPTIK</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GSG</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat Teknik</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lab Teknik</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lab Terpadu Teknik</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Stadion UNIB</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung FKIP</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Fakultas Kedokteran</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Sekretariat UKM</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat FMIPA</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Sekretariat BEM FMIPA</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung Fisika</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Ruang Baca Pertanian</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lab Agronomi</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">GLT</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Masjid Darul Ulum</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lab Ilmu Tanah</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat Pertanian</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat Hukum</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lab Hukum</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat FEB</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Magister Ilmu Ekonomi</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Jurusan Ekonomi Pembangunan</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">UPT BING</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung J</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung K</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gedung C</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Danau UNIB</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Mushola Shelter</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat FISIP</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Dekanat FKIP</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Keluar UNIB Depan</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Keluar UNIB Belakang</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Asrama PGSD</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">S2 Matematika</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Klinik Pratama UNIB</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Sekretariat Teknik</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Gerbang Utama Rektorat</td>
  </tr>
  <tr>
    <td style="padding: 8px; border-bottom: 1px solid #eee;">Lapangan Olahraga UNIB</td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;"></td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;"></td>
    <td style="padding: 8px; border-bottom: 1px solid #eee;"></td>
  </tr>
</table>

<small>💡 Gunakan nama lokasi persis seperti tertulis untuk hasil terbaik </small>

---

## 📷 Tampilan Output

- File HTML: `unib_navigation_aco.html`
- Elemen visual:
  - Jalur terpendek berwarna biru
  - Marker titik asal (hijau) & tujuan (merah)
  - Panel info di kiri bawah:
    - Nama lokasi
    - Jarak (meter)
    - Jarak antara node sebenarnya dengan node terdekat yang diambil dari OSM
    - Estimasi waktu untuk 3 moda transportasi
    - Waktu eksekusi (di terminal)
  - Panel  info di kanan atas:
    - informasi akses semua gerbang yang ada di UNIB
      
---

## 📷 Analisis Program dari Output (Sebelum Update)

- Melakukan 10 kali percobaan berhasil dari dekanat teknik ke 10 lokasi berbeda
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin: 20px 0;">
  <img src="https://github.com/user-attachments/assets/7704ae91-f6e2-4f76-a202-c5ae438a1c95" alt="Rute 1" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/0241aefd-9110-4162-93e9-9833c2d1782e" alt="Rute 2" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/d245bab0-68c1-4652-96f4-f3d987cc9a8b" alt="Rute 3" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/e726f130-fd63-4f8f-887b-3ee42ae52837" alt="Rute 4" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/7cad9475-47ce-4d64-8aaa-028f42e3d2f6" alt="Rute 5" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/144aa892-94e8-480e-97d7-5e16a8bc9240" alt="Rute 6" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/88bcb97c-92ab-4cce-a41b-fba44ad2eabb" alt="Rute 7" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/1846f9e8-8259-48e1-90d7-e5876a8a05df" alt="Rute 8" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/5fee661c-4b58-492c-b77d-5c8ac8b45ce5" alt="Rute 9" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
  <img src="https://github.com/user-attachments/assets/fc9090a6-c347-4396-838c-af11d3c5df15" alt="Rute 10" style="width: 180px; height: auto; border: 1px solid #eee; border-radius: 5px;">
</div>

Dari 10 lokasi yang dituju dan ditampilkan di atas, merupakan hasil dari rute yang berhasil ditemukan
Namun ada beberapa rute yang tidak bisa/ belum bisa diakses dari lokasi awal yaitu dekanat teknik ke lokasi tujuan, yaitu sekitaran unib depan

- Melakukan 10 kali percobaan berhasil dari dekanat teknik ke laboratorium tanah untuk melihat perbedaan jalur yang dihasilkan
<div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center;">
  <img src="https://github.com/user-attachments/assets/a258ba45-9828-45d4-82e1-704bca68533f" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/468f35c8-2398-427b-b294-548d6c07f1bb" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/5e74441d-6d5f-4a8f-b074-167f96852c3e" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/ff91e0b8-76c6-413e-bc21-d3c2e7eb5f15" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/0b7ddc0b-4aaa-44e2-b6d5-97ef2be40547" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/bce57fa2-4002-409a-8d85-3e29e1de179c" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/ce0927ae-73d1-436d-9fd8-63a443863b09" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/b805a398-d150-4206-ad13-a25e2effd6c8" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/72d559f0-a94d-4f4a-95f8-3ae4426eda36" width="180" style="border: 1px solid #ddd;">
  <img src="https://github.com/user-attachments/assets/9732cd5b-86bf-4385-8f9a-56ddf5a61e4d" width="180" style="border: 1px solid #ddd;">
</div>
Dari 10 kali percobaan berhasil tersebut, terdapat 9 kali percobaan yang gagal menemukan rute sehingga total percobaan yaitu 19 kali percobaan
Kemudian terlihat dari gambar bahwa setiap percobaan menghasilkan rute yang berbeda beda sehingga menampilkan jalur yang berbeda dan menjadi shortest path yang lebih baik

- Analisis lain
  - Terdapat empat kasus yang kami temukan jika lokasi awal dan tujuan sudah ditemukan:
    - rute ditemukan, yaitu map akan langsung ditampilkan dan shortest path ditemukan oleh ant colony
    - rute tidak ditemukan, yaitu ant colony tidak menemukan rute dari lokasi awal ke lokasi tujuan
    - rute di percobaan sebelumnya ditemukan namun di percobaan selanjutnya tidak ditemukan
    - rute di percobaan sebelumnya tidak ditemukan namun di percobaan selanjutnya ditemukan
  - Estimasi waktu yang dibutuhkan program untuk dijalankan dari awal memuat peta hingga menampilkan peta
    - rata rata yang dibutuhkan untuk menjalankan program yaitu sekitar 8 detik
    - penginputan lokasi dari user juga berkontribusi dalam estimasi waktu dijalankannya program

---

## 📷 Analisis Program dari Output (Setelah Update)

Setelah melakukan banyak sekali percobaan dari yang error hingga berhasil, maka dapat kami simpulkan bahwa program shortest path menggunakan algoritma ACO ini sudah berjalan dengan performa yang lebih baik. Terlihat dengan ketika memasukkan inputan yang sama, maka output rute yang dihasilkan sudah tidak berbeda beda, hal ini dikarenakan ACO sudah menemukan path yang paling optimal. Berikut rute yang dihasilkan dari dekanat teknik ke laboratorium ilmu tanah

### 📊 Perbandingan Hasil Rute

<table style="width:100%; border-collapse: collapse; margin: 20px 0;">
  <tr>
    <!-- Kolom Pertama -->
    <td style="width:50%; padding: 10px; text-align: center; vertical-align: top;">
      <img src="https://github.com/user-attachments/assets/c327c333-4b29-4a0d-be5d-c378c7db1445" 
           alt="Visualisasi Rute 20 April" 
           style="width: 90%; max-width: 350px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
      <p style="margin-top: 8px; font-size: 0.9em; color: #555; font-weight: 500;">20 April 2025</p>
    </td>
    <!-- Kolom Kedua -->
    <td style="width:50%; padding: 10px; text-align: center; vertical-align: top;">
      <img src="https://github.com/user-attachments/assets/5993dc1b-1a5c-4a0c-9692-da32077d0e7d" 
           alt="Visualisasi Rute 22 April" 
           style="width: 90%; max-width: 350px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
      <p style="margin-top: 8px; font-size: 0.9em; color: #555; font-weight: 500;">22 April 2025</p>
    </td>
  </tr>
</table>

### Kode yang Diperbarui
Jika dilihat dari output terbaru yang dihasilkan akan terlihat bahwa ada penambahan program akses 6 gerbang yang ada di UNIB, dan sudah disesuaikan dengan aturan yang berlaku di UNIB yaitu akses gerbang dari Senin - Jumat jam 07.00 - 18.00, dan selain dari itu. Adapun untuk performa ACO sendiri, kami tidak terlalu mengupdate ants dan iteration pada kode, hanya saja kami telah melakukan lebih kurang 100 kali percobaan dan hal itulah yang membuat performa ACO atau program AI ini dapat belajar dan berkembang menjadi lebih baik.

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

### Solusi yang telah diterapkan
- telah dimasukkan program akses gerbang untuk alternatif lain dalam menerapkan constraint aturan UNIB di dunia nyata
- menggunakan database lokal untuk menentukan node agar tepat pada gedung
- ACO telah dioptimalkan dengan dilakukannya percobaan berkali-kali

### Solusi yang diperlukan
- diperlukan pengembangan program lebih lanjut agar dapat mengatur constraint seperti perbedaan 2 jalur dan 1 jalur seperti di dunia nyata
- diperlukan juga pengembangan program untuk dapat mendeteksi typo pada inputan user

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
