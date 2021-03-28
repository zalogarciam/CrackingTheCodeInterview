class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        show = ""
        temp = self.head
        while temp:
            show += str(temp.data) + ' '
            temp = temp.next
        print(show)

    def append_to_end(self, data):
        current = self.head
        if current is None:
            self.head = Node(data)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def remove_duplicates(self):
        current = self.head
        numbers = {current.data: 1}
        while current.next is not None:
            current = current.next
            if current.data not in numbers:
                numbers[current.data] = 1
            else:
                numbers[current.data] += 1

        for number in numbers:
            for i in range(1, numbers[number]):
                self.delete(number)

    def delete(self, data):
        current = self.head

        if current.data == data:
            current.data = None
            self.head = current.next
        else:
            while current.next is not None:
                if current.next.data == data:
                    current.next.data = None
                    current.next = current.next.next
                    break
                else:
                    current = current.next


linkedList3 = LinkedList()
linkedList3.append_to_end(3)
linkedList3.append_to_end(9)
linkedList3.append_to_end(8)
linkedList3.append_to_end(2)
linkedList3.append_to_end(6)
linkedList3.append_to_end(8)
linkedList3.print_list()
linkedList3.remove_duplicates()
linkedList3.print_list()
