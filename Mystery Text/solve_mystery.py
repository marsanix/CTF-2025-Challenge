def decrypt():
    try:
        with open('mystery.txt', 'r') as f:
            ciphertext = f.read().strip()
        
        key = 0x13
        plaintext = ''.join(chr(ord(c) ^ key) for c in ciphertext)
        
        print(f"Ciphertext: {ciphertext}")
        print(f"Plaintext:  {plaintext}")
        
    except FileNotFoundError:
        print("Error: mystery.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    decrypt()
