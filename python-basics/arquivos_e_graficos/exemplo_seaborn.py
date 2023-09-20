import random

import pandas as pd
import seaborn as sea
from matplotlib import pyplot as plt


def exemplo_basico():
    # Carregando um dos datasets que vem com o Seaborn
    dados = sea.load_dataset("tips")

    # O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
    # sea.jointplot("total_bill", "tip", dados, kind = 'reg')
    sea.jointplot("total_bill", "tip", dados, kind="hex")

    plt.show()


def exemplo_com_pandas():
    # Construindo um dataframe com Pandas
    df = pd.DataFrame()

    # Alimentando o Dataframe com valores aleatórios
    df["a"] = random.sample(range(1, 100), 25)
    df["b"] = random.sample(range(1, 100), 25)

    # Scatter Plot
    # sea.lmplot('a', 'b', data=df, fit_reg=True)

    # Density Plot
    # sea.kdeplot(df.b)

    # sea.kdeplot(df.b, df.a)

    sea.distplot(df.a)

    plt.show()


def dataset_gammas():
    # O método tsplot cria plots a partir de séries temporais
    gammas = sea.load_dataset("gammas")
    sea.tsplot(gammas, "timepoint", "subject", "ROI", "BOLD signal", color="muted")

    plt.grid()
    plt.show()


dataset_gammas()
