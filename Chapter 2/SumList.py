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


def append_to_beginning(list, data):
    node = Node(data)
    node.next = list.head
    list.head = node
    return list


def sum_list(one, two):
    one_head = one.head
    two_head = two.head
    result = LinkedList()
    carry = 0

    count_one = 0
    count_two = 0

    while one_head is not None:
        count_one += 1
        one_head = one_head.next

    while two_head is not None:
        count_two += 1
        two_head = two_head.next

    if count_one > count_two:
        for i in range(count_one - count_two):
            two = append_to_beginning(two, 0)
    else:
        for i in range(count_two - count_one):
            one = append_to_beginning(one, 0)

    one_head = one.head
    two_head = two.head
    while one_head != None and two_head != None:
        res = (one_head.data + two_head.data + carry) % 10
        result.append_to_end(res)
        if res > 0:
            carry = 1
        else:
            carry = 0
        one_head = one_head.next
        two_head = two_head.next

    return result


ll1 = LinkedList()
ll1.append_to_end(7)
ll1.append_to_end(1)
ll1.append_to_end(6)

ll2 = LinkedList()
ll2.append_to_end(5)
ll2.append_to_end(9)
ll2.append_to_end(2)
ll2.append_to_end(2)

append_to_beginning(ll1, 0)
ll1.print_list()
ll2.print_list()
sum_list(ll1, ll2).print_list()
