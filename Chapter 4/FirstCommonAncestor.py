
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

    def find_path(self, root , n, path):
        if not root:
            return
        path.append(root.data)

        if root.data == n.data:
            return path
        else:
            if root.left is not None or root.right is not None:
                return self.find_path(root.left, n, path) or self.find_path(root.right ,n, path)
        path.pop(-1)

    def first_common_ancestor_v2(self, root, n1, n2):

        path_n1 = self.find_path(root, n1, [])
        path_n2 = self.find_path(root, n2, [])
        print(path_n1, path_n2)
        ancestor = None
        for i, j in zip(path_n1, path_n2):
            if i == j:
                ancestor = i
        print('Ancestor:', ancestor)

        return path_n1, path_n2

    def first_common_ancestor(self, root, n1, n2):
        if root is None:
            return None
        if root.data == n1.data or root.data == n2.data:
            return root

        left = self.first_common_ancestor(root.left, n1, n2)
        right = self.first_common_ancestor(root.right, n1, n2)

        if left is not None and right is not None:
            return root
        if left is None and right is None:
            return None
        return left if left is not None else right


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

tree.in_orderv2()
print('Answer', tree.first_common_ancestor(root, third_left, first_right).data) # 10 22
print('Answer',tree.first_common_ancestor(root, first_left, first_right).data) #
print('Answer',tree.first_common_ancestor(root, third_right, third_right_right).data) #
print('Answer',tree.first_common_ancestor(root, second_left, second_right).data) #
tree.first_common_ancestor_v2(root, third_left, first_right) # 10 22
tree.first_common_ancestor_v2(root, third_right, third_right_right) # 14 24
tree.first_common_ancestor_v2(root, second_left, second_right) # 14 24