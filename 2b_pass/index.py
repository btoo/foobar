"""
proof that if the sum of all digits is divisible by 3, so is the number:
http://www.apronus.com/math/threediv.htm
"""

def answer(l):
    l = sorted(l, reverse=True) # digits in descending order
    sum = reduce(
        lambda x, y: x+y,
        filter(lambda x: x % 3 == 0, l),
        0
    ) # filter by non-multiples of 3 and get sum of those digits
    # print sum
    # remainder = sum % 3
    # print remainder
    # if remainder > 1:

    
    return int(''.join(map(str, l)))
