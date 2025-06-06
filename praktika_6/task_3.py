def f1(x):
    try:
        result = (x**2 + 3*x + 2) / (x - 5)
        return result
    except ZeroDivisionError:
        print(f"Ошибка: ZeroDivisionError (деление на ноль при x=5)")
        new_x = 6
        print(f"Пример работы с x={new_x}: {(new_x**2 + 3*new_x + 2) / (new_x - 5)}")
        return None
    except TypeError:
        print("Ошибка: TypeError. Введите числовое значение для x.")
        return None

def f2(x, y):
    try:
        return x * y * z
    except NameError:
        print(f"Ошибка: NameError (переменная z не определена).")
        z = 1
        print(f"Пример работы с z=1: {x * y * z}")
        return None
    except TypeError:
        print("Ошибка: TypeError. Убедитесь, что x и y - числа.")
        return None

def f3(s):
    try:
        return len(s)
    except TypeError:
        print("Ошибка: TypeError. Функция ожидает строку в качестве аргумента.")
        example = "пример"
        print(f"Пример работы со строкой '{example}': {len(example)}")
        return None


print("Тест f1():")
print(f1(5))
print(f1("a"))
print(f1(6))

print("\nТест f2():")
print(f2(2, 3))
z = 10
print(f2(2, 3))
print(f2("a", 3))

print("\nТест f3():")
print(f3(123))
print(f3("abc"))