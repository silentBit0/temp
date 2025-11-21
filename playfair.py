import string


def generate_key_square(key):
    key = key.upper().replace("J", "I")
    key = "".join(c for c in key if c.isalpha())

    used = set()
    square = []

    for c in key:
        if c not in used:
            used.add(c)
            square.append(c)

    for c in string.ascii_uppercase:
        if c == "J":
            continue
        if c not in used:
            used.add(c)
            square.append(c)

    return [square[i : i + 5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == "J":
        ch = "I"
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None, None


def prepare_plaintext(text):
    text = text.upper().replace(" ", "")
    text = text.replace("J", "I")
    result = []
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
        else:
            result.append(a)
            result.append("X")
            break
        if a == b:
            result.append(a)
            result.append("X")
            i += 1
        else:
            result.append(a)
            result.append(b)
            i += 2
    return result


def playfair_encrypt(digraphs, matrix):
    ciphertext = ""
    for i in range(0, len(digraphs), 2):
        a = digraphs[i]
        b = digraphs[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5]
            ciphertext += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1]
            ciphertext += matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]
    return ciphertext


def playfair_decrypt(cipher, matrix):
    plaintext = ""

    for i in range(0, len(cipher), 2):
        a = cipher[i]
        b = cipher[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


def main():
    key = input("Enter key: ")
    plaintext = input("Enter plaintext: ")

    matrix = generate_key_square(key)
    print("\nKey Square:")
    for row in matrix:
        print(" ".join(row))

    digraphs = prepare_plaintext(plaintext)
    print("\nPrepared digraphs:", digraphs)

    cipher = playfair_encrypt(digraphs, matrix)
    print("Ciphertext:", cipher)

    decrypted = playfair_decrypt(cipher, matrix)
    print("Decrypted (raw):", decrypted)


main()
