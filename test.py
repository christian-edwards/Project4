import unittest
from DiceRoller import roller

class MyTestCase(unittest.TestCase):
    def test_oneside(self):
        sides = 1
        result = rollerWith(1)
        self.assertFalse(result)  # add assertion here
    def test_two_or_more(self):
        sides = 2
        result = rollerWith(sides)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
