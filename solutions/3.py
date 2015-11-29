from itertools import count
from functools import reduce





# PRIME NUMBER GENERATOR

def primes():

    # as we discover primes, record them internally
    memo = [2]
    yield 2

    # count up from 3
    for n in count(3, 1):
        is_prime = True

        # work out if the number is prime
        for prime in memo:
            if 0 == n%prime:
                is_prime = False
                break

        # yield it if prime
        if is_prime:
            memo.append(n)
            yield n





# find the factors of the sample number

#factors = []
#sample = 13195
#
#for prime in primes():
#    if reduce(lambda x, y: x*y, factors, 1) == sample:
#        break
#    elif 0 == sample%prime:
#        factors.append(prime)
#
#print("The prime factors of 13195 are:", factors)





# SOLVE PROBLEM 3!

factors = []
number = 600851475143

for prime in primes():
    if reduce(lambda x, y: x*y, factors, 1) == number:
        break
    elif 0 == number%prime:
        factors.append(prime)

print("The prime factors of 600851475143 are:", factors)

largest_factor = max(factors)

print("The largest prime factor of 600851475143 is:", largest_factor)
