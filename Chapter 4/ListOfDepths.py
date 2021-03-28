
class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        current = self.head
        if self.head is None:
            self.head = LNode(data)
        else:
            while current.next is not None:
                current = current.next
            current.next = LNode(data)

    def print_list(self):
        current = self.head
        show = str(current.data) + ' '
        while current.next is not None:
            current = current.next
            show += str(current.data) + ' '
        print(show)

linked = LinkedList()
linked.add(1)
linked.add(2)
linked.add(3)
linked.add(4)
linked.print_list()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def post_order(self, root):
        if root != None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)

    def min_tree(self, list):
        n = len(list)
        if n == 0:
            return None
        if n == 1:
            return Node(list[0])

        middle = n // 2
        root = Node(list[middle])
        root.right = self.min_tree(list[n // 2 + 1:])
        root.left = self.min_tree(list[: n // 2])

        self.root = root
        return self.root

    def list_of_depths(self, root, level, lists):
        if root != None:
            lists[level].add(root.data)
            self.list_of_depths(root.left, level + 1, lists)
            self.list_of_depths(root.right, level + 1, lists)
            print(root.data, level, lists)

    def list_of_depths_v2(self, root, level , lists):
        if root is not None:
            lists[level].add(root.data)
            self.list_of_depths_v2(root.left, level + 1, lists)
            self.list_of_depths_v2(root.right, level + 1, lists)

        return lists

list = [1, 2, 3 , 4 ,5 ,6, 7]
my_tree = Tree()
my_tree.min_tree(list)
my_tree.post_order(my_tree.root)
lists = [LinkedList() for i in range(3)]
my_tree.list_of_depths(my_tree.root, 0, lists)
res = my_tree.list_of_depths_v2(my_tree.root, 0, lists)
for r in res:
    r.print_list()