# Juara Kompetisi — Write-up Singkat

**Ringkasan**
- Berkas `piagamPenghargaan.pdf` ternyata bukan PDF biasa; isinya adalah blok sertifikat X.509 dalam format PEM.
- Di extension `Subject Alternative Name` terdapat string bertema CTF: `CYBERLAB{sertifikat}`.
- Hint di challenge: “istilah lain dari piagam penghargaan?” → jawabannya “sertifikat”, yang menjadi isi flag.

**Analisis Berkas**
- Struktur berkas dimulai dengan `-----BEGIN CERTIFICATE-----` dan diakhiri `-----END CERTIFICATE-----`.
- Sertifikat X.509 menyimpan metadata seperti `Subject`, `Issuer`, dan extension. Flag disisipkan di extension `Subject Alternative Name (SAN)` sebagai teks.

**Langkah Ekstraksi (Windows)**
- Salin isi antara `BEGIN` dan `END` ke file `cert.pem`.
- Dump sertifikat:
  - `certutil -dump cert.pem`
  - atau `openssl x509 -in cert.pem -text -noout`
- Cari bagian `Subject Alternative Name`; akan terlihat pola `CYBERLAB{sertifikat}`.

**Flag**
- `CYBERLAB{sertifikat}`

**Catatan**
- Bila viewer PDF gagal membuka, itu normal karena konten sebenarnya bukan PDF.
- Teknik ini memanfaatkan penyembunyian data di struktur sertifikat (steganografi ringan dalam metadata).

**Contoh Output (certutil)**
- Jalankan: `certutil -dump cert.pem`
- Potongan relevan:
```
X509 Certificate:
...
Subject Alternative Name:
    DNS Name=localhost
    DNS Name=bar.org
    Other Name=CYBERLAB{sertifikat}
...
```

**Contoh Output (OpenSSL)**
- Jalankan: `openssl x509 -in cert.pem -text -noout`
- Potongan relevan:
```
X509v3 Subject Alternative Name:
    DNS:localhost, DNS:bar.org, CYBERLAB{sertifikat}
```