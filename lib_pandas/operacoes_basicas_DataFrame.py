import pandas as pd
import numpy as np
import pydataset


def avaliar_cada_linha_df():
    df = pd.DataFrame(
        {
            "semestre 1": [1, 2, 3, 4, 5, 6, 7],
            "semestre 2": [4, 5, 1, 7, 2, 8, 9],
            "semestre 3": [7, 8, 4, 8, 3, 8, 1],
            "semestre 4": [6, 4, 2, 6, 8, 2, 7],
        }
    )

    print("adicionar mais duas colunas com o valor minino e máximo de cada linha")

    # uma maneira de avaliar cada linha
    df["minimo 3-4"] = df[["semestre 3", "semestre 4"]].min(axis=1)

    # outra maneira de avaliar cada linha
    df["maximo 1-2"] = df.iloc[:, 0:2].max(axis=1)

    df["media"] = df.iloc[:].mean(axis=1)

    print(df)

    # seleciona registros em que o valor do semestre 1 é igual ou menor que 4
    print(df[df["semestre 1"] <= 4])


def criar_DataFrame():
    df = pd.DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], columns=["dados 1", "dados 2"])
    print(df)

    """
        Iteratively appending rows to a DataFrame can be more computationally intensive
        than a single concatenate. A better solution is to append those rows to a list and
        then concatenate the list with the original DataFrame all at once.
        https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html
    """

    df2 = pd.DataFrame([[3, 5], [11, 5]], columns=["dados 1", "dados 2"])
    df = df.append(df2, ignore_index=True)

    print(df)

    """
         Generate a DataFrame from multiple data sources, more efficient:
         https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html
    """
    df2 = pd.concat(
        [pd.DataFrame([[i, j]], columns=list("AB")) for i, j in enumerate(range(5))],
        ignore_index=True,
    )
    print(df2)


def axis_array():
    a = np.array([[1, 5, 2, 7], [2, 7, 8, 3], [7, 9, 3, 4], [7, 5, 6, 7]])

    print(np.mean(a, axis=1))
    print(a.mean(axis=0))


def converter_DF_to_list():
    # usar dataset iris do pydataset
    iris = pydataset.data("iris")

    # converter dataframe para list
    iris["Species"] = iris["Species"].map(
        {"setosa": 0, "versicolor": 1, "virginica": 2}
    )
    x = np.array(iris.iloc[:, :4].values.tolist())
    y = np.array(iris.iloc[:, 4].values.tolist())

    print(x)
    print(y)


# avaliar_cada_linha_df()
# axis_array()
# criar_DataFrame()
converter_DF_to_list()
