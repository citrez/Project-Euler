# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# prime seive
# this took more concentration than id like to admit
n = 10 ** 6
sieve = list(range(2, n))
counter = 0
check = sieve[counter]

while check < round(n ** 0.5):
    sieve = [p for p in sieve if p % check != 0 or p == check]
    counter += 1
    check = sieve[counter]

if len(sieve) > 10001:
    print(sieve[0:5])
    print(sieve[10001])
