def clean(text):
    return "".join(c for c in text.upper() if c.isalpha())


def vigenere_key_extend(keyword, length):
    keyword = clean(keyword)
    return (keyword * (length // len(keyword) + 1))[:length]


def vigenere_encrypt(plaintext, keyword):
    plaintext = clean(plaintext)
    key = vigenere_key_extend(keyword, len(plaintext))

    ciphertext = ""
    for p, k in zip(plaintext, key):
        pi = ord(p) - 65
        ki = ord(k) - 65
        ci = (pi + ki) % 26
        ciphertext += chr(ci + 65)
    return ciphertext, key


def vigenere_decrypt(ciphertext, keyword):
    ciphertext = clean(ciphertext)
    key = vigenere_key_extend(keyword, len(ciphertext))

    plaintext = ""
    for c, k in zip(ciphertext, key):
        ci = ord(c) - 65
        ki = ord(k) - 65
        pi = (ci - ki) % 26
        plaintext += chr(pi + 65)
    return plaintext, key


def main():
    keyword = input("Enter keyword: ")
    plaintext = input("Enter plaintext: ")

    cipher, used_key = vigenere_encrypt(plaintext, keyword)
    print("Generated key:", used_key)
    print("Ciphertext:", cipher)

    decrypted, _ = vigenere_decrypt(cipher, keyword)
    print("Decrypted:", decrypted)


main()
