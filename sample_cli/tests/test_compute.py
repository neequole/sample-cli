from unittest import TestCase

from ..compute import add, subtract, multiply, divide


class TestCompute(TestCase):
    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(4, 3) == 1

    def test_multiply(self):
        assert multiply(12, 2) == 24

    def test_normal_divide(self):
        assert divide(13, 2) == 6.5

    def test_floor_divide(self):
        assert divide(13, 2, True) == 6
