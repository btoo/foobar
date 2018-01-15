import unittest
from index import answer

class TestCodes(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(answer([3, 1, 4, 1]), 4311)
        self.assertEqual(answer([3, 1, 4, 1, 5, 9]), 94311)
        self.assertEqual(answer([6, 2, 4, 1]), 642)
        self.assertEqual(answer([6, 2, 4, 2]), 642)
        self.assertEqual(answer([6, 2, 4, 1, 1]), 642)
        self.assertEqual(answer([6, 3, 4, 7]), 63)
        self.assertEqual(answer([6, 3, 8, 8, 2]), 63882)
        self.assertEqual(answer([0]), 0)
        self.assertEqual(answer([2]), 0)

if __name__ == '__main__':
    unittest.main()
