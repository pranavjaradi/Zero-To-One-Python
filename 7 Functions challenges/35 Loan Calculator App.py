"""
Loan Calculator App:
You are responsible for writing a program that gathers information about a loan such as starting
principal, interest rate, and desired monthly payment. From this information, your program will
first determine if it is possible to pay off the loan based on the desired monthly payment. If it is
possible, your program will simulate making monthly payments until the loan is completely paid
off. Your program will then display statistics such as how long it took to pay the loan off, the
total amount spent on the loan, and the amount spent on interest. For simplicity, we will
assume that the loan compounds once a month, or twelve times in a year. Upon completion of
paying off the Loan, your program will make a graph showing the rate of change of the principal
to time using the matplotlib library.
"""

from matplotlib import pyplot

def get_loan_info():
    """return a dictionary with all details of loan

    Returns:
        dictionary: Loan info - principal amount, rate, EMI, and money paid
    """
    loan = {}
    loan['principal'] = float(input("\nEnter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: "))/100
    loan['monthly payment'] = float(input("Enter the desired monthly payment amount: "))
    loan['money paid'] = 0
    return loan

def show_loan_info(current_loan , months):
    """Show loan info based on months passed

    Args:
        current_loan (dictionary): Current loan info
        months (number): time in which from which loan started
    """
    print("\n----Loan information after {} months----".format(months))
    for key, value in current_loan.items():
        print("{}: {}".format(key.title(), value))

def collect_interest(current_loan):
    """Update the principal amount based on monthly intrest rate (rate/12)

    Args:
        current_loan (dictionary): Current loan info
    """
    current_loan['principal'] = current_loan['principal'] * (1 + current_loan['rate']/12)


def make_monthly_payment(current_loan):
    """Increase money paid & decrease principal by monthly payment if principal is more than monthly payment. Loan is still left to pay
    If principal is less than monthly payment then money paid is equal to principal and close the loan by setting principal = 0

    Args:
        current_loan (dictionary): Current loan info
    """
    current_loan['principal'] = current_loan['principal'] - current_loan['monthly payment']
    if current_loan['principal'] > 0:
        current_loan['money paid'] += current_loan['monthly payment']
    elif current_loan['principal'] < 0:
        current_loan['money paid'] += current_loan['monthly payment'] + current_loan['principal']
        current_loan['principal'] = 0

def summarize_loan(current_loan, month, initial_principal):
    """It will summarise the loan after it is closed ie principal = 0
    It will print initial loan amount & rate, time took to pay loan in months, EMI, total amount paid and total interest paid.

    Args:
        current_loan (dictionary): Current loan info
        month (integer): month required to pay the loan
        initial_principal (float): loan amount taken initially
    """
    print("\nCongratulations! You paid off your loan in {} months!".format(month))
    print("Your initial loan was ${} at a rate of {}%.".format(initial_principal, current_loan['rate']*100))
    print("Your monthly payment was ${}".format(current_loan['monthly payment']))
    print("You spent ${} total.".format(round(current_loan['money paid'] , 2)))
    print("You spent ${} on interest!".format(round(current_loan['money paid']- initial_principal , 2)))

def create_graph(data_set, loan):
    """It will create graph using matplotlib

    Args:
        data_set (Lisy): It is a list which will contain all the tuples in format (month, principal)
        loan (dictionary): Current loan info
    """
    x_values = []
    y_values = []
    for data in data_set:
        x_values.append(data[0])
        y_values.append(data[1])

    pyplot.plot(x_values, y_values)
    pyplot.title(str(100 * loan['rate']) + "% Interest" + " With $" + str(loan['monthly payment']) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

#Main code
print("Welcome to the Loan Calculator App")

#Initialise the variables
month_number = 0 #It will maintain month number
loan = get_loan_info() #Creating a loan
starting_principal = loan['principal']
data_to_plot = []

show_loan_info(loan , month_number) #Showing initial loan at start

#Simulating loan payment
input("Press 'enter' to begin paying off your loan.")
while loan['principal'] > 0:
    
    #If principal is increased after EMI then break the loop
    print(loan['principal'] > starting_principal)
    if loan['principal'] > starting_principal:
        break
    
    #Increasing the month, collect interset, making monthly payment and appending data to plot later
    collect_interest(loan)
    make_monthly_payment(loan)
    month_number += 1
    data_to_plot.append((month_number, loan['principal']))
    
    #showing loan info to user after each month
    show_loan_info(loan, month_number)

if loan['principal'] == 0:
    #If the loan has been paid off
    summarize_loan(loan, month_number, starting_principal)
    create_graph(data_to_plot, loan)
else:
    #if the loop break initially ie customer is not  able to pay the loan
    print("\nYou will never pay off your loan!!!")
    print("You cannot get ahead of the interest! :-(")