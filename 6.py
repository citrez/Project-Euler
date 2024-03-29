# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025-285 = 2640
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

# sum of squared
sum_of_squares = sum([i ** 2 for i in range(1, 101)])
square_of_sum = sum(range(1, 101)) ** 2

print(square_of_sum - sum_of_squares)
