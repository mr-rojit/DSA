class Node:

    def __init__(self, data):
        self.data = data
        self.prev= None
        self.next = None

    def __str__(self):
        return str(self.data)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.prev=a
b.next=c
c.prev=b
c.next=d
d.prev=c


def traverse(head):
    temp = head

    while temp:
        print(temp.prev, ' <- ',temp.data, ' -> ', temp.next)
        temp = temp.next

head = a

traverse(head)
