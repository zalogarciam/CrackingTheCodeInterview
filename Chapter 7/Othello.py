class Othello:
    def __init__(self, size):
        self.size = size
        self.empty_piece = Piece('Empty')
        self.capacity = size * size
        self.board = [[self.empty_piece] * size for i in range(size)]
        self.players = []
        self.initialize()

    def print_board(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.board[r][c].color, end=' ')
            print()
        print()

    def add_players(self, p1, p2):
        if len(self.players) > 2:
            print('We can only allow 2 players')
        else:
            self.players.append(p1)
            self.players.append(p2)

    def initialize(self):
        self.board[3][3] = Piece('Black')
        self.board[4][3] = Piece('White')
        self.board[3][4] = Piece('White')
        self.board[4][4] = Piece('Black')

    def play(self, player, row, column):
        if self.capacity == 0:
            print('Game is finished')
            self.check_winner()
        else:
            print(player.name, 'is playing his/her turn ...')
            current_piece = self.board[row][column]
            if current_piece.color == 'Empty':
                self.capacity -= 1
                if player.color == 'Black':
                    self.board[row][column] = Piece('Black')
                    self.check_surrounding_pieces(row, column)
                else:
                    self.board[row][column] = Piece('White')
                    self.check_surrounding_pieces(row, column)
            else:
                print('Error: you cannot put a piece where there is already one ...')

    def check_winner(self):
        player_1 = self.players[0]
        player_2 = self.players[1]
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c].color == player_1.color:
                    player_1.score += 1
                if self.board[r][c].color == player_2.color:
                    player_2.score += 1

        if player_1.score == player_2.score:
            print('No Winner, it is a Tie')
        elif player_1.score > player_2.score:
            print(player_1.name, 'is the Winner')
        else:
            print(player_2.name, 'is the Winner')

    def check_surrounding_pieces(self, row, column):
        current_piece = self.board[row][column]
        if current_piece.color == 'Black':
            search_for = 'White'
        else:
            search_for = 'Black'
        if self.board[row - 1][column].color == search_for:
            if self.board[row - 2][column].color == current_piece.color:
                self.board[row - 1][column].color = current_piece.color
        if self.board[row][column - 1].color == search_for:
            if self.board[row][column - 2].color == current_piece.color:
                self.board[row][column - 1].color = current_piece.color
        if self.board[row + 1][column].color == search_for:
            if self.board[row + 2][column].color == current_piece.color:
                self.board[row + 1][column].color = current_piece.color
        if self.board[row][column + 1].color == search_for:
            if self.board[row][column + 2].color == current_piece.color:
                self.board[row][column + 1].color = current_piece.color


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0


class Piece:
    def __init__(self, color):
        self.color = color

    def flip_color(self):
        if self.color != 'Empty':
            if self.color == 'White':
                self.color = 'Black'
            else:
                self.color = 'White'


player1 = Player('Player 1', 'Black')
player2 = Player('Player 2', 'White')
othello = Othello(8)
othello.add_players(player1, player2)


print('Initial board')
othello.print_board()


othello.play(player1, 5, 3)
othello.print_board()
othello.play(player2, 3, 2)
othello.print_board()
othello.check_winner()
