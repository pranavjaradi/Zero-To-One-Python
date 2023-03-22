"""
Prime Number App:
You are responsible for writing a program that will either determine if a given number is prime or
display all prime numbers within a given range of values. When determining all prime numbers
within a given range, your program will time the process and report how long the calculations
took to the user. It is important to time certain processes within our programs so we can so how
efficient our code is.
"""

print("welcome to the Prime Number App.")

#Flag for keeping loop running
running = True

while running:
    #taking user input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")

    #Checking a number is prime if choice is 1.
    if choice == '1':
        number = int(input("Enter a number to determine if it is prime or not: "))
        prime_flag = True
        for i in range(2, number):
            if number%i == 0:
                prime_flag = False
                break
        if prime_flag == False:
            print("Number is not prime")
        else:
            print("Number is prime")
