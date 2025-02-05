# Python recreation of the card game 'War'.
# Each player draws a card from the deck and the player with the highest value card wins (Ace high).

from random import shuffle

# Card
class Card:
    
    # Card has the two class variables suits and values. To create for e.g. 2 of Hearts, pass in Card(2,1).
    suits = ["Spades","Hearts","Diamonds","Clubs"]
    # None are used for the first two indices so that the numeric card values match the list indices
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,value,suit):
        """ instance variables value and suit are ints """
        self.value = value
        self.suit = suit

    # Overridden less than method ( < ). 
    # Also handles cases where card values are the same and then compares by suit.
    def __lt__(self,card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    # Overridden greater than method ( > ). 
    # Also handles cases where card values are the same and then compares by suit.
    def __gt__(self,card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False        

    # Overridden object print method
    def __repr__(self):
        print_value = self.values[self.value] + " of " + self.suits[self.suit]
        return print_value

# Deck
class Deck:
    # Creates a full deck of cards (cards instance variable) and mimics shuffling the deck.
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    # Removes and returns a card from the top of the deck until the deck is empty
    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# Player
class Player:
    # This class keeps track of how many rounds a player has won (wins),
    # the current card a player is holding (card),
    # and the name of the player (name)
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

# Game
class Game:
    
    # Creates a deck, creates objects for Player 1 and Player 2
    def __init__(self):
        name1 = input("Enter player 1 name:\n")
        name2 = input("Enter player 2 name:\n")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    # Prints who won the round
    def wins(self,winner_name):
        winner_string = "{} wins this round!".format(winner_name)
        print(winner_string)

    # Prints what card each player drew
    def draw(self,p1_name,p1_card,p2_name,p2_card):
        cards_drawn = "{} drew: [{}]. {} drew: [{}].".format(p1_name,p1_card,p2_name,p2_card)
        print(cards_drawn)

    # Main game loop logic
    def play_game(self):
        # card variable assigned the Deck instance
        cards = self.deck.cards
        print("Game started. Let's play War!")
        # Game loop
        # While there are 2 or more cards in the deck
        while len(cards) >= 2:
            response = input("Press \'q\' to quit. Press any key to play a round:\n")
            if response == 'q':
                break
            p1c = self.deck.remove_card() 
            p2c = self.deck.remove_card()
            p1n = self.p1.name
            p2n = self.p2.name
            # Print what each player drew
            self.draw(p1n,p1c,p2n,p2c)
            # Compare the drawn cards, increment wins as necessary and print the round winner
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        winner = self.winner(self.p1,self.p2)
        print("Game over. {} won the war!".format(winner))
     
    # Returns the name of the player who won the game
    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "It was a tie. Neither player "
    

# Create a Game instance and call the play_game method to start the game
game = Game()
game.play_game()
