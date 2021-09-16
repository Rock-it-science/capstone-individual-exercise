import unittest
from parseInput import parseInput
from sortArray import sortArray

class TestMethods(unittest.TestCase):
    def test_parsing1(self):
        self.assertEqual(parseInput('1,2,3'), [1, 2, 3])
    def test_parsing2(self):
        self.assertEqual(parseInput('9, 657,\n 7,5466'),[9, 657, 7, 5466])
    
    def test_sorting1(self):
        self.assertEqual(sortArray([3, 2, 1, 5, 9]), [1, 2, 3, 5, 9])

if __name__ == "__main__":
    unittest.main()