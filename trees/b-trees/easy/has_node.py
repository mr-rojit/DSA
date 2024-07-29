class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')




a.left= b
a.right = c
b.left=d
b.right=e
c.left=f
d.left = g

# """
#         A
#       /   \
#      B      C
#     /  \    /
#    D    E   F
#   /
#  G

# """

def has_node(node, value)-> bool:

    if not node:
        return False

    if node.data == value:
        return True
    
    left = has_node(node.left, value)
    right = has_node(node.right, value)

    return left or right

is_true = has_node(a, 'P')
print(is_true)