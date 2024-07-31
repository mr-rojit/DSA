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
i = Node('I')



a.left= b
a.right = c
b.left=d
b.right=e
c.left=f
d.left = g
g.left=i

# """
#         A
#       /   \
#      B      C
#     /  \    /
#    D    E   F
#   /
#  G

# """

def check_balanced(node:Node):
    if not node:
        return [True, 0]
    
    lb = check_balanced(node.left)
    rb = check_balanced(node.right)

    ltb = lb[0]
    rtb = rb[0]
    diff = abs(lb[1] - rb[1]) <=1
    ans = [False, max(lb[1], rb[1]) + 1]

    if ltb and rtb and diff:
        ans[0] = True
        return ans
    return ans
    
print(check_balanced(a))