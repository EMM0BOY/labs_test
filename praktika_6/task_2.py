# 1) Функция с делением на ноль при определенном x
def f1(x):
    return (x**2 + 3 * x + 2) / (x - 5)


# 2) Функция с использованием необъявленной переменной
def f2(x, y):
    return x * y * z


# 3) Функция, возвращающая длину строки
def f3(s):
    return len(s)


# 4) Функция сравнения средних четных и нечетных чисел
def f4(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]

    avg_even = sum(even) / len(even) if even else 0
    avg_odd = sum(odd) / len(odd) if odd else 0

    if avg_even > avg_odd:
        return "Среднее четных больше"
    elif avg_odd > avg_even:
        return "Среднее нечетных больше"
    else:
        return "Средние равны"


# 5) Функция с логической ошибкой (неправильное вычисление факториала)
def f5(n):
    result = 1
    for i in range(n):  # Должно быть range(1, n+1)
        result *= i
    return result


# print(f1(5))
# print(f2(1,2))
print(f3("123"))
print(f3("Hello"))
print(f4([1, 2, 3, 4, 5]))
