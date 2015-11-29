from itertools import count





# BRUTE FORCE

def problem_five(n):

    # start at 1 and count up
    for m in count(2, 1):

        # check if the number is divisible by 1 to n
        divisible = True
        for p in range(1, n+1):
            if 0 != (m%p):
                divisible = False
                break
        if divisible:
            return m


print(problem_five(10))
print(problem_five(20))
