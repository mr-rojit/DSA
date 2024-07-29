class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'

a = Node(10)
b = Node(8)
c = Node(15)
d = Node(3)
e = Node(9)
f = Node(12)


a.left= b
a.right = c
b.left=d
b.right=e
c.left=f


def tree_sum(node)-> int:

    if not node:
        return 0
    
    left = tree_sum(node.left)
    right = tree_sum(node.right)

    return left + right + node.data

total = tree_sum(a)
print(total)