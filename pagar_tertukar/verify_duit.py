ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "DUIT"

print("DUIT KEY VERIFICATION")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}\n")

# Standard Vigenere decryption
result = ""
for i, c in enumerate(ciphertext):
    if c.isalpha():
        key_val = ord(key[i % len(key)].upper()) - ord('A')
        if c.isupper():
            new_char = chr((ord(c) - ord('A') - key_val + 26) % 26 + ord('A'))
        else:
            new_char = chr((ord(c) - ord('a') - key_val + 26) % 26 + ord('a'))
        result += new_char
    else:
        result += c

print(f"Vigenere Decrypt: {result}")
print(f"\nFull flag: cyberlab{{{result}}}")
