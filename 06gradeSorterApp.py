"""
Problem Statement:
You are responsible for writing a program that will collect four grades from a user. Your
program will then sort these grades from highest to lowest. Then, your program will simulate
dropping the lowest two grades the user entered. Lastly, it will comment on the users highest 
grade.
"""

print("Welcome to the grade sorter app.")

#Initialising list and taking inputs.
grades = []
grade = int(input("Please enter your first grade (0-100): "))
grades.append(grade)
grade = int(input("Please enter your second grade (0-100): "))
grades.append(grade)
grade = int(input("Please enter your third grade (0-100): "))
grades.append(grade)
grade = int(input("Please enter your fourth grade (0-100): "))
grades.append(grade)

#Printing grades and printing sorted grades.
print("Your grades are: {}".format(grades))
grades.sort(reverse=True)
print("Your grades from highest to lowest are: {}".format(grades))

#Dropping lowest two grades
print("Lowest two grades will be now dropped.")
removedGrade = grades.pop()
print("Removed Grade: {}".format(removedGrade))
removedGrade = grades.pop()
print("Removed Grade: {}".format(removedGrade))

#Printing remaining grades and highest grade.
print("Your remaining grades are: {}".format(grades))
print("Nice Work! Your highest grade is {}.".format(grades[0]))
