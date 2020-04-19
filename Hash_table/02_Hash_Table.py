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
    
    def find_node_with_key(self, key):
        iterator = self.head   

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

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

class Hash_Table:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [Linked_List() for _ in range(self._capacity)]
    
    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

    def _hash_function(self, key):
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def _look_up_node(self, key):
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        return self._look_up_node(key).value
    
    def insert(self, key, value):
        existing_node = self._look_up_node(key)

        if existing_node is not None:
            existing_node.value = value
        else:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)
    
    def delete_by_key(self, key):
        existing_node = self._look_up_node(key)
        if existing_node is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(existing_node)

test_scores = Hash_Table(50)

test_scores.insert("현승", 85)
test_scores.insert("태호", 90)
test_scores.insert("지웅", 99)
test_scores.insert("규식", 97)
test_scores.insert("신의", 88)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
print(test_scores)

print("===================")
test_scores.delete_by_key("현승")
test_scores.delete_by_key("태호")
test_scores.delete_by_key("지웅")
print(test_scores)