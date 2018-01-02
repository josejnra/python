'''
Os indices das listas podem ser visualizados da seguinte forma:

- - - - - - - - - - - - - - -
| -5 | -4  | -3  | -2  | -1  |  indices negativos
- - - - - - - - - - - - - - -
|  0 |  1  |  2  |  3  |  4  |  indices tradicionais
- - - - - - - - - - - - - - -
|  j |  u  |  l  |  i  |  a  |  lista
- - - - - - - - - - - - - - -

A lista pode ser acessada usando tanto os indices negativos quantos os positivos.

'''

nome = "julia"

print("String sem a ultima letra")
print(nome[:-1])
# irá acessar da esquerda para direita até -1 (não incluso)
# o mesmo resultado pode ser obtido com:
print(nome[:len(nome) - 1])

print("String a partir da segunda letra até a penúltima")
print(nome[1:-1])
# o mesmo resultado pode ser obtido com:
print(nome[-4:len(nome) - 1])

print("String a partir da segunda letra até a penúltima")
print(nome[-1:])
# o mesmo resultado pode ser obtido com:
print(nome[-4:len(nome) - 1])
