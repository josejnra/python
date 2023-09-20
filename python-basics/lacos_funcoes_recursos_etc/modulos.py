"""
Em python um módulo é lido como se fosse um script. Deste modo, sempre que
um módulo for importado será executado como um script. Por isso tomar cuidado
ao importar módulos.

Se o objetivo for criar um módulo que funcione como um script, sendo executando
diretamente, pode ser necessário utilizar __name__ == "__main__". Com isso,
ao executar o módulo, a ordem de execução do script será definida de acordo com
o conteúdo desta condição.

The simplest explanation for the __name__ variable (imho) is the following:
Create the following files.

modulo a
# a.py
import b

and

modulo b
# b.py
print "Hello World from %s!" % __name__
if __name__ == '__main__':
    print "Hello World again from %s!" % __name__

Running them will get you this output:

$ python a.py
Hello World from b!

As you can see, when a module is imported, Python sets globals()['__name__'] in this module to the module's name.
Executando o módulo b como se fosse um script.

$ python b.py
Hello World from __main__!
Hello World again from __main__!

As you can see, when a file is executed, Python sets globals()['__name__'] in this file to "__main__".
Só é executado o que está dentro da condição.

font: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
"""
import sys


def erro(msg):
    print("Erro:", msg)
    sys.exit(1)


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def quadrado(x):
    return x**2


if __name__ == "__main__":
    print(inc(10))
    print(dec(10))
    print(quadrado(5))
    input("Presione ENTER para sair...")
