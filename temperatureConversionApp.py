# A tempearture converter app from Fahrenheit to degrees Celsius and degrees Kelvin.


print("Welcome to temperature coversion app.")
print("\nNow we will convert your tempearture in Fahrenheit into Celsius and Kelvin")


#Taking inpur from user
tempInF = float(input("\nWhat is your temperature in Fahrenheit: "))

#Converting temperature in F and then converting it into C and K and rounding off till 4 decimal places.
tempInC = round((tempInF - 32) * (5/9), 4)
tempInK = round(tempInC + 273.15, 4)

#Printing summary table
print("Degrees Farheneit:\t" + str(tempInF))
print("Degrees Celsius:\t" + str(tempInC))
print("Degrees Kelvin:\t\t" +  str(tempInK))