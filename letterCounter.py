#Basic Letter Counter App

print("Welcome to the Letter counter App")

#Get user name
nameOfUser = input("\nWhat is your name: ").title().strip()
print("Hello and welcome " + nameOfUser + "!")

print("I will count the frequency of specific letter in a message.")

#Taking message from user and converting to lower case for standardising
messageByUser = input("\nPlease enter your message: ").lower()

#Taking user input for counting the frquency of letter
letterByUser = input("Which letter would you like to count the frequency of: ").lower()


#Counting the letter frequency in message using count() and displaying result
if (len(letterByUser) == 1):
    letterFrequency = messageByUser.count(letterByUser)
    print("\n" + nameOfUser + ", your message has " + str(letterFrequency) + " " + letterByUser + "'s in it.")
    print ("Thank You!!")
else:
    print("Please enter valid letter as input.")
