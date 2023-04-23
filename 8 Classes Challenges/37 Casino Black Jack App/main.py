"""
Casino Black Jack App:
You are responsible for writing a program that allows a user to play casino Black Jack. The
user will put a set amount of money onto the table and make a minimum $20 bet each hand.
Each hand, the user will be dealt two cards and be given the option to hit or stay. If the user hits
21 or goes over the round will end. The dealer will continue to hit until their hand has a
minimum value of 17 as per casino guidelines. The user will be able to play as long as their
total money is greater than or equal to the minimum bet of the table.
"""

from gameclasses import *

#Welcoming user and informing about minimum bet amount
print("Welcome to the Blackjack App.")
print("The minimum bet at this table is $20.")

#taking user input for money and creating the game object from it
money = int(input("\nHow much money would you like to place on table: "))
game = Game(money)

playing = True
while playing:
    game_deck = Deck()
    game_deck.build_deck() #Building the deck
    game_deck.shuffle_deck() #Shuffling the deck
    
    #Creating player and dealer object
    player = Player()
    dealer = Dealer()
    
    #Displaying money and setting the bet using Game class
    game.display_money()
    game.set_bet()
    
    #Drawing player and dealer hand by using their respective class
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)
    
    #Displaying money and bet amount using Game class and first card
    game.display_money_and_bet()
    
    #Printing first card of dealer
    print("\nThe dealer is showing {} of {}.".format(dealer.hand[0].rank, dealer.hand[0].suit))
    
    #While player is playing their hand displaying hand, getting value of their hand and updating the hand
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)
    
    #allowing dealer to hit till they reach 17
    dealer.hit(game_deck)
    dealer.display_hand()
    
    #Calculating score and finalising payout
    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()
    
    #If game money is less than 20 then stopping the game as minimum bet is 20
    if game.money < 20:
        playing = False
        print("Oh ho, you run out of money. Please try again")