### This is a possible interview coding question.
Task: Given an integer x perform the following conditional actions:
If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'
Constraint: input integer is always within the range 1 to 100 inclusive
###

# EXAMPLE SOLUTION

def is_within_range(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False

def is_even(num):
    return num % 2 == 0

def red_or_blue(num):
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'

    if (is_even(num) and num > 20) or num in [2, 4]:
        return 'Blue'
    
#create a test file (use test_unit_test_example.py), import the function and test it.   

from unittest import TestCase, main
from main import red_or_blue


class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(num=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)

    def test_range_6_to_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
