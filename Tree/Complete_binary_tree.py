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

# 실행 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = find_left_child(tree, root_node_index)
right_child_index = find_right_child(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = find_parent(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = find_parent(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = find_left_child(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = find_right_child(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)