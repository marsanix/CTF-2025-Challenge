# MyKisahCrypto — Write-up

## Deskripsi Tantangan
**Soal:**
"Sebuah file terkompresi jatuh dari isekai. Kerahkan seluruh kemampuan kriptografi-mu untuk menemukan flag-nya!"

**Hint:**
Algoritma yang digunakan diantaranya: SHA, AES, Base64, HEX, dan Caesar Cipher.

**File:**
- `MyKisahCrypto.zip`: File arsip utama yang berisi banyak file lain.

## Analisis
Tantangan ini termasuk kategori **Forensics** dan **Mixed Cryptography**. Kita diberikan sebuah file ZIP yang kemungkinan berisi banyak file lain (nested zip atau kumpulan file) yang menyembunyikan flag.

Mengingat banyaknya kemungkinan tempat persembunyian (ZIP comment, metadata gambar, steganografi LSB, data appended), penyelesaian manual akan sangat memakan waktu.

## Strategi Penyelesaian (Thinking Process)
1.  **Eksplorasi:** Ekstrak `MyKisahCrypto.zip`. Terlihat banyak file dengan nama acak atau struktur folder yang dalam.
2.  **Identifikasi Pola:**
    -   Cek komentar ZIP.
    -   Cek file gambar (PNG) untuk steganografi (LSB, chunk text, data setelah IEND).
    -   Cek file teks untuk string terenkripsi (Base64, Hex).
3.  **Otomatisasi:** Karena kompleksitasnya, kita perlu membuat script "Solver" yang dapat memindai semua file dan mencoba berbagai metode dekoding secara otomatis.

## Tools
-   **Python 3**: Bahasa utama untuk scripting.
-   **Library**: `struct`, `zlib`, `base64`, `binascii`, `re`.

## Langkah Penyelesaian
Kami menggunakan script `doit.py` yang melakukan hal berikut:

1.  **Scanning ZIP:** Membaca setiap file ZIP di direktori.
2.  **ZIP Comment:** Memeriksa apakah ada flag atau teks terenkripsi di komentar ZIP.
3.  **Analisis PNG:**
    -   Mengekstrak teks dari chunk `tEXt`, `iTXt`, `zTXt`.
    -   Mengecek data tersembunyi setelah penanda akhir file `IEND`.
    -   Melakukan analisis LSB (Least Significant Bit) untuk mengekstrak pesan tersembunyi di piksel gambar.
4.  **Pipeline Dekoding:** Setiap teks yang ditemukan (dari komentar, chunk, atau LSB) dimasukkan ke dalam pipeline dekoding:
    -   Coba decode **Base64**.
    -   Coba decode **Hex**.
    -   Coba **Caesar Cipher** (Brute-force 26 shift).
5.  **Pencarian Flag:** Setiap hasil dekoding dicek apakah mengandung pola `CYBERLAB{...}` atau `CTF{...}`.

### Script Solver (`doit.py`)
Script lengkap dapat dilihat pada file `doit.py` di dalam folder challenge. Script ini secara rekursif mencoba membongkar lapisan enkripsi.

## Kesimpulan
Tantangan ini mengajarkan kita untuk tidak hanya melihat file dari luarnya saja, tetapi juga memeriksa metadata, struktur internal file (seperti chunk PNG), dan kemungkinan steganografi. Otomatisasi adalah kunci untuk menyelesaikan tantangan dengan ruang pencarian yang besar seperti ini.
