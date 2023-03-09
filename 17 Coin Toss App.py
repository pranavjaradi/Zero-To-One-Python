"""
Coin Toss App:
You are responsible for writing a program that will simulate flipping a coin n number of times.
Your program will present the user an option to see the result of each individual flip. Your
program will also inform the user any time the number of heads flipped is equal to the number of
tails flipped. Upon completion of all flips, your program will provide a summary table that shows
the number and percentage of each flip.
"""
import random

print("Welcome to Coin Toss App")
print("\nI will flip coin a set number of times.")

#Taking user input for number of tossing coin and user choice to see result of each toss.

count = int(input("\nHow many times would you like to flip the coin: "))
choice = input("Would you like to see the result of each flip: ").lower().strip()

#Tossing coin
print("\nFlipping!!!!\n")

heads = 0
tails = 0

random.randint(0,1)

for toss in range(count):
    coin = random.randint(0,1)
    if coin == 0:
        heads += 1
        if choice.startswith("y"):
            print("HEADS")
        
    else:
        tails += 1
        if choice.startswith("y"):
            print("TAILS")
    
    if heads == tails:
        print("At {} flips, the number of heads and tails were equal at {} each.".format(toss+1, heads))

#Calculating result
heads_percentage = round((heads * 100) / (count), 2)
tails_percentage = round((tails * 100) / (count), 2)

#Printing result summary
print("\nResult of flipping a coin {} times:".format(count))
print("Side\tCount\t\tPercentage")
print("HEADS\t\t{}\t\t{}%".format(heads, heads_percentage))
print("TAILS\t\t{}\t\t{}%".format(tails, tails_percentage))