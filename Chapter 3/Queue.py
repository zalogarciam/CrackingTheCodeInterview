class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self):
        self.head = self.head.next
        if self.head == None:
            self.head = None
            self.tail = None

    def print_list(self):
        current = self.head
        show = ""
        while current != None:
            show += str(current.data) + ' '
            current = current.next
        return show


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.add(1)
print(queue.print_list())
