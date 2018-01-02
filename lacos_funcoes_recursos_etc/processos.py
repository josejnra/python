'''
   Criação de processos e como utilizar é bastante semelhante a C
'''

import os

def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
          # Apenas o processo criado (filho) tem acesso a esse bloco de código
         child()
      else:
         # Apenas o processo pai tem acesso a esse bloco de código
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)

      reply = input("q for quit / c for new fork")
      if reply == 'c':
          continue
      else:
          break

parent()
