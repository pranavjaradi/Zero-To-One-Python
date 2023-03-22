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
name = input("\nEnter your username: ")

#getting user password.
if name in log_on_information.keys():
    password = input("Enter your password: ")
    if password == log_on_information[name]:
        #Logging in user if password matches database.
        print("\nHello " + "! You are logged in!")
        if name == 'admin00':
            #showing whole database to admin account.
            print("\nHere is the current user database:")
            for key, value in log_on_information.items():
                print("Username: " + key + "\t\tPassword: " + value)
        else:
            #Simulating change password for non admin users
            password_change_choice = input("Would you like to change your password: ").lower().strip()
            if password_change_choice == 'yes':
                new_password = input("What would you like to your new password to be (minimum 8 characters): ")
                if len(new_password) >= 8:
                    #changing password if it is 8 or more characters long
                    log_on_information[name] = new_password
                else:
                    print("Password should be of minimum 8 characters")
                print("\n" + name + " your password is " + log_on_information[name])
            else:
                print("\nThank you, goodbye.")

    #User did not entered correct password.
    else:
        print("Incorrect password!")

#User is not in database
else:
    print("Username not in database. Goodbye.")