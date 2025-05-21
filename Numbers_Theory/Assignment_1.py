#Question 1
"""
1. Write a program in Python or Java to find whether a given integer is a prime number.
"""


def is_prime(n):
    if n <= 1:
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2 


num = int(input("Enter an integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



#Question 2
"""
2. Write a program in Python or Java to generate the prime numbers within the limit of an integer
200.
"""

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]  

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

primes = sieve_of_eratosthenes(200)
print("Prime numbers up to 200 are:")
print(primes)
