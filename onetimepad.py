import os


def to_bits(s):
    return "".join(f"{ord(c):08b}" for c in s)


def from_bits(bitstring):
    chars = [bitstring[i : i + 8] for i in range(0, len(bitstring), 8)]
    return "".join(chr(int(b, 2)) for b in chars)


def xor_bits(a, b):
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def generate_random_key(length):
    random_bytes = os.urandom(length // 8)
    return "".join(f"{byte:08b}" for byte in random_bytes)


def main():
    plaintext = input("Enter plaintext: ")

    p_bits = to_bits(plaintext)
    print("Plaintext bits:", p_bits)

    key = generate_random_key(len(p_bits))
    print("Key bits:", key)

    cipher = xor_bits(p_bits, key)
    print("Ciphertext bits:", cipher)

    decrypted_bits = xor_bits(cipher, key)
    decrypted = from_bits(decrypted_bits)
    print("Decrypted plaintext:", decrypted)


main()
