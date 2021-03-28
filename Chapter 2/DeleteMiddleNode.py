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

    def delete_middle_node(self, node):
        node.data = node.next.data
        node.next = node.next.next


linkedList5 = LinkedList()
linkedList5.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
linkedList5.head.next = second
second.next = third
third.next = four
four.next = five
linkedList5.print_list()
linkedList5.delete_middle_node(third)
linkedList5.print_list()