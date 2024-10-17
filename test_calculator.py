import unittest
from web_calculator import add_numbers

class TestStockCalculator(unittest.TestCase):
    # Test adding two numbers
    def test_add_two_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    # # Test adding three numbers
    # def test_add_three_numbers(self):
    #     self.assertEqual(add_numbers(5, 15, 10, number_of_inputs=3), 30)

    # Test case with negative numbers
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -15), -20)

    # Test case where all inputs are zero
    # def test_add_zeros(self):
    #     self.assertEqual(add_numbers(0, 0, 0, number_of_inputs=3), 0)

    # # Test adding mixed positive and negative numbers
    # def test_add_mixed_numbers(self):
    #     self.assertEqual(add_numbers(-10, 20, -5, number_of_inputs=3), 5)

if __name__ == "__main__":
    unittest.main()
