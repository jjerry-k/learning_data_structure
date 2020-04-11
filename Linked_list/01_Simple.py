class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

head_node = Node(2)
node1 = Node(6)
node2 = Node(8)
node3 = Node(12)
tail_node = Node(1)


head_node.next = node1
node1.next = node2
node2.next = node3
node3.next = tail_node

iterator = head_node

while iterator:
    print(iterator.data)
    iterator = iterator.next