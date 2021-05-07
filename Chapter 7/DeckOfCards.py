import random
from collections import Counter


class Card:
    def __init__(self):
        self.suit_list = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Deck:
    def __init__(self):
        self.size = 52
        self.deck = Counter()
        self.init_deck()

    def init_deck(self):
        print('Initializing deck ...')
        self.deck.clear()
        card = Card()
        for i in card.suit_list:
            for j in card.number_list:
                self.deck[(j, i)] = 1
        self.shuffle()
        print("Shuffling deck ...")
        print("I am playing with my Deck of " + str(self.size) + " cards ... ")

    def shuffle(self):
        keys = list(self.deck.keys())
        random.shuffle(keys)

        shuffled_deck = dict()
        for key in keys:
            shuffled_deck.update({key: self.deck[key]})
        self.deck = shuffled_deck

    def show_deck(self):
        print(self.deck)


class BlackJack(Deck):

    def __init__(self):
        Deck.__init__(self)
        self.opponent = []
        self.player = []

    def check_scores(self, player_score, opponent_score):
        if player_score > 21 and opponent_score > 21:
            print('Both Lost!')
            return True
        if player_score == 21 or opponent_score > 21:
            print('Winner: Player')
            print('Looser: Opponent')
            return True
        if opponent_score == 21 or player_score > 21:
            print('Winner: Opponent')
            print('Looser: Player')
            return True
        return False

    def play(self):
        print('I am playing BlackJack ... ')
        self.initialize_game()
        for card in self.deck:
            if self.deck[card] > 0:
                print('Sum of Player: ' + str(sum(self.player)))
                print('Sum of Opponent: ' + str(sum(self.opponent)))

                if self.check_scores(sum(self.player), sum(self.opponent)):
                    print('End Game')
                    return

                answer = input("Would you like to take another card? (Yes or No): ").lower()
                if answer == 'yes':
                    self.player.append(int(card[0]))
                    self.opponent.append(int(card[0]))
                    continue
                else:
                    self.opponent.append(int(card[0]))
                    break

        print('Sum of Player: ' + str(sum(self.player)))
        print('Sum of Opponent: ' + str(sum(self.opponent)))
        if sum(self.player) > sum(self.opponent):
            print('Winner: Player')
            print('Looser: Opponent')
        else:
            print('Winner: Opponent')
            print('Looser: Player')
        print('End Game')
        return

    def initialize_game(self):
        self.player.append(list(self.deck.keys())[0][0])
        self.opponent.append(list(self.deck.keys())[1][0])
        self.player.append(list(self.deck.keys())[2][0])
        self.opponent.append(list(self.deck.keys())[3][0])
        count = 0
        for card in self.deck:
            if count < 4:
                self.deck[card] = 0
                count += 1
            else:
                break


deck = BlackJack()
deck.play()