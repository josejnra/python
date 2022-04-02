# Importando Matplotlib e Numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score

# Importando o módulo de Regressão Linear do scikit-learn
from sklearn.linear_model import LinearRegression


def preco_pizza():
    # Diâmetros (cm)
    Diametros = [[7], [10], [15], [30], [45]]

    # Preços (R$)
    Precos = [[8], [11], [16], [38.5], [52]]

    # Vvisualizar estes dados construindo um plot
    """
    plt.figure()
    plt.xlabel('Diâmetro(cm)')
    plt.ylabel('Preço(R$)')
    plt.title('Diâmetro x Preço')
    plt.plot(Diametros, Precos, 'k.')
    plt.axis([0, 60, 0, 60])
    plt.grid()
    plt.show()
    """
    # Preparando os dados de treino

    # Vamos chamar de X os dados de diâmetro da Pizza.
    X = [[7], [10], [15], [30], [45]]

    # Vamos chamar de Y os dados de preço da Pizza.
    Y = [[8], [11], [16], [38.5], [52]]

    # Criando o modelo
    modelo = LinearRegression()

    # Treinando o modelo
    modelo.fit(X, Y)

    # Prevendo o preço de uma pizza de 20 cm de diâmetro
    print(
        "Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([20][0])
    )

    # Construindo um scatter plot
    # Coeficientes
    print("Coeficiente: \n", modelo.coef_)

    # MSE (mean square error)
    print("MSE: %.2f" % np.mean((modelo.predict(X) - Y) ** 2))

    # Score de variação: 1 representa predição perfeita
    print("Score de variação: %.2f" % modelo.score(X, Y))

    # Scatter Plot representando a regressão linear
    plt.scatter(X, Y, color="black")
    plt.plot(X, modelo.predict(X), color="blue", linewidth=3)
    plt.xlabel("X")
    plt.ylabel("Y")
    # plt.xticks(())
    # plt.yticks(())
    plt.grid()
    plt.show()


def boston_housing():
    # O dataset boston já está disponível no scikit-learn. Assim, apenas carregá-lo.
    boston = datasets.load_boston()
    # Convertendo o dataset em um DataFrame pandas
    df = pd.DataFrame(boston.data)

    # Convertendo o título das colunas
    df.columns = boston.feature_names

    # Adicionando o preço da casa ao DataFrame
    df["PRICE"] = boston.target

    # Não queremos o preço da casa como variável dependente
    x = df.drop("PRICE", axis=1)

    # Definindo Y (preço das casas)
    y = df.PRICE

    # Criando o objeto de regressão linear
    regr = LinearRegression()

    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

    # Treinando o modelo
    regr.fit(x_treino, y_treino)

    # Prevendo o preço da casa
    previsto = regr.predict(x_teste)

    # Comparando preços originais x preços previstos
    plt.scatter(y_teste, previsto)
    plt.xlabel("Preço")
    plt.ylabel("Preço Previsto")
    plt.title("Preço Original x Preço Previsto")
    plt.grid()
    plt.show()

    # MSE (Mean Squared Error)
    mse1 = np.mean((y_teste - previsto) ** 2)
    print(mse1)


# preco_pizza()
boston_housing()
