letters = ["a", "b", "c", "d", "e"]
numbers = [10, 20, 30, 40, 50]
result_dict = dict(zip(letters, numbers))
print("Словарь:", result_dict)
sum_values = sum(result_dict.values())
print("Сумма значений:", sum_values)
with open("ex2-1.txt", "w", encoding="utf-8") as file:
    file.write(str(sum_values))
