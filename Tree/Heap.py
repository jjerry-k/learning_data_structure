# Heap
# Morphological attribute: Complete binary tree
# Heap attribute: Every node > each child node


# Heap Sorting

# left child: i * 2
# right child: i * 2 + 1


def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index

    if (0 < left_child_index < tree_size) and tree[index] < tree[left_child_index]:
        largest = left_child_index
        
    if (0 < right_child_index < tree_size) and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)

# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]
heapify(tree, 2, len(tree))
print(tree)


def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    for index in range(tree_size, 0, -1):
        heapify(tree, index, tree_size)
    
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)

data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)