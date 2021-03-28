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


def intersection(l1, l2):
    curr1 = l1.head
    curr2 = l2.head

    count1 = 0
    count2 = 0
    while curr1 != None:
        curr1 = curr1.next
        count1 += 1

    while curr2 != None:
        curr2 = curr2.next
        count2 += 1

    curr1 = l1.head
    curr2 = l2.head

    if count1 < count2:
        for i in range (count2 - count1):
            curr2 = curr2.next
    else:
        for i in range(count1 - count2):
            curr1 = curr1.next

    while curr1 != None:
        if curr1 == curr2:
            print('Intersection:', curr2.data)
            return True
        curr1 = curr1.next
        curr2 = curr2.next
    return False


ll5 = LinkedList()
ll5.head = Node(3)
second = Node(1)
third = Node(5)
four = Node(9)
five = Node(7)
six = Node(2)
seven = Node(1)
ll5.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
six.next = seven

ll6 = LinkedList()
ll6.head = Node(4)
seconds = Node(6)
ll6.head.next = seconds
seconds.next = five
five.next = six
six.next = seven

print(intersection(ll5, ll6))