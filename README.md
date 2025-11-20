# CTF 2025 - Challenge Write-ups

Dokumentasi ini berisi kumpulan *write-up* (pembahasan) untuk soal-soal CTF yang digunakan pada kegiatan **HMTI x CyberLabs CTF 2025** untuk siswa SMK di Batam.

## Daftar Challenge

| No | Nama Challenge | Kategori | Tingkat Kesulitan |
|----|----------------|----------|-------------------|
| 1 | **Again n again** | Encoding | Easy |
| 2 | **Mystery Text** | Cryptography (XOR) | Easy |
| 3 | **Morse Sandi** | Cryptography (Audio) | Medium |
| 4 | **a-symm-wae** | Cryptography (RSA) | Medium |
| 5 | **Pagar Tertukar** | Cryptography (Classic) | Medium |
| 6 | **Juara Kompetisi** | Steganography/Forensics | Easy |
| 7 | **CatchMeIfYouCan3** | Logic/Trivia | Easy |
| 8 | **CatchMeIfYouCan5** | Logic/Trivia | Easy |
| 9 | **MyKisahCrypto** | Cryptography (Mixed) | Hard |

---

## Pembahasan Singkat

### 1. Again n again
**Deskripsi:** Teks terenkripsi Base64 berulang kali.
**Solusi:** Dekode Base64 secara rekursif (sekitar 8 kali) hingga menemukan format flag.
**Poin Belajar:** Pengenalan encoding Base64 dan otomatisasi sederhana.

### 2. Mystery Text
**Deskripsi:** File `mystery.txt` berisi ciphertext yang di-XOR.
**Solusi:**
- Analisis header ciphertext dengan known-plaintext `CYBERLAB{`.
- Ditemukan kunci XOR `0x13`.
- Dekripsi seluruh file dengan kunci tersebut.
**Poin Belajar:** Konsep dasar XOR cipher dan known-plaintext attack.

### 3. Morse Sandi
**Deskripsi:** File audio `.wav` berisi sinyal morse.
**Solusi:** Decode audio morse menggunakan tools online (seperti morsefm.com) atau spektogram.
**Poin Belajar:** Encoding sinyal audio dan sandi morse.

### 4. a-symm-wae
**Deskripsi:** Tiga file dengan ekstensi yang salah (`.bmp`, `.png`, `.jpeg`).
**Solusi:**
- Identifikasi tipe file asli: `1key.bmp` (Public Key), `2key.png` (Private Key), `flag.jpeg` (Encrypted Data).
- Lakukan dekripsi RSA Raw menggunakan Private Key.
**Poin Belajar:** Asymmetric encryption (RSA) dan analisis file signature.

### 5. Pagar Tertukar
**Deskripsi:** Ciphertext `XfzTPfmbdXokxuiFqEqTSEZKjji` dengan hint "DUIT".
**Solusi:**
- Tahap 1: Vigenere Cipher dengan key `DUIT`.
- Tahap 2: Rail Fence Cipher (4 rails).
- Hasil: Tongue twister "Ular Melingkar Di Pagar Pak Umar".
**Poin Belajar:** Kombinasi cipher klasik (Polyalphabetic & Transposition).

### 6. Juara Kompetisi
**Deskripsi:** File sertifikat dalam format PDF (palsu).
**Solusi:** Analisis file sebagai sertifikat X.509 (SSL/TLS). Flag tersembunyi di field `Subject Alternative Name`.
**Poin Belajar:** Struktur sertifikat digital dan metadata.

### 7. CatchMeIfYouCan3
**Deskripsi:** Soal logika tentang "Advanced Cryptanalysis".
**Solusi:** Kata kunci "Advanced" mengarah pada **AES** (Advanced Encryption Standard).
**Poin Belajar:** Pengetahuan umum algoritma kriptografi.

### 8. CatchMeIfYouCan5
**Deskripsi:** Soal logika tentang "Penguin's Key" dan kegunaan lain dari kunci.
**Solusi:** Kunci selain untuk enkripsi digunakan untuk **Digital Signature**.
**Poin Belajar:** Fungsi kunci kriptografi (Confidentiality vs Authenticity/Integrity).

---

**Catatan:**
Setiap folder challenge memiliki file `README.md` atau `Challenge.txt` yang berisi detail lebih lengkap mengenai cara penyelesaian masing-masing soal.

---

## ⚠️ Disclaimer

Dokumentasi ini disusun secara independen dan **bukan** merupakan rilis resmi dari penyelenggara maupun pembuat soal HMTI x CyberLabs CTF 2025. Seluruh konten dalam repository ini dibuat semata-mata untuk tujuan **pembelajaran individu**.

Harapannya, dokumentasi ini dapat bermanfaat bagi teman-teman siswa SMK yang ingin mempelajari penyelesaian soal-soal CTF sebagai persiapan untuk mengikuti kompetisi serupa di kemudian hari.

---

## ❤️ Ucapan Terimakasih

Terima kasih yang sebesar-besarnya kami ucapkan kepada:

*   **HMTI (Himpunan Mahasiswa Teknik Informatika) Politeknik Negeri Batam** selaku penyelenggara acara.
*   **CyberLabs** dan semua yang berada didalamnya,selaku pembuat soal (challenge creator) yang telah menyajikan tantangan-tantangan yang kreatif, edukatif, dan menyenangkan.
*   Serta seluruh pihak yang terlibat dalam menyukseskan kegiatan **HMTI x CyberLabs CTF 2025**.

*Keep learning and happy hacking!*


