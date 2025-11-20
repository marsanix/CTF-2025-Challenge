import math
import itertools

def decrypt_rail_fence(cipher, rails):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(rails)]
    
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
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
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
    return("".join(result))

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
            # Vigenere usually uses same case for key, but let's assume case-insensitive key or handle case matching
            # Standard Vigenere: (C - K) mod 26
            # We need to handle the key case. Let's assume key is uppercase PAGAR
            k = key_as_int[i % key_length]
            if 97 <= k <= 122:
                k -= 32 # Make key uppercase for calculation
            
            value = (ciphertext_int[i] - 97 - (k - 65) + 26) % 26
            decrypted_text.append(chr(value + 97))
        else:
            decrypted_text.append(chr(ciphertext_int[i]))
            
    return "".join(decrypted_text)

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "PAGAR"

print(f"Ciphertext: {ciphertext}")
print("-" * 20)

print(f"Vigenere with key {key}: {decrypt_vigenere(ciphertext, key)}")

def decrypt_caesar(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            result += chr((ord(char) - start - shift + 26) % 26 + start)
        else:
            result += char
    return result

print("-" * 20)
print("Caesar Cipher Results:")
for i in range(26):
    print(f"Shift {i}: {decrypt_caesar(ciphertext, i)}")

print("-" * 20)
print("Rail Fence on Reversed Ciphertext:")
reversed_cipher = ciphertext[::-1]
for i in range(2, len(reversed_cipher)):
    try:
        decrypted = decrypt_rail_fence(reversed_cipher, i)
        print(f"Rails {i} (Reversed): {decrypted}")
    except Exception as e:
        print(f"Error with {i} rails: {e}")

def decrypt_columnar(ciphertext, key):
    msg_len = len(ciphertext)
    msg_lst = list(ciphertext)
    col_len = len(key)
    row_len = math.ceil(msg_len / col_len)
    
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row_len):
        dec_cipher += [[None] * col_len]
    
    k_idx = 0
    msg_idx = 0
    for k in key_lst:
        # Find the index of the key character in the original key
        # Handle duplicate characters in key
        curr_idx = key.find(k)
        # If duplicate, we need to find the next occurrence
        # But standard columnar usually uses a stable sort or unique keys.
        # Let's assume standard behavior: if 'A' appears twice, the first 'A' in sorted list corresponds to first 'A' in key.
        # To handle this properly, let's create a list of (char, original_index)
        pass

    # Let's implement a simpler version that handles duplicates by index
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    # Calculate number of characters in each column
    # Some columns might be short if msg_len % col_len != 0
    # The last (msg_len % col_len) columns have row_len characters?
    # No, the first (msg_len % col_len) columns have row_len characters, others have row_len - 1?
    # It depends on how it was filled. Usually row by row.
    
    # Let's use a library-like approach or a robust implementation
    
    num_rows = msg_len // col_len
    num_extra = msg_len % col_len
    
    # Determine the length of each column
    col_lengths = [num_rows + (1 if i < num_extra else 0) for i in range(col_len)]
    
    # But we need to map this to the sorted key indices
    # The columns are read in the order of the sorted key
    
    # Reconstruct the matrix
    matrix = [['' for _ in range(col_len)] for _ in range(num_rows + 1)]
    
    current_idx = 0
    for k_i in key_indices:
        length = col_lengths[k_i]
        for r in range(length):
            if current_idx < msg_len:
                matrix[r][k_i] = ciphertext[current_idx]
                current_idx += 1
                
    result = ""
    for r in range(num_rows + 1):
        for c in range(col_len):
            if matrix[r][c] != '':
                result += matrix[r][c]
    return result

import itertools

def decrypt_rail_fence_permuted(cipher, rails):
    # Calculate the length of each rail
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
            
    # Generate all permutations of rail order
    for perm in itertools.permutations(range(rails)):
        # Reconstruct the rails based on the permutation
        current_rails = [''] * rails
        idx = 0
        
        # The cipher text is formed by reading rails in some order.
        # If standard, it's 0, 1, 2...
        # If permuted, we assume the ciphertext segments correspond to rails in the permuted order?
        # OR the rails were read in the permuted order to form the ciphertext.
        # So we split the ciphertext into chunks based on rail lengths, but which length corresponds to which segment?
        # The lengths are fixed by the zig-zag pattern.
        # If the reading order was permuted, then the first segment of ciphertext corresponds to rail perm[0], etc.
        
        # We need to know which rail has which length.
        # rail_lens[i] is the length of rail i (0-indexed from top).
        
        # If reading order was perm[0], perm[1]...
        # Then first chunk of ciphertext is rail perm[0], length rail_lens[perm[0]].
        
        chunks = {}
        current_pos = 0
        possible = True
        for rail_idx in perm:
            length = rail_lens[rail_idx]
            if current_pos + length > len(cipher):
                possible = False
                break
            chunks[rail_idx] = cipher[current_pos:current_pos+length]
            current_pos += length
            
        if not possible:
            continue
            
        # Now reconstruct the message using the zig-zag pattern
        result = []
        row, col = 0, 0
        rail_indices = [0] * rails
        dir_down = True
        
        for _ in cipher:
            # We need to pick the character from the correct rail
            if rail_indices[row] < len(chunks[row]):
                result.append(chunks[row][rail_indices[row]])
                rail_indices[row] += 1
            else:
                result.append('?') # Should not happen
                
            if row == 0:
                dir_down = True
            elif row == rails - 1:
                dir_down = False
            
            if dir_down:
                row += 1
            else:
                row -= 1
        
        decoded = "".join(result)
        print(f"Rails {rails}, Perm {perm}: {decoded}")

