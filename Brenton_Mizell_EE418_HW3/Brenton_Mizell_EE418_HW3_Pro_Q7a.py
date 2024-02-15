import math
from itertools import combinations

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a


def main():
    n = int(input("Enter the value of n: "))
    num_equations = int(input("Enter the number of equations: "))

    equations = []
    for _ in range(num_equations):
        x, y = map(int, input("Enter x and y (x^2 ≡ y mod n) separated by space: ").split())
        equations.append((x, y))


        # Calculate gcds to find non-trivial factors
        gcd1 = gcd(x - y, n)
        gcd2 = gcd(x + y, n)

        print(f"Non-trivial factors of n using y's : {y} are gcd1: {gcd1}, gcd2: {gcd2}")

if __name__ == "__main__":
    main()

"""
Output:
    Enter the value of n: 537069139875071
    Enter the number of equations: 1
    Enter x and y (x^2 ≡ y mod n) separated by space: 85975324443166 462436106261
    Non-trivial factors of n using y's : 462436106261 are gcd1: 9876469, gcd2: 54378659
"""