#a)
"""
-find if there is any combination of y's which will result in a perfect square
-if there is a combo that results in a y^2 find the product of the correlating x's mod n
-find the nontrivial factors using GCD (x-y,n) and GCD(x+y,n) using the x's mod n and y^2
"""

#b)
import math
from itertools import combinations

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def is_perfect_square(n):
    """Check if n is a perfect square."""
    return n == math.isqrt(n) ** 2

def main():
    n = int(input("Enter the value of n: "))
    num_equations = int(input("Enter the number of equations: "))

    equations = []
    for _ in range(num_equations):
        x, y = map(int, input("Enter x and y (x^2 ≡ y mod n) separated by space: ").split())
        equations.append((x, y))

    # Check combinations of all lengths
    for r in range(2, num_equations + 1):
        for combo in combinations(equations, r):
            xs, ys = zip(*combo)
            product_y = math.prod(ys)

            if is_perfect_square(product_y):
                x_product_mod_n = math.prod(xs) % n
                square_root_y = math.isqrt(product_y)

                # Calculate gcds to find non-trivial factors
                gcd1 = gcd(x_product_mod_n - square_root_y, n)
                gcd2 = gcd(x_product_mod_n + square_root_y, n)

                print(f"Non-trivial factors of n using y's : {ys} are gcd1: {gcd1}, gcd2: {gcd2}")

if __name__ == "__main__":
    main()
"""
Output:
    Enter the value of n: 2288233
    Enter the number of equations: 4
    Enter x and y (x^2 ≡ y mod n) separated by space: 880525 2
    Enter x and y (x^2 ≡ y mod n) separated by space: 2057202 3
    Enter x and y (x^2 ≡ y mod n) separated by space: 648581 6
    Enter x and y (x^2 ≡ y mod n) separated by space: 668676 77
    Non-trivial factors of n using y's : (2, 3, 6) are gcd1: 1871, gcd2: 1223
"""