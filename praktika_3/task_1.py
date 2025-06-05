n = int(input("Введите число n < 10: "))

if n >= 10:
    print("Число должно быть меньше 10!")
else:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()