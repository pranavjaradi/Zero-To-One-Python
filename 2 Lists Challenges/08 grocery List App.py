""""
Problem Statement:
You are responsible for writing a program that will simulate a grocery shopping list. Your
program will start with two items on the shopping list, meat and cheese, and then allow a user to
add three new items to the list. To simulate shopping, your program will ask the user what item
they just purchased and then remove the item from the shopping list. Upon having only two
items in the shopping list, your program will inform the user that the store is out of a particular
item and prompt the user to replace the item with a new item. You will use the datetime library
to display the current date and time the shopping is taking place in mm/dd hh:mm format.
"""
import datetime

#Date time object and storing current time and date
time = datetime.datetime.now()
day = str(time.day)
month = str(time.month)
hour = str(time.hour)
minute = str(time.minute)

#Printing current grocery list and adding new items into the list
print("Welcome to Grocery List App.")
foods = ["Meat", "Cheese"]
print("You currently have {} and {} in your list.".format(foods[0],foods[1]))

food = input("Type of food to add to the grocery list: ").title()
foods.append(food)
food = input("Type of food to add to the grocery list: ").title()
foods.append(food)
food = input("Type of food to add to the grocery list: ").title()
foods.append(food)

print("Your grocery list contains:\n{}".format(foods))
foods.sort()
print("Here is your grocery list sorted:\n{}".format(foods))

#Simulating shopping
print("Simulating grocerry shopping....")
print("\nCurrent grocery list: {}".format(len(foods)))
print(foods)
foodBought = input("What food did you just buy: ").title()
foods.remove(foodBought)
print("Removing {} from the list.".format(foodBought))

print("\nCurrent grocery list: {}".format(len(foods)))
print(foods)
foodBought = input("What food did you just buy: ").title()
foods.remove(foodBought)
print("Removing {} from the list.".format(foodBought))

print("\nCurrent grocery list: {}".format(len(foods)))
print(foods)
foodBought = input("What food did you just buy: ").title()
foods.remove(foodBought)
print("Removing {} from the list.".format(foodBought))

#Item out of stock


print("\nCurrent grocery list: {}".format(len(foods)))
print(foods)
noItem = foods.pop()
print("Sorry {} is out of stock.".format(noItem))

newItem = input("What food would you like instead: ").title()
foods.insert(0, newItem)
print("Here is what remains in your shopping list.\n{}".format(foods))
