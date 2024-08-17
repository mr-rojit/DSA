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


head = a



def traverse_linkedlist(node):
    temp = node
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print()


def insert_at_kth( head, value, k):

    new_node = Node(value)


    if not head:
        head = new_node
        return head
    
    temp = head 

    for _ in range(k-1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node

    return head

    
head = insert_at_kth(head, 'Z', 4)

traverse_linkedlist(head)







