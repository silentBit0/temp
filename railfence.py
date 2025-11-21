def clean_text(text):
    return "".join(c for c in text.upper() if c.isalpha())


def rail_fence_encrypt(plaintext, rails):
    plaintext = clean_text(plaintext)
    if rails <= 1 or len(plaintext) <= 1:
        return plaintext

    rows = [""] * rails
    row = 0
    step = 1

    for ch in plaintext:
        rows[row] += ch
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return "".join(rows)


def rail_fence_decrypt(ciphertext, rails):
    ciphertext = clean_text(ciphertext)
    if rails <= 1 or len(ciphertext) <= 1:
        return ciphertext

    n = len(ciphertext)

    # 1. Determine which rail each character position belongs to (zig-zag pattern)
    rail_for_pos = [0] * n
    row = 0
    step = 1
    for i in range(n):
        rail_for_pos[i] = row
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    # 2. Count how many characters go to each rail
    counts = [rail_for_pos.count(r) for r in range(rails)]

    # 3. Slice ciphertext into pieces for each rail
    rails_text = []
    idx = 0
    for c in counts:
        rails_text.append(ciphertext[idx : idx + c])
        idx += c

    # 4. Rebuild plaintext by walking the zig-zag and taking chars from each rail
    rail_indices = [0] * rails
    plaintext_chars = []
    for r in rail_for_pos:
        plaintext_chars.append(rails_text[r][rail_indices[r]])
        rail_indices[r] += 1

    return "".join(plaintext_chars)


def main():
    choice = input("Encrypt(E) or Decrypt(D): ").strip().upper()
    rails = int(input("Number of rails: ").strip())

    if choice == "E":
        plaintext = input("Enter plaintext: ")
        cipher = rail_fence_encrypt(plaintext, rails)
        print("Ciphertext:", cipher)
    elif choice == "D":
        ciphertext = input("Enter ciphertext: ")
        plain = rail_fence_decrypt(ciphertext, rails)
        print("Decrypted plaintext:", plain)
    else:
        print("Invalid choice.")


main()
