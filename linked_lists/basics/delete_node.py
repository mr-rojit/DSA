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


def traverse(head):
    temp = head

    while temp:
        print(temp.data)
        temp = temp.next


def delete_node(head, val):
    temp = head

    while(temp and temp.data == val):
        head = temp.next
        temp = temp.next

    while temp and temp.next:
        if temp.next.data == val:
            temp.next = temp.next.next
            temp = temp.next
        else:
            temp = temp.next

    return head
head = a

head = delete_node(head, 'a')

traverse(head)

