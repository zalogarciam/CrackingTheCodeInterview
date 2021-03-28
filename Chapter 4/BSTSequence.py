
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def permute(self, permutations, options):
        if len(options) == 0:
            return permutations
        total_permutations = []
        for i in range(len(options)):
            option = options[i]
            new_options = options[:i] + options[i + 1:]
            if option.left is not None:
                new_options.append(option.left)
            if option.right is not None:
                new_options.append(option.right)

            new_permutations = []
            print(permutations)
            for permutation in permutations:
                new_permutations.append(permutation.copy())
            print(new_permutations)
            for new_permutation in new_permutations:
                new_permutation.append(option.data)

            total_permutations.extend(self.permute(new_permutations, new_options))
        return total_permutations

    def bst_sequence(self, root):
        return print(self.permute([[]], [root]))


small_tree = Tree()
small_tree.root = Node(2)
small_tree.root.right = Node(3)
small_tree.root.left = Node(1)
small_tree.root.right.right = Node(4)
small_tree.root.left.left = Node(0)
small_tree.bst_sequence(small_tree.root)
print(small_tree.bst_sequence_v2(small_tree.root))