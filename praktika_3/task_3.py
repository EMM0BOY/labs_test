with open('z3.1-1.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

if not numbers:
    print("Файл пуст или не содержит чисел")
else:
    min_num = min(numbers)
    max_num = max(numbers)

    with open('srez.txt', 'w') as output_file:
        output_file.write(f"Минимальное число: {min_num}\n")
        output_file.write(f"Максимальное число: {max_num}\n")

    print(f"Результаты записаны в srez.txt: min = {min_num}, max = {max_num}")