# SOLUTION FOR GENERAL CASE

def problem_six(n):
    sum_of_squares = sum(x**2 for x in range(1, n+1))

    square_of_sum = sum(range(1, n+1))**2

    return square_of_sum - sum_of_squares


print(problem_six(10))
print(problem_six(100))
