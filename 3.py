# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# prime factors
number = 600851475143
divisors = []

for i in range(1, round(number ** 0.5) + 1):
    if number % i == 0:
        divisors.append(i)
        number = number / i

print(divisors)
