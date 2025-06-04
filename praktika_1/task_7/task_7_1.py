import random


def create_random_list(length, start=1, end=10):
    """Создает список случайных чисел."""
    return [random.randint(start, end) for _ in range(length)]


def is_even(number):
    return number % 2 == 0


def greet(name):
    return f"Привет, {name}!"
