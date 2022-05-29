import numpy as np


def rombo(i, j, k):
    RC[i][j] = k
    if i == v and j == v:  # CASO BASE k == (v**2 + (v + 1)**2)
        return RC
    elif j == v and i > v:
        rombo(n - i, j, k + 1)
    elif j == v and i <= v:
        rombo(i + 1, j - 1, k + 1)
    elif j < v:
        rombo(i, n - (j + 1), k + 1)
    elif j > v and i < v:
        rombo(i + 1, n - (j + 1) - 1, k + 1)
    elif j > v and i >= v:
        rombo(i + 1, n - (j + 1) + 1, k + 1)


n = 2
while n % 2 == 0:
    n = int(input("Número de filas y columnas n = "))
v = (n - 1)//2
RC = np.zeros((n, n))
rombo(0, v, 1)
# Imprimir
print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in RC]))
