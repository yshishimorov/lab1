"""
Модуль вспомогательных функций для обработки строк.
Создан в отдельной ветке feature для демонстрации ветвления в Git.
"""


def reverse_string(s: str) -> str:
    """Возвращает перевёрнутую строку."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Проверяет, является ли строка палиндромом (без учёта пробелов и регистра)."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Подсчитывает количество гласных букв в строке."""
    vowels = set("aeiouyаеёиоуыэюя")
    return sum(1 for ch in s.lower() if ch in vowels)
