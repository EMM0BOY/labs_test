import unittest
from task_4 import add, multiply, is_even, square, subtract

from nose2.tools import params

class TestMyFunctions(unittest.TestCase):

    @params(
        (1, 2, 3),
        (-1, -1, -2),
        (0, 0, 0),
    )
    def test_add(self, a, b, expected):
        self.assertEqual(add(a, b), expected)

    @params(
        (2, 3, 6),
        (-1, 5, -5),
        (0, 10, 0),
    )
    def test_multiply(self, a, b, expected):
        self.assertEqual(multiply(a, b), expected)

    @params(
        (2, True),
        (3, False),
        (0, True),
    )
    def test_is_even(self, n, expected):
        self.assertEqual(is_even(n), expected)

    @params(
        (2, 4),
        (-3, 9),
        (0, 0),
    )
    def test_square(self, n, expected):
        self.assertEqual(square(n), expected)

    @params(
        (5, 3, 2),
        (0, 0, 0),
        (-1, -1, 0),
    )
    def test_subtract(self, a, b, expected):
        self.assertEqual(subtract(a, b), expected)
