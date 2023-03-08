#Right Triangle Solver app
#App will take two bases of a right angled Triangle and give user the hypotenuse & area by calculating it.

import math

print("Welcome to Right Triangle Solver app.")

side_a = float(input("What is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))

#Calculations for third side and area
side_c = math.sqrt( (side_a ** 2) + (side_b ** 2) )
side_c = round(side_c, 3)
areaOfTriangle = 0.5 * side_a * side_b
areaOfTriangle = round(areaOfTriangle, 3)
perimeterOfTriangle = round((side_a+side_b+side_c),3)

#Printing results with different formatting
print("\nHypotenuse of a triangle with sides {} and {} is {}.".format(side_a,side_b,side_c))
print(f"\nArea of the triangle with sides {side_a} and {side_b} is {areaOfTriangle}.")
print("\nPerimeter of triangle with sides as {}, {} and {} is {}.".format(side_a,side_b,side_c,perimeterOfTriangle))
