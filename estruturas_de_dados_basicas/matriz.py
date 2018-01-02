'''
Ler matriz
'''

matriz = []
l = 3

# ler matriz l(3) x n
for i in range(l):
    matriz.append([int(x) for x in input().split()])

# imprime matriz lida
print(matriz)

# alterar célula da matriz
matriz[0][2] = 5

# imprime matriz alterada
print(matriz)


'''
Multiplicação de matrizes
'''

import numpy as np

# ler matriz 2 x n
a = []
for i in range(2):
    a.append([int(x) for x in input().split()])

# imprime matriz lida
print(a)

# ler matriz 2 x n
b = []
for i in range(2):
    b.append([int(x) for x in input().split()])

# imprime matriz lida
print(b)

# quebra de linha
print()

# multiplica matriz a pela matriz b
print("AxB:", np.dot(a, b))

# multiplica matriz b pela matriz a
print("AxB:", np.dot(b, a))
