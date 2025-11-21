def caesar_cipher(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def main():
    plaintext = input("Enter plaintext: ")
    k = int(input("Enter key (number): "))

    ciphertext = caesar_cipher(plaintext, k)
    print("Encrypted text:", ciphertext)


main()
