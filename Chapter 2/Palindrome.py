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

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self.head
    
    def palindrome(self):
        reverse = self.reverse()
        curr = self.head
        while curr != None and reverse != None:
            if curr.data != reverse.data:
                return False
            curr = curr.next
            reverse = reverse.next
        return True

    def palindromev2(self):
        curr = self.head
        runner = self.head
        stack = []
        while runner.next != None:
            stack.append(curr.data)
            curr = curr.next
            runner = runner.next.next
            if runner is None:
                break
            if runner.next is None:
                curr = curr.next

        while curr != None:
            item = stack.pop()
            if curr.data != item:
                return False
            curr = curr.next
        return True


ll3 = LinkedList()
ll3.append_to_end(3)
ll3.append_to_end(2)
ll3.append_to_end(1)
ll3.append_to_end(0)
ll3.append_to_end(1)
ll3.append_to_end(2)
ll3.append_to_end(3)
print(ll3.palindrome())
print(ll3.palindromev2())

ll4 = LinkedList()
ll4.append_to_end(3)
ll4.append_to_end(2)
ll4.append_to_end(1)
ll4.append_to_end(1)
ll4.append_to_end(2)
ll4.append_to_end(3)
print(ll4.palindromev2())