import math
import random

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b  # Use Euclidean algorithm for finding GCD
    return a

def pollards_rho(n):
    """Pollard's Rho Algorithm for integer factorization."""
    if n % 2 == 0:  # Check if n is even
        return 2  # 2 is a factor
    
    # Initialize x, y, and c for the algorithm
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1  # Initialize d to 1 (gcd of x - y and n)

    # Iterate until a non-trivial divisor is found
    while d == 1:
        x = (x**2 + c) % n  # Update x
        y = (y**2 + c) % n  # Update y twice as fast
        y = (y**2 + c) % n
        d = gcd(abs(x - y), n)  # Compute GCD of |x - y| and n

        if d == n:  # If d equals n, retry with different values
            return pollards_rho(n)
    
    return d  # Return the non-trivial divisor

def find_xy(n):
    """Find x and y such that x^2 ≡ y^2 mod n and x ≠ ±y mod n."""
    factor = pollards_rho(n)  # Find a non-trivial factor of n
    x = math.sqrt(factor)  # Compute square root of the factor
    y = math.sqrt(n // factor)  # Compute square root of n divided by the factor
    return int(x), int(y)

# Main execution
n = 985739879 * 1388749507
x, y = find_xy(n)
print(f"x: {x}, y: {y}")
