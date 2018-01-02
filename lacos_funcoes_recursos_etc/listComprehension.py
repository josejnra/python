'''
Inspirado em conceitos matemáticos como:
Notação matemática de conjunto, utilizada para descrever um conjunto composto
pelo dobro de cada um dos números naturais de 0 até 9:
                S = {x*2 | x pertence N, x < 10}

Tal notação descreve um conjunto de elementos através de propriedades que
seus elementos devem satisfazer. A expressão acima pode também ser lida como:
S é um conjunto que contém como elementos os dobros de todos números naturais
menores que 10. Resultando no seguinte conjunto:
{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

Em Python, é possível descrevermos uma lista através de uma construção
semelhante à notação matemática para descrição de conjuntos.
Tal construção é chamada de list comprehensions:
'''

S = [x*2 for x in range(0, 10)]
print(S)


'''
Também é permitido que sejam utilizadas expressões condicionais dentro de list comprehensions:
'''
S = [x*2 for x in range(0, 10) if x % 2 == 0]
print(S)


'''
E utilizando o else:
'''
S = [x*2 if x % 2 == 0 else x*3 for x in range(0, 10)]
print(S)


'''
Com isso é possível ler multiplas entradas ao mesmo tempo
'''
vetor_int = [int(x) for x in input().split()]
print(vetor_int)
