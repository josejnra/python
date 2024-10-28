"""
Lista Encadeada (Linked List)
fonte: https://stackoverflow.com/questions/280243/python-linked-list
"""


# nó da lista
class Node:
    def __init__(self, data):
        self.data = data  # holds the data
        self.next = None  # contains the reference to the next node


# a lista encadeada
class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    # adicionar um novo nó na lista
    def add_node(self, data):
        # cria um novo nó apontando para ninguém
        new_node = Node(data)

        # variável last_node irá apontar para o novo nó, assim a lista pode recuperar
        # o último nó sem precisar percorrer toda a lista
        self.last_node = new_node

        # se a lista estiver vazia, adiciona o novo nó e termina
        if self.first_node == None:
            self.first_node = new_node
            return

        # lista não está vazia, então percorre a lista até o último nó
        node_aux = self.first_node
        while node_aux.next != None:
            node_aux = node_aux.next

        # último nó da lista irá apontar para o novo nó
        node_aux.next = new_node

    # imprime lista
    def list_print(self):
        node = self.first_node  # cant point to ll!
        while node:
            print(node.data)
            node = node.next

    def reverse(self):
        prev = None
        current = self.first_node
        self.first_node = self.last_node
        self.last_node = current

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node


ll = LinkedList()

# add elementos
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

# imprime lista
ll.list_print()

print("reverse order:")
# inverte a lista
ll.reverse()
# imprime lista
ll.list_print()
