# CatchMeIfYouCan5 — Write-up Singkat

**Deskripsi**
- “Well, well, you found the penguin's key. So, what else can a key be used for?”

**Observasi**
- Folder challenge hanya memuat screenshot; tidak ada ciphertext, key file, atau script.
- Soal menekankan “penguin” → maskot Linux (Tux) dan “key”.

**Analisis**
- “You found the penguin's key” menyiratkan kunci kriptografi (contoh RSA) pada sistem Linux.
- Pertanyaan “what else can a key be used for?” menuntun ke fungsi lain dari kunci selain enkripsi: penandatanganan (digital signature).
- Di ekosistem Linux, kunci (GPG/SSH/RSA) lazim dipakai untuk “signing” paket/repositori dan autentikasi; hint ini mengarah ke konsep “signature”.

**Flag**
- `CYBERLAB{signature}`

**Verifikasi Logika**
- Tidak ada artefak untuk didekripsi; jawaban berbasis interpretasi semantik.
- Kunci kriptografi: enkripsi dan penandatanganan. “else” → fungsi kedua → signature.
- Format flag mengikuti konvensi platform `CYBERLAB{...}`.