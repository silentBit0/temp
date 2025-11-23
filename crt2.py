def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No inverse for {} mod {}".format(a, m))
    return x % m


def crt_prepare(moduli):
    M = 1
    for m in moduli:
        M *= m
    Mi, inv = [], []
    for m in moduli:
        Mi.append(M // m)
    for i, m in enumerate(moduli):
        inv.append(modinv(Mi[i], m))
    return M, Mi, inv


def to_residues(x, moduli):
    return [x % m for m in moduli]


def crt_reconstruct(residues, moduli, M, Mi, inv):
    total = 0
    for ci, Mi_i, inv_i in zip(residues, Mi, inv):
        total += ci * Mi_i * inv_i
    return total % M


def add_res(a, b, moduli):
    return [(ai + bi) % mi for ai, bi, mi in zip(a, b, moduli)]


def sub_res(a, b, moduli):
    return [(ai - bi) % mi for ai, bi, mi in zip(a, b, moduli)]


def mul_res(a, b, moduli):
    return [(ai * bi) % mi for ai, bi, mi in zip(a, b, moduli)]


def div_res(a, b, moduli):
    res = []
    for ai, bi, mi in zip(a, b, moduli):
        inv = modinv(bi, mi)
        res.append((ai * inv) % mi)
    return res


def main():
    print("Chinese Remainder Theorem Operations")
    k = int(input("Enter number of moduli (k): "))
    moduli = list(
        map(int, input("Enter {} pairwise coprime moduli: ".format(k)).split())
    )
    M, Mi, inv = crt_prepare(moduli)

    while True:
        print("\n------ MENU ------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        ch = input("Enter choice (1-5): ")

        if ch == "5":
            print("Exiting program.")
            break

        A = int(input("Enter A: "))
        B = int(input("Enter B: "))
        a_res = to_residues(A, moduli)
        b_res = to_residues(B, moduli)

        print("\nResidues Representation")
        print("{:<8}{:<20}".format("Number", "Residues"))
        print("-" * 28)
        print("{:<8}{:<20}".format("A", str(a_res)))
        print("{:<8}{:<20}".format("B", str(b_res)))

        if ch == "1":
            c_res = add_res(a_res, b_res, moduli)
            op = "A + B"
        elif ch == "2":
            c_res = sub_res(a_res, b_res, moduli)
            op = "A - B"
        elif ch == "3":
            c_res = mul_res(a_res, b_res, moduli)
            op = "A * B"
        elif ch == "4":
            try:
                c_res = div_res(a_res, b_res, moduli)
                op = "A / B"
            except ValueError as e:
                print("\nDivision not possible:", e)
                continue
        else:
            print("Invalid choice")
            continue

        C = crt_reconstruct(c_res, moduli, M, Mi, inv)

        print("\nOperation:", op)
        print("{:<15}{:<20}".format("Result residues", str(c_res)))
        print(
            "{:<15}{:<20}".format("Reconstructed C", str(C) + " (mod " + str(M) + ")")
        )


if __name__ == "__main__":
    main()
