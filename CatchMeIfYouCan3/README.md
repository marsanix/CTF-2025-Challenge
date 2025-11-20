# CatchMeIfYouCan3 — Write-up Singkat

**Deskripsi**
- “I'm an 'advanced' hacker, you know. I protected the real location with... uh... 'advanced cryptanalysis'. Yeah, that's it.”

**Observasi**
- Folder challenge hanya berisi screenshot soal; tidak ada artefak kriptografi (ciphertext, key, script).
- Artinya jawaban bergantung pada penafsiran frasa dalam deskripsi, bukan proses dekripsi berkas.

**Analisis**
- Kata kunci: “advanced” + “cryptanalysis”. Istilah “advanced” dalam kriptografi sangat identik dengan “Advanced Encryption Standard” (AES).
- Penggunaan kata “cryptanalysis” di sini sengaja menyesatkan; si pembuat challenge menyamarkan “encryption” dengan “cryptanalysis” untuk memancing tebakkan akronim “Advanced …”.
- Pola penamaan flag di challenge sebelumnya pada platform yang sama menggunakan `CYBERLAB{...}`, sehingga konsisten mengemas jawaban sebagai `CYBERLAB{AES}`.

**Flag**
- `CYBERLAB{AES}`

**Verifikasi Logika**
- Tidak tersedia data untuk didekripsi; maka “advanced cryptanalysis” adalah petunjuk semantik.
- “Advanced” → AES (Advanced Encryption Standard).
- Format flag mengikuti konvensi platform → `CYBERLAB{AES}`.

**Catatan**
- Bila nantinya ada lampiran tambahan (ciphertext/berkas) di challenge asli, pendekatan akan berubah ke kripto praktis (faktor RSA, analisis nonce AES-GCM, dsb.). Pada folder ini, solusi adalah berbasis hint semantik.