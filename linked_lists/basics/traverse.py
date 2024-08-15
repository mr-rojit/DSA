class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d



def traverse_linkedlist(node):
    temp = node
    while temp:
        print(temp.data)
        temp = temp.next

def traverse_recursive(node):
    if not node:
        return
    print(node.data)
    traverse_recursive(node.next)

head = a


traverse_linkedlist(head)

# traverse_recursive(head)



