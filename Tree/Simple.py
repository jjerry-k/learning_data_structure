class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


root_node = Node("A")

root_node.left_child = Node("B")
root_node.right_child = Node("C")

root_node.left_child.left_child = Node("D")
root_node.left_child.right_child = Node("E")

root_node.right_child.right_child = Node("F")

root_node.left_child.right_child.left_child = Node("G")
root_node.left_child.right_child.right_child = Node("H")

test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)