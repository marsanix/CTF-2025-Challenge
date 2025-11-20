ciphertext = "XfzTPfmbdXokxuiFqEqTSEZKjji"

print("SIMPLE EXTRACTION PATTERNS")
print("=" * 60)
print(f"Ciphertext: {ciphertext}")
print(f"Length: {len(ciphertext)}")
print()

# Try reading every nth character
print("--- Reading every Nth character ---")
for n in range(2, 10):
    result = ciphertext[::n]
    print(f"Every {n}th char: {result}")
    if len(result) >= 5:
        result2 = ciphertext[1::n]
        print(f"Every {n}th char (offset 1): {result2}")
print()

# Try alternating uppercase/lowercase
print("--- Uppercase only ---")
uppercase = ''.join([c for c in ciphertext if c.isupper()])
print(f"Uppercase: {uppercase}")

print("\n--- Lowercase only ---")
lowercase = ''.join([c for c in ciphertext if c.islower()])
print(f"Lowercase: {lowercase}")
print()

# Try reading positions based on PAGAR (P=15, A=0, G=6, A=0, R=17)
print("--- Reading positions based on 'PAGAR' letter values ---")
key = "PAGAR"
positions = [ord(c.upper()) - ord('A') for c in key]
print(f"PAGAR positions: {positions}")

# Try extracting characters at those positions
result = ""
for i, pos in enumerate(positions):
    if pos < len(ciphertext):
        result += ciphertext[pos]
print(f"Characters at PAGAR positions: {result}")
print()

# Try splitting into groups of 5 (length of PAGAR)
print("--- Splitting into groups of 5 ---")
groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
for i, g in enumerate(groups):
    print(f"Group {i}: {g}")
print()

# Try reading first char of each group
first_chars = ''.join([g[0] if len(g) > 0 else '' for g in groups])
print(f"First char of each group: {first_chars}")

# Try reading diagonally
print("\n--- Reading diagonally (5 columns) ---")
cols = 5
rows = len(ciphertext) // cols + (1 if len(ciphertext) % cols else 0)
matrix = []
idx = 0
for r in range(rows):
    row = []
    for c in range(cols):
        if idx < len(ciphertext):
            row.append(ciphertext[idx])
            idx += 1
        else:
            row.append('')
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(' '.join(row))

# Read diagonals
print("\nDiagonals:")
for start_col in range(cols):
    diag = ""
    r, c = 0, start_col
    while r < rows and c < cols:
        if c < len(matrix[r]):
            diag += matrix[r][c]
        r += 1
        c += 1
    print(f"Diagonal from col {start_col}: {diag}")
