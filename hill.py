from sympy import Matrix
from math import gcd


def to_nums(text):
    return [ord(c.upper()) - 65 for c in text if c.isalpha()]


def to_text(nums):
    return "".join(chr(n + 65) for n in nums)


def is_invertible_mod26(K):
    det = int(K.det()) % 26
    return det != 0 and gcd(det, 26) == 1


def hill_encrypt(text, K):
    nums = to_nums(text)
    n = K.rows
    original_len = len(nums)

    while len(nums) % n != 0:
        nums.append(ord("X") - 65)

    cipher = []
    for i in range(0, len(nums), n):
        block = Matrix(nums[i : i + n])
        C = (K * block) % 26
        cipher += list(C)

    pad_cnt = len(nums) - original_len

    return to_text(cipher), pad_cnt


def hill_decrypt(cipher, K):
    nums = to_nums(cipher)
    n = K.rows
    Kinv = K.inv_mod(26)

    plain_nums = []
    for i in range(0, len(nums), n):
        block = Matrix(nums[i : i + n])
        P = (Kinv * block) % 26
        plain_nums += list(P)

    full_plain = to_text(plain_nums)
    cleaned_plain = full_plain.rstrip("X")

    return full_plain, cleaned_plain


def main():
    size = int(input("Matrix size (2 or 3): "))

    key_string = input(f"Enter a {size*size}-letter key (row-wise): ")

    vals = to_nums(key_string)
    K = Matrix(size, size, vals)
    K = Matrix(size, size, to_nums(key_string))
    if not is_invertible_mod26(K):
        print("Error: Key matrix is NOT invertible modulo 26. Choose another matrix.")
        return

    plaintext = input("Enter plaintext: ")

    ciphertext, pad_count = hill_encrypt(plaintext, K)
    print("Encrypted (with padding):", ciphertext)
    if pad_count > 0:
        print(f"Padding applied: {pad_count} 'X' character(s)")

    decrypted_with_x, decrypted_clean = hill_decrypt(ciphertext, K)


main()
