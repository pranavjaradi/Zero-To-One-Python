"""
The Python Dice App:
You are responsible for writing a program that will roll a given number of dice of any number of
sides and sum the total. Your program will continue to run until the user desires to quit.
"""

import random

#Defining Function which will be used in code
#Defining a function which will take input from user for number of dice sides.
def dics_sides():
    sides = int(input("How many sides would you like on your dice: "))
    return sides

#Defining a function which will take input from user for number of dice they want to roll.
def dics_number():
    number = int(input("How many dice would you like to roll: "))
    return number

#Function for rolling n-sided dice m number of times
def roll_dice(sides, number):
    dice = []
    print("\nYou rolled {} {}-sided dices".format(number, sides))
    print("\n-----Results are as followed-----")
    for i in range(number):
        dice_value = random.randint(1, sides)
        print(dice_value)
        dice.append(dice_value)
    return dice

#Function for summation of all dice in a list
def sum_dice(dices):
    sum = 0
    for dice in dices:
        sum += dice
    print("The total value of your roll is " + str(sum))

#Function for user input for rolling dice again
def roll_again():
    choice = input("\nWould you like to roll again (y/n): ")
    return choice == 'y'

# Main code
print("Welcome to The Python Dice App:\n")

is_running = True
while is_running:
    
    #Taking dice sides and number
    sides = dics_sides()
    number = dics_number()
    
    #Rolling dice and adding dice values
    dices = roll_dice(sides, number)
    sum_dice(dices)
    
    #Roll again
    is_running = roll_again()

print("\nThank you for using the Python Dice App.")