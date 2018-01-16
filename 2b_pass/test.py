import unittest
from index import answer

class TestCodes(unittest.TestCase):

    # given tests with confirmed answers
    def test_given(self):
        self.assertEqual(answer([3, 1, 4, 1]), 4311)
        # self.assertEqual(answer([3, 1, 4, 1, 5, 9]), 94311)

    # sum of digits has remainder 1
    def test_sum_has_remainder_1(self):
        
        # remove 1 digit with a remainder 1
        self.assertEqual(answer([3, 1, 4, 1, 5, 8]), 85431)
        self.assertEqual(answer([6, 2, 4, 1]), 642)

        # no digits with remainder 1, so discard two digits with remainder 2
        self.assertEqual(answer([6, 2, 2]), 6)
        self.assertEqual(answer([8, 8]), 0)

        # not a single digit with remainder 1 and no two digits with remainder 2, so answer is 0
        self.assertEqual(answer([2]), 0)
        self.assertEqual(answer([5]), 0)
        self.assertEqual(answer([8]), 0)

    # sum of digits has remainder 2
    def test_sum_has_remainder_2(self):
        
        # remove 1 digit with remainder 2
        self.assertEqual(answer([6, 2, 4, 2]), 642)
        
        # remove 2 digits with remainder 1
        self.assertEqual(answer([6, 4, 1, 1, 7]), 7641)

        # not a single digit with remainder 2 and no two digits with remainder 1, so answer is 0
        self.assertEqual(answer([1]), 0)
        self.assertEqual(answer([4]), 0)
        self.assertEqual(answer([7]), 0)
        

    # def test_custom(self):
    #     # self.assertEqual(answer([6, 3, 4, 7]), 63)
    #     # self.assertEqual(answer([6, 3, 8, 8, 2]), 63882)
    #     # self.assertEqual(answer([0]), 0)
    #     # self.assertEqual(answer([2]), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
