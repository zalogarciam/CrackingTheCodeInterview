
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.rnd_node = None

    def insert(self, root, data):
        if root is None:
            root = TreeNode(data)
            return root
        else:
            if root.left is None:
                root.left = TreeNode(data)
                return
            if root.right is None:
                root.right = TreeNode(data)
                return
            return self.insert(root.left, data) and self.insert(root.right, data)

    def get_right_most(self, root):
        if root.right is not None:
            return self.get_right_most(root.right)
        else:
            if root.left is None:
                return root.data
            else:
                return root.left.data


    def insert_v2(self, root, data):
        if not root:
            return TreeNode(data)
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)

            if not node.left:
                node.left = TreeNode(data)
                return node
            if not node.right:
                node.right = TreeNode(data)
                return node

            queue.append(node.left)
            queue.append(node.right)

    def find(self, root, data):
        if root is not None:
            if root.data == data:
                return True
            else:
                return self.find(root.left, data) or self.find(root.right, data)
        return False

    def get_rnd_node(self):
        return self.rnd_node

    def random_node(self, root, rnd):
        if self.count == rnd:
            self.rnd_node = root.data
            return
        else:
            if root.left is not None:
                self.count += 1
                self.random_node(root.left, rnd)
            if root.right is not None:
                self.count += 1
                self.random_node(root.right, rnd)
        return

    def print_tree(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.print_tree(root.left)
            self.print_tree(root.right)

    def get_number_of_nodes(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.get_number_of_nodes(root.right) + self.get_number_of_nodes(root.left)


binary_tree = BinaryTree()
root = TreeNode(0)

binary_tree.insert_v2(root, 1)
binary_tree.insert_v2(root, 2)
binary_tree.insert_v2(root, 3)
binary_tree.insert_v2(root, 4)
binary_tree.insert_v2(root, 5)

binary_tree.insert(binary_tree.root, 3)
binary_tree.insert(binary_tree.root, 4)
binary_tree.insert(binary_tree.root, 5)

print()
binary_tree.print_tree(root)
print()

limit_nodes = binary_tree.get_number_of_nodes(root)
from random import randint
rnd_n = randint(0,limit_nodes - 1)
print(binary_tree.get_right_most(root))

print('Random:', rnd_n)
binary_tree.random_node(root, rnd_n)
print(binary_tree.get_rnd_node())
