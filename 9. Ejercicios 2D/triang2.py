import numpy as np


def triangulo(i, j, k):
    RC[i][j] = k
    if k == nc ** 2:  # CASO BASE (k==nc**2)
        return RC
    elif j == nc - 1 and (i + j) % 2 == 0:
        triangulo(i + 1, j, k + 1)
    elif j == i + 2 - nc and (i + j) % 2 == 1:
        triangulo(i + 1, j, k + 1)
    elif (j + i) % 2 == 0:
        triangulo(i - 1, j + 1, k + 1)
    elif (j + i) % 2 == 1:
        triangulo(i + 1, j - 1, k + 1)


nc = 2
while nc % 2 == 0:
    nc = int(input("Número de columnas nc = "))
nf = 2 * nc - 1
RC = np.zeros((nf, nc))
triangulo(nc - 1, 0, 1)
# Imprimir
print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in RC]))