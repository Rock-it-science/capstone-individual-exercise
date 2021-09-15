import unittest
from parseInput import parseInput

class TestMethods(unittest.TestCase):
    def test_parsing1(self):
        self.assertEqual(parseInput('1,2,3'), [1, 2, 3])
    def test_parsing2(self):
        self.assertEqual(parseInput('9, 657,\n 7,5466'),[9, 657, 7, 5466])

if __name__ == "__main__":
    unittest.main()