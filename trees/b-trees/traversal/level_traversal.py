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

def in_order_traversal(node):

    if not node:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

def pre_order_traversal(node):

    if not node:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def post_order_traversal(node):

    if not node:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
 

post_order_traversal(a)

