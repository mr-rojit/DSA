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
        print(temp.data, end="->")
        temp = temp.next
    print()


def insert_at_end(node, data):
    temp = node
    
    while temp.next:
        temp = temp.next
    new_node = Node(data)
    temp.next = new_node

head = a

print("Before Inserting")
traverse_linkedlist(head)

insert_at_end(head, 'E')

print("After Inserting")
traverse_linkedlist(head)




        