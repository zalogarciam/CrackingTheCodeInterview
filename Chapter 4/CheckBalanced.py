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

    def insert(self, root, data):
        if root is None:
            self.root = Node(data)
        else:
            if data > root.data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
            else:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)

    def min(self, root):
        if root.left != None:
            return self.min(root.left)
        else:
            return root.data

    def max(self, root):
        if root.right != None:
            return self.max(root.right)
        else:
            return root.data

    # Remove when is a leaf
    # Remove when it has one child
    # Remove when it has two children
    def remove(self, root, data):
        if not root:
            return root
        if root.data > data:
            root.left = self.remove(root.left, data)
        elif root.data < data:
            root.right = self.remove(root.right, data)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            # If both left and right children exist in the node replace its value with
            # the minmimum value in the right subtree. Now delete that minimum node
            # in the right subtree
            tmp = self.min()
            root.data = tmp.data
            root.right = self.remove(root.right, tmp.data)
        return root

    def DFS(self, root, visited):
        if root not in visited and root is not None:
            print(root.data)
            visited.append(root)
            self.DFS(root.left, visited)
            self.DFS(root.right, visited)

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

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.right), self.height(root.left))

    def check_height(self, root):
        if root is None: return -1

        left_height = self.check_height(root.left)
        if left_height == -999: return -999

        right_height = self.check_height(root.right)
        if right_height == -999: return -999

        print(right_height, left_height)

        diff = (left_height - right_height)
        if abs(diff) > 1:
            return -999
        else:
            return max(left_height, right_height) + 1
        
    def is_balanced_tree(self, root):
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        print(left_height, right_height)
        if abs(left_height - right_height) > 1:
            print('Not balanced')
        else:
            print('Balanced')

    def is_balanced_tree_opt(self, root):
        return self.check_height(root) > 1

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

list = [1, 2, 3, 4, 5, 6, 7]
new_tree = Tree()
root_new = new_tree.min_tree(list)
new_tree.is_balanced_tree(root_new)
new_tree.is_balanced_tree(root)
print(new_tree.is_balanced_tree_opt(root_new))
print(new_tree.is_balanced_tree_opt(root_new))
print(tree.is_balanced_tree_opt(root))