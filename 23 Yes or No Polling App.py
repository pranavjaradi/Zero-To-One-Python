"""
Yes or No Polling App:
You are responsible for writing a program that will conduct a poll on a yes or no issue. Upon
starting the program a user will be prompted for an issue to vote on, the number of voters, and a
password to view the poll results. You program will then conduct the poll. Each time a user
votes, your program will ask for the voters full name to verify that they have not yet voted. If the
voter has not yet voted, they will be presented with the issue and can vote yes or no. The vote
will be recorded. Once the number of voters specified by the user has been reached, the poll
will close and a summary will be displayed. If the user enters the correct password a result of
each voters name and how they voted will be displayed.
"""

print("Welcome to the Yes or No Polling App.")

#Taking user input for issue to vote on, number of voters and password to view poll results.
issue = input("\nWhat is the yes or no issue you will be voting on today: ")
voters_count = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

#Initialising votes and dictionary for holding voter name and their respective vote
yes_count = 0
no_count = 0
poll_data = {}

for voters in range(voters_count):
    name = input("\nEnter your full name: ").title().strip()
    if name not in poll_data.keys():
        print("Here is our issue: " + issue)
        vote = input("What do you think...yes or no: ").lower().strip()
        
        #Counting votes
        if vote.startswith('y'):
            yes_count += 1
        elif vote.startswith('n'):
            no_count += 1
        else:
            print("That is not a yes or no answer, but okay...")

        print("Thank you " + name + "! Your vote of " + vote + " has been recorded.")
        
        #Adding voter and vote into dictionary
        poll_data[name] = vote
    
    else:
        #Not allowing to vote if user with same name already voted.
        print("Sorry, it seems that someone with that name has already voted.")

#Printing voters names.
total_votes = len(poll_data.keys())
print("The following " + str(total_votes) + " people voted: ")
for voter in poll_data.keys():
    print("\t" + voter)

#printing poll result.
print("\nOn the following issue: " + issue)
if yes_count > no_count:
    print("Yes wins! " + str(yes_count) + " votes to " + str(no_count) + ".")
elif no_count > yes_count:
    print("No wins! " + str(yes_count) + " votes to " + str(no_count) + ".")
else:
    print("It was a tie!  " + str(yes_count) + " votes to " + str(no_count) + ".")
    
#Showing admin who voted whom.
guess = input("To see the voting results enter the admin password: ")
if password == guess:
    for key, value in poll_data.items():
        print("Voter: " + key + "\tVote: " + value)
else:
    print("Sorry, that is not the correct password. Goodbye...")
print("\nThank you for using the Yes or No Issue Polling App.")
