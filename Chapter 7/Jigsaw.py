import random as rnd
from collections import Counter


class Shape:
    INNER = 0
    OUTER = 1
    FLAT = 2


class Piece:
    def __init__(self, top_shape, bot_shape, left_shape, right_shape):
        self.top = top_shape
        self.bot = bot_shape
        self.left = left_shape
        self.right = right_shape

    def print(self):
        print('Top', self.top, 'Bot', self.bot, 'Left', self.left, 'Right', self.right, end=' --- ')

    def check_shape(self):
        count = Counter()
        for shape in range(3):
            if self.top == shape: count[shape] += 1
            if self.bot == shape: count[shape] += 1
            if self.left == shape: count[shape] += 1
            if self.right == shape: count[shape] += 1
        return count


class Jigsaw:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.n_pieces = height * width
        self.pieces = [[None] * width for i in range(self.height)]

    def print_pieces(self):
        for piece in list(self.pieces):
            for item in piece:
                item.print()
            print()

    # I know the board is not well initialized since it is not obeying the rules of corners - flat
    # But it is ok for class structuring purposes. Random numbers will ruin my game for sure
    def init_pieces(self):
        for row in range(self.height):
            for column in range(self.width):
                top = rnd.randint(0, 2)
                bot = rnd.randint(0, 2)
                left = rnd.randint(0, 2)
                right = rnd.randint(0, 2)
                piece = Piece(top, bot, left, right)
                self.pieces[row][column] = piece

    def solve(self):
        for row in range(self.height):
            for column in range(self.width):
                count = self.pieces[row][column].check_shape()
                if count[Shape.OUTER] + count[Shape.INNER] == 4:
                    print('This is a Inside piece')
                    continue
                if count[Shape.FLAT] == 1 and count[Shape.OUTER] == 3 or \
                        count[Shape.FLAT] == 1 and count[Shape.INNER] == 3:
                    print('This is a Border piece')
                    continue
                if count[Shape.FLAT] == 2 and count[Shape.OUTER] == 2 or \
                        count[Shape.FLAT] == 2 and count[Shape.INNER] == 2:
                    print('This is a Corner piece')
                    continue


jigsaw = Jigsaw(6, 4)
jigsaw.init_pieces()
jigsaw.print_pieces()
print()


jigsaw.solve()