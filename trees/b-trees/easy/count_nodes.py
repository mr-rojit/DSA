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


# a.left= b
# a.right = c
# b.left=d
# b.right=e
# c.left=f
# d.left=g


def count_nodes(node):

    if not node:
        return 0
    left = count_nodes(node.left)
    right = count_nodes(node.right)

    return left + right + 1

nodes = count_nodes(a)

print(nodes)