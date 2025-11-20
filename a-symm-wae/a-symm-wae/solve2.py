#!/usr/bin/env python3
"""
CTF Solution for a-symm-wae challenge - Alternative approach
Try different RSA padding schemes
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64

def solve():
    # Read the private key from the misnamed PNG file
    with open('2key.png', 'r') as f:
        private_key_data = f.read().strip()
    
    # Add PEM headers if not present
    if not private_key_data.startswith('-----BEGIN'):
        private_key_pem = "-----BEGIN RSA PRIVATE KEY-----\n" + private_key_data + "\n-----END RSA PRIVATE KEY-----"
    else:
        private_key_pem = private_key_data
    
    # Import the private RSA key
    private_key = RSA.import_key(private_key_pem)
    
    # Read the encrypted flag from the misnamed JPEG file
    with open('flag.jpeg', 'rb') as f:
        encrypted_flag = f.read()
    
    print(f"Encrypted flag length: {len(encrypted_flag)} bytes")
    print(f"RSA key size: {private_key.size_in_bytes()} bytes")
    
    # Try PKCS1_v1_5 (older padding scheme)
    print("\n[1] Trying PKCS1_v1_5 decryption...")
    try:
        cipher = PKCS1_v1_5.new(private_key)
        sentinel = b'DECRYPTION_FAILED'
        decrypted_flag = cipher.decrypt(encrypted_flag, sentinel)
        if decrypted_flag != sentinel:
            print("✓ Flag found with PKCS1_v1_5:")
            print(decrypted_flag.decode('utf-8', errors='ignore'))
            return
    except Exception as e:
        print(f"  Failed: {e}")
    
    # Try raw RSA decryption (no padding)
    print("\n[2] Trying raw RSA decryption...")
    try:
        # Convert bytes to integer
        encrypted_int = int.from_bytes(encrypted_flag, byteorder='big')
        # Decrypt using private key
        decrypted_int = pow(encrypted_int, private_key.d, private_key.n)
        # Convert back to bytes
        decrypted_bytes = decrypted_int.to_bytes(private_key.size_in_bytes(), byteorder='big')
        # Remove padding manually (PKCS#1 v1.5 padding starts with 0x00 0x02)
        if decrypted_bytes[0:2] == b'\x00\x02':
            # Find the 0x00 separator
            separator_index = decrypted_bytes.index(b'\x00', 2)
            decrypted_flag = decrypted_bytes[separator_index+1:]
            print("✓ Flag found with raw RSA + manual padding removal:")
            print(decrypted_flag.decode('utf-8', errors='ignore'))
            return
        else:
            print("  Padding format not recognized")
            print(f"  First bytes: {decrypted_bytes[:20].hex()}")
    except Exception as e:
        print(f"  Failed: {e}")
    
    # Try PKCS1_OAEP again with more details
    print("\n[3] Trying PKCS1_OAEP with error details...")
    try:
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_flag = cipher.decrypt(encrypted_flag)
        print("✓ Flag found with PKCS1_OAEP:")
        print(decrypted_flag.decode('utf-8'))
    except Exception as e:
        print(f"  Failed: {e}")

if __name__ == "__main__":
    solve()
