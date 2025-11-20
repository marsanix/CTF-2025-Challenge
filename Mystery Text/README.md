# Mystery Text - Write Up

## Deskripsi Tantangan
**Soal:**
Di ruang server, sebuah komputer tertinggal menyala dengan file `mystery.txt` terbuka ditinggalkan oleh teknisi yang terburu-buru. Tugasmu: pecahkan isi file tersebut.

**Hint:** Coba gunakan XOR

## Analisis
File `mystery.txt` berisi ciphertext:
`PJQVA_RQhXa"cg#L"gfL~fw'{Lqfx'}n`

Kita tahu format flag biasanya dimulai dengan `CYBERLAB{`.
Dengan menggunakan operasi XOR pada karakter pertama ciphertext dengan karakter pertama format flag yang diketahui, kita dapat mencari kuncinya.

- `P` (0x50) XOR `C` (0x43) = `0x13`
- `J` (0x4A) XOR `Y` (0x59) = `0x13`
- `Q` (0x51) XOR `B` (0x42) = `0x13`

Kunci (key) yang konsisten ditemukan adalah `0x13` (desimal 19).

## Penyelesaian
Kami membuat script Python sederhana untuk melakukan operasi XOR pada seluruh isi file dengan kunci `0x13`.

```python
def decrypt():
    with open('mystery.txt', 'r') as f:
        ciphertext = f.read().strip()
    
    key = 0x13
    plaintext = ''.join(chr(ord(c) ^ key) for c in ciphertext)
    print(plaintext)

if __name__ == "__main__":
    decrypt()
```

## Flag
Setelah didekripsi, didapatkan flag:
`CYBERLAB{Kr1pt0_1tu_mud4h_buk4n}`

## Konsep Dasar XOR (Exclusive OR)
Untuk memahami bagaimana kunci `0x13` ditemukan, mari kita bedah operasi XOR pada level biner.

**Prinsip XOR:**
- Jika bit sama (0 vs 0 atau 1 vs 1), hasilnya **0**.
- Jika bit beda (0 vs 1 atau 1 vs 0), hasilnya **1**.

### Contoh 1: P XOR C = 0x13
1.  **Huruf 'P' (Ciphertext)**
    - ASCII: 80
    - Hex: `0x50`
    - Biner: `0101 0000`
2.  **Huruf 'C' (Plaintext yang diharapkan)**
    - ASCII: 67
    - Hex: `0x43`
    - Biner: `0100 0011`
3.  **Operasi XOR:**
    ```text
      0101 0000  (P / 0x50)
    ^ 0100 0011  (C / 0x43)
    -----------
      0001 0011
    ```
    Hasil biner `0001 0011` jika diubah ke Hex menjadi **`0x13`**.

### Contoh 2: J XOR Y = 0x13
1.  **Huruf 'J'** (`0x4A` / `0100 1010`)
2.  **Huruf 'Y'** (`0x59` / `0101 1001`)
3.  **Operasi:**
    ```text
      0100 1010  (J)
    ^ 0101 1001  (Y)
    -----------
      0001 0011  -> 0x13
    ```

### Sifat Unik XOR
XOR memiliki sifat **Reversible** (dapat dibalik):
- Jika `A XOR B = K`
- Maka `A XOR K = B`
- Dan `B XOR K = A`

Inilah mengapa jika kita tahu Ciphertext (`A`) dan sebagian Plaintext (`B`), kita bisa menemukan Kunci (`K`) dengan cara `A XOR B`.

