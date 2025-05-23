import pandas as pd
import pydataset


def exemplo_simples():

    df = pd.DataFrame(
        [
            ["fchollet/keras", 11302],
            ["opeanai/universe", 4350],
            ["pandas-dev/pandas", 8168],
        ],
        columns=["repository", "stars"],
    )

    print(f"\nDimensão do dataframe, (linhas, colunas): \n{df.shape}")

    print(f"\nDataframe: \n{df}")

    print("\nImpressão de uma das colunas: \n{}".format(df["stars"]))

    print(f"\nBusca pelo índice: \n{df.iloc[0]}")


def mexendo_com_datasets():

    print("Todos conjuntos de dataset existente na lib")
    print(pydataset.data())

    # recupera o dataset titanic
    titanic = pydataset.data("titanic")

    print("\nImprime os 5 primeiros registros:")
    print(titanic.head())

    print("\nLocaliza quais registros atendem a condição - INDEXAÇÃO BOOLEANA:")
    print(titanic.loc[titanic["sex"] == "man"])

    print("\nNúmero de objetos únicos da coluna class:")
    print("{}".format(titanic["class"].value_counts()))

    print("\nMemória ocupada em bytes para cada coluna:")
    print(f"{titanic.memory_usage()}")

    print("\nMemória total ocupada pelo dataframe:")
    print("{} MB".format(round(float(titanic["sex"].nbytes * 5 / 1024), 3)))

    print("\nMemória ocupada por um registro do dataframe:")
    print(f"{titanic.iloc[0].nbytes} Bytes")


mexendo_com_datasets()
# exemplo_simples()
