"""
    Plotar gráfico a partir de dados em um arquivo CSV
"""

from matplotlib import pyplot as plt

# ler arquivo CSV com os dados
f = open("arquivos_texto/semperda.csv")
x = list()
y = list()
for linha in f:
    # é feito um split para seperar os dados, já que os dados são separados por ','
    i = linha.split(",")
    # converter cada valor para float e salvar em uma lista
    x.append(float(i[0]))
    y.append(float(i[1]))
f.close()

# definir uma função a plotar
plt.scatter(x, y, label="Fronteira Nominal", alpha=0.5, marker="*", c="green")

# definir o título dos eixos
plt.xlabel("Fuel Cost $/h")
plt.ylabel("Emission ton/h")

# colocar legenda
plt.legend(loc="best")

# definir limites dos eixos
# axes = plt.gca()
# axes.set_xlim([597, 639])
# axes.set_ylim([0.1875, 0.202])

# outra maneira de definir os limites dos eixos
plt.xlim(597, 639)
plt.ylim(0.1875, 0.202)


plt.show()

# plt.savefig('grafico_python.svg')
