"""
Shipping Accounts Program
You are responsible for writing a program that will simulate logging into a business's shipping
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

#checking if user is in list
if user in users:
    #Welcoming user and printing shipping price summary
    print("\nHello {}, Welcome to your account.".format(user))
    print("Shipping orders 0 to 100: \t$5.10 each")
    print("Shipping orders 100 to 500: \t$5.00 each")
    print("Shipping orders 500 to 1000: \t$4.95 each")
    print("Shipping orders over 1000: \t$4.80 each")
    
    #Determining shipping cost based on user quatity
    quantity = int(input("\nHow many items would you like to ship: "))
    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80
    
    #Displaying final bill
    bill = cost * quantity
    bill = round(bill, 2)
    print("It will cost you ${} at ${} per item to ship {} items.".format(bill, cost, quantity))
    
    #Placing order based on user choice.
    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith("y"):
        print("Okay. Shipping your {} items.".format(quantity))
    else:
        print("Okay, no order is being placed at this time.")
    
else:
    print("Sorry, you do not have an account with us. Goodbye.")

    
"""
Learnings:
1. Nested if else.
2. if/else/elif
3. startswith method
"""