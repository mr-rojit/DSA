class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    

a = LinkedList(10)
b = LinkedList(6)
c = LinkedList(2)
d = LinkedList(3)

a.next = b
b.next = c
c.next = d


def sum_node(node):

    if not node:
        return 0
    val = sum_node(node.next)
    return val + node.data

print(sum_node(a))
