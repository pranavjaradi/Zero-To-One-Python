"""
Description:
You are responsible for writing a program that will create a list of a user’s favorite teachers. It
will display these teachers ranked (assuming the first teacher entered is the favorite, the second
teacher entered is the next favorite, ect…), alphabetically, in reverse alphabetical order, the top
two teachers, the next two teachers, the last favorite teacher, and the total number of favorite
teachers in the list. Your program will then add and remove teachers from this list, each time
displaying a similar summary.
"""

print("Welcome to Favorite Teachers Program")

#Taking users favorite teacher names.
teachers = []

teacher = input("Who is your first favorite teacher: ").title()
teachers.append(teacher)
teacher = input("Who is your second favorite teacher: ").title()
teachers.append(teacher)
teacher = input("Who is your third favorite teacher: ").title()
teachers.append(teacher)
teacher = input("Who is your fourth favorite teacher: ").title()
teachers.append(teacher)

#Printing teachers list
print("\nYour favorite teacher rank are: {}".format(teachers))
print("Your favorite teacher alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teacher in reverse alphabetically are: {}".format(sorted(teachers, reverse=True)))

#Printing top two, next top two and least favorite teachers name
print("\nYour top two favorite teachers are: {} and {}.".format(teachers[0], teachers[1]))
print("Your next top two favorite teachers are: {} and {}.".format(teachers[2], teachers[3]))
print("Your least favorite teachers is: {}.".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))

#Adding new teacher
print("\nOops, {} is no longer your first favorite teacher.".format(teachers[0]))
newTeacher = input("Who is your new favorite teacher: ").title()
teachers.insert(0,newTeacher)


#Printing teachers list with new addition
print("\nYour favorite teacher rank are: {}".format(teachers))
print("Your favorite teacher alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teacher in reverse alphabetically are: {}".format(sorted(teachers, reverse=True)))

#Printing top two, next top two and least favorite teachers name with new addition
print("\nYour top two favorite teachers are: {} and {}.".format(teachers[0], teachers[1]))
print("Your next top two favorite teachers are: {} and {}.".format(teachers[2], teachers[3]))
print("Your least favorite teachers is: {}.".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))

#Removing a teacher which is no longer a favorite.
print("\nYou have decided you no longer like a teacher.")
removeTeacher = input("Which teacher would your like to remove from the list: ").title()
teachers.remove(removeTeacher)

#Printing teachers list with removal of one teacher
print("\nYour favorite teacher rank are: {}".format(teachers))
print("Your favorite teacher alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teacher in reverse alphabetically are: {}".format(sorted(teachers, reverse=True)))

#Printing top two, next top two and least favorite teachers name removal of one teacher
print("\nYour top two favorite teachers are: {} and {}.".format(teachers[0], teachers[1]))
print("Your next top two favorite teachers are: {} and {}.".format(teachers[2], teachers[3]))
print("Your least favorite teachers is: {}.".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))