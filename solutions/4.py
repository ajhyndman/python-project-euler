# I: Pretty thoughtless answer


# PALINDROME CHECKER

def is_palindrome(x):
    string = str(x)

    i = 0
    while i <= (len(string) // 2):
        # work from both ends simultaneously
        if string[i] != string[-(i+1)]:
            return False
        i += 1

    return True


# List all possible 3-digit products
products = []
for a in range(100, 1000):
    for b in range(100, 1000):
        products.append(a*b)

# Sort the list
products.sort()

# Reverse the list (biggest first)
products = products[::-1]

# Grab the very first palindrome encountered
for x in products:
    if is_palindrome(x):

        # Yay, solution
        print("The largest product of two three digit numbers that is also a palindrome is:", x)
        break





# II: List comprehension


# I like this answer!

solution = max(x*y for x in range(100, 1000) for y in range(100, 1000) if str(x*y) == str(x*y)[::-1])

print("The largest product of two three digit numbers that is also a palindrome is:", solution)
