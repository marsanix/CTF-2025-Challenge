Ekstraksi

- nextFile : true
- fileName (SHA-256 hex, perlu dicocokkan ke nama file): b8f0f85e3704455b5094af36f318efeeee4fe203a30641f22df83b6d2e0cf071
- filePassword (Base64 → teks): TheFragranceFlowerIsSweet
Langkah lanjut

- Temukan ZIP yang namanya di-hash menjadi nilai di atas:
  - Jalankan di folder c:\Users\infin\Documents\LABS\POLTEK\MyKisahCrypto\MyKisahCrypto :
    - python - << 'PY'\nimport os,hashlib\nroot=r'c:\\Users\\infin\\Documents\\LABS\\POLTEK\\MyKisahCrypto\\MyKisahCrypto'\nneedle='b8f0f85e3704455b5094af36f318efeeee4fe203a30641f22df83b6d2e0cf071'\nfor f in os.listdir(root):\n  if f.endswith('.zip'):\n    h=hashlib.sha256(f.encode()).hexdigest()\n    if h==needle:\n      print('match:', f)\nPY
- Buka ZIP yang terdeteksi dengan password TheFragranceFlowerIsSweet .
- Ulangi pola decoding untuk artefak berikutnya sesuai hint (Base64, HEX, Caesar, AES, SHA).