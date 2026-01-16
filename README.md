# UAS ROBOTIKA DAN SISTEM OTONOM
## NOMOR 2:
Sebuah robot bergerak dua roda (differential drive robot) telah berhasil menghasilkan lintasan referensi dari Titik Start (S) menuju Titik Goal (G) menggunakan algoritma path planning (misalnya Dijkstra, A*, atau RRT). Lintasan tersebut direpresentasikan sebagai sekumpulan titik (𝑥,𝑦) yang harus diikuti oleh robot. 

Namun, pada tahap pengujian, robot menunjukkan beberapa permasalahan berikut: 
- Robot tidak mampu mengikuti lintasan dengan presisi, terutama pada tikungan tajam,
- Terjadi osilasi arah gerak saat robot mencoba kembali ke lintasan,
- Error lintasan (cross-track error) cukup besar ketika kecepatan robot ditingkatkan. 
 
Untuk mengatasi permasalahan tersebut, tim Anda diminta untuk merancang metode path tracking dan kontroler robot yang mampu membuat robot mengikuti lintasan hasil path planning secara stabil dan akurat. 
 
Pertanyaan: 
Bagaimana Anda merancang sistem path tracking dan kontroler pada robot bergerak dua roda agar robot dapat mengikuti lintasan hasil path planning dengan baik? 
 
Jelaskan secara rinci: 
1. Pemilihan dan prinsip kerja metode path tracking yang digunakan (misalnya Pure Pursuit, Stanley Controller, atau metode lain), termasuk parameter utama yang mempengaruhi performa tracking.
2. Perancangan kontroler robot (misalnya PID atau kontroler sederhana berbasis error sudut dan jarak) untuk menghasilkan perintah kecepatan linear dan sudut (𝑣,𝜔) pada robot differential drive.
3. Hubungan antara model kinematika robot dengan path tracking dan kontroler yang dirancang, serta bagaimana keterbatasan robot (kecepatan maksimum, radius belok minimum) dipertimbangkan.
4. Analisis hasil simulasi, meliputi:
   - perbandingan lintasan referensi dan lintasan aktual robot,
   - nilai error lintasan (cross-track error) terhadap waktu,
   - pengaruh perubahan parameter kontroler terhadap kestabilan dan akurasi tracking. 
 
Hasil dapat disajikan dalam bentuk kode Python dan visualisasi grafik (lintasan referensi vs lintasan robot, serta grafik error).

# DIBUAT OLEH:
## KELOMPOK 1:
- JAROT WIWOHO               (41422110036)
- RAIHAN RAMANDHA SAPUTRA    (41422110039)
