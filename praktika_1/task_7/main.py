from task_7_1 import create_random_list, is_even, greet

numbers = create_random_list(5)
print("Случайные числа:", numbers)
print("Четные числа:",end = " ")
for num in numbers:
    if is_even(num):
        print(num, end=" ")

print()
print(greet("Дмитрий"))
