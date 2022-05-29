import numpy as np


def uzumaki(i, j, k):
    Mat[i][j] = k
    if k == v ** 2 + (nf - v) * nc:
        return Mat
    elif i == v + 1:
        uzumaki(i, j - 1, k + 1)
    elif i == v and j < v and j % 2 == 0:  # Negra
        uzumaki(2 * v + 1 - j, 0, k + 1)
    elif i == v and j % 2 != 0 and j >= v:
        uzumaki(2 * v - (nc - j) + 2,  nc - 1, k + 1)
    elif j == nc - 1 and i > v and i % 2 != 0:
        uzumaki(v, j - i + 2, k + 1)
    elif j == 0 and i > v and i % 2 == 0:
        uzumaki(v, i - 2, k + 1)
    elif i > v and i % 2 != 0:
        uzumaki(i, j + 1, k + 1)
    elif i == v and j == v:
        uzumaki(v + 1, nc - 1, k + 1)
    elif i <= v and (i + j) % 2 == 0:
        iv = i - abs(j - v)
        uzumaki(iv + abs((j - 1) - v), j - 1, k + 1)
    elif i <= v and (i + j) % 2 != 0:
        iv = i - abs(j - v)
        uzumaki(iv + abs((j + 1) - v), j + 1, k + 1)
    else:
        uzumaki(i, j - 1, k + 1)


def imprimir(matriz):
    print('\n'.join([
        ''.join(['{:4}'.format(int(item) if item != 0 else '')
                 for item in row])
        for row in matriz
    ]))


# Programa principal

v = int(input('Digite número de filas del triangulo: '))
v = v - 1
nc = 2 * v + 1
nf = nc + 1
v2 = v + (nf - v) // 2
print(nf)
Mat = np.zeros((nf, nc))
uzumaki(v, nc - 1, 1)
imprimir(Mat)
