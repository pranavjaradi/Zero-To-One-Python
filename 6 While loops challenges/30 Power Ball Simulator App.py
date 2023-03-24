"""
Power Ball Simulator App:
You are responsible for writing a program that simulates the Power Ball Lottery. The traditional
power ball is played by randomly choosing 5 white balls numbered 1 through 69 then randomly
choosing 1 red ball numbered 1 through 26. The traditional power ball has astronomically low
odds of winning. Therefore, your program will allow users to adjust the odds by setting how
many balls the lottery will choose from. Your program will then calculate the odds the user has
of winning. The user will purchase tickets in a set interval, without purchasing repeated losing
tickets, until they either win the lottery or choose to give up.
"""
import random

print("--------------------Power-Ball Simulator--------------------")

#Taking user input for white & red ball
white_ball = int(input("\nHow many white-balls to draw from for the 5 winning numbers (Normally 69): "))
red_ball = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))

#Setting white ball equal to 5 if user selects less than 5 balls
if white_ball < 5:
    white_ball = 5

#Setting red ball equal to 1 if user selects less than 1 balls
if red_ball < 1:
    red_ball = 1

#Generating odds
odds = 1
for i in range(5):
    odds *= white_ball-i
odds = (odds * red_ball) / 120
print("You have a 1 in {} chance of winning this lottery.".format(odds))

#taking input for ticket interval 
interval = int(input("Purchase tickets in what interval: "))

#Creating winning numbers
winning_numbers = []
while len(winning_numbers)<5:
    number = random.randint(1,white_ball)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

#Generating red power ball
number = random.randint(1, red_ball)
winning_numbers.append(number)

#Welcoming user and displaying winning number
print("\n\n---------Welcome to the Power-Ball-----------")
print("Tonight's winning numbers are:", end = ' ')
for number in winning_numbers:
    print(number, end=" ")
input("\nPress 'Enter' to begin purchasing tickets!!!")

#starting draws
tickets_purchased = 0
active = True
tickets_sold = []

#Keeping game till winning ticket is generated in draw or till when user wants
while winning_numbers not in tickets_sold and active == True:
    #Creating lottery_numbers
    lottery_numbers = []
    while len(lottery_numbers)<5:
        number = random.randint(1,white_ball)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()

    #Red power ball in lottery
    number = random.randint(1, red_ball)
    lottery_numbers.append(number)
    
    #Selling ticket if not already sold
    if lottery_numbers not in tickets_sold:
        tickets_sold.append(lottery_numbers)
        tickets_purchased += 1
        #Printing the lottery numbers
        print(lottery_numbers)

    #Disregarding the ticket already sold
    else:
        print("Losing ticket generated; disregard...")

    #Informing user about number of tickets purchased till now and asking to keep playing or not
    if tickets_purchased%interval == 0:
        print("{} tickets purchased so far with no winners...".format(tickets_purchased))
        choice = input("\nKeep purchasing tickets (y/n): ").lower()
        if choice != 'y':
            active = False

#The lottery draw is over, now if we get winning number then informing user.
if lottery_numbers == winning_numbers:
    print("Winning ticket numbers: ", end='')
    for number in lottery_numbers:
        print(number, end=' ')
    print("\nPurchased a total of {} tickets.".format(tickets_purchased))

else:
    #Else user chose to stop the draw and did not win
    print("\nYou bought {} tickets and still lost!".format(tickets_purchased))
    print("Better luck next time!")