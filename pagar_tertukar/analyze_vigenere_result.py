import itertools

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

vigenere_result = "UlrAMleiaDgruaaMnKiAPKRRgpa"
target = "UlarMelingkarDiPagarPakUmar"

print("=" * 60)
print("SECOND-STAGE DECRYPTION ANALYSIS")
print("=" * 60)
print(f"Vigenere Result: {vigenere_result}")
print(f"Target Text:     {target}")
print(f"Length: {len(vigenere_result)}")
print()

# Compare character by character
print("Character comparison:")
for i, (v, t) in enumerate(zip(vigenere_result, target)):
    match = "✓" if v.lower() == t.lower() else "✗"
    print(f"{i:2d}: {v} vs {t} {match}")
print()

# Check if it's an anagram
from collections import Counter
v_counter = Counter(vigenere_result.lower())
t_counter = Counter(target.lower())
print(f"Is anagram? {v_counter == t_counter}")
print()

# Try Rail Fence on Vigenere result
print("--- Rail Fence on Vigenere Result ---")
for rails in range(2, 10):
    result = decrypt_rail_fence(vigenere_result, rails)
    print(f"Rails {rails}: {result}")
    if "ular" in result.lower() and "melingkar" in result.lower():
        print(f"  *** POSSIBLE MATCH ***")
print()

# Try simple transpositions
print("--- Simple Transpositions ---")
print(f"Reversed: {vigenere_result[::-1]}")

# Try swapping pairs
result = list(vigenere_result)
for i in range(0, len(result) - 1, 2):
    result[i], result[i+1] = result[i+1], result[i]
print(f"Pair swap: {''.join(result)}")

# Try reading every other character
even_chars = vigenere_result[::2]
odd_chars = vigenere_result[1::2]
print(f"Even positions: {even_chars}")
print(f"Odd positions:  {odd_chars}")
print(f"Odd + Even:     {odd_chars + even_chars}")
