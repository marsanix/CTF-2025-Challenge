#!/usr/bin/env python3
"""
CTF Solution for a-symm-wae challenge - Check both keys
Maybe the challenge encrypted with the private key and we need to decrypt with public?
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64

def solve():
    # Read both keys
    with open('1key.bmp', 'r') as f:
        public_key_data = f.read().strip()
    
    with open('2key.png', 'r') as f:
        private_key_data = f.read().strip()
    
    # Add PEM headers if not present
    if not public_key_data.startswith('-----BEGIN'):
        public_key_pem = "-----BEGIN PUBLIC KEY-----\n" + public_key_data + "\n-----END PUBLIC KEY-----"
    else:
        public_key_pem = public_key_data
        
    if not private_key_data.startswith('-----BEGIN'):
        private_key_pem = "-----BEGIN RSA PRIVATE KEY-----\n" + private_key_data + "\n-----END RSA PRIVATE KEY-----"
    else:
        private_key_pem = private_key_data
    
    # Import both keys
    try:
        public_key = RSA.import_key(public_key_pem)
        print("✓ Public key loaded successfully")
        print(f"  Public key n: {hex(public_key.n)[:50]}...")
        print(f"  Public key e: {public_key.e}")
    except Exception as e:
        print(f"✗ Failed to load public key: {e}")
        return
    
    try:
        private_key = RSA.import_key(private_key_pem)
        print("✓ Private key loaded successfully")
        print(f"  Private key n: {hex(private_key.n)[:50]}...")
        print(f"  Private key e: {private_key.e}")
        print(f"  Private key d: {hex(private_key.d)[:50]}...")
    except Exception as e:
        print(f"✗ Failed to load private key: {e}")
        return
    
    # Check if keys match
    if public_key.n == private_key.n:
        print("✓ Keys are a matching pair (same modulus)")
    else:
        print("✗ WARNING: Keys don't match!")
    
    # Read the encrypted flag
    with open('flag.jpeg', 'rb') as f:
        encrypted_flag = f.read()
    
    print(f"\nEncrypted flag length: {len(encrypted_flag)} bytes")
    print(f"Encrypted flag (hex): {encrypted_flag.hex()}")
    
    # Try decrypting with private key using PKCS1_v1_5
    print("\n[Attempt 1] Private key + PKCS1_v1_5...")
    try:
        cipher = PKCS1_v1_5.new(private_key)
        sentinel = b'FAIL'
        decrypted = cipher.decrypt(encrypted_flag, sentinel)
        if decrypted != sentinel:
            print("✓ Success!")
            print(f"Decrypted: {decrypted}")
            try:
                print(f"As text: {decrypted.decode('utf-8')}")
            except:
                print(f"As hex: {decrypted.hex()}")
            return
    except Exception as e:
        print(f"  Failed: {e}")
    
    # Try raw decryption and examine the output more carefully
    print("\n[Attempt 2] Raw RSA with private key...")
    try:
        encrypted_int = int.from_bytes(encrypted_flag, byteorder='big')
        decrypted_int = pow(encrypted_int, private_key.d, private_key.n)
        decrypted_bytes = decrypted_int.to_bytes(private_key.size_in_bytes(), byteorder='big')
        
        print(f"Decrypted (hex): {decrypted_bytes.hex()}")
        print(f"Decrypted (raw): {decrypted_bytes}")
        
        # Try to find printable content
        for i in range(len(decrypted_bytes)):
            if decrypted_bytes[i] != 0:
                print(f"First non-zero byte at position {i}: {decrypted_bytes[i:].hex()}")
                try:
                    print(f"As text: {decrypted_bytes[i:].decode('utf-8', errors='ignore')}")
                except:
                    pass
                break
    except Exception as e:
        print(f"  Failed: {e}")

if __name__ == "__main__":
    solve()
