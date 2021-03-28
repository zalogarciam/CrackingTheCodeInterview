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
        root.right = self.min_tree(list[n // 2 + 1:])
        root.left = self.min_tree(list[: n // 2])

        self.root = root
        return self.root

    def validate_bst(self, root, list):
        if root is not None:
            self.validate_bst(root.left, list)
            list.append(root.data)
            self.validate_bst(root.right, list)

        return list

    def check_BST(self, list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                print('Not a BST')
                return
        print('BST')

    def validate_bst_v2(self, root, min, max):
        # Base condition
        if root is None:
            return True

        # if right node exist then check it has
        # correct data or not i.e. right node's data
        # should be greater than root's data
        if min is None and max is not None and root.data >= max.data:
            return False

        # if left node exist then check it has
        # correct data or not i.e. left node's data
        # should be less than root's data
        if max is None and min is not None and root.data <= min.data:
            return False

        # check recursively for every node.
        return self.validate_bst_v2(root.left, min, root) and self.validate_bst_v2(root.right, root, max)

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

list = [1, 2, 3 , 4 ,5 ,6, 7]
new_tree = Tree()
root_new = new_tree.min_tree(list)
list = new_tree.validate_bst(root_new, [])
new_tree.check_BST(list)
print(new_tree.validate_bst_v2(root_new, None, None))
tree.in_orderv2()
