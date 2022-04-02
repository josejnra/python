#!/usr/bin/env python3.4

salario = int(input("Salario? "))
imposto = 27

while imposto > 0:
    imposto = input("Imposto em % (ex: 27.5)? ")
    if not imposto:
        imposto = 27
    elif imposto == "s":
        break
    else:
        imposto = float(imposto)

    print("Valor real: {}".format(salario - (salario * (imposto * 0.01))))

input("Presione ENTER para sair...")
