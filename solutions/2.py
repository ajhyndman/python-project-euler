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
