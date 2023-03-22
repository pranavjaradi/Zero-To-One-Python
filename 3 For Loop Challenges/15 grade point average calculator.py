"""
Description:
You are responsible for writing a program that will collect any number of grades from a user.
Your program will sort these grades numerically from highest to lowest and calculate the grade
point average of the user. Your program will then ask for the average the user desires and
calculate what the user must get on their next assignment to achieve this average. Lastly, your
program will make a copy of the users grades and allow them to alter one of their previous
grades to see how doing worse or better on an assignment would have changed their overall
average.
"""

print("Welcome to the Average Calculator App")

#taking the User details and grades
name = input("\nWhat is your Name: ").title().strip()
grades_num = int(input("How many grades would you like to enter: "))

grades = []
for i in range(grades_num):
    grade = int(input("Enter Grade: "))
    grades.append(grade)

#Displaying sorted grades.
grades.sort(reverse=True)
print("\nGrades from highest to lowest:")
for grade in grades:
    print("\t{}".format(grade))


#calculating average of grades
average = sum(grades)/len(grades)
average = round(average, 2)

#Displaying grades summary
print("\n{}'s grade summary:".format(name))
print("\tTotal number of grades: {}".format(grades_num))
print("\tHighest grade: {}".format(grades[0]))
print("\tLowest grade: {}".format(grades[-1]))
print("\tAverage grade: {}".format(average))

#Getting desired average and calculating next assignment score to acheive that average
desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)

#Printing Summary
print("\nGood luck {}!".format(name))
print("You will need to get a {} on your next assignment to earn a {} average".format(grade_req, desired_avg))

#Coping old grades list and swapping one grade
new_grades = grades.copy()
print("\nLets see what your average could have been if you did better/worse on an assignment.")
old_grade = int(input("What grade would you like to change: "))
new_grade = int(input("What grade would you like to change {} to: ".format(old_grade)))
new_grades.remove(old_grade)
new_grades.append(new_grade)
print(new_grades)

#Displaying new sorted grades.
new_grades.sort(reverse=True)
print("\nGrades from highest to lowest:")
for grade in new_grades:
    print("\t{}".format(grade))


#calculating average of new grades
new_average = sum(new_grades)/len(new_grades)
new_average = round(new_average, 2)

#Displaying new grades summary
print("\n{}'s grade summary:".format(name))
print("\tTotal number of grades: {}".format(len(new_grades)))
print("\tHighest grade: {}".format(new_grades[0]))
print("\tLowest grade: {}".format(new_grades[-1]))
print("\tAverage grade: {}".format(new_average))

#printing average change summary
average_change = new_average - average
average_change = round(average_change, 2)
print("\nYour new average would be a {} compared to your real average of {}!".format(new_average, average))
print("That's a change of {} points!".format(average_change))

#Too bad the original grades are still intact
print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit!")
