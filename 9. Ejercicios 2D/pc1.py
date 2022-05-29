import numpy as np


def triangulo(i: int, j: int, k: int):
    #print(f"i={i}\tj={j}")
    Matriz[i][j] = k
    ds = j + i
    dp = j - i
    vj = (j - abs(iv - i))
    #print(f"dp={dp}\tds={ds}\tvj={vj}")
    #imprimir(Matriz)
    # Caso base
    if k == nc ** 2:
        return Matriz
    # Singularidades
    elif i < iv and j > jv and i % 2 == 0 and j % 2 == 1 and iv + ((nc - 1) - j) == ds:  # Naranja
        triangulo(i + 1, j, k + 1)
    elif i > iv and j > jv and i % 2 == 0 and j % 2 == 0 and ((nc - 1) - j) == vj:  # Verde claro
        triangulo(i - 1, j, k + 1)
    elif i < iv and j > jv and i % 2 == 1 and j % 2 == 0 and iv + ((nc - 1) - j) + 1 == ds:  # Morada
        triangulo(abs(1 - abs(iv - i)) + iv, j - 1, k + 1)
    elif i > iv and j > jv and i % 2 == 1 and j % 2 == 1 and ((nc - 1) - j) + 1 == vj:  # Negra
        triangulo(iv + nc - 2*(j - 1) - 1, j - 1, k + 1)
    # Llamados recursivos más pequeños
    elif j % 2 == 0 and j > jv and (iv + nc - 2 * j) < i < (2 * j - nc + 1 + iv):  # Verde
        triangulo(i - 1, j, k + 1)
    elif j % 2 == 1 and j > jv and (iv + nc - 1 - 2 * j) < i < (abs(nc - iv - 2 * j)):  # Gris
        triangulo(i + 1, j, k + 1)
    elif vj % 2 == 0:
        triangulo(i + 1, vj + abs(iv - (i + 1)), k + 1)  # Amarilla
    else:
        triangulo(i - 1, vj + abs(iv - (i - 1)), k + 1)  # Azul celeste


def imprimir(matriz: np.matrix):
    print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in matriz]))


# Programa principal
nc = 2
while nc % 2 == 0:
    nc = int(input("Digite una cantidad impar de columnas: "))
nf = 2 * nc - 1
iv = nf // 2  # Vértice en i
jv = nc // 2  # Vértice en j
#print(iv, jv)

Matriz = np.zeros((nf, nc))
triangulo(0, nc - 1, 1)  # Llamado generador
imprimir(Matriz)
