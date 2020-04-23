# Priority queue
# Abstract data type

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

def reverse_heapify(tree, index):
    parent_index = index // 2  
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  
        reverse_heapify(tree, parent_index)  


class PriorityQueue:
    def __init__(self):
        self.heap = [None] 


    def insert(self, data):
        
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap)-1)
        
    def extract_max(self):
        root = 1
        tail = len(self.heap)-1
        swap(self.heap, root, tail)
        val = self.heap.pop()
        heapify(self.heap, root, len(self.heap))
        return val

    def __str__(self):
        return str(self.heap)


# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)

priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())