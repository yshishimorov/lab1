"""
Модуль калькулятора математических операций.
Используется для демонстрации работы с СКВ Git.
"""


def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление первого числа на второе с проверкой деления на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b


def calculate_power(base: float, exponent: float) -> float:
    """Возведение числа в степень."""
    return base ** exponent
