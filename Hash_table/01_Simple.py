class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        res_str = ""

        iterator = self.head

        while iterator is not None:
            res_str += f"{iterator.key}: {iterator.value}\n"
            iterator = iterator.next

        return res_str

    def append(self, key, value):
        
        new_node = Node(key, value)

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

    def delete(self, node_to_delete):

        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

hash_list = Linked_List()

hash_list.append(101, "최지웅")
hash_list.append(204, "강영훈")
hash_list.append(305, "성태호")

print(hash_list)