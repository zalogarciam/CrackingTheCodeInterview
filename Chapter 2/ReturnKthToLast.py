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

    def return_k_to_last(self, k):
        current = self.head
        k_to_last = []

        while current.next is not None:
            if current.data == k:
                k_to_last.append(current.data)
                while current.next is not None:
                    current = current.next
                    k_to_last.append(current.data)
            else:
                current = current.next
        return k_to_last

    def return_k_to_last_v2(self, k):
        p1 = self.head
        p2 = self.head

        count = 0
        while count < (k - 1):
            p1 = p1.next
            count += 1

        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        print(p2.data)


linkedList4 = LinkedList()
linkedList4.append_to_end(2)
linkedList4.append_to_end(4)
linkedList4.append_to_end(5)
linkedList4.append_to_end(8)
linkedList4.append_to_end(9)
linkedList4.append_to_end(10)
print(linkedList4.return_k_to_last(5))
