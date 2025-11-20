# Pagar Tertukar - CTF Challenge Solution

## 📋 Challenge Information

**Challenge Name:** Pagar Tertukar (Swapped Fence)  
**Category:** Cryptography  
**Difficulty:** Medium  
**Files:** `PAGAR.txt`

## 🎯 Challenge Description

File `PAGAR.txt` berisi teks yang sebagian besar adalah kata "PAGAR" yang berulang, dengan flag CTF tersembunyi di dalamnya:

```
PAGAR...PAGAR...cyberlab{XfzTPfmbdXokxuiFqEqTSEZKjji}...PAGAR...PAGAR
```

**Ciphertext:** `XfzTPfmbdXokxuiFqEqTSEZKjji`

**Petunjuk dari soal:** Kata "DUIT" ditekankan dalam deskripsi soal.

## 🔐 Solution

### Metode Enkripsi

Challenge ini menggunakan **enkripsi 2 tahap**:
1. **Rail Fence Cipher** (4 rails)
2. **Vigenere Cipher** (key: "DUIT")

### Proses Dekripsi

Untuk mendekripsi, kita perlu membalikkan urutan enkripsi:

#### Tahap 1: Vigenere Decryption

**Input:** `XfzTPfmbdXokxuiFqEqTSEZKjji`  
**Key:** `DUIT`  
**Output:** `UlrAMleiaDgruaaMnKiAPKRRgpa`

Rumus Vigenere decryption:
```
P = (C - K) mod 26
```

Di mana:
- P = Plaintext
- C = Ciphertext
- K = Key

#### Tahap 2: Rail Fence Decryption

**Input:** `UlrAMleiaDgruaaMnKiAPKRRgpa`  
**Rails:** `4`  
**Output:** `UlaRMelingKarDipAgArPaKuMaR`

Rail Fence dengan 4 rails membaca teks dalam pola zigzag:

```
U . . . M . . . K . . . A . . . a . . . M . .
. l . A . l . i . a . g . u . a . M . K . A . R
. . r . . . e . . . D . . . r . . . a . . . P . .
. . . . . . . . . . . . . . . . . . . n . . . K . . g . . p .
```

### Final Answer

**Plaintext:** `UlarMelingkarDiPagarPakUmar`

Dengan spasi yang tepat: **"Ular Melingkar Di Pagar Pak Umar"**

Ini adalah tongue twister Indonesia yang terkenal untuk melatih pengucapan huruf R di akhir kata!

### Flag

```
cyberlab{UlarMelingkarDiPagarPakUmar}
```

## 💻 Running the Solution

### Prerequisites

- Python 3.x

### Usage

Jalankan script solusi:

```bash
python SOLUTION.py
```

Output:
```
============================================================
FINAL SOLUTION - PAGAR TERTUKAR CTF
============================================================
Original Ciphertext: XfzTPfmbdXokxuiFqEqTSEZKjji

Step 1 - Vigenere with key 'DUIT':
  Result: UlrAMleiaDgruaaMnKiAPKRRgpa

Step 2 - Rail Fence with 4 rails:
  Result: UlaRMelingKarDipAgArPaKuMaR

============================================================
FINAL FLAG:
============================================================
Plaintext: Ular Melingkar Di Pagar Pak Umar
Flag (formatted): cyberlab{UlarMelingkarDiPagarPakUmar}

This is the famous Indonesian tongue twister!
'Ular Melingkar Di Pagar Pak Umar'
(A snake coiling around Mr. Umar's fence)
```

## 🔍 Analysis Process

### 1. Initial Analysis
- Menemukan ciphertext di dalam file `PAGAR.txt`
- Mencoba berbagai cipher klasik (Caesar, Atbash, dll) tanpa hasil

### 2. Key Discovery
- Petunjuk "DUIT" dari soal adalah kunci penting
- Mencoba Vigenere cipher dengan key "DUIT"
- Hasil: `UlrAMleiaDgruaaMnKiAPKRRgpa` (mirip tapi tidak persis dengan tongue twister)

### 3. Second Stage
- Menyadari hasil Vigenere adalah **anagram** dari "Ular Melingkar Di Pagar Pak Umar"
- Nama challenge "Pagar Tertukar" mengindikasikan Rail Fence cipher
- Mencoba Rail Fence dengan berbagai jumlah rails
- **Rail Fence 4 rails** memberikan hasil yang benar!

## 🎓 Key Insights

1. **Challenge Name Clue:** "Pagar Tertukar" = Rail Fence cipher (pagar = fence, tertukar = swapped/rearranged)
2. **Two-Stage Encryption:** Kombinasi Rail Fence + Vigenere
3. **Cultural Element:** Menggunakan tongue twister Indonesia yang terkenal
4. **Anagram Detection:** Hasil Vigenere yang "mirip tapi tidak persis" adalah petunjuk untuk transposition cipher

## 📁 Files

- `PAGAR.txt` - File challenge berisi ciphertext
- `SOLUTION.py` - Script solusi lengkap
- `analyze_vigenere_result.py` - Script analisis tahap kedua
- `README.md` - Dokumentasi ini

## 🏆 Credits

Challenge ini menggabungkan:
- Kriptografi klasik (Vigenere + Rail Fence)
- Budaya Indonesia (tongue twister)
- Pemecahan masalah bertahap

---

**Author:** Solution by AI Assistant, prompted by Marsanix  
**Date:** November 2025
