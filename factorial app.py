"""
Description:
You are responsible for writing a program that will calculate the factorial of any given number.
Your program will display the mathematical relationship of the factorial. It will then use the math
library to compute the value of the given factorial. Lastly, your program will use its own
algorithm to compute the value of the given factorial and compare the results.
"""

import math
print("Welcome to Factorial Calculator App.")

#Taking user input and printing factorial representation of it.
number = int(input(("\nEnter your number of which you want factorial of: ")))
print("{}! = ".format(number), end="")
for multiple in range(1,number):
    print("{}".format(multiple), end="*")
print(number)

#Calculating using factorial function in math library
factorial = math.factorial(number)
print("\nHere is the result from math library.")
print(factorial)

#calculating factorial using for loop
factorial = 1
for multiple in range(1,number+1):
    factorial *= multiple
print("\nHere is the result from our own algorithm.")
print(factorial)

print("\nIt is shown twice that {}! = {} (with excitement)".format(number,factorial))