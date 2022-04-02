# print("Olá {}!".format(input("Qual é o seu nome? ")))


# Estrutura básica:
# print("Mensagem %s %s") % (variavel1, variavel2)

print("Olá %s como vai %s?" % (input("Qual seu nome? "), input("Outro nome? ")))

# Estrutura básica:
# print("Mensagem {a} {b}".format(a = valor1, b = valor2))

print(
    "Olá {nome} como está {outra}?".format(
        nome=input("Seu nome? "), outra=input("outro nome? ")
    )
)
input("Presione ENTER para sair...")

# Exibir mensagens na mesma linha
print("José Nunes", end=" ")
print("Rodrigues de Assis")

for item in range(0, 10):
    print(item + 1, end=" ")
