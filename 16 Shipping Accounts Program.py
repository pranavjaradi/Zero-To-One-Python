"""
Shipping Accounts Program
You are responsible for writing a program that will simulate logging into a business’s shipping
accounts software. Once logged in your program will display the current costs of shipping x
amount of items. Based on the number of items shipped, the cost to ship each item will vary.
Once the cost to ship an item is set, your program will calculate the cost of shipping the entire
order. Upon confirmation of the order, your program will place the order and prepare the
shipment.
"""

print("Welcome to the Shipping Accounts Program.")

#Creating user lists and logging in user
users = ["Jack", "Steve", "Mike", "Kim", "Chris"]

user = input("\nHello, What is your username: ").title()

#Welcoming user and displaying current shipping prices
if user in users:
    print("\nHello {}, Welcome to your account.".format(user))
else:
    print("Sorry, you do not have an account with us. Goodbye.")

#Welcoming user and displaying current shipping prices
print("Shipping orders 0 to 100: \t\t$5.10 each")
print("Shipping orders 100 to 500: \t\t$5.00 each")
print("Shipping orders 500 to 1000: \t\t$4.95 each")
print("Shipping orders over 1000: \t\t$4.80 each")

