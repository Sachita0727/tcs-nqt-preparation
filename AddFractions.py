def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def simple(num3, den3):
    g = gcd(num3, den3)
    num3 //= g
    den3 //= g
    return num3, den3

def main():
    num1, den1 = 3, 4
    num2, den2 = 1, 7

    lcm = (den1 * den2) // gcd(den1, den2)

    # answer denominator
    den3 = lcm

    # changing numerators to same denominator and adding
    num3 = num1 * (den3 // den1) + num2 * (den3 // den2)

    # simplify fraction
    num3, den3 = simple(num3, den3)

    print(f"{num1}/{den1} + {num2}/{den2} = {num3}/{den3}")

if __name__ == "__main__":
    main()
