"""
This is a Multiplcation table and exponent table app.
It will take a number as input from user and then, give multiple and exponent of that number from 1 to 9.
"""

#Gathering user input
print("Welcome to the multiplication & exponent table app")
nameOfUser = input("What is your name: ").title( ).strip()
number = float(input("What number would you like to work with: "))
message = nameOfUser + ", Math is cool!"


#Multiplication Table
print("Multiplication table for {}".format(number))
print("1.0 * {} = {}".format(number, round(number*1, 4)))
print("2.0 * {} = {}".format(number, round(number*2, 4)))
print("3.0 * {} = {}".format(number, round(number*3, 4)))
print("4.0 * {} = {}".format(number, round(number*4, 4)))
print("5.0 * {} = {}".format(number, round(number*5, 4)))
print("6.0 * {} = {}".format(number, round(number*6, 4)))
print("7.0 * {} = {}".format(number, round(number*7, 4)))
print("8.0 * {} = {}".format(number, round(number*8, 4)))
print("9.0 * {} = {}".format(number, round(number*9, 4)))

#Exponent Table
print("Exponent table for {}".format(number))
print("1.0 ** {} = {}".format(number, round(number ** 1, 4)))
print("2.0 ** {} = {}".format(number, round(number ** 2, 4)))
print("3.0 ** {} = {}".format(number, round(number ** 3, 4)))
print("4.0 ** {} = {}".format(number, round(number ** 4, 4)))
print("5.0 ** {} = {}".format(number, round(number ** 5, 4)))
print("6.0 ** {} = {}".format(number, round(number ** 6, 4)))
print("7.0 ** {} = {}".format(number, round(number ** 7, 4)))
print("8.0 ** {} = {}".format(number, round(number ** 8, 4)))
print("9.0 ** {} = {}".format(number, round(number ** 9, 4)))

#Math is cool
print("\n"+message)
print("\t"+message.lower())
print("\t\t"+message.title())
print("\t\t\t"+message.upper())
