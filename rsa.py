from math import gcd


def rsa(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    for d in range(2, phi):
        if (d * e) % phi == 1:
            break
    pub_key = (e, n)
    pvt_key = (d, n)
    return pub_key, pvt_key


def encrypt(plain_txt, pub_key):
    e, n = pub_key
    cipher = []

    for ch in plain_txt:
        c = pow(ord(ch), e, n)
        cipher.append(c)

    return cipher


def decrypt(cipher_txt, pvt_key):
    d, n = pvt_key
    plain_txt = ""

    for c in cipher_txt:
        ch = chr(pow(c, d, n))
        plain_txt += ch

    return plain_txt


def main():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    pub_key, pvt_key = rsa(int(p), int(q))

    print("Generated Public Key: ", pub_key)
    print("Generated Private Key: ", pvt_key)

    plain_txt = input("Enter message/plaintxt to encrypt: ")

    cipher_txt = encrypt(plain_txt, pub_key)
    print("Encrypted message: ", cipher_txt)
    decrypted_txt = decrypt(cipher_txt, pvt_key)
    print("Decrypted message: ", decrypted_txt)


main()
