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


def loop_detection(list):
    slow = list.head
    fast = list.head

    while slow.next != fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow = slow.next
    fast = fast.next.next

    slow = list.head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    slow = slow.next
    fast = fast.next

    print(slow.data, fast.data)
    return slow


ll7 = LinkedList()
ll7.head = Node(0)
second = Node(1)
third = Node(2)
four = Node(3)
five = Node(4)
six = Node(5)
seven = Node(6)
eight = Node(7)
nine = Node(8)
ten = Node(9)
eleven = Node(10)
twelve = Node(11)
thirteen = Node(12)
fourteen = Node(13)

ll7.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten
ten.next = eleven
eleven.next = twelve
twelve.next = thirteen
thirteen.next = fourteen
fourteen.next = five

loop_detection(ll7)
