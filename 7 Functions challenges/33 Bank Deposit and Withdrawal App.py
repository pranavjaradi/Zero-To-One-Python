"""
Bank Deposit and Withdrawal App:
You are responsible for writing a program that will simulate an online banking application. A
user will create an account with your fictitious bank. The account will include a savings account
and a checking account. Users will then be able to make deposits or withdrawals from either
account as long as the remaining balance is non negative.
"""

#Defining Functions

def get_info():
    """
    It will welcome user and ask for their name, initial deposit in savings & checking account.
    Returns:
        dictionary: user information 
    """
    print("Welcome to the Bank of zeroToOne in Python")
    name = input("\nHello What is your name: ").title()
    saving = float(input("How much money would you like to set up your savings account with: "))
    checking = float(input("How much money would you like to set up your checking account with: "))
    user_info = {
        'Name' : name,
        'Saving' : saving,
        'Checking' : checking
    }
    return user_info

def make_deposit(user_info, account_type, deposit):
    """It will make a deposit in selected account type  of a user
    Args:
        account_info (a dictionary): it will have user name, balance in savings and checking account
        account_type (string): savings or checking
        deposit (float): money to deposit
    """
    user_info[account_type] += deposit
    print("\nDeposited ${} into {}'s {} account.".format(deposit, user_info['Name'], account_type.lower()))

def make_withdrawal(user_info, account_type, withdraw):
    """It will withdraw money from specific type of account

    Args:
        user_info (dictionary):
        account_type (string): saving/checking
        withdraw (float): money
    """
    if user_info[account_type] >= withdraw:
        user_info[account_type] -= withdraw
        print("\nWithdrew ${} from {}'s {} account.".format(withdraw, user_info['Name'], account_type.lower()))
    else:
        print("\nSorry, by withdrawing ${} you will have a negative balance.".format(withdraw))

def display_info(user_info):
    """It will print user info from dictionary

    Args:
        user_info (Dictionary): it contain user name, deposits in saving and checking account
    """
    print("\nCurrent Account Information")
    for key, value in user_info.items():
        if key == 'Name':
            print("{}: {}".format(key, value))
        else:
            print("{}: ${}".format(key, value))

#Main Program
#Getting user info.
user_info = get_info()

is_running = True
while is_running:
    #Displaying user info.
    display_info(user_info)

    #Getting user input for transaction type, money in the account
    account = input("What account would you like to access (Saving or Checking): ").title()
    transaction = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title()
    money = float(input("How much money: "))

    #making transaction according to user input
    if account in ['Saving', 'Checking']:
        if transaction == 'Deposit':
            #calling deposit function when transaction type is deposit
            make_deposit(user_info, account, money)
        elif transaction == 'Withdrawal':
            #calling function for withdrawal when transaction type is withdrawal
            make_withdrawal(user_info, account, money)
        else:
            #transaction type is not deposit or withdrawal
            print("I'm sorry, we cannot do that for you today.")

    else:
        #When account type is not saving or checking
        print("I'm sorry, we cannot do that for you today.")

    #Asking user to more transaction or not
    choice = input("Would you like to make another transaction (y/n): ").lower()
    if choice != 'y':
        display_info(user_info)
        print("\nThank you. Have a great day!")
        is_running = False