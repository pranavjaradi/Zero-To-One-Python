"""
Database Admin Program:
You are responsible for writing a program that will simulate logging into a database and
prompting a user to change their password. All usernames and passwords to the database will
be stored in a dictionary. Upon entering the correct credentials, your program will prompt the
user to enter a new password that is a minimum of eight characters long. If the new password
meets the criteria, it will be accepted, otherwise the new password will be rejected. If the user
who logged in is the admin, a list of all usernames and passwords will be displayed.
"""

print("Welcome to Database Admin Program.")

#Creating dictionary in username:password format.
log_on_information = {
    'admin00' : 'admin1234',
    'mooman74':'alskes145',
    'meramo1986':'kehns010101',
    'nickyD':'world1star',
    'george2':'booo3oha'
    }

#Taking user input for logging in
name = print("\nEnter your username: ")

if name in log_on_information.keys():
    password = input("Enter your password: ")
