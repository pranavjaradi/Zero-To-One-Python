"""
Prime Number App:
You are responsible for writing a program that will either determine if a given number is prime or
display all prime numbers within a given range of values. When determining all prime numbers
within a given range, your program will time the process and report how long the calculations
took to the user. It is important to time certain processes within our programs so we can so how
efficient our code is.
"""

import time

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
                #If we get 0 reminder when our number is divided by 2 to number then breaking the loop and setting prime_flag = false.
                prime_flag = False
                break
        if prime_flag:
            print("{} is prime!".format(number))
        else:
            print("{} is not prime!".format(number))            

    elif choice == '2':
        #taking upper and lower bound for finding prime numbers between them
        lower_bound = int(input("\nEnter the lower bound of your range: "))
        upper_bound = int(input("Enter the upper bound of your range: "))
        
        #Creating a list which will contain all prime numbers and taking start time to calculate time taken for calculation.
        primes = []
        start_time = time.time()
        
        #Running loop for finding prime
        for prime_candidate in range(lower_bound, upper_bound):
            prime_status = True
            if prime_candidate == 1:
                prime_status = False
            else:
                for i in range(2, prime_candidate):
                    if prime_candidate % i == 0:
                    #If we get 0 reminder when our number is divided by 2 to number then breaking the loop and setting prime_flag = false.
                        prime_status = False
                        break
                if prime_status:
                    primes.append(prime_candidate)
        end_time = time.time()
        time_delta = round(end_time-start_time,4)


        #Printing Summary
        print("\nCalculation took a total of " + str(time_delta) + " seconds.")
        print("The following numbers between {} and {} are prime.".format(lower_bound, upper_bound))
        input("Press enter to continue.")
        for prime in primes:
            print(prime)

    else:
        #If user invalid input ie not 1 or 2.
        print("That is not a valid option.")

    #Asking user to continue program or not
    choice = input("Would you like to run the program again (y/n): ")
    if choice != 'y':
        running = False
        print("\nThank you for using the program. Have a nice day.")