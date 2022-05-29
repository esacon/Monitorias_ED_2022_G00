import numpy as np


def triangulo(i : int, j : int, k : int):
  print(f"i={i}\tj={j}")
  Matriz[i][j] = k
  ds = j + i
  dp = j - i
  print(f"dp={dp}\tds={ds}")
  imprimir(Matriz) 
  # Caso base
  if k == nc**2:  
    return Matriz
  # Singularidades
  elif j == nc - 1 and i > vi and i % 2 == 0:  # Azul
    triangulo(i - 1, j, k + 1)
  elif j == nc - 1 and i < vi and i % 2 == 1:  # Amarilla
    triangulo(i + 1, j, k + 1)
  elif i == vi and j % 2 == 0:  # Gris
    triangulo(i + 1, j + 1, k + 1)
  elif i == vi and j % 2 == 1:  # Negro
    triangulo(i - 1, j + 1, k + 1)
  # Llamados recursivos más pequeños
  elif ds % 2 == 0 and i < vi:  # Naranja
    triangulo(i + 1, j - 1, k + 1)
  elif abs(dp) % 2 == 0 and i > vi:  # Naranja
    triangulo(i + 1, j + 1, k + 1)
  elif abs(dp) % 2 == 1 and i > vi:  # Verde
    triangulo(i - 1, j - 1, k + 1)
  elif ds % 2 == 1 and i < vi:  # Verde
    triangulo(i - 1, j + 1, k + 1)


def imprimir(matriz : np.matrix):
    print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in matriz]))

# Programa principal
nc = 2
while nc % 2 == 0:
  nc = int(input("Digite una cantidad impar de columnas: "))
nf = 2 * nc - 1
vi = nf // 2  # Vértice en i
vj = nc // 2  # Vértice en j

Matriz = np.zeros((nf, nc))
triangulo(0, nc - 1, 1)  # Llamado generador
# imprimir(Matriz) 