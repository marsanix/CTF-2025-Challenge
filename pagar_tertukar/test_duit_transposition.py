import math

def decrypt_columnar(ciphertext, key):
    msg_len = len(ciphertext)
    col_len = len(key)
    
    # Create key indices sorted alphabetically
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    num_rows = msg_len // col_len
    num_extra = msg_len % col_len
    
    # Determine the length of each column
    col_lengths = [num_rows + (1 if i < num_extra else 0) for i in range(col_len)]
    
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

ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"
key = "DUIT"

print("=" * 60)
print("TESTING DUIT WITH COLUMNAR TRANSPOSITION AND RAIL FENCE")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print()

print("--- Columnar Transposition with DUIT ---")
result = decrypt_columnar(ciphertext, key)
print(f"Result: {result}")
print()

print("--- Rail Fence (2-6 rails) on Columnar result ---")
for rails in range(2, 7):
    rf_result = decrypt_rail_fence(result, rails)
    print(f"Rails {rails}: {rf_result}")
print()

print("--- Columnar on Rail Fence results ---")
for rails in range(2, 7):
    rf_result = decrypt_rail_fence(ciphertext, rails)
    col_result = decrypt_columnar(rf_result, key)
    print(f"Rails {rails} -> Columnar: {col_result}")
