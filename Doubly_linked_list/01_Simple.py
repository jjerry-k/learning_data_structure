class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

head_node = Node(2)
node1 = Node(6)
node2 = Node(8)
node3 = Node(12)
tail_node = Node(1)


head_node.next = node1
node1.prev, node1.next = head_node, node2
node2.prev, node2.next = node1, node3
node3.prev, node3.next = node2, tail_node
tail_node.prev = node3

iterator = head_node

txt = ""
while iterator:
    txt += f"| {iterator.data} "
    iterator = iterator.next
txt += "|"
print(txt)

print("======================")


iterator = tail_node

txt = ""
while iterator:
    txt += f"| {iterator.data} "
    iterator = iterator.prev
txt += "|"
print(txt)