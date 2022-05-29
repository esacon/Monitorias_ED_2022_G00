import numpy as np


def romboC(i, j, k):
    RC[i][j] = k
    if i == v and j == v:
        return RC
    elif j == v and i > v:  # SINGULARIDADES
        romboC(i - 1, j + 1, k + 1)  # CIAN
    elif j == v + 1 and i <= v:
        romboC(i, j - 1, k + 1)  # VERDE
    else:
        if j <= v:
            jv = j - abs(v - i)  # NARANJA
            romboC(i + 1, jv + abs(v - (i + 1)), k + 1)
        else:
            jv = j + abs(v - i)  # AZUL
            romboC(i - 1, jv - abs(v - (i - 1)), k + 1)

n = 2
while n % 2 == 0:
    n = int(input("Número de filas y columnas n = "))
v = (n - 1) // 2
RC = np.zeros((n, n))
romboC(0, v, 1)
# Imprimir
print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in RC]))
