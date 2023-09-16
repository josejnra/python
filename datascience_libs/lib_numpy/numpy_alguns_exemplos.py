import numpy as np

# matriz 3x3, tipo ndarray
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# média ao longo do eixo 0 (linhas).
# média de cada coluna.
print(np.mean(mat, axis=0))

# média ao longo do eixo 1 (colunas).
# média de cada linha.
print(mat.mean(axis=1))

print(mat)

# matriz do tipo list
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mat = np.column_stack(mat)
print(mat)

# matriz com duas colunas, resultado parecido com uma matriz transposta
costs = np.column_stack(([2, 3, 2, 1, 3, 1, 1, 1], [7, 4, 7, 6, 6, 5, 7, 4]))

print(costs)

# média dos valores da segunda coluna
mean_costs = np.mean(costs[:, 1])

print(mean_costs)
