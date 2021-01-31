"""

Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600,851,475,143?

"""

from math import ceil

# Returns True if n is prime, False otherwise
def is_prime(n):
    # All even numbers except 2 are NOT prime
    if n >= 2 and n % 2 == 0:
        return False

    # Corner cases
    if n > 1 and n <= 3:
        return True

    for i in range(2, int(n/2)):
        if n % i == 0:
            return False

    return True

# Returns an array of the factors of the given number n
def factors(n):
    factors = [1]

    for i in range(2, ceil(n/2) + 1):
        if n % i == 0:
            factors.append(i)

    return factors

# Returns an array of the prime factors of the given number n
def prime_factors(n):
    prime_factors = []

    for i in factors(n):
        if is_prime(i):
            prime_factors.append(i)

    return prime_factors

print("Largest prime factor of 600,851,475,143: " +
    str(max(prime_factors(600851475143))))
