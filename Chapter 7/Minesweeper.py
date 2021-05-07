# The play functionality is not implemented, however this can provide insights about
# the structure of the game.
import time
import random


class Game:
    def __init__(self, size, player):
        self.size = size
        self.start_time = None
        self.start_timer()
        self.player = player
        self.board = Board(size)
        self.game_status = True

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        end = time.time()
        print('Time:', end - self.start_time)

    def start_game(self):
        print('Playing as: ', player.name)
        self.board.print_board()

    def play(self, row, col):
        print(player.name, 'is playing ...')
        if self.game_status:
            self.board.print_board()
            self.game_status = self.board.update_board(row, col)
        else:
            print('Error, you already lose')



class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for i in range(size)]
        self.number_bombs = size
        self.number_flags = size
        self.end = False
        self.init_board()

    def print_board(self):
        for row in range (self.size):
            for col in range (self.size):
                print(self.board[row][col].state, end= ' ')
            print()
        print()

    def init_board(self):
        for row in range(self.size):
            for col in range(self.size):
                cell_bomb = Cell('Bomb')
                cell_none = Cell('None')
                if row == col:
                    self.board[row][col] = cell_bomb
                else:
                    self.board[row][col] = cell_none
            print()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.board)
        for sublist in self.board:
            random.shuffle(sublist)

    def update_board(self, row, col):
        if self.end:
            print('Game Over')
        else:
            random_number = random.randint(1, 5)
            if self.board[row][col].state == 'None':
                self.board[row][col] = Cell(' ' + str(random_number) + '  ')
            elif self.board[row][col].state == 'Bomb':
                print('Game Over')
                return False
        return True


class Cell:
    def __init__(self, state):
        self.state = state


class Player:
    def __init__(self, name):
        self.name = name


player = Player('Player')
game = Game(7, player)
game.start_timer()
game.start_game()
game.play(4, 5)
game.play(1, 6)
game.play(2, 0)
game.play(3, 6)
game.play(4, 0)
game.play(4, 1)
game.end_timer()