def sum_1(n):
    return sum(1 / (i ** 2) for i in range(1, n + 1))

def sum_2(n, m):
    return sum(i ** n for i in range(1, m + 1))

def select_operation(choice):
    if choice == 1:
        return sum_1
    elif choice == 2:
        return sum_2
    else:
        raise ValueError("Некорректный выбор. Допустимые значения: 1 или 2.")

print("Сумма 1 (n=5):", select_operation(1)(3))
print("Сумма 2 (n=2, m=3):", select_operation(2)(2, 3))