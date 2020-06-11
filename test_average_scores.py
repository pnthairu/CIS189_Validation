#Start Program
"""
Program: test_average_scores.py
Author: Paul Thairu
Last date modified: 06/03/2020

This program is for unit testing the average of three test scores
"""
import unittest
from format_output import average_scores


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(average_scores.average(15), 5)

# testing letters instead numbers
    def test_alphanumeric(self):
        self.assertEqual(average_scores.average(15), test)

# testing negatives numbers
    def test_alphanumeric(self):
        self.assertEqual(average_scores.average(15), -5)


if __name__ == '__main__':
    unittest.main()
