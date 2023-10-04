# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# this is a cache with, {number: the collnatz seq of this number}
import numpy as np

collatz_cache = dict()

def next_collatz(n: int):
    """returns the next term of the collatz sequence"""
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)



def collatz_seq(n):
    seq = [n]
    _next = next_collatz(n)
    global collatz_cache
    while _next!=1:
        seq.append( _next )
        _next = next_collatz(_next)
    return seq


for i in range(2, 15):
    collatz_seq(i)
# print(collatz_cache)

lengths = [(i,len(x)) for i,x in enumerate(collatz_cache.values() ) ]
print(lengths)
# my_index = [i for i,x in enumerate(lengths==np.max(lengths)) if x]
# print([i for i in my_index] )
print(list(collatz_cache.keys())[7] )
# print(np.max(lengths))

# def collatz_len(n):
#     length = len(collatz_seq(n) )
#     return length

# for i in range(2,10):
#     print(collatz_seq(i))
#     collatz_len(i)
