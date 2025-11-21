import string
import random


def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))


def encrypt(plaintext, key):
    ciphertext = []
    for ch in plaintext:
        if ch.upper() in key:
            mapped = key[ch.upper()]
            ciphertext.append(mapped if ch.isupper() else mapped.lower())
        else:
            ciphertext.append(ch)
    return "".join(ciphertext)


def main():
    print("1. Generate random key")
    print("2. Enter your own 26-letter key")
    choice = input("Choose: ")

    if choice == "1":
        key = generate_key()
    else:
        custom = input("Enter 26-letter key: ").upper()
        if len(custom) != 26 or len(set(custom)) != 26:
            print("Invalid key. Must contain 26 unique letters.")
            return
        key = dict(zip(string.ascii_uppercase, custom))

    print("Key:", key)

    plaintext = input("Enter plaintext: ")
    print("Ciphertext: ", encrypt(plaintext, key))


main()
