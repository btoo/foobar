"""
proof that if the sum of all digits is divisible by 3, so is the number:
http://www.apronus.com/math/threediv.htm
"""

def reduce_to_digits_filtered_by_remainder(accumulator, digit):
    accumulator[digit % 3] = accumulator[digit % 3] + [digit]
    return accumulator

iterable_to_int = lambda iterable: int(''.join(map(str, list(reversed(iterable)))))

def answer(digits):
    digits = sorted(digits)
    digits_filtered_by_remainder = reduce(
        reduce_to_digits_filtered_by_remainder,
        digits,
        [
            [], # multiples of 3
            [], # digits with remainder 1
            []  # digits with remainder 2
        ]
    )

    # we only care about digits that aren't multiples of 3
    digits_sum = sum(digits_filtered_by_remainder[1]) + sum(digits_filtered_by_remainder[2])
    digits_sum_remainder = digits_sum % 3

    """
    we just need the sum of the removable digits
    (ie the digits that are not multiples of 3)
    to be a multiple of 3. if the sum isn't so,
    remove the smallest number(s)
    """

    if digits_sum_remainder == 0:
        return iterable_to_int(digits)
    elif digits_filtered_by_remainder == 1:
        return


    # removables = filter(lambda x: x % 3 != 0, digits) # filter out non-multiples of 3 because they are the only ones that may need to be removed
    # sum = reduce(lambda x, y: x + y, removables, 0) # get sum of those digits

    # print l

    
    # remainder = sum % 3
    # if remainder > 0:
    #     for removable in reversed(removables):
    #         if removable % remainder ==

    return int(''.join(map(str, digits)))
