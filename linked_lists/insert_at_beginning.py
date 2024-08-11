class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next:LinkedList | None = None

    def __str__(self):
        return str(self.data)
    

a = LinkedList('A')
b = LinkedList('B')
c = LinkedList('C')
d = LinkedList('D')

a.next = b
b.next = c
c.next = d


def insert_at_beginning(head: LinkedList, data):
    new_node = LinkedList(data)
    new_node.next = head
    return new_node


def traverse(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


head = a

print("Before insering")
traverse(head)

head = insert_at_beginning(head, 'first node yay!!')
head = insert_at_beginning(head, 'Da real first node')


print('After insering')
traverse(head)
