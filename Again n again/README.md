# Again n again — Write-up

## Deskripsi Tantangan
**Soal:**
Diberikan sebuah file `Challenge.txt` yang berisi string panjang yang terlihat seperti encoding Base64.
Hint: "Jarvis, tolong anukan dulu biar ga apa kali enkripsinya"

**Ciphertext Awal:**
`Vm0weE5GbFdWWGhUV0d4VlYwZG9WRll3Wkc5V1ZteHlXa1pPVjFadGVGcFpNRlpyVm1zeFYyTkljRmRpVkZab1ZrZHplRll5VGtkYVJtaG9UVmhDZVZkV1VrZFRNVnBYVjI1S2FWSnNjSEJXTUZWM1pVWmFjVk5xVW1oTlZYQjVWR3hhYjFWR1duVlJia0pYVFVkU1QxcFZXbXRXTVZaeVUyMTRVMkpXU2twV2JHUXdZekZXZEZOcmFGWmlSa3BoVm01d1JtUXhVblJsUjNSWFRWWmFlVmRyWkc5VWJGcHlZMFZ3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ==`

## Analisis
1.  **Identifikasi Pola:** String diakhiri dengan `==`, yang merupakan ciri khas padding Base64. Karakter yang digunakan (A-Z, a-z, 0-9, +, /) juga sesuai dengan charset Base64.
2.  **Percobaan Pertama:** Melakukan decoding Base64 satu kali.
    -   Hasil: `Vm0xNFlWVXhTWGxVV0doVFYwZG9WVmxyWkZOV1ZteFpZMFZrV...`
    -   Observasi: Hasilnya masih terlihat seperti Base64 (masih acak, charset terbatas).
3.  **Hipotesis:** Ini adalah **Recursive Base64**, di mana plaintext di-encode berkali-kali.

## Proses Penyelesaian (Thinking Process)
Karena melakukan decode manual berulang-ulang akan melelahkan dan rentan kesalahan, solusi terbaik adalah menggunakan **script otomatisasi** atau tools seperti CyberChef dengan resep "Magic" atau loop.

Kami memilih menggunakan Python untuk mendekode secara berulang sampai pola flag `CYBERLAB` ditemukan.

## Tools
-   **Python 3**: Untuk scripting otomatis.
-   **Library `base64`**: Modul bawaan Python.

## Langkah Penyelesaian
Berikut adalah script yang digunakan untuk menyelesaikan tantangan ini:

```python
import base64
import binascii

def solve():
    # String awal dari Challenge.txt
    encoded = "Vm0weE5GbFdWWGhUV0d4VlYwZG9WRll3Wkc5V1ZteHlXa1pPVjFadGVGcFpNRlpyVm1zeFYyTkljRmRpVkZab1ZrZHplRll5VGtkYVJtaG9UVmhDZVZkV1VrZFRNVnBYVjI1S2FWSnNjSEJXTUZWM1pVWmFjVk5xVW1oTlZYQjVWR3hhYjFWR1duVlJia0pYVFVkU1QxcFZXbXRXTVZaeVUyMTRVMkpXU2twV2JHUXdZekZXZEZOcmFGWmlSa3BoVm01d1JtUXhVblJsUjNSWFRWWmFlVmRyWkc5VWJGcHlZMFZ3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ=="
    
    count = 0
    while True:
        try:
            # Coba decode
            decoded = base64.b64decode(encoded).decode('utf-8')
            count += 1
            print(f"Round {count}: {decoded[:30]}...")
            
            # Update string encoded dengan hasil decode untuk putaran berikutnya
            encoded = decoded
            
            # Cek apakah flag sudah muncul
            if "CYBERLAB" in encoded:
                print(f"\n[+] Flag Found after {count} rounds!")
                print(f"Flag: {encoded}")
                break
        except (binascii.Error, UnicodeDecodeError):
            # Berhenti jika error (bukan base64 valid lagi)
            print("Decoding stopped/failed.")
            break

if __name__ == "__main__":
    solve()
```

### Hasil Eksekusi
Setelah dijalankan, script melakukan decoding sebanyak **8 kali** sebelum akhirnya mendapatkan teks yang dapat dibaca (plaintext).

**Output:**
```text
Round 1: Vm0xNFlWVXhTWGxVV0doVFYwZG9WVm...
...
Round 7: Q1lCRVJMQUJ7UGVtNGFOYXNhbl9kMW...
Round 8: CYBERLAB{Pem4aNasan_d1kiT_wkWK}
```

## Flag
`CYBERLAB{Pem4aNasan_d1kiT_wkWK}`

## Kesimpulan & Pelajaran
-   **Encoding vs Encryption:** Base64 adalah encoding, bukan enkripsi. Ia tidak menyembunyikan data (hanya mengubah representasi) dan mudah dibalikkan tanpa kunci.
-   **Rekursif:** Dalam CTF, seringkali tantangan melibatkan lapisan (layers) yang berulang.
-   **Scripting:** Kemampuan membuat script sederhana sangat membantu untuk tugas yang repetitif.