print("-" * 20)
print("Pair Swapping Results:")
def pair_swap(text):
    result = list(text)
    for i in range(0, len(text) - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)

print(f"Pair Swap: {pair_swap(ciphertext)}")

# Also try swapping pairs of words? No, it's a single string.
# Try swapping halves again but with different split points?
# Try swapping every 3 chars?
def chunk_swap(text, chunk_size):
    result = ""
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        result += chunk[::-1]
    return result

def decrypt_atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

print("-" * 20)
print(f"Atbash: {decrypt_atbash(ciphertext)}")

print("-" * 20)
print("Additional Vigenere Keys:")
keys = ["TERTUKAR", "PAGARTERTUKAR", "TUKAR", "SWAP", "REVERSE", "RAIL", "FENCE", "PAGAR"]
for k in keys:
    print(f"Key {k}: {decrypt_vigenere(ciphertext, k)}")

print("-" * 20)
print("Vigenere + Rail Fence Combination:")

base_key = "PAGAR"
rotated_keys = [base_key[i:] + base_key[:i] for i in range(len(base_key))]

for key in rotated_keys:
    print(f"--- Trying Vigenere Key: {key} ---")
    vig_decrypted = decrypt_vigenere(ciphertext, key)
    print(f"Vigenere Output: {vig_decrypted}")
    
    # Try Rail Fence on this output
    for r in range(2, 6):
        try:
            rf_decrypted = decrypt_rail_fence(vig_decrypted, r)
            print(f"  + Rail Fence {r}: {rf_decrypted}")
        except:
            pass
            
    # Try Rail Fence on Reversed Vigenere Output
    rev_vig = vig_decrypted[::-1]
    for r in range(2, 6):
        try:
            rf_decrypted = decrypt_rail_fence(rev_vig, r)
            print(f"  + Rail Fence {r} (Reversed): {rf_decrypted}")
        except:
            pass
            
print("-" * 20)
print("Permuted Rail Fence Results (5 rails, filtered):")
# We need to modify the function to return the result or just call it
# But the function prints. Let's modify the function or just copy-paste logic for 5 rails
# Actually, let's just call it and filter stdout? No, that's hard.
# Let's redefine the function to filter
def decrypt_rail_fence_permuted_filtered(cipher, rails, filter_str):
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
            
    for perm in itertools.permutations(range(rails)):
        chunks = {}
        current_pos = 0
        possible = True
        for rail_idx in perm:
            length = rail_lens[rail_idx]
            if current_pos + length > len(cipher):
                possible = False
                break
            chunks[rail_idx] = cipher[current_pos:current_pos+length]
            current_pos += length
            
        if not possible:
            continue
            
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
        
        decoded = "".join(result)
        if filter_str in decoded:
            print(f"Rails {rails}, Perm {perm}: {decoded}")

def decrypt_scytale(text, key):
    # Scytale is just reading every key-th character?
    # Or reading columns of height 'key'?
    # If we wrap text around a cylinder of diameter 'd' (circumference),
    # we write in rows of length 'd'? No, we write along the strip (rows) and read along the cylinder (cols)?
    # Usually: Write in rows of width K, read columns. (Same as Columnar with key 0,1,2...)
    # Or: Write in columns of height K, read rows.
    
    sz = len(text)
    cols = math.ceil(sz / key)
    # Write in rows of length 'cols', read columns?
    # Let's try both standard Columnar (key=0..k-1) and Transpose.
    
    # Implementation 1: Read every k-th char
    res1 = [''] * sz
    idx = 0
    for i in range(key):
        for j in range(i, sz, key):
            res1[j] = text[idx]
            idx += 1
    return "".join(res1)

print("-" * 20)
print("Scytale Results:")
for i in range(2, 10):
    print(f"Scytale {i}: {decrypt_scytale(ciphertext, i)}")

print("-" * 20)
print("Permuted Rail Fence Results (2-4 rails, verbose):")
for r in range(2, 5):
    decrypt_rail_fence_permuted_filtered(ciphertext, r, "") # Empty filter to print all

print("-" * 20)
print("Permuted Rail Fence Results (5 rails, filtered extended):")
decrypt_rail_fence_permuted_filtered(ciphertext, 5, "CYBER")
decrypt_rail_fence_permuted_filtered(ciphertext, 5, "LAB")
decrypt_rail_fence_permuted_filtered(ciphertext, 5, "flag")
decrypt_rail_fence_permuted_filtered(ciphertext, 5, "CTF")
decrypt_rail_fence_permuted_filtered(ciphertext, 5, "Xfz")
