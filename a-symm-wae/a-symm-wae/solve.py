#!/usr/bin/env python3
"""
CTF Solution for a-symm-wae challenge
The hint suggests changing file extensions - the files are misnamed:
- 1key.bmp is actually an RSA public key
- 2key.png is actually an RSA private key  
- flag.jpeg is likely encrypted data
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
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
    
    # Create cipher for decryption
    cipher = PKCS1_OAEP.new(private_key)
    
    # Read the encrypted flag from the misnamed JPEG file
    with open('flag.jpeg', 'rb') as f:
        encrypted_flag = f.read()
    
    print(f"Encrypted flag length: {len(encrypted_flag)} bytes")
    print(f"First few bytes: {encrypted_flag[:20]}")
    
    # Decrypt the flag
    try:
        decrypted_flag = cipher.decrypt(encrypted_flag)
        print("\n✓ Flag found:")
        print(decrypted_flag.decode('utf-8'))
    except Exception as e:
        print(f"Direct decryption failed: {e}")
        print("\nTrying alternative methods...")
        
        # Try base64 decoding first if needed
        try:
            encrypted_data = base64.b64decode(encrypted_flag)
            decrypted_flag = cipher.decrypt(encrypted_data)
            print("\n✓ Flag found (after base64 decode):")
            print(decrypted_flag.decode('utf-8'))
        except Exception as e2:
            print(f"Base64 method also failed: {e2}")
            
            # Try reading as text and base64 decode
            try:
                with open('flag.jpeg', 'r') as f:
                    encrypted_text = f.read().strip()
                encrypted_data = base64.b64decode(encrypted_text)
                decrypted_flag = cipher.decrypt(encrypted_data)
                print("\n✓ Flag found (text base64 decode):")
                print(decrypted_flag.decode('utf-8'))
            except Exception as e3:
                print(f"Text base64 method also failed: {e3}")

if __name__ == "__main__":
    solve()
