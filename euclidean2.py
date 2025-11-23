def basic_euclidean(a, b):
    print("\nBasic Euclidean Algorithm for GCD")
    print("{:<5}{:<8}{:<8}{:<8}".format("q", "r1", "r2", "r"))
    print("-" * 30)
    r1, r2 = a, b
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        print("{:<5}{:<8}{:<8}{:<8}".format(q, r1, r2, r))
        r1, r2 = r2, r
    print("-" * 30)
    print("{:<5}{:<8}{:<8}{:<8}".format("-", r1, r2, "-"))
    print("After last shift → GCD =", r1)


def extended_euclidean(a, b):
    print("\nExtended Euclidean Algorithm for GCD and (s, t) pair")
    print(
        "{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            "q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"
        )
    )
    print("-" * 65)
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - s2 * q
        t = t1 - t2 * q
        print(
            "{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
                q, r1, r2, r, s1, s2, s, t1, t2, t
            )
        )
        r1, r2, s1, s2, t1, t2 = r2, r, s2, s, t2, t
    print("-" * 65)
    print(
        "{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            "-", r1, r2, "-", s1, s2, "-", t1, t2, "-"
        )
    )
    print("After last shift → GCD = {}, s = {}, t = {}".format(r1, s1, t1))


def multiplicative_inverse(a, m):
    print("\nEuclidean Algorithm for GCD and MI")
    print(
        "{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            "q", "r1", "r2", "r", "t1", "t2", "t"
        )
    )
    print("-" * 50)
    r1, r2 = m, a
    t1, t2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - t2 * q
        print("{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(q, r1, r2, r, t1, t2, t))
        r1, r2, t1, t2 = r2, r, t2, t

    if r1 != 1:
        print("-" * 50)
        print("{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format("-", r1, r2, "-", t1, t2, t))
        print("No multiplicative inverse exists.")
    else:
        mi = t1 % m
        print("-" * 50)
        print(
            "{:<5}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format("-", r1, r2, "-", t1, t2, "-")
        )
        print("After last shift → GCD = {}, MI = {}".format(r1, mi))


def main():
    while True:
        print("\n------ MENU ------")
        print("1. Basic Euclidean Algorithm for GCD")
        print("2. Extended Euclidean Algorithm for GCD and (s,t)")
        print("3. Multiplicative Inverse using Euclidean Algorithm")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            basic_euclidean(a, b)
        elif choice == "2":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            extended_euclidean(a, b)
        elif choice == "3":
            a = int(input("Enter number (a): "))
            m = int(input("Enter modulus (m): "))
            multiplicative_inverse(a, m)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1-4.")


if __name__ == "__main__":
    main()
