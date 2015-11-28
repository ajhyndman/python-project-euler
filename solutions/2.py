import itertools

# Memoized Function solution.

# memoization list
memofib = [1, 1]

# recursive (but memoized) function declaration
def fibonacci(n):
    if n < 0:
        return undefined
    elif n < len(memofib):
        return memofib[n]
    else:
        memofib.append(fibonacci(n-2) + fibonacci(n-1))
        return memofib[n]


# solution calculation
i = 0
solution = 0
while fibonacci(i) <= 4000000:
    if 0 == fibonacci(i)%2:
        solution += fibonacci(i)
    i += 1


print(solution)





# I discovered generators!

def fibonacci():
    previous, current = 1, 1
    while True:
        yield current
        previous, current = current, previous + current


solution = 0
for x in fibonacci():
    if x >= 4000000:
        break
    elif 0 == x%2:
        solution += x


print(solution)
