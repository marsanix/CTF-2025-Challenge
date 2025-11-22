# Juara Kompetisi — Write-up Singkat

**Ringkasan**
- Berkas `piagamPenghargaan.pdf` ternyata bukan PDF biasa; isinya adalah blok sertifikat X.509 dalam format PEM.
- Di extension `Subject Alternative Name` terdapat **dua petunjuk**:
  - DNS Name dengan placeholder: `CYBERLAB{????????????????????????}`
  - DNS Name dengan flag sebenarnya (leet speak): `s3rt1f1k4tny4_4sl1_buk4n_d1p4lsuk4n_3j8n9v2`
- Hint di challenge: "istilah lain dari piagam penghargaan?" → jawabannya "sertifikat", yang menjadi tema flag.

**Analisis Berkas**
- Struktur berkas dimulai dengan `-----BEGIN CERTIFICATE-----` dan diakhiri `-----END CERTIFICATE-----`.
- Sertifikat X.509 menyimpan metadata seperti `Subject`, `Issuer`, dan extension. Flag disisipkan di extension `Subject Alternative Name (SAN)` sebagai DNS Name.
- Challenge ini menggunakan teknik **double hint**: satu DNS Name menunjukkan format flag dengan placeholder, DNS Name lainnya berisi flag sebenarnya dalam leet speak.

**Langkah Ekstraksi (Windows)**
- Salin isi antara `BEGIN` dan `END` ke file `cert.pem`.
- Dump sertifikat:
  - `certutil -dump cert.pem`
  - atau `openssl x509 -in cert.pem -text -noout`
- Cari bagian `Subject Alternative Name`; akan terlihat beberapa DNS Name termasuk placeholder dan flag sebenarnya.

**Flag**
- `CYBERLAB{s3rt1f1k4tny4_4sl1_buk4n_d1p4lsuk4n_3j8n9v2}`

**Penjelasan Flag (Leet Speak)**
- `s3rt1f1k4tny4` → "sertifikatnya"
- `4sl1` → "asli"
- `buk4n` → "bukan"
- `d1p4lsuk4n` → "dipalsukan"
- `3j8n9v2` → kode acak/hash
- **Makna**: "Sertifikatnya asli bukan dipalsukan"

**Catatan**
- Bila viewer PDF gagal membuka, itu normal karena konten sebenarnya bukan PDF.
- Teknik ini memanfaatkan penyembunyian data di struktur sertifikat (steganografi ringan dalam metadata).
- Challenge menggunakan **double hint technique**: placeholder flag untuk menunjukkan format, dan flag sebenarnya tersembunyi di DNS Name lain.

**Contoh Output (certutil)**
- Jalankan: `certutil -dump cert.pem`
- Potongan relevan:
```
X509 Certificate:
...
Subject Alternative Name:
    DNS Name=localhost
    DNS Name=bar.org
    DNS Name=CYBERLAB{????????????????????????}
    DNS Name=*.foo.net
    DNS Name=s3rt1f1k4tny4_4sl1_buk4n_d1p4lsuk4n_3j8n9v2
    IP Address=127.0.0.1
    IP Address=192.168.100.1
...
```

**Contoh Output (OpenSSL)**
- Jalankan: `openssl x509 -in cert.pem -text -noout`
- Potongan relevan:
```
X509v3 Subject Alternative Name:
    DNS:localhost, DNS:bar.org, DNS:CYBERLAB{????????????????????????}, 
    DNS:*.foo.net, DNS:s3rt1f1k4tny4_4sl1_buk4n_d1p4lsuk4n_3j8n9v2, 
    IP:127.0.0.1, IP:192.168.100.1
```