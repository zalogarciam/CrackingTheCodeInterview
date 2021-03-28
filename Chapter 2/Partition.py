class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_end(self, data):
        current = self.head
        if current == None:
            self.head = Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data)
            
    def print_list(self):
        show = ""
        temp = self.head
        while temp:
            show += str(temp.data) + ' '
            temp = temp.next
        print(show)

    def partition(self, x):
        current = self.head
        list = LinkedList()

        while current is not None:
            if current.data < x:
                list.append_to_end(current.data)
            current = current.next

        current = self.head
        while current is not None:
            if current.data >= x:
                list.append_to_end(current.data)
            current = current.next
        list.print_list()

    def partition2(self, k):
        current = self.head

        after_head = Node(0)
        after = after_head
        before_head = Node(0)
        before = before_head

        while current is not None:
            if current.data < k:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next

            current = current.next
        after.next = None
        before.next = after_head.next
        return before


linkedList6 = LinkedList()
linkedList6.head = Node(3)
second = Node(5)
third = Node(8)
four = Node(5)
five = Node(10)
six = Node(2)
seven = Node(1)
linkedList6.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
six.next = seven

linkedList6.print_list()
linkedList6.partition(5)
linkedList6.partition2(5)
linkedList6.print_list()