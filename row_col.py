def row_column_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    
    rows = -(-len(text) // cols)
    text += 'X' * (rows * cols - len(text))

    matrix = [text[i*cols:(i+1)*cols] for i in range(rows)]
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    cipher = ""

    for col in key_order:
        for row in matrix:
            cipher += row[col]

    return cipher

def row_column_decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols
    
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Create empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    idx = 0

    for col in key_order:
        for row in range(rows):
            matrix[row][col] = cipher[idx]
            idx += 1

    # Read row-wise
    plain = ""
    for row in matrix:
        plain += ''.join(row)

    return plain
