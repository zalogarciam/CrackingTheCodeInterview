
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def in_orderv2(self):
        if self.root != None:
            self.in_order(self.root.left)
            print(self.root.data)
            self.in_order(self.root.right)

    def min_tree(self, list):
        n = len(list)
        if n == 0:
            return None
        if n == 1:
            return Node(list[0])

        middle = n // 2
        root = Node(list[middle])
        root.right = self.min_tree(list[n//2 + 1:])
        root.left = self.min_tree(list[: n//2])

        self.root = root
        return self.root

list = [1, 2, 3 , 4 ,5 ,6, 7]
my_tree = Tree()
my_tree.min_tree(list)
my_tree.in_orderv2()
print(my_tree.root.data)
print(my_tree.root.right.data)
print(my_tree.root.left.data)