"""
Description:
You are responsible for writing a program that will generate binary and hexadecimal values from
1 up to a specified user value. Recall that decimal is a base 10 number system, binary is a
base 2 number system, and hexadecimal is a base 16 number system. Your program will use
list slicing to first only show a portion of these values. Your program will then loop through the
entire lists of decimal, binary, and hexadecimal values to show the relationship between
numbers of different bases.
"""

print("Welcome to the Binary/Hexadecimal Converter App")

#Taking user input and generating list of 0b and 0x numbers.

numbers = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))


decimalList = list(range(1, numbers+1))
binaryList = []
hexaList = []

for num in decimalList:
    binaryList.append(bin(num).replace("0b", ""))
    hexaList.append(hex(num).replace("0x", ""))

print("Generating lists..... complete!")

#Get slicing index from user.
lowerRange = int(input("\nUsing slices, we will now show a portion of each list.\nWhat decimal number would you like to start at: "))
upperRange = int(input("What decimal number would you like to stop at: "))

#slicing through lists as per user input
print("\nDecimal values from {} to {}:".format(lowerRange, upperRange))
for num in decimalList[lowerRange-1:upperRange]:
    print(num)

print("\nBinary values from {} to {}:".format(lowerRange, upperRange))
for num in binaryList[lowerRange-1:upperRange]:
    print(num)
    
print("\nHexadecimal values from {} to {}:".format(lowerRange, upperRange))
for num in hexaList[lowerRange-1:upperRange]:
    print(num)
    
#Printing whole decimal, binary, hexadecimal lists
input("\nPress enter to see all values from 1 to {}.".format(numbers))
print("Decimal-----Binary-----Hexadecimal")
for d,b,h in zip(decimalList,binaryList,hexaList):
    print("{}-----{}-----{}".format(d,b,h))
