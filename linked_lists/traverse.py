class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    

a = LinkedList('A')
b = LinkedList('B')
c = LinkedList('C')
d = LinkedList('D')

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


traverse_linkedlist(a)

# traverse_recursive(a)



