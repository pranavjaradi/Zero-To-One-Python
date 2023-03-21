"""
Factor Generator App:
You are responsible for writing a program that generates all factors of a given number. Your
program will display the factors individually and give a mathematically summary of how different
pairs of factors can be multiplied together to get the given number.
"""

print("Welcome to Factor Generator App!")

#flag for keeping while loop run
flag = True

while flag == True:

    #Getting user input to take a number for calculating factors
    number = int(input("\nEnter a number to determine all factors of that number: "))
    #Calculating factors
    factors = []
    for i in range(1, number+1):
        if number%i == 0:
            factors.append(i)

    #Displaying Factors
    print("\nFactors of " + str(number) + " are:")
    for factor in factors:
        print(factor)

    #printing summary
    print("\nIn Summary:")
    for i in range(int(len(factors)/2)):
        print("{} * {} = {}".format(factors[i], factors[-i-1], number))

    #Asking user to continue or stop
    choice = input("Run again (y/n): ").lower()
    if choice != "y":
        flag = False
        print("Thank you for using the program. Have a great day.")