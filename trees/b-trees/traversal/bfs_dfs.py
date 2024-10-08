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

"""
        A
      /   \
     B      C
    /  \    /
   D    E   F
  /
 G

"""


def bfs(node):
    q = []

    q.append(node)

    while q:
        current = q.pop(0)
        print(current)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

# bfs(a)


def dfs(node):
    stack = []

    stack.append(node)

    while stack:
        current = stack.pop()
        print(current)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

# dfs(a)



def dfs_recursive(node):

    print(node.data)
    
    if not node.left and not node.right:
        return
    
    if node.left:
        left = dfs_recursive(node.left)

    if node.right:
        right = dfs_recursive(node.right)

dfs_recursive(a)