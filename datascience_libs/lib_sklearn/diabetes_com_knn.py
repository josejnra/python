import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

dados = datasets.load_diabetes()

x = dados.data
y = dados.target

knn = KNeighborsRegressor(n_neighbors=5)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

knn.fit(x_train, y_train)

predict = knn.predict(x_test)

"""
for i in range(len(predict)):
    print('Predito: {}'.format(predict[i]), end='')
    print('\t Correto: {}'.format(y_test[i]))
"""

print(f"Número de amostras para treino: {len(x_train)}")
print(f"Número de amostras para validação: {len(x_test)}")
print(f"Número total de amostras: {len(x)}")

erro_medio_quadrado = mean_squared_error(y_test, predict)

print(f"Erro médio quadrado: {erro_medio_quadrado}")

plt.plot(np.linspace(1, len(y_test), len(y_test)), y_test, label="Correto", c="#000000")
plt.plot(np.linspace(-1, len(predict), len(predict)), predict, label="Predito", c="r")

plt.legend()

plt.show()
