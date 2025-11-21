import os


def text_to_bits(text):
    return "".join(f"{ord(c):08b}" for c in text)


def bits_to_text(bits):
    chars = [bits[i : i + 8] for i in range(0, len(bits), 8)]
    return "".join(chr(int(b, 2)) for b in chars)


def xor_bits(a, b):
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def vernam_encrypt(plaintext):
    p_bits = text_to_bits(plaintext)
    key = os.urandom(len(plaintext))
    key_bits = "".join(f"{byte:08b}" for byte in key)

    cipher_bits = xor_bits(p_bits, key_bits)
    return cipher_bits, key_bits


def vernam_decrypt(cipher_bits, key_bits):
    p_bits = xor_bits(cipher_bits, key_bits)
    return bits_to_text(p_bits)


def main():
    plaintext = input("Enter plaintext: ")

    cipher_bits, key_bits = vernam_encrypt(plaintext)
    print("Plaintext bits :", text_to_bits(plaintext))
    print("Key bits       :", key_bits)
    print("Cipher bits    :", cipher_bits)

    decrypted = vernam_decrypt(cipher_bits, key_bits)
    print("Decrypted text :", decrypted)


main()
