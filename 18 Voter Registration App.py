"""
Voter Registration App
You are responsible for writing a program that will simulate registering to vote. If a user is 18 or
older, your program will present them with a list of potential political parties to register for. Upon
choosing a party, your program will confirm that the user has registered and print a specific
message depending on the party joined.
"""

print("Welcome to the Voter Registration App")

#taking user details and creating parties list
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

#Restricting user to vote if there age is less than 18 years.
if age < 18:
    print("\nYou are not old enough to vote.")

#Allowing user to vote if he/she is 18 or older.
else:
    print("\nCongratulations {}! You are old enough to register to vote.\n".format(name))
    print("Here is a list of political parties to join.")
    for party in parties:
        print(party)
    
    #Taking user desired party to join
    vote = input("\nWhat party would you like to join: ").title().strip()
    if vote in parties:
        print("\nCongratulations {}! You have joined the {} party!".format(name, vote))
        if vote in ["Republican", "Democratic"]:
            print("That is a major party!")
        elif vote in ["Libertarian", "Green"]:
            print("That is not a major party!")
        else:
            print("You are an Independent person!")
    else:
        print("That is not a given party.")