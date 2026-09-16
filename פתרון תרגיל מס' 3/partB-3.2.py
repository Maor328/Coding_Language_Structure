# Helper to check if a number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Prime numbers generator
def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Example usage:
primes = prime_generator()
print(next(primes))
print(next(primes))