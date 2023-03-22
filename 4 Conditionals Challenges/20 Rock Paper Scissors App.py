"""
20: Rock, Paper, Scissors App
You are responsible for writing a program that will simulate playing the classic game Rock,
Paper, Scissors against computer AI. Your program will ask the user how many rounds of the
game they would like to play, simulate each round, keep score, and determine an overall
winner. Your program will also print the classic phrases such as “Paper covers rock” or
“Scissors cut paper”.
"""

import random

print("Welcome to the game of Rock, Paper, Scissors!")

#Getting number of rounds from user.
rounds = int(input("\nHow many rounds your like to play: "))

#Initialising variables
user_score = 0
computer_score = 0
moves = ["Rock", "Paper", "Scissors"]
winners = ["Player", "Computer", "Tie"]

#Simulating rounds.
for round in range(rounds):

    #Generating computer move.
    computer_choice = random.randint(0,2)
    computer_move = moves[computer_choice]

    #Taking user move
    print("\nRound {}".format(round+1))
    print("Player: {}\tComputer: {}".format(user_score, computer_score))
    user_move = input("Time to pick...rock, paper, scissors: ").title().strip()

    #MComparing moves if input is valid
    if user_move in moves:
        print("\nComputer: {}".format(computer_move))
        print("Player: {}".format(user_move))
        
        #If player and 
        if user_move == computer_move:
            winner = winners[2]
            phrase = "It is a tie, how boring!"
        else:

            #If computer move is Rock
            if computer_move == moves[0]:
                if user_move == moves[1]:
                    winner = winners[0]
                    phrase = "Paper covers rock!"
                elif user_move == moves[2]:
                    winner = winners[1]
                    phrase = "Rock smashes scissors!"

            #If computer move if Paper
            elif computer_move == moves[1]:
                if user_move == moves[0]:
                    winner = winners[1]
                    phrase = "Paper covers rock!"
                elif user_move == moves[2]:
                    winner = winners[0]
                    phrase = "Scissors cut paper!"

            #If computer move if scissors
            elif computer_move == moves[2]:
                if user_move == moves[0]:
                    winner = winners[0]
                    phrase = "Rock smashes scissors!"
                elif user_move == moves[1]:
                    winner = winners[1]
                    phrase = "Scissors cut paper!"

            #Catch for any other condition
            else:
                print("Round winner not calculated")
                winner = winners[2]
                phrase = "It is a tie, how boring!"

        #Displaying round result:
        print(phrase)
        if winner == winners[0]:
            print("You win round {}.".format(round+1))
            user_score += 1
        elif winner == winners[1]:
            print("Computer gets the point in round {}.".format(round+1))
            computer_score += 1
        else:
            print("This round was a tie.")
    #If user move is invalid.
    else:
        computer_score += 1
        print("That is not a valid game option!")
        print("Computer gets the point!")

#Displaying final result.
print("\nFinal Game Results")
print("\tRounds Played: {}".format(rounds))
print("\tPlayer Score: {}".format(user_score))
print("\tComputer Score: {}".format(computer_score))

if user_score > computer_score:
    print("\tWinner: PLAYER!!!")
elif user_score < computer_score:
    print("\tWinner: Computer :(")
else:
    print("\tThe game was a time")