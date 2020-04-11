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


linked_list = Linked_List()
print(linked_list)

for i in range(5):
    linked_list.append(i)
    print(linked_list)