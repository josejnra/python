# percorrer listas
nomes = [
    "jose",
    "talita",
    "aline santos",
    "jessica",
    "sabrina",
    "juliana",
    "julia",
    "sasha",
]

print("Listar todos os elementos:")
for nome in nomes:
    # caso a condição seja satisfeita, é pulado para a próxima iteração com o 'continue'
    if nome.startswith("S"):
        continue
    print(nome)

# percorrer intervalos com range()
# abaixo é percorrido a lista do indice 1 ao indice 7
print("\nElementos de um intervalo:")
for x in range(1, len(nomes)):
    print(nomes[x])

# enumerando os elementos de uma coleção
print("\nEnumerando uma coleção:")
for i, nome in enumerate(nomes):
    print(i, nome)

input("\nPress ENTER to leave...")


# iterar de forma decrescente
# O 3º parâmetro ali é o "passo". No caso o Python vai subtraindo de 1 em 1.
# imprime de 14 a 0
for i in range(14, -1, -1):
    print(i)

# da mesma forma pode ser feito para ordem crescente
# imprime de 2 a 10, apenas os pares
for i in range(2, 11, 2):
    print(i)
