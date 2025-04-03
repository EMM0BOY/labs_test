n = int(input("Введите размер списка: "))

numbers = []
for i in range(n):
    num = int(input(f"Введите {i + 1}-е число: "))
    numbers.append(num)

print("Исходный список:", numbers)

if n >= 1:
    temp = numbers[-1]
    numbers[-1] = numbers[0]
    numbers[0] = temp

print("Список после обмена:", numbers)
