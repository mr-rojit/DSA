"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""
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


def find_diameter(node):
    if not node:
        return 0
    
    left = find_diameter(node.left)
    right = find_diameter(node.right)
    
