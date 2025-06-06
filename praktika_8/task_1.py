def is_prime(n):
    """
    Проверяет, является ли число простым.
    Простое число — это целое число больше 1, которое делится только на 1 и на само себя.

    Примеры:
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    >>> is_prime(23)
    True
    """
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
