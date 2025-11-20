import itertools

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

with open("results.txt", "w") as f:
    f.write("RAIL FENCE PERMUTATION RESULTS\n")
    f.write("=" * 80 + "\n")
    f.write(f"Ciphertext: {ciphertext}\n\n")
    
    for rails in range(2, 6):
        f.write(f"\n--- {rails} Rails ---\n")
        for perm in itertools.permutations(range(rails)):
            result = decrypt_rail_fence_permuted(ciphertext, rails, perm)
            if result:
                f.write(f"Perm {perm}: {result}\n")
                if "CYBER" in result or "cyber" in result:
                    f.write(f"  *** POSSIBLE FLAG FOUND ***\n")

print("Results written to results.txt")
print("\nSearching for 'CYBER' or 'cyber' in results...")

# Also print any matches to console
with open("results.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "CYBER" in line or "cyber" in line or "POSSIBLE FLAG" in line:
            # Print context
            start = max(0, i-1)
            end = min(len(lines), i+2)
            for j in range(start, end):
                print(lines[j].rstrip())
            print()
