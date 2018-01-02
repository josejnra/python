# importando o módulo math e foi usado um alias para ele (matematica)
# caso seja usado um alias, não poderá ser usado o nome 'original'
import math as matematica

print(matematica.sqrt(9))

# importar um objeto específico de um módulo
from unittest import TestCase
from unittest import mock
from math import log2

print(log2(1024))
input("Presione ENTER para sair...")
