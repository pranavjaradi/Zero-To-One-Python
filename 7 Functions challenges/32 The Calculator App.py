"""
The Python Calculator App:
You are responsible for writing a program that simulates a calculator application that will take in
any two numbers, and a basic mathematical operation (addition, subtraction, multiplication,
division, or exponentiation), perform that operation, print a lexical statement of the operation,
and return a mathematical statement that describes the mathematical results. Upon completion,
your program will print out a history of all calculations performed including any error messages
that may have occurred such as division by zero.
"""

# FUNCTIONS
#Function for addition which will take two parameters and give their sum
def add(a, b):
    sum_value = round(a+b, 4)
    print("The sum of {} and {} is {}.".format(a, b, sum_value))
    return "{} + {} = {}".format(a,b,sum_value)

#Function for subtraction which will take two parameters and give their differnce
def subtraction(a, b):
    subtract_value = round(a-b, 4)
    print("The difference of {} and {} is {}.".format(a, b, subtract_value))
    return "{} - {} = {}".format(a,b,subtract_value)

#Function for multiplication which will take two parameters and give their product
def multiplication(a, b):
    multiplied_value = round(a*b, 4)
    print("The product of {} and {} is {}.".format(a, b, multiplied_value))
    return "{} X {} = {}".format(a,b,multiplied_value)

#Function for multiplication which will take two parameters and give their product
def division(a, b):
    if b != 0:
        divided_value = round(a/b, 4)
        print("The quotient of {} divided by {} is {}.".format(a, b, divided_value))
        return "{} / {} = {}".format(a,b,divided_value)
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"

#Function for exponent which will take two parameters and exponential value
def exponent(a, b):
    exponent_value = round(a ** b, 4)
    print("{} raised to the power of {} is {}.".format(a, b, exponent_value))
    return "{} ** {} = {}".format(a,b,exponent_value)

#Main Code
print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

#history list it will contain all the operations performed till user stops
history = []

is_running = True
while is_running:
    #Taking user input.
    num_1 = float(input("\nEnter first number: "))
    num_2 = float(input("Enter second number: "))
    operation = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower().strip()

    #Performing action based on user choosen operation
    #If user choose to add numbers
    if operation == 'addition' or operation == 'a':
        result = add(num_1, num_2)

    #If user choose to subtract numbers
    elif operation == 'subtraction' or operation == 's':
        result = subtraction(num_1, num_2)

    #If user choose to multiply numbers
    elif operation == 'multiplication' or operation == 'm':
        result = multiplication(num_1, num_2)

    #If user choose to divide numbers
    elif operation == 'division' or operation == 'd':
        result = division(num_1, num_2)

    #If user choose to find exponent
    elif operation == 'exponentiation' or operation == 'e':
        result = exponent(num_1, num_2)

    #User enters invalid operation
    else:
        print("That is not a valid operation. Try again.")
        result = "OPP ERROR"

    #Appending result into history
    history.append(result)

    #Asking user to continue or stop operations
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        print("\nCalculation Summary:")
        for calculation in history:
            print(calculation)
        print("\nThank you for using The Python Calculator App. Goodbye")
        is_running = False

