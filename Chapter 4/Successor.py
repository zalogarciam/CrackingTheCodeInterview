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

    def pre_order(self, root):
        if root != None:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root != None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)

    def left_most(self, root):
        while root.left is not None:
            root = root.left
        return root.data

    def right_most(self, root):
        while root.right is not None:
            root = root.right
        return root.data

    def successor(self, root, node):
        if node.right is not None:
            return self.left_most(node.right)
        else:
            tmp = Node(None)
            while root is not None:
                if root.data < node.data:
                    root = root.right
                elif root.data > node.data:
                    tmp = root
                    root = root.left
                else:
                    break
            return tmp.data

    def predecessor(self, root, node):
        if node.left is not None:
            return self.right_most(node.left)
        else:
            tmp = Node(node)
            while root is not None:
                if root.data > node.data:
                    root = root.left
                elif root.data < node.data:
                    tmp = root
                    root = root.right
                else:
                    break
            return tmp.data




tree = Tree()
root = Node(20)
tree.root = root
first_left = Node(8)
root.left = first_left
first_right = Node(22)
root.right = first_right

second_left = Node(4)
second_right = Node(12)
first_left.left = second_left
first_left.right = second_right

third_left = Node(10)
third_right = Node(14)

second_right.left = third_left
second_right.right = third_right

third_right_left = Node(21)
third_right_right = Node(24)

first_right.right = third_right_right
first_right.left = third_right_left

print(tree.successor(root, first_left))
print(tree.successor(root, third_left))
print(tree.successor(root, third_right))
print(tree.predecessor(root, first_left))
print(tree.predecessor(root, third_left))
print(tree.predecessor(root, third_right))