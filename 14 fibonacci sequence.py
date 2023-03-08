"""
Description:
You are responsible for writing a program that will compute the first n terms of the Fibonacci
Sequence. Your program will then display these terms. Next, your program will calculate the
ratios of consecutive Fibonacci numbers to prove that these ratios approach the irrational
mathematical constant of Phi; 1.618….
"""

print("Welcome to the Fibonacci calculator App.")

number = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))

#Generating fibonacci series according to user input.
fib = [1,1]
for num in range (0,number-2):
    fib.append(fib[num] + fib[num+1])
    
#Printing fibonacci series.
print("\nThe First {} in Fibonacci sequence are:")
for i in fib:
    print(i)
    
#Generating golden ratio
golden = []
for j in range(number-1):
    ratio = round(fib[j+1] / fib[j], 5)
    golden.append(ratio)

#Printing golden ratio
print("\nThe golden ratio for generated fibonacci sequence are:")
for k in golden:
    print(k)

print("\nThe ratio of consecutive Fibonacci terms approaches phi that is 1.618.")
