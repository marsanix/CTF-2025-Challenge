def decrypt_vigenere(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if 65 <= ciphertext_int[i] <= 90:
            value = (ciphertext_int[i] - key_as_int[i % key_length] + 26) % 26
            decrypted_text.append(chr(value + 65))
        elif 97 <= ciphertext_int[i] <= 122:
            k = key_as_int[i % key_length]
            if 97 <= k <= 122:
                k -= 32
            value = (ciphertext_int[i] - 97 - (k - 65) + 26) % 26
            decrypted_text.append(chr(value + 97))
        else:
            decrypted_text.append(chr(ciphertext_int[i]))
    return "".join(decrypted_text)

def decrypt_beaufort(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if 65 <= ciphertext_int[i] <= 90:
            value = (key_as_int[i % key_length] - ciphertext_int[i] + 26) % 26
            decrypted_text.append(chr(value + 65))
        elif 97 <= ciphertext_int[i] <= 122:
            k = key_as_int[i % key_length]
            if 97 <= k <= 122:
                k -= 32
            value = (k - 65 - (ciphertext_int[i] - 97) + 26) % 26
            decrypted_text.append(chr(value + 97))
        else:
            decrypted_text.append(chr(ciphertext_int[i]))
    return "".join(decrypted_text)

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "DUIT"

print("=" * 60)
print("TESTING WITH KEY: DUIT")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print()

print("--- Vigenere Cipher ---")
result = decrypt_vigenere(ciphertext, key)
print(f"Key DUIT: {result}")
print()

print("--- Beaufort Cipher ---")
result = decrypt_beaufort(ciphertext, key)
print(f"Key DUIT: {result}")
print()

print("--- Reversed Ciphertext + Vigenere ---")
reversed_cipher = ciphertext[::-1]
result = decrypt_vigenere(reversed_cipher, key)
print(f"Reversed + DUIT: {result}")
print()

print("--- Vigenere with reversed key ---")
reversed_key = key[::-1]
result = decrypt_vigenere(ciphertext, reversed_key)
print(f"Key {reversed_key}: {result}")
print()

print("--- All rotations of DUIT ---")
for i in range(len(key)):
    rotated_key = key[i:] + key[:i]
    result = decrypt_vigenere(ciphertext, rotated_key)
    print(f"Key {rotated_key}: {result}")
