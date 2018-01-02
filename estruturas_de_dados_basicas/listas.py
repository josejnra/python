# Alguns exemplos de listas em Python
# coding: utf-8

"""
Listas são similares a strings, que são uma sequência de caracteres, no entanto,
diferentemente de strings, os itens de uma lista podem ser de tipos diferentes (heterogêneas).
Listas são mutáveis, enquanto Strings não são.
Para indicar que um objeto é uma lista é utilizado colchetes [].
"""

lista = [1, 2, 3, 4, 5]
print(lista)

print("\nadicionar um novo elemento no final da lista")
lista.append(6)
print(lista)

print("\ninserir um novo elemento em uma posição arbitrária i")
lista.insert(1, 7)
print(lista)

print("\nremover um objeto da lista")
lista.remove(7)
print(lista)

print("\nremover um elemento da lista, porém ele é retornado, caso não seja informado o índice do elemento é último elemento é removido")
print(lista.pop())
print(lista)

print("\ninverter a ordem dos elementos")
lista.reverse()
print(lista)

print("\nodernar por valor")
lista.sort()
print(lista)

print("\nconcatenar com outra lista")
lista_b = [6, 7, 8]
lista.extend(lista_b)
print(lista)

print("\ndescobrir a posição de um elemento: 5")
print(lista.index(5))

print("\napagar todo os elementos da lista")
lista.clear()
print(lista)

print("\npercorrer lista em ordem reversa")
for i in reversed(lista):
    print(i)

print("\npercorrer duas listas em parelelo")
li = lista[:]
for i, j in zip(lista, li):
    print(i, j)

# converter os elementos de uma lista, de string para int
# é utilizado list comprehensions
lista_de_strings = ['1', '2', '5', '4']
print(lista_de_strings)
lista_de_strings = [int(x) for x in lista_de_strings]
print(lista_de_strings)

# copiar lista, não apontará para a mesma lista, utilizar o operador fatiamento (slicing) [:]
# pode ser feito a copia com list comprehensions também [x for x in lista_a_ser_copiada]
# outra forma é com list(lista_a_ser_copiada)
lista_original = [1, 2, 3, 4, 5]
copia_lista = lista_original[:]
copia_lista.append(10)
print(copia_lista)
print(lista_original)

# intersecção de Listas
lista_a = [1,2,3,4,5]
lista_b = [1,3,5,6]
lista_c = list(set(lista_a) & set(lista_b))
print(lista_c)
# [1, 3, 5]

# uniao de Listas
lista_a = [1,2,3,4,5]
lista_b = [1,3,5,6]
lista_c = list(set().union(lista_a,lista_b))
print(lista_c)
# [1, 2, 3, 4, 5, 6]


# inserir ordenado
# importar o módulo bisect
import bisect
a = [1, 2, 4, 5]
bisect.insort(a, 3)
print(a)
# Output: [1, 2, 3, 4, 5]



'''
Listas como pilhas
'''
pilha = [3, 4, 5]
print(pilha)

print('Empilha')
pilha.append(6)
pilha.append(7)
print(pilha)

print('Desempilha')
pilha.pop()
print(pilha)

'''
Listas como filas, porém, listas não são eficientes para esta finalidade.
Embora appends e pops no final da lista sejam rápidos,
fazer inserts ou pops no início da lista é lento (porque todos os
demais elementos têm que ser deslocados).

Para implementar uma fila, use a classe collections.deque que
foi projetada para permitir appends e pops eficientes nas duas extremidades.
'''
from collections import deque
fila = deque(["Eric", "John", "Michael"])

fila.append("Terry")    # Terry chega
fila.append("Graham")   # Graham chega

fila.popleft()          # O primeiro a chegar parte
fila.popleft()          # O segundo a chegar parte

print(fila)             # O resto da fila, em ordem de chegada


'''
Para inserir ordenado pode-se utilizar o módulo bisect.
'''
import bisect

lista_ordenada = []

bisect.insort(lista_ordenada, 10)
bisect.insort(lista_ordenada, 5)
bisect.insort(lista_ordenada, 15)
bisect.insort(lista_ordenada, 35)
bisect.insort(lista_ordenada, 1)

print(lista_ordenada)
