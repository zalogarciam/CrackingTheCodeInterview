class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
            return self.head

    def search(self, data):
        current = self.head
        while current.data != data:
            current = current.next
        return current.data

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


class HashTable:
    def __init__(self, capacity):
        self.dictionary = {}
        self.capacity = capacity

    def add(self, data):
        hash = self.hash_function(data)
        if hash not in self.dictionary:
            linked_list = LinkedList()
            linked_list.insert(data)
            self.dictionary[hash] = linked_list
        else:
            self.dictionary[hash].insert(data)

    def get(self, data):
        linked_list = self.dictionary[self.hash_function(data)]
        return linked_list.search(data)

    def print(self):
        for item in self.dictionary:
            print('Linked List with index', item,':', end=' ')
            self.dictionary[item].print()

    def hash_function(self, data):
        sum = 0
        for char in data:
            sum += ord(char)
        index = sum % self.capacity
        return index


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.print()
print(linked_list.search(5))


hash_table = HashTable(5)
hash_table.add('Mia')
hash_table.add('Ray')
hash_table.add('Ben')
hash_table.add('Ana')
hash_table.add('Bri')
hash_table.print()
print(hash_table.get('Mia'))