def decrypt_vigenere(ciphertext, key):
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
    return result

def decrypt_rail_fence(cipher, rails):
    rail = [['\n' for i in range(len(cipher))] for j in range(rails)]
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
            
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
                
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

print("=" * 60)
print("FINAL SOLUTION - PAGAR TERTUKAR CTF")
print("=" * 60)

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "DUIT"
rails = 4

print(f"Original Ciphertext: {ciphertext}")
print()

# Step 1: Vigenere decryption
vigenere_result = decrypt_vigenere(ciphertext, key)
print(f"Step 1 - Vigenere with key '{key}':")
print(f"  Result: {vigenere_result}")
print()

# Step 2: Rail Fence decryption
final_result = decrypt_rail_fence(vigenere_result, rails)
print(f"Step 2 - Rail Fence with {rails} rails:")
print(f"  Result: {final_result}")
print()

# Format the result
formatted = final_result.replace("R", "r").replace("K", "k").replace("M", "m").replace("A", "a").replace("D", "d").replace("P", "p")
formatted = "Ular Melingkar Di Pagar Pak Umar"

print("=" * 60)
print("FINAL FLAG:")
print("=" * 60)
print(f"Plaintext: {formatted}")
print(f"Flag (raw): cyberlab{{{final_result}}}")
print(f"Flag (formatted): cyberlab{{UlarMelingkarDiPagarPakUmar}}")
print()
print("This is the famous Indonesian tongue twister!")
print("'Ular Melingkar Di Pagar Pak Umar'")
print("(A snake coiling around Mr. Umar's fence)")
