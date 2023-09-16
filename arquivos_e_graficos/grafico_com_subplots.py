import numpy as np
from matplotlib import pyplot as plt


def texto():
    plt.legend(loc="best", prop={"size": 15})

    plt.xlabel("Fuel Cost ($/hour)", fontsize=15)
    plt.ylabel("Emission (ton/hour)", fontsize=15)

    plt.grid(alpha=0.35)

    plt.xlim(597, 637)
    plt.ylim(0.1875, 0.207)


"""
    É lido_arquivos CSV e armazenado os valores em arrays
"""
amostras13 = np.genfromtxt("../arquivos_texto/13amostras.csv", delimiter=",")
amostras1000 = np.genfromtxt("../arquivos_texto/1000amostras.csv", delimiter=",")
amostras10000 = np.genfromtxt("../arquivos_texto/10000amostras.csv", delimiter=",")
reoa = np.genfromtxt("../arquivos_texto/robusto_reoa.csv", delimiter=",")


"""
    Gráfico linhas Finas
"""

# é retornado um subplot na posião 1, sendo que o plot terá 1 linha e 2 colunas
plt.subplot(1, 2, 1)

# Círculos azuis vazados
plt.scatter(
    amostras13[:, 0],
    amostras13[:, 1],
    label="WCSA for 13 samples",
    marker="o",
    facecolor="none",
    edgecolors="#0000FF",
    s=80,
)

# Estrelas amarelas
plt.scatter(
    amostras1000[:, 0],
    amostras1000[:, 1],
    label="WCSA for 1000 samples",
    marker=(8, 2, 0),
    c="#FFFF00",
    s=160,
)

texto()

# é retornado um subplot na posião 2, sendo que o plot terá 1 linha e 2 colunas
plt.subplot(1, 2, 2)

# Losangos verdes vazados
plt.scatter(
    amostras10000[:, 0],
    amostras10000[:, 1],
    label="WCSA for 10000 samples",
    marker="D",
    facecolor="none",
    edgecolors="#00FF00",
    s=80,
)

# Quadrados vermelhos vazados
plt.scatter(
    reoa[:, 0],
    reoa[:, 1],
    label="REOA",
    marker="s",
    facecolor="none",
    edgecolors="#FF0000",
    s=80,
)

texto()

plt.show()

# plt.savefig('teste.svg')
