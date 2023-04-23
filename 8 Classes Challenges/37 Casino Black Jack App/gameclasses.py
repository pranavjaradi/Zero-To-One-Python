import random
import time

class Card():
    """
    Card class which will create a card object and a method to print card info
    """
    def __init__(self, rank, value, suit):
        """
        Card object creation, taking rank, value and suit of card

        Args:
            rank (string): It will be rank of card which will have values (2-10, J ,Q ,K ,A)
            value (integer): Value of each will the corresponding value of the card.
            suit (string): It is suit of the card viz. hearts, spades, clubs, and diamonds
        """
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        """
        Printing the card information eg: K of Hearts, 10 of Spades etc.
        """
        print("{} of {}".format(self.rank, self.suit))

class Deck():
    """
    Deck class for building, shuffling deck and dealing card
    """
    def __init__(self):
        """
        Contains list of deck of cards
        """
        self.cards = []

    def build_deck(self):
        """
        Build a deck containing 13 cards of each of 4 deck equivalent to total 52 cards.
        """
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        ranks = {'A' : 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8' : 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}
        
        #Looping through each suit to build deck using dictionary
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        """Generating a shuffled card using random module
        """
        random.shuffle(self.cards)
    
    def deal_card(self):
        """Dealing a card from deck of cards
    
        Returns:
            object: Instance of class Card.
        """
        return self.cards.pop()



class Player():
    """A class for user playing Black Jack
    """
    def __init__(self):
        """Initialise the player
        """
        self.hand = [] #List for player's card
        self.hand_value = 0 #Total value of player hand
        self.playing_hand = True #Bool to track if player is playing hand or not
    
    def draw_hand(self, deck):
        """Deal the player the starting hand

        Args:
            deck (list): Deck of card
        """
        for i in range(2):
            #Two cards are must for game to start
            card = deck.deal_card()
            self.hand.append(card)
    
    def display_hand(self):
        """Show the players hand"""
        print("\nPlayer's hand: ")
        for card in self.hand:
            card.display_card()
    
    def hit(self, deck):
        """Give a new card to player"""
        card = deck.deal_card()
        self.hand.append(card)
    
    def get_hand_value(self):
        """Compute the hand value"""
        self.hand_value = 0
        ace_in_hand = False #bool to track if player have an ace
        for card in self.hand:
            self.hand_value += card.value
            if card == 'A':
                #checked for ace
                ace_in_hand = True
        
        if self.hand_value > 21 and ace_in_hand == True:
            #Treating ace value 1 if hand value is more than 21 and player has an ace
            self.hand_value -= 10 #Ace value is 11 but treating here as 1 so deducting 1-
        
        print("Total value: {}".format(self.hand_value))
    
    def update_hand(self, deck):
        """Updating hannd of player by allowing them to hit

        Args:
            deck (list): Deck of cards
        """
        #The player has option to hit
        if self.hand_value < 21:
            choice = input("Would you like to hit(y/n): ").lower()
            if choice.startswith('y'):
                self.hit(deck)
            else:
                self.playing_hand = False
        #player is over 21, can not hit again
        else:
            self.playing_hand = False


class Dealer():
    """Simulating dealer, must hit up to 7 and they must reveal their first card.
    """
    def __init__(self):
        """Initialise the Dealer
        """
        self.hand = [] #List for dealer's card
        self.hand_value = 0 #Total value of hand
        self.playing_hand = True #Bool
    
    def draw_hand(self, deck):
        """Deal the dealer the starting hand

        Args:
            deck (list): Deck of card
        """
        for i in range(2):
            #Two cards are must for game to start
            card = deck.deal_card()
            self.hand.append(card)
    
    def display_hand(self):
        """Show the dealers hand one card at a time"""
        input("Press enter to reveal the dealers hand. ")
        for card in self.hand:
            card.display_card()
            time.sleep(2) #Building suspense
    
    def hit(self, deck):
        """The dealer must hit until they reach 17, then they must stop.

        Args:
            deck (list): deck of cards
        """
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("Dealer is set with a total of {} cards.".format(len(self.hand)))
    
    def get_hand_value(self):
        """Compute the hand value"""
        self.hand_value = 0
        ace_in_hand = False #bool to track if player have an ace
        for card in self.hand:
            self.hand_value += card.value
            if card == 'A':
                #checked for ace
                ace_in_hand = True
        
        if self.hand_value > 21 and ace_in_hand == True:
            #Treating ace value 1 if hand value is more than 21 and player has an ace
            self.hand_value -= 10 #Ace value is 11 but treating here as 1 so deducting 1-


class Game():
    """Class for handling bet and payout
    """
    def __init__(self, money):
        """Initialising the game class with game money and bet amount.

        Args:
            money (integer): Money from which player is starting the game.
        """
        self.money = int(money)
        self.bet = 20 #Min bet is 20
        winner = "" #a blank string
    
    def set_bet(self):
        """Setting the bet amount.
        """
        betting = True
        while betting:
            bet = int(input("What would you like to bet (minimum bet of 20): "))
            if bet < 20:
                bet = 20
            
            if bet > self.money:
                print("Sorry! You can not afford the bet.")
            else:
                self.bet = bet
                betting = False
    
    def scoring(self, p_hand_val, d_hand_val):
        """Method for determining the winner of game

        Args:
            p_hand_val (int): Player hand value
            d_hand_val (int): Dealer hand value
        """
        if p_hand_val == 21:
            print("Congrats! Player got the BlackJack. You win!")
            self.winner = 'p' #Player is winner if their hand value is 21
        elif d_hand_val == 21:
            print("Oh! Dealer got the BlackJack. You loose!")
            self.winner = 'd' #Dealer is winner if their hand value is 21
        elif p_hand_val > 21:
            print("Your hand value is more than 21. You loose")
            self.winner = 'd'
        elif d_hand_val > 21:
            print("Dealer hand value is more than 21. You win!")
            self.winner = 'p'
        else:
            #winner will be based on who has more hand value
            if p_hand_val > d_hand_val:
                print("Value of players hand is {} and dealers hand is {}. You win!".format(p_hand_val, d_hand_val))
                self.winner = 'p'
            elif p_hand_val < d_hand_val:
                print("Value of players hand is {} and dealers hand is {}. You loose!".format(p_hand_val, d_hand_val))
                self.winner = 'd'
            else:
                print("Value of hand for both player and dealer is {}.".format(p_hand_val))
                self.winner = 'tie'
    
    def payout(self):
        """Increasing the money if player won otherwise deducting it.
        """
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet
    
    def display_money(self):
        """Displaying the current money player has
        """
        print("\nThe current money with player is {}.".format(self.money))
    
    def display_money_and_bet(self):
        """Displaying the current money user has and the current bet amount
        """
        print("\nThe current money with player is {}.".format(self.money))
        print("The current bet amount is {}.".format(self.bet))