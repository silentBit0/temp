def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


def extended_euclidean_gcd(a, b):
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while b != 0:
        q = a // b
        r = a % b
        s = s1 - q * s2
        t = t1 - q * t2
        a, b = b, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    return a, s1, t1


def euclidean_mi(a, b):
    og_b = b
    t1, t2 = 1, 0
    while b != 0:
        q = a // b
        r = a % b
        t = t1 - q * t2
        a, b = b, r
        t1, t2 = t2, t
    if a != 1:
        return None
    else:
        return t1 % og_b


def main():
    while True:
        print("\n--- Number Theory Tools ---")
        print("1. Euclidean GCD")
        print("2. Extended Euclidean")
        print("3. Euclidean MI")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 4:
            print("Exiting...")
            break

        if choice not in [1, 2, 3]:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = int(input("Enter first number (a): "))
            b = int(input("Enter second number (b): "))
        except ValueError:
            print("Inputs must be integers.")
            continue

        if choice == 1:
            print(f"GCD of {a} and {b} is {euclidean_gcd(a, b)}")
        elif choice == 2:
            gcd, x, y = extended_euclidean_gcd(a, b)
            print(f"GCD: {gcd}")
            print(f"Equation: {a}*({x}) + {b}*({y}) = {gcd}")
        elif choice == 3:
            mi = euclidean_mi(a, b)
            if mi is None:
                print(f"Modular Inverse does not exist for {a} mod {b} (GCD != 1)")
            else:
                print(f"Modular Inverse of {a} mod {b} is {mi}")


main()
