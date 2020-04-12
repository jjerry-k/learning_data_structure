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


doubly_linked_list = Doubly_Linked_List()
print(doubly_linked_list)

for i in range(5):
    doubly_linked_list.append(i)
    print(doubly_linked_list)

print("=====================")
iterator = doubly_linked_list.tail
txt = ""
while iterator:
    txt += f"| {iterator.data} "
    iterator = iterator.prev
txt += "|"
print(txt)