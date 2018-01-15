from bisect import insort

"""
proof that if the sum of all digits is divisible by 3, so is the number:
http://www.apronus.com/math/threediv.htm
"""

def reduce_to_digits_filtered_by_remainder(accumulator, digit):
    accumulator[digit % 3] = accumulator[digit % 3] + [digit]
    return accumulator

def convert_ascending_list_to_descending_int(sequence):
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
    def insort_second(second_to_keep):
        second = insort_into_first(second_to_keep) # second = sorted(first_to_keep + second_to_keep)
        insort_into_second = insort_list(second)
        # 3. provide the third list of digits (some of these digits (at most 2) will be discarded
        def insort_third(third_to_discard_from):
            # 4. provide the list of digits to discard from third_to_discard_from
            def discard_from_third(digits_to_discard):
                third_to_keep = reduce(
                    discard_digit_from_accumulator,
                    digits_to_discard,
                    third_to_discard_from
                )
                third = insort_into_second(third_to_keep) # third = sorted(second_to_keep + third_to_keep)
                return convert_ascending_list_to_descending_int(third)
            return discard_from_third
        return insort_third
    return insort_second


# def answer(digits):
#     digits = sorted(digits)
#     digits_filtered_by_remainder = reduce(
#         reduce_to_digits_filtered_by_remainder,
#         digits,
#         [
#             [], # multiples of 3
#             [], # digits with remainder 1
#             []  # digits with remainder 2
#         ]
#     )

#     # we only care about digits that aren't multiples of 3
#     digits_sum = sum(digits_filtered_by_remainder[1]) + sum(digits_filtered_by_remainder[2])
#     digits_sum_remainder = digits_sum % 3

#     """
#     we just need the sum of the removable digits
#     (ie the digits that are not multiples of 3)
#     to be a multiple of 3. if the sum isn't so,
#     remove the smallest number(s)
#     """

#     if digits_sum_remainder == 0:
#         return convert_sequence_to_int(digits)
#     elif digits_sum_remainder == 1:
#         remainder_1s = digits_filtered_by_remainder[1]
#         if len(digits_filtered_by_remainder[1]) >= 1:
#             insort_digits = insort_digits_then_convert_to_int(digits_filtered_by_remainder[0] + digits_filtered_by_remainder[2])
#             return insort_digits([remainder_1s[0]])



#     return int(''.join(map(str, digits)))
