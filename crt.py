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


def chinese_remainder_theorem():
    try:
        n = int(input("Enter the number of equations (n): "))
    except ValueError:
        print("Invalid input.")
        return

    rem = []
    mod = []

    print("\nEnter inputs for x = a_i mod m_i")
    for i in range(n):
        print(f"\nEquation {i+1}:")
        a = int(input(f"  Enter remainder (a{i+1}): "))
        m = int(input(f"  Enter modulus   (m{i+1}): "))
        rem.append(a)
        mod.append(m)

    M = 1
    for x in mod:
        M *= x

    print(f"\nTotal Product (M) = {M}\n")
    print(f"{'i':<5}{'ai':<8}{'mi':<8}{'Mi':<8}{'yi':<8}{'Term (ai*Mi*yi)':<20}")
    print("-" * 55)

    # x = sum(ai * Mi * yi)
    total_sum = 0

    for i in range(n):
        ai = rem[i]
        mi = mod[i]

        # Mi = M / mi
        Mi = M // mi

        yi = euclidean_mi(Mi, mi)

        term = ai * Mi * yi
        total_sum += term

        print(f"{i+1:<5}{ai:<8}{mi:<8}{Mi:<8}{yi:<8}{term:<20}")

    print("-" * 55)

    # 5. Final Result
    x = total_sum % M

    print(f"\nSummation (before mod M): {total_sum}")
    print(f"Final Calculation: {total_sum} % {M}")
    print(f"x = {x}")


if __name__ == "__main__":
    chinese_remainder_theorem()
