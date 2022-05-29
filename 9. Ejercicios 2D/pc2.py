import numpy as np


def triangulo(i, j, k):
    print(f"i: {i}\tj: {j}")
    Matriz[i][j] = k
    imprimir(Matriz)
    if i == v and j == nc // 2:
        return Matriz
    elif i == 2 * j and i > v and j % 2 == 0:
        triangulo(i - 1, j, k + 1)
    elif i == nf - 2 * j and i < v and j % 2 == 0:
        triangulo(nf - i - 2, j - 1, k + 1)
    elif (j == (nf - 1 - i) / 2) and i < v and j % 2 != 0:
        triangulo(i + 1, j, k + 1)
    elif (i == nf - 1 - (nf - 2 * j)) and i > v and j % 2 != 0:
        triangulo(nf - i, j - 1, k + 1)
    else:
        if j % 2 == 0 and nf - 2 * j <= i and i < 2 * j:
            triangulo(i - 1, j, k + 1)
        elif j % 2 != 0 and nf - 2 * j <= i and i < 2 * j - 1:
            triangulo(i + 1, j, k + 1)
        elif (j - abs(v - i)) % 2 == 0:
            triangulo(i + 1, abs(j - abs(v - i) + abs(v - (i + 1))), k + 1)
        elif j - abs(v - i) % 2 != 0:
            triangulo(i - 1, abs(j - abs(v - i) + abs(v - (i - 1))), k + 1)


def imprimir(matriz: np.matrix):
    print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in matriz]))


# Programa principal
nc = 2
while nc % 2 == 0:
    nc = int(input("Digite una cantidad impar de columnas: "))
nf = 2 * nc - 1
v = nc - 1

Matriz = np.zeros((nf, nc))
triangulo(0, nc - 1, 1)  # Llamado generador
imprimir(Matriz)
