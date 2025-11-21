def main():
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice's private key a: "))
    b = int(input("Enter Bob's private key b: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Alice's Public Key A:", A)
    print("Bob's Public Key B:", B)

    secret_A = pow(B, a, p)
    secret_B = pow(A, b, p)

    print("Alice Computes Shared Secret:", secret_A)
    print("Bob Computes Shared Secret:  ", secret_B)

    if secret_A == secret_B:
        print("\nSecure shared key established:", secret_A)
    else:
        print("\nError: Secrets do not match (should never happen).")


main()
