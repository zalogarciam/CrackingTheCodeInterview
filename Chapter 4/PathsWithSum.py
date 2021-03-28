
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

    def print_tree(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.print_tree(root.left)
            self.print_tree(root.right)

    def paths_with_sum(self, root, target_sum, tracker_dict, running_total):
        if root is None:
            return 0

        matches = 0
        running_total += root.data
        print(running_total)
        if running_total == target_sum:
            matches += 1

        diff = running_total - target_sum
        if diff in tracker_dict:
            matches += tracker_dict[diff]

        if running_total in tracker_dict:
            tracker_dict[running_total] += 1
        else:
            tracker_dict[running_total] = 1

        print(tracker_dict)
        matches += self.paths_with_sum(root.left, target_sum, tracker_dict, running_total)
        matches += self.paths_with_sum(root.right, target_sum, tracker_dict, running_total)

        tracker_dict[running_total] -= 1
        return matches

    def printVector(self, path, i):
        for j in range(i, len(path)):
            print(path[j], end=" ")
        print()

    def print_paths_sum(self, root, path, sum):
        if (not root):
            return
        path.append(root.data)
        self.print_paths_sum(root.left, path, sum)
        self.print_paths_sum(root.right, path, sum)

        print(path)
        f = 0
        for j in range(len(path) - 1, -1, -1):
            f += path[j]
            if (f == sum):
                self.printVector(path, j)
            print(f)
        path.pop(-1)

    def path_to(self, root, target, path):
        if root is None:
            return None
        path.append(root.data)

        self.path_to(root.left, target, path)
        self.path_to(root.right, target, path)

        if target == path[len(path) - 1]:
            print(path)

        path.pop(-1)

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


mytree = BinaryTree()
root = TreeNode(10)
mytree.root = root
mytree.root.left = TreeNode(5)
mytree.root.right = TreeNode(-3)

mytree.root.left.left = TreeNode(3)
mytree.root.left.right = TreeNode(2)
mytree.root.right.right = TreeNode(11)

mytree.root.left.left.left = TreeNode(3)
mytree.root.left.left.right = TreeNode(-2)
mytree.root.left.right.right = TreeNode(1)
mytree.root.right.right.right = TreeNode(8)

print('Rpta', mytree.paths_with_sum(root, 8, {}, 0))
mytree.print_paths_sum(root, [], 8)
print('Rpta', mytree.path_to(root,  -2, []))
print('Rpta', mytree.path_to(root,  11, []))
print('Rpta', mytree.path_to(root,  2, []))

print(mytree.find_path(root, mytree.root.left.left.right, []))