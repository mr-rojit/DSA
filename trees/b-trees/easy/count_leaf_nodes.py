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


a.left= b
a.right = c
b.left=d
b.right=e
c.left=f
d.left=g


def count_leaf_nodes(node):

    if not node:
        return 0

    if not node.left and not node.right:
        return 1
    left = count_leaf_nodes(node.left)
    right = count_leaf_nodes(node.right)

    print(node.data, left+right)

    return left+right


print(count_leaf_nodes(a))
