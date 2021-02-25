import math

# Eratosthene's sieve to get primes
def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve_without_nulls = set([x for x in sieve if x != 0])
    return set(sieve_without_nulls)

# Mersenne numbers
def mersen_numbers(n):
    return set([2 ** i - 1 for i in range(2, int(math.log(n + 1, 2)) + 1)])


print("Enter n:")
n = input()
if n.isdigit():
    n = int(n)
    result = list(eratosthenes(n).intersection(mersen_numbers(n))) # Mersenne primes
    print("Mersen primes less than {}:".format(n), sorted(result))
else:
    print("You've entered not natural number")
