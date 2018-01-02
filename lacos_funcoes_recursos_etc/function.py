# Declarações de funções são feitas usando o comando def
def sum(a, b):
    return a + b

c = sum(1, 3)
print(c)

# funções com valores padrões para seus argumentos
def nome_completo(primeiro_nome, segundo_nome = "nunes"):
    return (primeiro_nome + " " + segundo_nome)


# funções com quantidade indefinidade de argumentos
# o asterico transforma elementos de uma lista em argumentos de uma função
# realizando um desempacotamento dos elementos
def foo(*args):
    return sum(*args)

# funções lambda
a = lambda x: x*2

print(nome_completo("jose", "rodrigues"))
print(nome_completo("jose"))
print(foo([1, 2, 3, 4, 5, 6]))
print(a(10))
input("Presione ENTER para sair...")
