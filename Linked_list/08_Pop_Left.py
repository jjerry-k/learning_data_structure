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

    def delete_next(self, prev_node):
        
        if prev_node.next is self.tail:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = prev_node.next.next

    def pop_left(self):
        
        pop_data = self.head

        if self.head is self.tail:
            self.head, self.next = None, None
        else:
            self.head = self.head.next
        
        return pop_data

linked_list = Linked_List()

for i in range(5, 10):
    linked_list.append(i)
print(linked_list)

print("=====================")

node_pop = linked_list.pop_left()
print(node_pop.data)
print(linked_list)