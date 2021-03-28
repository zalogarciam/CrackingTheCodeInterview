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


class MyQueue:
    def __init__(self):
        self.old_stack = Stack()
        self.new_stack = Stack()

    def add(self, data):
        self.old_stack.push(data)
    def print_list(self):
        print('Old stack:', self.old_stack.print_list())
        print('New stack:', self.new_stack.print_list())

    def move_data(self):
        self.new_stack = Stack()
        count = 0
        old_stack_size = self.old_stack.get_size()
        while count < old_stack_size:
            pop_item = self.old_stack.pop()
            if pop_item != None:
                self.new_stack.push(pop_item)
                count += 1

    def remove(self):
        if self.new_stack.get_size() == 0:
            self.move_data()
        self.new_stack.pop()


class MyQueueV2:
    def __init__(self):
        self.old_stack = []
        self.new_stack = []

    def add(self, data):
        self.old_stack.append(data)
        if len(self.new_stack) > 0:
            self.new_stack.insert(0, data)

    def print_list(self):
        print('Old stack:')
        old_show = ''
        new_show = ''
        for i in self.old_stack:
            old_show += str(i) + ' '
        print(old_show)
        print('New stack:')
        for i in self.new_stack:
            new_show += str(i) + ' '
        print(new_show)

    def remove(self):
        if len(self.new_stack) == 0:
            while len(self.old_stack) > 0:
                pop_item = self.old_stack.pop()
                self.new_stack.append(pop_item)

        self.new_stack.pop()

myQueue = MyQueue()
myQueue.add(1)
myQueue.add(6)
myQueue.add(3)
myQueue.add(2)
myQueue.add(4)
myQueue.print_list()
myQueue.remove()
myQueue.print_list()
myQueue.add(10)
myQueue.print_list()
myQueue.remove()
myQueue.remove()
myQueue.print_list()

myQueue = MyQueueV2()
myQueue.add(1)
myQueue.add(5)
myQueue.add(3)
myQueue.add(2)
myQueue.add(6)
myQueue.print_list()
myQueue.remove()
myQueue.print_list()
myQueue.add(10)
myQueue.print_list()
myQueue.remove()
myQueue.remove()
myQueue.print_list()