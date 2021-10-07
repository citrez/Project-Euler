# prime seive 
# this took more concentration than id like to admit
n = 2*10**6
sieve = list(range(2,(n+1))) # initiate all numbers that im going to check though
counter = 0
# we go through all numbered, take it, and then delete all multiples of it.
check = sieve[counter]
while check < int(max(sieve)**0.5) : # after we get to the square root, we know all primes up to that point,
    # for any number after the sq root, if it is timed by something above the sq root,
    # it will product to more than 100, and we only can about primes up to 100,
    # any thing we product by less than the sq root wont be in the sieve any more
    
    # print(f"Check: {check}")
    print(f"Counter: {counter}")
    # print(f"{sieve}: {len(sieve)}")
    print('\n')
    # update to sieve, only numbered taht are not a multiple of the check
    # we also keep the check itself
    sieve = [p for p in sieve if p%check !=0 or p==check ]
    # iterate the counter to check the next number in the sieve
 
    counter+=1
    check = sieve[counter]

print(sum(sieve))
