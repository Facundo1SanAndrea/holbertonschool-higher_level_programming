#!/usr/bin/python3
"""test of unity for import"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """creat test for testing the function and it correct output"""

    def test_1(self):
        with self.assertRaises(TypeError):
            max_integer(['tati', 7, 9, 2])

    def test_2(self):
        self.assertEqual(max_integer([]), None)

    def test_3(self):
        self.assertEqual(max_integer([3, 5, 8, 43, 77, 89]), 89)

    def test_4(self):
        self.assertEqual(max_integer([19, 19, 19, 19, 19]), 19)

    def test_5(self):
        self.assertEqual(max_integer([-7, -9, 2, 37, -44, 52]), 52)


if __name__ == '__main__':
    unittest.main()