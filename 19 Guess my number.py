"""
Guess My Number App
You are responsible for writing a program that will play the classic “Hi Low” game. Your
program will randomly pick a number between 1 and 20. Users will then guess the number.
With each guess, your program will respond that the user's guess is either too high or too low.
When the user guesses correct, or after 5 guesses, your program will end the game and
summarize the results.
"""
import random

print ("Welcome to Guess my Number Game.")

name = input("\nHello! What is your name: ").title().strip()

#Generating a random number between 1 to 20 and asking user to guess
number = random.randint(1,20)
print("Well {}, I am thinking of a number between 1 to 20.\n".format(name))

#Taking user guess upto 5 times
for turn in range(5):
    guess = int(input("Take a guess: "))
    if guess > number:
        print("Your guess is high. Try Again!")
    elif guess < number:
        print("Your guess is low. Try Again!")
    else:
        break

#The game is done, displaying result.
if guess == number:    
    print("Good job, {}! You guessed my number in {} guesses!".format(name, turn+1))
else:
    print("Game Over. The number I was thinking of was {}.".format(number))