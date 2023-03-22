"""
Even Odd Number Sorter App:
You are responsible for writing a program that sorts a list of comma separated numbers as
either even or odd. Upon sorting the numbers into two groups, your program will then sort each
group numerically and display the results.
"""

print("Welcome to the Odd Number Sorter App.")

flag = True

while flag:
    #Taking user input in form a string of numbers eg 1,2,4 ,712, .....
    numbers = input("\nEnter a string of numbers separated by a comma (,): ").strip()
    numbers = numbers.replace(' ', '')  #Replacing any whitespace
    numbers = numbers.split(',')    #spliting numbers into list

    #Creating list to hold even and odd numbers
    even_numbers = []
    odd_numbers = []

    #Printing Result Summary
    print("----- Result Summary -----")
    #Printing even/odd of each number
    for number in numbers:
        number = int(number)
        if number%2 == 0:
            even_numbers.append(number)
            print("{} is even!".format(number))
        else:
            odd_numbers.append(number)
            print("{} is odd!".format(number))

    #Sorting even numbers
    even_numbers.sort()

    #Sorting odd numbers
    odd_numbers.sort()

    #Printing even/odd numbers
    print("\nThe following {} numbers are even:".format(len(even_numbers)))
    for number in even_numbers:
        print(number)

    print("\nThe following {} numbers are odd:".format(len(odd_numbers)))
    for number in odd_numbers:
        print(number)

    #Asking user to continue or stop
    choice = input("Would you like to run program again (y/n): ").lower()
    if choice != "y":
        flag = False
        print("Thank you for using the program. Have a great day.")
        
    """
    Learnings:
    1. While loop
    """