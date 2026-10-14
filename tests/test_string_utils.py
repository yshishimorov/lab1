"""
Модульные тесты для string_utils.py.
"""

import unittest
from src.string_utils import reverse_string, is_palindrome, count_vowels


class TestStringUtils(unittest.TestCase):
    """Тестирование функций работы со строками."""

    def test_reverse_string(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_is_palindrome(self) -> None:
        self.assertTrue(is_palindrome("топот"))
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertFalse(is_palindrome("привет"))

    def test_count_vowels(self) -> None:
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("программирование"), 7)
        self.assertEqual(count_vowels("bcdfg"), 0)


if __name__ == "__main__":
    unittest.main()
