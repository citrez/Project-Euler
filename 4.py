# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palendrome(number):
    number_str = str(number)
    half_length = int(len(number_str)/2)

    for i in range(1,half_length+1):
        if number_str[i-1] == number_str[-i]:
            pass
        else:
            return False
    return True

print(is_palendrome(909))
print(is_palendrome(9097))
print(is_palendrome(936799))

palendromes = []

for i in range(900,999):
    for j in range(i,999):
        product = i*j
        if is_palendrome(product):
            print(f"Hurrah, the number {product} = {i} * {j} is a palendrome")
            palendromes.append(product)

print(max(palendromes))