class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

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
            self.tail = new_node
        else:
            new_node.next, prev_node.next = prev_node.next, new_node
        
    def prepend(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next, self.head = self.head, new_node

linked_list = Linked_List()

for i in range(5, 10):
    linked_list.append(i)
print(linked_list)

print("=====================")

linked_list.prepend(32)
print(linked_list)