class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    

a = Node(10)
b = Node(6)
c = Node(2)
d = Node(3)

a.next = b
b.next = c
c.next = d


def sum_node(node):

    if not node:
        return 0
    val = sum_node(node.next)
    return val + node.data

head = a

print(sum_node(head))
