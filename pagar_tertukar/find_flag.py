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

def decrypt_rail_fence_permuted(cipher, rails, perm):
    rail_lens = [0] * rails
    row = 0
    dir_down = True
    for _ in cipher:
        rail_lens[row] += 1
        if row == 0:
            dir_down = True
        elif row == rails - 1:
            dir_down = False
        if dir_down:
            row += 1
        else:
            row -= 1
            
    chunks = {}
    current_pos = 0
    for rail_idx in perm:
        length = rail_lens[rail_idx]
        if current_pos + length > len(cipher):
            return None
        chunks[rail_idx] = cipher[current_pos:current_pos+length]
        current_pos += length
        
    result = []
    row, col = 0, 0
    rail_indices = [0] * rails
    dir_down = True
    
    for _ in cipher:
        if rail_indices[row] < len(chunks[row]):
            result.append(chunks[row][rail_indices[row]])
            rail_indices[row] += 1
        else:
            result.append('?')
            
        if row == 0:
            dir_down = True
        elif row == rails - 1:
            dir_down = False
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    return "".join(result)

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"

print("=" * 60)
print("SEARCHING FOR FLAG IN CIPHERTEXT")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print()

# Test all permutations of 2, 3, 4, 5 rails
for rails in range(2, 6):
    print(f"\n--- Testing {rails} Rails (Permuted) ---")
    count = 0
    for perm in itertools.permutations(range(rails)):
        result = decrypt_rail_fence_permuted(ciphertext, rails, perm)
        if result and ("CYBER" in result or "cyber" in result or "LAB" in result or "lab" in result or "Flag" in result or "flag" in result):
            print(f"  *** FOUND: Rails {rails}, Perm {perm}: {result}")
            count += 1
    if count == 0:
        print(f"  No matches found for {rails} rails")

print("\n" + "=" * 60)
print("STANDARD RAIL FENCE (NO PERMUTATION)")
print("=" * 60)
for rails in range(2, 10):
    result = decrypt_rail_fence(ciphertext, rails)
    if "CYBER" in result or "cyber" in result or "LAB" in result or "lab" in result:
        print(f"*** FOUND: Rails {rails}: {result}")
