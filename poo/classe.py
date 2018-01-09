'''
Classes em python, exemplo com cao
'''

class Cao:
    '''
    O construtor em python é definido pelo método __init__
    O self refere-se a instancia da classe (objeto).
    Sendo obrigatório o self como primeiro argumento em todos métodos.
    Pode ser qualquer palavra, porém é convenção o uso de self.
    '''
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def bark(self):
        print("Woof")

    '''
    Similar o toString de Java, em Python há o __str__.
    Esse método retorna o que será impresso ao passar um objeto Cao para print().
    '''
    def __str__(self):
        return 'nome:'+ self.nome + ' cor:' + self.cor

    '''
    Alternativamente há o __repr__, que basicamente possui o mesmo objetivo do
    __str__, converter um objeto para string.
    O __str__ serve para exibir o objeto para usuário final, usada pelo comando
    print e pela função __str__.
    O __repr__ serve para exibir o objeto para o programador, usada pelo console
    do Python e pela funçao repr.
    Ou seja, geralmente o __repr__ possui mais detalhes que o __str__.
    fonte: https://pt.stackoverflow.com/questions/176464/qual-%C3%A9-a-diferen%C3%A7a-entre-str-e-repr
    '''
    def __repr__(self):
        return 'nome:'+ self.nome + ' cor:' + self.cor

    '''
    Similar ao equals de Java, em Python há o __eq__.
    Esse método retorna se o objeto é igual a outro passado como argumento
    com base na definição do método. No exemplo abaixo um objeto Cao é
    igual a outro se tiverem o mesmo nome.
    '''
    def __eq__(self, other):
        return self.nome == other.nome

'''
Criar objetos da classe Cao
'''
c1 = Cao('koba', "ouro")
c2 = Cao('kobaa', "ouro")

'''
Executar um método da classe é como acessar um atributo.
É feito através de ponto.
'''
print(c1.nome)
c1.bark()


'''
Apesar de c1 e c2 possuirem atributos iguais, eles não referenciam o mesmo objeto.
Ou seja, são objetos diferentes.
'''
print(id(c1))
print(id(c2))

print(c1 == c2)
# imprime False
