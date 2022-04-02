import pydataset
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


def iris_com_pydataset():
    dados = pydataset.data("iris")
    # misturar dados do dataset
    # The frac keyword argument specifies the fraction of rows to return in the random sample,
    # so frac=1 means return all rows (in random order).
    # Here, specifying drop=True prevents .reset_index from creating a column containing the old index entries.
    # And reset index.
    # dados = dados.sample(frac=1).reset_index(drop=True)

    # outra forma de embaralhar o dataset
    from sklearn.utils import shuffle

    dados = shuffle(dados)

    # porcentagem que será usado para treino, o resto é teste
    p = 0.7
    # valor de k para classificar novos dados
    k = 5
    limite = int(len(dados) * p)
    # é selecionado os n (limite) primeiros dados para treino, o resto é para teste
    treinamento, teste = dados.iloc[:limite], dados.iloc[limite:]

    # atributos dos casos de treino
    x = treinamento.iloc[:, :4]
    # classifcação(label) dos casos de treino
    y = treinamento.iloc[:, 4]

    # k mais próximos para classifcar
    knn = KNeighborsClassifier(n_neighbors=k)

    # treinar
    knn.fit(x, y)

    # validação
    predicted = knn.predict(teste.iloc[:, :4])
    print("eficiência iris: %.2f" % accuracy_score(teste.iloc[:, 4], predicted))

    # outra forma(mesma coisa que a anterior) de avaliar
    print("eficiência iris: %.2f" % knn.score(teste.iloc[:, :4], teste.iloc[:, 4]))


def iris_com_dataset():
    iris = datasets.load_iris()

    # atributos do dataset
    x = iris.data
    # classificação do dataset
    y = iris.target

    k = 5
    knn = KNeighborsClassifier(n_neighbors=k)

    # cv é o número de folds que é utilizado para o processo de validação cruzada, o mínimo é 2
    # https://pt.wikipedia.org/wiki/Valida%C3%A7%C3%A3o_cruzada
    score = cross_val_score(knn, x, y, cv=3, n_jobs=-1)
    # s = cross_val_predict(knn, x, )
    print(score)


def avaliar_K(k):
    iris = datasets.load_iris()

    # atributos do dataset
    x = iris.data
    # classificação do dataset
    y = iris.target

    # avaliar dataset com k variando de 1 até k (parametro)
    k_range = range(1, k + 1)

    # lista com desempenho de cada valor de k
    k_score = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        # pontução do valor de k para 10 folds
        scores = cross_val_score(knn, x, y, cv=10, scoring="accuracy")
        # é armazenado a média do valores encontrado pela validação cruzada para k
        k_score.append(scores.mean())

    plt.plot(k_range, k_score)
    plt.xlabel("Value of K for KNN")
    plt.ylabel("Cross Val Accuracy")

    # mostrar gráfico para o desempenho de k
    plt.show()


# iris_com_pydataset()
# iris_com_dataset()
avaliar_K(60)
