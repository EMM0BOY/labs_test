import random


def printMatrix(N, M):
    matrix = [[random.randint(20, 80) for _ in range(M)] for _ in range(N)]
    for row in matrix:
        formatted_row = " ".join("{:3}".format(num) for num in row)
        print(formatted_row)


N = 4  # Количество строк
M = 5  # Количество столбцов
printMatrix(N, M)
