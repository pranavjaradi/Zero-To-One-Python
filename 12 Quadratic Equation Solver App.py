"""
Description:
You are responsible for writing a program that will display the solutions to any number of
quadratic equations. Your program will ask the user how many quadratic equations they would
like to solve, ask for the coefficients of the equation in the standard form of ax^2 + xb + c = 0
solve for x, and then display the solutions. Your program will allow for both real and complex
solutions.
"""
import cmath

#Welcoming user and giving brief about quadratic equations and complex numbers
print("\nWelcome to Quadratic equation solver app.")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")


#Taking equation count and solving them
eqCount = int(input("How many equations would you like to solve: "))

for eq in range(eqCount):
    print("\nSolving equation number {}.".format(eq))
    print("----------------------------------------------")
    a = float(input("\nPlease enter your value of (coefficient of x^2) : "))
    b = float(input("Please enter your value of (coefficient of x) : "))
    c = float(input("Please enter your value of (constant) : "))
    
    #Calculating roots
    x1 = (-b + cmath.sqrt((b**2) - (4 * a * c)))/(2 * a)
    x2 = (-b - cmath.sqrt((b**2) - (4 * a * c)))/(2 * a)
    
    #printing results
    print("The solutions to equation {}x^2 + {}x + {} are:\n".format(a,b,c))
    print("x1: {}".format(x1))
    print("x2: {}".format(x2))

print("Thank you for using the Quadratic Equation Solver App. Goodbye.")
