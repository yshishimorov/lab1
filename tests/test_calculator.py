"""
Модульные тесты для модуля calculator.
"""

import unittest
from src.calculator import add, subtract, multiply, divide, calculate_power


class TestCalculator(unittest.TestCase):
    """Тестирование функций калькулятора."""

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 10), -5)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self) -> None:
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-9, 3), -3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_calculate_power(self) -> None:
        self.assertEqual(calculate_power(2, 3), 8)
        self.assertEqual(calculate_power(5, 0), 1)
        self.assertEqual(calculate_power(4, 0.5), 2)


if __name__ == "__main__":
    unittest.main()
