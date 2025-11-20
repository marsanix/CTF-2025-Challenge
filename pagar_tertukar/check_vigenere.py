
def decrypt_vigenere(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if 65 <= ciphertext_int[i] <= 90: # Uppercase
            value = (ciphertext_int[i] - key_as_int[i % key_length] + 26) % 26
            decrypted_text.append(chr(value + 65))
        elif 97 <= ciphertext_int[i] <= 122: # Lowercase
            k = key_as_int[i % key_length]
            if 97 <= k <= 122:
                k -= 32
            
            value = (ciphertext_int[i] - 97 - (k - 65) + 26) % 26
            decrypted_text.append(chr(value + 97))
        else:
            decrypted_text.append(chr(ciphertext_int[i]))
            
    return "".join(decrypted_text)

def decrypt_variant_beaufort(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if 65 <= ciphertext_int[i] <= 90: # Uppercase
            # Variant Beaufort: P = (C - K) % 26? No, that's Vigenere.
            # Beaufort: C = (K - P) % 26 => P = (K - C) % 26
            # Variant Beaufort: C = (P - K) % 26? No, that's Vigenere.
            # Let's try P = (K - C) % 26 (Beaufort)
            value = (key_as_int[i % key_length] - ciphertext_int[i] + 26) % 26
            decrypted_text.append(chr(value + 65))
        elif 97 <= ciphertext_int[i] <= 122: # Lowercase
            k = key_as_int[i % key_length]
            if 97 <= k <= 122:
                k -= 32
            
            value = (k - 65 - (ciphertext_int[i] - 97) + 26) % 26
            decrypted_text.append(chr(value + 97))
        else:
            decrypted_text.append(chr(ciphertext_int[i]))
            
    return "".join(decrypted_text)

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"

print("-" * 20)
print("Beaufort Cipher Results:")
keys = ["PAGAR", "TERTUKAR", "PAGARTERTUKAR"]
for k in keys:
    print(f"Key {k}: {decrypt_variant_beaufort(ciphertext, k)}")
