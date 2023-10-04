# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# evenly divisible by an number is equivelent to being divisible
# by that number and 2.
from math import prod


def prime_factorise(numb):
    "Prime factorisation using reccursion"
    # still a bit shocked this actually works
    if numb == 1:
        return [1]
    prime_factors = []
    for i in range(2, numb + 1):
        if numb % i == 0:
            prime_factors = [i] + prime_factorise(int(numb / i))
            return prime_factors


# print(prime_factorise(28))


def lcm(*args):
    all_pf = [prime_factorise(numb) for numb in args]
    all_pf_unnest = [j for i in all_pf for j in i]
    unique_factors = set(all_pf_unnest)

    pf_lcm = []
    for i in unique_factors:
        max_index = max([pf.count(i) for pf in all_pf])
        pf_lcm = pf_lcm + [i ** max_index]
    return prod(pf_lcm)


print(lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))


def is_evenly_divisible(numb, divisor):
    if numb % divisor == 0:
        if (numb / divisor) % 2 == 0:
            return True
        else:
            return False
    else:
        return False


print(is_evenly_divisible(232792560, 20))

# def is_divisible_1_to_n(numb,n):
#     "Check is a number is divisible by all numbers from 1 to n"
#     for i in range(1,n):
#         if numb%i==0:
#             pass
#         else:
#             return False
#     return True

# print(is_divisible_1_to_n(2520,10))

# def is_evenly_divisible_1_to_n(numb,n):
#     "Check is a number is divisible by all numbers from 1 to n"
#     for i in range(1,(n+1)):
#         if numb%i==0:
#             if (numb/i)%2 == 0:
#                 pass
#             else:
#                 return False
#         else:
#             return False
#     return True
