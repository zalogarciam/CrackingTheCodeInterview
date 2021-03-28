class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.minimum = []
        self.size = 0

    def get_size(self):
        return self.size

    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.minimum.append(node.data)
        self.size += 1

    def min(self):
        print(min(self.minimum))
        return min(self.minimum)

    def print_list(self):
        current = self.head
        show = ""
        while current != None:
            show += str(current.data) + ' '
            current = current.next
        return show

    def pop(self):
        if self.head == None:
            self.minimum = []
            self.size = 0
            return None
        else:
            tmp = self.head
            self.head = tmp.next
            self.minimum.remove(tmp.data)

            if tmp.data is not None:
                self.size += 1
            return tmp.data



stack = Stack()
stack.push(2)
stack.push(4)
stack.push(3)
stack.push(1)
stack.min()
stack.print_list()
stack.pop()
stack.min()
stack.pop()
stack.min()
stack.print_list()
stack.pop()
stack.min()