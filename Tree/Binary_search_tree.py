# Left child < Parent node < Right child

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0

def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def print_sorted_tree(self):
        print_inorder(self.root)

    def insert(self, data):
        new_node = Node(data)  

        if self.root is None:
            self.root = new_node
            return

        curr_node = self.root

        while curr_node:
            if data < curr_node.data:
                # left child
                if not curr_node.left_child:
                    curr_node.left_child = new_node
                    new_node.parent = curr_node
                    return
                
                else:
                    curr_node = curr_node.left_child

            else :
                # right child
                if not curr_node.right_child:
                    curr_node.right_child = new_node
                    new_node.parent = curr_node
                    return
                
                else:
                    curr_node = curr_node.right_child

    def search(self, data):
        
        curr_node = self.root

        while curr_node:
            # Start from root node
            # data > current node: right, data < current node: left
            # Iterate

            if data > curr_node.data:
                curr_node = curr_node.right_child
            
            elif data < curr_node.data:
                curr_node = curr_node.left_child
            
            else:
                return curr_node

        return None

    @staticmethod
    def find_min(node):
        
        curr_node = node

        while curr_node.left_child:
            curr_node = curr_node.left_child
        
        return curr_node

# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()

# 노드 탐색과 출력
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))

print(bst.find_min(bst.root).data)
print(bst.find_min(bst.root.right_child).data)