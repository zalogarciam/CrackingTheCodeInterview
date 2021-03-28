class Node():
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

    def sort(self):
        tmp_stack = Stack()
        prev_item = self.pop()
        tmp_stack.push(prev_item)
        while self.get_size() > 0 :
            print('List Self', self.print_list())
            print('List Tmp:', tmp_stack.print_list())

            pop_item = self.pop()
            print("_________________", pop_item, prev_item)
            if pop_item == None :
                break
            if prev_item > pop_item:
                print('Items --> pop_item:', pop_item, 'prev_item', prev_item)
                tmp_stack.push(pop_item)
                prev_item = pop_item
            else:
                prev_item = tmp_stack.pop()
                print('Aqui', pop_item, prev_item)
                while pop_item > prev_item:
                    print('Items --> pop_item:', pop_item, 'prev_item', prev_item)

                    self.push(prev_item)
                    prev_item = tmp_stack.pop()
                    if tmp_stack.get_size() == 0:
                        tmp_stack.push(pop_item)
                        prev_item = pop_item
                        break


        print(tmp_stack.print_list())


sort_stack = Stack()
sort_stack.push(5)
sort_stack.push(4)
sort_stack.push(6)
sort_stack.push(2)
sort_stack.push(3)
print(sort_stack.print_list())
sort_stack.sort()
