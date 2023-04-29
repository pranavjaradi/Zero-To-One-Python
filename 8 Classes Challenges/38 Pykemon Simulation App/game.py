"""
Pykemon Simulation App:
You will be responsible for writing a program the emulates playing the hit game Pokemon. Your
program will generate Pykemon creatures randomly. Each Pykemon creature will be one of
three different elemental types: fire, water, or grass. Each Pykemon type will have its own set
of unique moves and each individual Pykemon will have it's one name, health stat, and speed
stat.You will be given one Pykemon and then be tasked with fighting other pykemon until you
run out of health. In the original Pokemon, the user is presented with three Pokemon to choose
from at the start of the game; one of each elemental type. Pykemon is no different. You will
choose your starting Pykemon and then be off on a journey to battle other wild Pykemon until
your Pykemon faints.
"""

from Pykemon import *

#Welcoming the user and setting narrative.
print("Welcome to Pykemon")
print("Can you become the worlds greatest Pykemon Trainer???")
print("\nDon't worry! Prof Eramo is here to help you on your quest.")
print("He would like to gift you your first Pykemon!")
print("Here are three potential Pykemon partners.")
input("Press Enter to know the Pykemons!\n")

playing_main = True #Bool to check if user is playing or not.
while playing_main: #The game loop
    game = Game() #game instance using Game class
    player_pykemon = game.choose_pykemon() #Allowing user to select a pykemon
    print("\nCongratulations Trainer, you have chosen {}!".format(player_pykemon.name))
    input("\nYour journey with {} beings now...Press Enter".format(player_pykemon.name))
    
    while player_pykemon.is_alive:
        #Battling till player pykemon is alive.
        computer_pykemon = game.create_pykemon() #Creating a computer pykemon
        
        #Informing about computer pykemon and its stats to user
        print("\nOH NO! A wild {} has approached!".format(computer_pykemon.name))
        computer_pykemon.show_stats()
        
        while computer_pykemon.is_alive and player_pykemon.is_alive:
            game.battle(player_pykemon, computer_pykemon) #simulating battle of both pykemons
            if computer_pykemon.is_alive and player_pykemon.is_alive:
                player_pykemon.show_stats()
                computer_pykemon.show_stats()
                print("---------------------------------------------")
        
        if player_pykemon.is_alive:
            game.battles_won += 1
    
    #Displaying the player pykemon battles won after they fainted
    print("\nPoor {} has fainted...".format(player_pykemon.name))
    print("But not before defeating {} Pykemon!".format(game.battles_won))
    
    #Asking user if they want to continue play and then controlling the loop accordingly.
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        print("Thank you for playing Pykemon!")
        playing_main = False