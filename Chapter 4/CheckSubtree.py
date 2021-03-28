
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

def get_path(root, path):
    if root is not None:
        path.append(root.data)
        get_path(root.left, path)
        get_path(root.right, path)
    return path

def check_subtree_v1(tree1, tree2):
    path2 = get_path(tree2.root, [])
    path1 = get_path(tree1.root, [])
    print(path2, path1)
    first = path2[0]
    j = 1
    flag = False
    for i in range(len(path1)):
        if flag:
            if j >= len(path2):
                print('Not subtree')
                return False

            if path1[i] != path2[j]:
                print('Not subtree')
                return False
            j += 1
        if path1[i] == first:
            flag = True

    if j == len(path2):
        print('Subtree')
        return True
    else:
        print('Not subtree')
        return False

def check_equal(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data == root2.data:
        return check_equal(root1.left, root2.left) and check_equal(root1.right, root2.right)
    else:
        return check_equal(root1.left, root2) or check_equal(root1.right, root2)


def check_subtree_v2(tree1, tree2):
    print(check_equal(tree1.root, tree2.root))


list = [1, 2, 3 , 4 ,5 ,6, 7]
my_tree = Tree()
my_tree.min_tree(list)

list = [5, 6, 7]

my_tree2 = Tree()
my_tree2.min_tree(list)

my_tree2.in_orderv2()
check_subtree_v1(my_tree, my_tree2)
check_subtree_v2(my_tree, my_tree2)