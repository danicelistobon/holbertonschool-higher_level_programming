#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for unittests"""

    def test_max_int(self):
        self.assertEqual(max_integer([4, 656, 34]), 656)

    def test_max_float(self):
        self.assertEqual(max_integer([23, 3454.21, 454]), 3454.21)

    def test_max_int_neg(self):
        self.assertEqual(max_integer([-21234, 0, 12, -3, 5]), 12)

    def test_max_one_int(self):
        self.assertEqual(max_integer([34]), 34)

    def test_max_none(self):
        self.assertEqual(max_integer(), None)

    def test_max_err(self):
        with self.assertRaises(TypeError):
            max_integer([4, 656, 'hola'])
