"""
Problem Statement:
You are responsible for writing a program that will build and display a basketball roster based off
user input. Your program will then simulate an injury to a specific player in the roster and
prompt the user to update the roster. Upon updating the roster, your program will display the
final roster and wish the newly add player good luck.
"""

print("Welcome to Basketball Roster Program.")
#Creating roster from user input.
roster = []
player = input("Who is your point guard: ").title()
roster.append(player)
player = input("Who is your shooting guard: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)

#Displaying roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard :\t\t{}".format(roster[0]))
print("\t\tShooting Guard :\t{}".format(roster[1]))
print("\t\tSmall Forward :\t\t{}".format(roster[2]))
print("\t\tPower Forward :\t\t{}".format(roster[3]))
print("\t\tCenter :\t\t{}".format(roster[4]))

#removing injured player and adding new player
injuredPlayer = roster.pop(2)
print("Oh no, {} is injured.".format(injuredPlayer))
replacementPlayer = input("Who will take place of {}: ".format(injuredPlayer)).title()
roster.insert(2,replacementPlayer)

#Printing updated roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard :\t\t{}".format(roster[0]))
print("\t\tShooting Guard :\t{}".format(roster[1]))
print("\t\tSmall Forward :\t\t{}".format(roster[2]))
print("\t\tPower Forward :\t\t{}".format(roster[3]))
print("\t\tCenter :\t\t{}".format(roster[4]))

print("\mGood luck {}, you will do great.".format(replacementPlayer))
print("Your roster now have {} players.".format(len(roster)))