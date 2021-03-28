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


class SetOfStacks:
    def __init__(self):
        self.stacks = []
        self.capacity = 3
        self.number_stacks = 0

    def push(self, data):
        if len(self.stacks) == 0:
            stack = Stack()
            stack.push(data)
            self.stacks.append(stack)

        else:
            current_stack = self.stacks[self.number_stacks]
            if current_stack.get_size() >= 3:
                new_stack = Stack()
                new_stack.push(data)
                self.stacks.append(new_stack)
                self.number_stacks += 1
            else:
                current_stack.push(data)

    def pop(self):
        last_index = len(self.stacks) - 1
        last_stack = self.stacks[last_index]
        last_stack.pop()
        if last_stack.get_size() == 0:
            self.number_stacks -= 1
            del self.stacks[last_index]

    def print_list(self):
        show = ""
        for i in range(len(self.stacks)):
            show += "Stack " + str(i+1) + ": "
            stack = self.stacks[i]
            show += stack.print_list()
            show += "\n"
        print(show)


set_of_stacks = SetOfStacks()
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(1)
set_of_stacks.push(0)
set_of_stacks.push(7)
set_of_stacks.push(9)

set_of_stacks.print_list()
set_of_stacks.pop()
set_of_stacks.pop()
set_of_stacks.pop()
set_of_stacks.print_list()