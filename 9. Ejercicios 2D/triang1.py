import numpy as np


def triangulo(i, j, k):
    Mat[i][j] = k
    if k == nf**2:     #  Caso base.
        return Mat
    elif j == 2 * i and i >= vi:
        triangulo(i, j - 1, k + 1)
    elif nc - 2 * i < j < 2 * i:
        triangulo(i, j - 1, k + 1)
    else:
        iv = i - np.abs(j - vj)
        triangulo(iv + np.abs((j + 1) - vj), j + 1, k + 1)


def imprimir(matriz):
    print('\n'.join([
        ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
        for row in matriz
    ]))


# Programa principal

nf = int(input('Digite número de filas: '))
nc = 2*nf - 1

vi = nf // 2
vj = nc // 2

Mat = np.zeros((nf, nc))
triangulo(nf - 1, 0, 1)
imprimir(Mat)