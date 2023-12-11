'''
Here are five commonly used algorithms for finding prime numbers:

    1. Trial Division:
    This is a basic algorithm that checks divisibility by all numbers up to the square root of the given number.

    2. Sieve of Eratosthenes:
    An efficient algorithm that finds all primes up to a given limit.

    3. AKS Primality Test:
    A deterministic primality-proving algorithm, although it's not the most practical for large numbers.

    4. Miller-Rabin Primality Test:
    A probabilistic algorithm that is widely used and efficient for large numbers.

    5. Lucas-Lehmer Primality Test (for Mersenne Primes):
    Specifically designed for Mersenne primes, which are primes that can be written in the form 2n−12n−1.
'''
import math
import random

# 1. Trial Division
def is_prime_trial(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2. Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for num in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    for num in range(int(math.sqrt(limit)) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

# 3. AKS Primality Test
# Note: The AKS algorithm is quite complex and not practical for this example.
def is_prime_aks(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Find the smallest r such that the order of n mod r > log2(n)^2
    r = 2
    while True:
        if math.gcd(r, n) > 1:
            return False
        if pow(2, r, n) == 1 or pow(2, r // 2, n) == n - 1:
            break
        r += 1

    # Check for small values of a
    for a in range(2, min(r, n - 1)):
        if math.gcd(a, n) > 1:
            return False
        if pow(a, n, n) != a % n:
            return False

    return True

# 5. Lucas-Lehmer Primality Test (for Mersenne Primes)
# Note: This is specifically for Mersenne primes (2^n - 1).
def is_prime_lucas_lehmer(p):
    if p == 2:
        return True

    s = 4
    m = 2 ** p - 1

    for _ in range(p - 2):
        s = (s * s - 2) % m

    return s == 0

# 4. Miller-Rabin Primality Test
def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Example usage
number_to_check = 37

# 1. Trial Division
print(f"Trial Division: {number_to_check} is prime: {is_prime_trial(number_to_check)}")

# 2. Sieve of Eratosthenes
limit = 50
print(f"Sieve of Eratosthenes (up to {limit}): {sieve_of_eratosthenes(limit)}")

# 3. AKS Primality Test
print(f"AKS Primality Test: {number_to_check} is prime: {is_prime_aks(number_to_check)}")


# 4. Miller-Rabin Primality Test
print(f"Miller-Rabin Primality Test: {number_to_check} is prime: {is_prime_miller_rabin(number_to_check)}")

# 5. Lucas-Lehmer Primality Test (for Mersenne Primes)
mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31]  # Example Mersenne primes
for exponent in mersenne_exponents:
    mersenne_prime = 2 ** exponent - 1
    print(f"Lucas-Lehmer Test for Mersenne Prime {mersenne_prime}: {is_prime_lucas_lehmer(exponent)}")
