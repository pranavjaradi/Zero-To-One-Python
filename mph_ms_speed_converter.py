# A speed converter app from miles per hour to meter per second.

print("Welcome to Miles per hour coversion app.")
print("Now we will convert your miles per hour speed into meter per second")


#Taking inpur from user
mphSpeed = float(input("What is your speed in miles per hour: "))

#Converting mph into mps by multiplying it to 0.4474 and then round off it to 2 decimal places using round function.
mpsSpeed = round(mphSpeed * 0.4474, 2)

print("Your speed in meter per second is " + str(mpsSpeed) + ".")