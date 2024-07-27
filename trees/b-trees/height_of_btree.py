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

def find_height(node)-> int:

    if not node:
        return 0
    
    left = find_height(node.left)

    right = find_height(node.right)

    return 1 + max(left, right)

height = find_height(a)
print(height)