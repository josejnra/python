'''
- Conjuntos não possuem elementos repetidos.
- São mutáveis.
- São Heterogêneas.
- Os elementos não são ordenados, não possuindo uma ordem especifica.
- Assim, os elementos não podem ser acessados por indice.
'''

# para 'substituir' um elemento deve-se removê-lo e então inserir o novo
s = {1, 2, 3, 4, "carro"}
s.remove("carro")
s.add("jose")
print(s)

# conjuntos
# opercoes de
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}

print("união")
uniao = s1 | s2
# ou
uniao = s1.union(s2)
print(uniao)

print("intersecção")
intersec = s1 & s2
# ou
intersec = s1.intersection(s2)
print(intersec)


print("diferença simétrica")
# elementos que apenas s1 e s2 tenham, (uniao - intersecção)
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# ou
# use symmetric_difference function on A
A.symmetric_difference(B)
# Output: {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
B.symmetric_difference(A)
# Output: {1, 2, 3, 6, 7, 8}

print("diferença")
# elementos que um conjunto possui que o outro não tem
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)
