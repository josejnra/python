import matplotlib.pyplot as plt
import numpy as np
import pydataset
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle


def titanic():
    dados = pydataset.data("titanic")
    dados = shuffle(dados)

    """
        Tratar dados
    """

    # mudar sexo
    dados["sex"] = dados["sex"].map({"women": 0, "man": 1})

    # mudar idade
    dados["age"] = dados["age"].map({"child": 0, "adults": 1})

    # mudar survived
    dados["survived"] = dados["survived"].map({"no": 0, "yes": 1})

    # mudar class
    dados["class"] = dados["class"].map(
        {"1st class": 0, "2nd class": 1, "3rd class": 2}
    )

    k = 3
    p = 0.6
    limite = int(len(dados) * p)

    print("limite: %d" % limite)

    treinamento, teste = dados.iloc[:limite], dados.iloc[limite:]

    print("treinamento: %d" % len(treinamento))
    print("teste: %d" % len(teste))

    knn = KNeighborsClassifier(n_neighbors=k)
    """
        Treinar
    """
    x = treinamento.iloc[:, 0:3]
    y = treinamento.iloc[:, 3]

    knn.fit(x, y)

    """
        Classificar
    """
    i = teste.iloc[:, :3]
    j = teste.iloc[:, 3]
    predicted = knn.predict(i)

    print("eficiência titanic: %.2f" % accuracy_score(j, predicted))

    print(
        "eficiência titanic: {}".format(
            cross_val_score(knn, x, y, cv=10, scoring="accuracy")
        )
    )


def titanic2():
    dados = pydataset.data("titanic")
    dados = shuffle(dados)

    """
        Tratar dados
    """

    # mudar sexo
    dados["sex"] = dados["sex"].map({"women": 0, "man": 1})

    # mudar idade
    dados["age"] = dados["age"].map({"child": 0, "adults": 1})

    # mudar survived
    dados["survived"] = dados["survived"].map({"no": 0, "yes": 1})

    # mudar class
    dados["class"] = dados["class"].map(
        {"1st class": 0, "2nd class": 1, "3rd class": 2}
    )

    x = np.array(dados.iloc[:, :3].values.tolist())
    y = np.array(dados.iloc[:, 3].values.tolist())

    """
        Classificar
    """

    k_range = range(1, 101)
    k_score = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, x, y, cv=10, scoring="accuracy", n_jobs=-1)
        k_score.append(scores.mean())
    # print(k_score)

    plt.plot(k_range, k_score)
    plt.xlabel("Value of K for KNN")
    plt.ylabel("Cross Val Accuracy")

    plt.show()


# titanic()
# titanic2()
