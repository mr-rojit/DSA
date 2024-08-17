class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
    

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

head = a

def traverse(head):

    if not head:
        return
    print(head.val)
    traverse(head.next)


def reverse(head):
    current = head
    prev = None

    if not head:
        return

    while current:
        temp = current.next
        current.next = prev
        prev= current
        current = temp
    return prev



print("Before Reversing : ")
traverse(head)

head = reverse(head)

print("After Reversing : ")
traverse(head)



