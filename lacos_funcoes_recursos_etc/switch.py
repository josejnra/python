"""
Em python não há o comando switch como em C e Java.
Uma forma de conseguir algo próximo a isso é utilizando dicionário.
O que se pode conseguir com isso é alguns valores de retorno, mas não
tem como utilizar trechos de códigos.
"""


def led(x):
    # valor 9 é o valor default
    return {1: 10, 2: 23, 3: 74}.get(x, 9)


print("Procurar por uma chave")
print(led(1))

print("Procurar por uma chave que não existe irá retornar sempre 9")
print(led(4))
