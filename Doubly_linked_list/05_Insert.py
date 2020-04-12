class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str

    def append(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_value_at(self, index):
        
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_value(self, value):
        idx = 0
        iterator = self.head

        while iterator:
            if iterator.data==value:
                return iterator, idx
            else:
                iterator = iterator.next
                idx += 1
        return None, None

    def insert(self, prev_node, data):
        new_node = Node(data)

        if prev_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            prev_node.next.prev = new_node
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node
        
doubly_linked_list = Doubly_Linked_List()

for i in range(5, 10):
    doubly_linked_list.append(i)
print(doubly_linked_list)

print("=====================")

find_node, idx = doubly_linked_list.find_value(7)
if not find_node:
    print("None")
else:
    print(find_node.data, idx)

doubly_linked_list.insert(find_node, 32)
print(doubly_linked_list)

print("=====================")
iterator = doubly_linked_list.tail
txt = ""
while iterator:
    txt += f"| {iterator.data} "
    iterator = iterator.prev
txt += "|"
print(txt)
