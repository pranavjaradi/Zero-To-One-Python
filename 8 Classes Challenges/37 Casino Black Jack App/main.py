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

active = True
while active:
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
    
    