from itertools import count





# FIBONACCI GENERATOR

def fibonacci():
    previous, current = 1, 1
    while True:
        yield current
        previous, current = current, previous + current





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
