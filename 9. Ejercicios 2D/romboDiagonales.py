import numpy as np

def rombo(i : int, j : int, k : int):
  print(f"i={i}\tj={j}")
  Matriz[i][j] = k
  ds = j + i
  dp = j - i
  print(f"dp={dp}\tds={ds}")
  imprimir(Matriz) 
  # Caso base
  if i == n - 1 and j == v:  
    return Matriz
  # Singularidades
  elif dp == -v and i >= v and j < v:  # Gris
    rombo(i, j + 1, k + 1)
  elif dp == v - 1 and i <= v and j >= v:  # Amarilla
    rombo(i, j + 1, k + 1)
  # Llamados recursivos más pequeños
  elif ds % 2 == 1:  # Naranja
    rombo(i + 1, j - 1, k + 1)
  elif ds % 2 == 0:  # Verde
    rombo(i - 1, j + 1, k + 1)


def imprimir(matriz : np.matrix):
    print('\n'.join([''.join(['{:4}'.format(int(item) if item != 0 else '') for item in row]) for row in matriz]))


# Programa prinipal
n = 2
while n % 2 == 0:
  n = int(input("Digite una cantidad impar de columnas: "))
v = n // 2  # Vértice en i

Matriz = np.zeros((n, n))
rombo(0, v, 1)  # Llamado generador
# imprimir(Matriz) 
