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
        print(temp.data, end="->")
        temp = temp.next
    print()


def insert_at_end(node, data):
    temp = node
    
    while temp.next:
        temp = temp.next
    new_node = LinkedList(data)
    temp.next = new_node

print("Before Inserting")
traverse_linkedlist(a)

insert_at_end(a, 'E')

print("After Inserting")
traverse_linkedlist(a)




        