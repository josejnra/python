'''
    Biblioteca que permite plotar gráficos em 2D
'''

from matplotlib import pyplot as plt

import numpy as np


def simpleGraph():
    salario_jose = np.array([100, 200, 300, 500, 400, 150])
    salario_jose_tempo = np.array([1.2, 2, 2.5, 3.2, 3.5, 3.9])
    salario_juliana = np.array([300, 100, 700, 300, 200, 100])
    salario_juliana_tempo = np.array([1.2, 2, 2.5, 3.2, 3.5, 3.9])

    plt.plot(salario_jose_tempo, salario_jose, c='black', ls='',
             marker='s', ms=8, label='Salário José')
    plt.plot(salario_juliana_tempo, salario_juliana, c='red', ls='--',
             marker='o', ms=8, label='Salário Juliana')

    # colocar legenda
    plt.legend(loc='upper left')

    # to show the plot
    #plt.show()

    savePlot(plt)

    # saving the graph
    # plt.savefig('/home/jose/grafico_python.svg')

def scatterGraph():
    x = np.arange(-50.0, 50.0, 0.5)
    #y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
    y = x ** 2
    # tamanho dos pontos
    s = np.random.rand(*x.shape) * 800 + 500

    #plt.scatter(x, y, s, c="g", alpha=0.5, marker='8', label="Luck")
    plt.scatter(x, y, c="g", alpha=0.5, marker='8', label="Luck")
    plt.xlabel("Leprechauns")
    plt.ylabel("Gold")
    plt.legend(loc='upper left')
    plt.show()
    #savePlot(plt)

def savePlot(grafico):
    grafico.savefig('/home/jose/grafico_python.svg')


#simpleGraph()
scatterGraph()
