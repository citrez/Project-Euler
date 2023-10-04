# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# find all pythag triples where a,b,c all less than 999

range_a = range(1, 999)
range_b = range(1, 999)

py_triples = []
for a in range_a:
    for b in range_b:
        if a < b:
            c_sq = a ** 2 + b ** 2
            if 0 < c_sq < 999 ** 2:
                c = c_sq ** 0.5
                if (c - int(c)) < 0.0001:
                    py_triples.append([a, b, c])
                    # print(f"{a}^2+{b}^2 = {c}^2")

py_triples_sum = [sum(trips) for trips in py_triples]

for i, bool in enumerate([int(sum) == 1000 for sum in py_triples_sum]):
    if bool:
        print(py_triples[i])

print(200 * 375 * 425)
