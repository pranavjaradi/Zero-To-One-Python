"""
Problem Statement:
You are responsible for writing a program that will highlight the similarities and differences
between four different types of lists: a list of strings, a list of integers, a list of floats, and a list of
lists. For each list, your program will describe the data type of the list, the elements of the list,
and the data type of the first element in the list. Your program will then highlight the similarities
and differences between sorting a list numerically and alphabetically.
"""


# Defining Lists
num_strings = ["15","100","55","42"]
num_ints = [15,100,55,42]
num_floats = [9.81, 3.41, 543.21, 0.361]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

#Printing summary table.
print("\t\tSummary Table")
print("The variable num_strings is a {}.".format(type(num_strings)))
print("It contains the elements: {}.".format(num_strings))
print("The variable {} is a {}.".format(num_strings[0],type(num_strings[0])))


print("\nThe variable num_ints is a {}.".format(type(num_ints)))
print("It contains the elements: {}.".format(num_ints))
print("The variable {} is a {}.".format(num_ints[0],type(num_ints[0])))


print("\nThe variable num_floats is a {}.".format(type(num_floats)))
print("It contains the elements: {}.".format(num_floats))
print("The variable {} is a {}.".format(num_floats[0],type(num_floats[0])))


print("\nThe variable num_lists is a {}.".format(type(num_lists)))
print("It contains the elements: {}.".format(num_lists))
print("The variable {} is a {}.".format(num_lists[0],type(num_lists[0])))

print("\nNow sorting num_strings and num_ints....")
num_strings.sort()
num_ints.sort()
print("Sorted num_strings is {}".format(num_strings))
print("Sorted num_ints is {}".format(num_ints))
print("\nStrings are sorted alphabetically and integers numerically!")

