class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularArray:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            return self.head

    def print(self):
        current = self.head
        if self.head == self.tail:
            print(self.head.data)
        else:
            while current != self.tail:
                print(current.data, end=' ')
                current = current.next
            print(current.data)

    def print_from(self, data):
        node = Node(data)
        current = self.head
        while current.data != node.data:
            current = current.next
        print(current.data, end=' ')
        while current.next.data != data:
            current = current.next
            print(current.data, end=' ')
        print()

    def remove(self, data):
        current = self.head
        if self.head.data == data:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            while current.next != self.tail:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next
            if current.next == self.tail:
                current.next = current.next.next
                self.tail = current


circular_array = CircularArray()
circular_array.insert('3')
circular_array.insert('5')
circular_array.insert('7')
circular_array.insert('1')
circular_array.insert('9')
circular_array.print()
circular_array.print_from('7')
circular_array.print_from('9')
circular_array.print_from('3')
circular_array.remove('3')
circular_array.print()
circular_array.remove('5')
circular_array.print()
circular_array.remove('9')
circular_array.print()