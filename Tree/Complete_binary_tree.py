def find_left_child(complete_binary_tree, index):
    if 0 < index * 2 < len(complete_binary_tree):
        return index * 2
    else:
        return None

def find_right_child(complete_binary_tree, index):
    if 0 < 2 * index + 1 < len(complete_binary_tree):
        return 2 * index + 1
    else:
        return None

def find_parent(complete_binary_tree, index):
    if 0 < index // 2 < len(complete_binary_tree):
        return index // 2
    else:
        return None

complete_binary_tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

root_node_index = 1

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

left_child_index = find_left_child(tree, root_node_index)
right_child_index = find_right_child(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

parent_index = find_parent(tree, 9)

print(tree[parent_index])

parent_index = find_parent(tree, 1)  
print(parent_index)

left_child_index = find_left_child(tree, 6)  
print(left_child_index)

right_child_index = find_right_child(tree, 8)  
print(right_child_index)