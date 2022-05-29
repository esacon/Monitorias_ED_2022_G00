import numpy as np


def bigZ(i, j, k):
    BigZ[i][j] = k
    BigZ[(n - 1) - i][(n - 1) - j] = n ** 2 - (k - 1)
    if i == (n - 1) // 2 and j == v:  # CASO BASE POR POSICIÓN.  # i = j = Entero((n - 1 +- Corrimiento)/Longitud)
        return BigZ
    elif i <= (n - 2) // 3 and j == i:
        bigZ(i, j + 1, k + 1)
    elif i <= (n - 2) // 3 and j == n - 1 - 2 * i:
        bigZ(i + 1, j - 1, k + 1)
    elif j <= (n - 3) // 3 and i == n - 2 - 2 * j:
        bigZ(i - 1, j, k + 1)
    elif j > i and j < n - 1 - 2 * i:
        bigZ(i, j + 1, k + 1)
    elif i > j and i < n - 2 - 2 * j:
        bigZ(i - 1, j, k + 1)
    else:
        bigZ(i + 1, j - 1, k + 1)


def imprimir(matriz, msg='  Rotado sentido horario'):
    print('\n', msg)
    print('\n'.join([
        ''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row])
        for row in matriz
    ]))


# Programa principal
n = int(input('Digite número impar: '))
v = n // 2
BigZ = np.zeros((n, n))
bigZ(n // 3, (n - 1) // 3, 1)  # i = j = Entero((n - 1 +- Corrimiento)/Longitud)
imprimir(BigZ, '')
# Imprimir sin números ceros
