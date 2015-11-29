# List Comprehension

def problem_one():
    return sum([x for x in range(1000) if (0 == x%5 or 0 == x%3)])


print(problem_one())
