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
collatz_cache = dict()

def next_collatz(n):
    if n%2 == 0:
        return( int( n/2) )
    else:
        return( int(3*n + 1 ))

def collatz_seq(n):
    seq = []
    i = n
    global collatz_cache
    # print(collatz_cache.keys())
    while True:   
        if str(int(i) )in list(collatz_cache.keys()):
            seq = seq + collatz_cache[str(int(i))]
            break
        else:
            seq.append(int(i) )
            i = next_collatz(i)
            if i==1:
                seq.append(1)
                break
    collatz_cache[str(int(n) )]=seq
    return seq

for i in range(2,10000):
    collatz_seq(i)


print( np.max( [len(i) for i in collatz_cache.values()]  ) )

# def collatz_len(n):
#     length = len(collatz_seq(n) )
#     return length

# for i in range(2,10):
#     print(collatz_seq(i))
#     collatz_len(i)
