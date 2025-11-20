ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "DUIT"

print("=" * 60)
print("COMPREHENSIVE DUIT KEY TESTING")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}")
print()

# Test 1: DUIT as position values (D=3, U=20, I=8, T=19)
print("--- DUIT as position values (0-indexed) ---")
positions = [ord(c.upper()) - ord('A') for c in key]
print(f"D={positions[0]}, U={positions[1]}, I={positions[2]}, T={positions[3]}")
print(f"Positions: {positions}")

# Extract characters at these positions cyclically
result = ""
for i in range(len(ciphertext)):
    pos = positions[i % len(positions)]
    if pos < len(ciphertext):
        result += ciphertext[pos]
print(f"Cyclic extraction: {result}")
print()

# Test 2: XOR with DUIT
print("--- XOR with DUIT ---")
result = ""
for i, c in enumerate(ciphertext):
    key_char = key[i % len(key)]
    xor_result = chr(ord(c) ^ ord(key_char))
    result += xor_result
print(f"XOR result: {result}")
print(f"XOR result (printable check): {repr(result)}")
print()

# Test 3: Subtract DUIT values from ciphertext
print("--- Subtract DUIT values (Caesar-like) ---")
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
print(f"Subtraction result: {result}")
print()

# Test 4: Add DUIT values
print("--- Add DUIT values ---")
result = ""
for i, c in enumerate(ciphertext):
    if c.isalpha():
        key_val = ord(key[i % len(key)].upper()) - ord('A')
        if c.isupper():
            new_char = chr((ord(c) - ord('A') + key_val) % 26 + ord('A'))
        else:
            new_char = chr((ord(c) - ord('a') + key_val) % 26 + ord('a'))
        result += new_char
    else:
        result += c
print(f"Addition result: {result}")
print()

# Test 5: DUIT determines which characters to extract
print("--- Extract characters at DUIT-indicated positions ---")
# D=3, U=20, I=8, T=19 - extract every 3rd, 20th, 8th, 19th char
for step in positions:
    if step > 0 and step < len(ciphertext):
        result = ciphertext[::step]
        print(f"Every {step}th character: {result}")
print()

# Test 6: Reverse operations
print("--- Reverse ciphertext + DUIT operations ---")
rev_cipher = ciphertext[::-1]
print(f"Reversed: {rev_cipher}")

# Vigenere on reversed
result = ""
for i, c in enumerate(rev_cipher):
    if c.isalpha():
        key_val = ord(key[i % len(key)].upper()) - ord('A')
        if c.isupper():
            new_char = chr((ord(c) - ord('A') - key_val + 26) % 26 + ord('A'))
        else:
            new_char = chr((ord(c) - ord('a') - key_val + 26) % 26 + ord('a'))
        result += new_char
    else:
        result += c
print(f"Reversed + Vigenere decrypt: {result}")

# Write all results to file
with open("duit_all_results.txt", "w", encoding="utf-8") as f:
    f.write("COMPREHENSIVE DUIT KEY TESTING RESULTS\n")
    f.write("=" * 60 + "\n")
    f.write(f"Ciphertext: {ciphertext}\n")
    f.write(f"Key: {key}\n\n")
    
    f.write("Subtraction result (Vigenere): " + result + "\n")
    
print("\nAll results written to duit_all_results.txt")
print("\nChecking for readable patterns...")

# Check the subtraction result more carefully
print(f"\nVigenere decrypt with DUIT: {result}")
if "flag" in result.lower() or "cyber" in result.lower():
    print("*** POSSIBLE FLAG FOUND ***")
