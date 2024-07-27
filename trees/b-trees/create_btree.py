class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'
    

def build_tree(node=None, side=None):

    if side:
        data = input(f'Enter data for {side} side: ')
    else:
        data = input('Enter data for root node: ')

    if not data:
        return None

    node = Node(data)
    node.left = build_tree(node.left, side='left')
    node.right = build_tree(node.right, side='right')

    return node


root = build_tree()
print(root, root.left, root.right)



