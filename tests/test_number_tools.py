import unittest

from number_tools import is_palindrome, reverse_integer


class NumberToolsTests(unittest.TestCase):
    def test_reverse_integer(self) -> None:
        cases = {
            12345: 54321,
            1200: 21,
            0: 0,
            -123: -321,
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(reverse_integer(value), expected)

    def test_is_palindrome(self) -> None:
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(1221))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(-121))


if __name__ == "__main__":
    unittest.main()
