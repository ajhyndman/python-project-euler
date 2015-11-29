from itertools import islice

from utilities.generators import primes


print(list(islice(primes(), 10000, 10001)))
