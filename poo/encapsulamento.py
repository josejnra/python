'''
Em python não há encapsulamento dos atributos, ou seja, todos atributos podem
ser acessador diretamente. Para indicar para o programador que determinado
atributo é para ser considerado privado, é utilizado single underscore.

Há também o double underscores (dunders). Isto é utilizado para evitar colisão
com variáveis com mesmo nomes nas subclasses. Assim, subclasses não herdarão os
atributos com dunders. Para tais atributos serem acessados é necessário uma forma
'diferente' de acesso.

'''

class Encapsulation:
    def __init__(self, a, b, c):
        self.myPublic = a
        self._myProtected = b
        self.__myPrivate = c


myEncapsulation = Encapsulation(1,2,3)

print(myEncapsulation.myPublic)
print(myEncapsulation._myProtected)
print(myEncapsulation._Encapsulation__myPrivate) # Acessar o atributo com dunders
print(myEncapsulation.__myPrivate) # irá dar erro, pois não pode acessar o atributo
# com dunders diretamente


'''
Outro exemplo abaixo, com herança.
'''

class A:
    a = 1  # atributo publico
    __b = 2  # atributo privado a class A


class B(A):
    __c = 3  # atributo privado a B

    def __init__(self):
        print(self.a)
        print(self.__c)
a = A()
print(a.a)  # imprime 1

b = B()
print(b.__b) # Erro, pois __b é privado a classe A.
print(b.__c) # Erro, __c é um atributo privado, somente chamado pela classe.

print(b._B__c) # Imprime __c = 3, muito pouco utilizada, mas existe.


'''
link: http://prorum.com/index.php/2306/python-trata-encapsulamento-programacao-orientada-objeto
'''
