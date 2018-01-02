'''
- São delimitados por chaves {} assim como os conjuntos.
- São mutáveis.
- Cada elemento do dicionário é uma combinação chave:valor.
- O dicionário é acessado por suas chaves, diferente das listas que são acessadas por indice.
- Se é adicionado uma nova chave, que já possui no dicionário, o valor
da chave é alterado para o novo valor.
- While values can be of any data type and can repeat, keys must be of immutable type
(string, number or tuple with immutable elements) and must be unique.
'''

d = {'jose':24, 'maria':30, 'pedro':15}
print(d)

print("Acessar valor:")
print(d['jose'])


print("Inserir novos elementos:")
d['jose'] = 20
d['joao'] = 45
print(d)

print("Imprimir valores do dicionário:")
for i in d:
    print(d[i], end=' ')
print()
# ou
print(d.values())

print("Imprimir chaves do dicionário:")
for i in d:
    print(i, end=' ')
print()
#ou
print(d.keys())


print("Pesquisar chave no dicionário:")
print("jose" in d)
# retorna True ou False


print("Ordenar dicionário por valor:")
d = {1:1.1, 2:3.14, 3:2.5, 4:2.8, 5:0.89}
a = sorted(d, key=d.get, reverse=False)
for i in a:
	print(d[i])

