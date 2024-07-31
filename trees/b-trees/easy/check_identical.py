class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


one = Node(1)
two = Node(2)
three = Node(3)
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)

one.left = two
one.right = three

a1.left = a2
a1.right=a3


def check_identical(node1, node2):

    if not node1 and not node2:
        return True

    if not node1 and node2:
        return False
    
    if node1 and not node2:
        return False
    
    left = check_identical(node1.left, node2.left)
    right = check_identical(node1.right, node2.right)

    if left and right and node1.val == node2.val:
        return True
    return False

print(check_identical(one, a1))

    
