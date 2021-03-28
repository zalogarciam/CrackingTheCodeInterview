class ThreeStack:
    def __init__(self):
        self.array = []
        self.max_size = 9
        self.number_stacks = 3
        self.current_size = [0, 0, 0]

    def push(self, data):
        if sum(self.current_size) == self.max_size:
            print('Stacks are full.')
        else:
            for i in range(self.number_stacks):
                if self.current_size[i] < (self.max_size // 3):
                    self.array.append(data)
                    self.current_size[i] += 1
                    break
                else:
                    continue

    def pop(self):
        size_per_stack = self.max_size // self.number_stacks

        for i in range (self.number_stacks):
            if self.current_size[i] == size_per_stack:
                continue
            else:
                del self.array[sum(self.current_size) - 1]
                self.current_size[i] -= 1
                break

    def print_list(self):
        div = self.max_size // 3
        stack_list = ""
        for i in range(self.number_stacks):
            separator = 0
            j = div * i
            stack_list += "Stack: " + str(i + 1) + "\n"
            size = self.current_size[i]
            while separator < size:
                stack_list += str(self.array[j]) + ' '
                j += 1
                separator += 1
            stack_list += '\n'
        print(stack_list)


three_stack = ThreeStack()
three_stack.push(2)
three_stack.push(4)
three_stack.push(1)
three_stack.push(0)
three_stack.push(3)
three_stack.push(5)
three_stack.push(9)
three_stack.print_list()
three_stack.pop()
three_stack.print_list()
three_stack.push(10)
three_stack.print_list()