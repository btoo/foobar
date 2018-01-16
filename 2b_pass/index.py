from bisect import insort

"""
proof that if the sum of all digits is divisible by 3, so is the number:
http://www.apronus.com/math/threediv.htm
"""

def reduce_to_digits_filtered_by_remainder(accumulator, digit):
    accumulator[digit % 3] = accumulator[digit % 3] + [digit]
    return accumulator

def convert_ascending_list_to_descending_int(sequence):
    if not len(sequence):
        return 0

    return int(''.join(map(str, list(reversed(sequence)))))

def insort_into_accumulator(accumulator, item):
    insort(accumulator, item)
    return accumulator

def insort_list(list_to_insort_into):
    def insort_list_with_list_to_insort(list_to_insort):
        return reduce(
            insort_into_accumulator,
            list_to_insort,
            list_to_insort_into
        )
    return insort_list_with_list_to_insort

def discard_digit_from_accumulator(accumulator, digit):
    accumulator.remove(digit)
    return accumulator


"""
compile_answer will return the answer when provided with all the arguments.
allows for partial function applications
"""
# 1. provide the first list of digits to keep (digits that are multiples of 3)
def compile_answer(first_to_keep):
    insort_into_first = insort_list(first_to_keep) # setup for insorting the second round of digits to keep
    # 2. provide the second list of the digits to keep (digits with a remainder of which all members are to be kept)
    def compile_answer2(second_to_keep):
        second = insort_into_first(second_to_keep) # second = sorted(first_to_keep + second_to_keep)
        insort_into_second = insort_list(second)
        # 3a. provide the third list of digits (some of these digits (at most 2) will be discarded
        def compile_answer3a(third_to_discard_from):
            # 3b. provide the list of digits to discard from third_to_discard_from
            def compile_answer3b(digits_to_discard):
                third_to_keep = reduce(
                    discard_digit_from_accumulator,
                    digits_to_discard,
                    third_to_discard_from
                )
                third = insort_into_second(third_to_keep) # third = sorted(second_to_keep + third_to_keep)
                compiled_answer = convert_ascending_list_to_descending_int(third)
                return compiled_answer
            return compile_answer3b
        return compile_answer3a
    return compile_answer2


def answer(digits):
    digits = sorted(digits)
    digits_by_remainder = reduce(
        reduce_to_digits_filtered_by_remainder,
        digits,
        [
            [], # digit % 3 == 0
            [], # digit % 3 == 1
            []  # digit % 3 == 2
        ]
    )

    digits0 = digits_by_remainder[0]
    digits1 = digits_by_remainder[1]
    digits2 = digits_by_remainder[2]

    # we only care about digits that aren't multiples of 3
    digits_sum = sum(digits1) + sum(digits2)
    digits_sum_remainder = digits_sum % 3

    """
    we just need the sum of the removable digits
    (ie the digits that are not multiples of 3)
    to be a multiple of 3. if the sum isn't so, remove
    the smallest and smallest number of digit(s)
    """

    if digits_sum_remainder == 0:
        return convert_ascending_list_to_descending_int(digits)
    
    compile_answer2 = compile_answer(digits0)

    if digits_sum_remainder == 1:
        if len(digits1) >= 1:
            compile_answer3a = compile_answer2(digits2)
            compile_answer3b = compile_answer3a(digits1)
            return compile_answer3b(digits1[:1])
        if len(digits2) >= 2:
            compile_answer3a = compile_answer2(digits1)
            compile_answer3b = compile_answer3a(digits2)
            return compile_answer3b(digits2[:2])

    if digits_sum_remainder == 2:
        if len(digits2) >= 1:
            compile_answer3a = compile_answer2(digits1)
            compile_answer3b = compile_answer3a(digits2)
            return compile_answer3b(digits2[:1])
        if len(digits1) >= 2:
            compile_answer3a = compile_answer2(digits2)
            compile_answer3b = compile_answer3a(digits1)
            return compile_answer3b(digits1[:2])
    
    return 0
