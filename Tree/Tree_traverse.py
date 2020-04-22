class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def traverse_pre_order(node):
    """
    print curr node data 
    traverse left child
    traverse right child
    """
    if node:
        print(node.data)
        if node.left_child: traverse_pre_order(node.left_child)
        if node.right_child: traverse_pre_order(node.right_child)

def traverse_post_order(node):
    """ 
    traverse left child
    traverse right child
    print curr node data
    """
    
    if node.left_child: traverse_post_order(node.left_child)
    if node.right_child: traverse_post_order(node.right_child)
    print(node.data)


def traverse_in_order(node):
    if node:
        if node.left_child:
            traverse_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            traverse_in_order(node.right_child)



node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

root_node = node_F

traverse_in_order(root_node)
print("\n")
traverse_pre_order(root_node)
print("\n")
traverse_post_order(root_node)