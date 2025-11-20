# CTF Walkthrough: a-symm-wae

## Challenge Overview

**Challenge Name:** a-symm-wae  
**Category:** Cryptography (Asymmetric Encryption)  
**Difficulty:** Medium  
**Flag:** `CYBERLAB{h3y_4nt3k_4nt3k_4s3ng_3444hAaA}`

## Challenge Description

> Can you find the flag?
> 
> **Hint:** Bagaimana jika ekstensi file-nya diubah? (What if the file extension is changed?)

## Files Provided

The challenge directory contained three files:
- `1key.bmp` (222 bytes)
- `2key.png` (840 bytes)
- `flag.jpeg` (128 bytes)

## Solution Process

### Step 1: Analyzing the Files

The hint suggested that file extensions might be misleading. Upon examining the files:

**1key.bmp** - Despite the `.bmp` extension, this file contained an **RSA public key**:
```
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzYLf+U3xrRdPoyIsqSwWDYL95
Bbyhlz6+xsUR+0A8m5Eqq1h98lW6uboD5sJJ0T0dUR1N0I6gwp4k2CLhLvxQ0uR2
N8hRecXb7QyfrfxBVXlRxvHZj4iQKfnxwCHbRa/WAj3pEL7Q82IKpKiZwe2Dmxec
GFfVh/HH4SO+R19A+QIDAQAB
```

**2key.png** - Despite the `.png` extension, this file contained an **RSA private key**:
```
MIICXgIBAAKBgQCzYLf+U3xrRdPoyIsqSwWDYL95Bbyhlz6+xsUR+0A8m5Eqq1h9
8lW6uboD5sJJ0T0dUR1N0I6gwp4k2CLhLvxQ0uR2N8hRecXb7QyfrfxBVXlRxvHZ
j4iQKfnxwCHbRa/WAj3pEL7Q82IKpKiZwe2DmxecGFfVh/HH4SO+R19A+QIDAQAB
...
```

**flag.jpeg** - This was 128 bytes of binary data (matching the RSA key size), containing the encrypted flag.

### Step 2: Understanding the Encryption

- The challenge used **RSA asymmetric encryption**
- Key size: 1024 bits (128 bytes)
- The flag was encrypted using RSA

### Step 3: Decryption Attempts

I tried multiple decryption approaches:

1. **PKCS1_OAEP padding** - Failed with "Incorrect decryption" error
2. **PKCS1_v1_5 padding** - Failed
3. **Raw RSA decryption** - **Success!** ✓

### Step 4: Final Solution

The working solution used **raw RSA decryption**.

**Solution Script:** [`a-symm-wae/solve3.py`](a-symm-wae/solve3.py)

Key parts of the solution:

```python
from Crypto.PublicKey import RSA

# Load the private key (with proper PEM headers)
with open('2key.png', 'r') as f:
    private_key_data = f.read().strip()

private_key_pem = "-----BEGIN RSA PRIVATE KEY-----\n" + private_key_data + "\n-----END RSA PRIVATE KEY-----"
private_key = RSA.import_key(private_key_pem)

# Read encrypted flag
with open('flag.jpeg', 'rb') as f:
    encrypted_flag = f.read()

# Perform raw RSA decryption
encrypted_int = int.from_bytes(encrypted_flag, byteorder='big')
decrypted_int = pow(encrypted_int, private_key.d, private_key.n)
decrypted_bytes = decrypted_int.to_bytes(private_key.size_in_bytes(), byteorder='big')

# Extract the flag (skip leading zeros)
for i in range(len(decrypted_bytes)):
    if decrypted_bytes[i] != 0:
        flag = decrypted_bytes[i:].decode('utf-8', errors='ignore')
        print(flag)
        break
```

### Running the Solution

```bash
cd a-symm-wae
python solve3.py
```

**Output:**
```
✓ Public key loaded successfully
  Public key n: 0xb360b7fe537c6b45d3e8c88b2a4b058360...
  Public key e: 65537
✓ Private key loaded successfully
  Private key n: 0xb360b7fe537c6b45d3e8c88b2a4b058360...
  Private key e: 65537
  Private key d: 0x46aec721eaa018b2c5b6f2d8f...
✓ Keys are a matching pair (same modulus)

Encrypted flag length: 128 bytes

[Attempt 2] Raw RSA with private key...
First non-zero byte at position 94: 435942455...
As text: CYBERLAB{h3y_4nt3k_4nt3k_4s3ng_3444hAaA}
```

## Flag

```
CYBERLAB{h3y_4nt3k_4nt3k_4s3ng_3444hAaA}
```

## Key Takeaways

1. **Don't trust file extensions** - The hint was crucial; files can be misnamed to mislead
2. **RSA encryption basics** - Understanding different padding schemes (OAEP, PKCS1_v1_5, raw)
3. **Raw RSA decryption** - Sometimes the simplest approach works when standard padding schemes fail
4. **File analysis** - Always examine file contents, not just extensions
5. **Key verification** - Verify that public and private keys match by comparing their modulus (n)

## Tools Used

- Python 3 with `pycryptodome` library
- RSA cryptography functions
- File analysis tools

## Files in This Repository

- `Challenge.txt` - Challenge description and hint
- `a-symm-wae/1key.bmp` - RSA public key (misnamed as .bmp)
- `a-symm-wae/2key.png` - RSA private key (misnamed as .png)
- `a-symm-wae/flag.jpeg` - Encrypted flag (misnamed as .jpeg)
- `a-symm-wae/solve3.py` - **Working solution script** ✓
- `a-symm-wae/solve2.py` - Alternative approach (testing different padding schemes)
- `a-symm-wae/solve.py` - Initial attempt

---

**Challenge completed successfully!** 🎉
