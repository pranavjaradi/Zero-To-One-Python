"""
Thesaurus App
You are responsible for writing a program that simulates a thesaurus. Your program will present
a user with a list of words that your thesaurus contains. Based on the users choice, you will
randomly present them with a synonym for their chosen word. Lastly, your program will display
all of the potential synonyms for each word in the thesaurus.
"""
import random

print("Welcome to the Thesaurus App!")

#Creating a dictionary
thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
    "simple":['clean', 'elementary', 'plain', 'quiet', 'smooth']
}

#Printing words in our thesaurus
print("\nChoose a word from the thesaurus and I will give you a synonym")
print("\nHere are the words in the thesaurus:")
for key in thesaurus.keys():
    print("\t- " + key)

#Asking user for a word from our words
user_word = input("\nWhat word would you like a synonym for: ").lower().strip()

#giving user a random synonym if the given word exist in our list.
if user_word in thesaurus.keys():
    index = random.randint(0,4)
    print("A synonym for " + user_word + " is " + thesaurus[user_word][index] + ".")

#Else informing user about the word not being in thesaurus.   
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

#Printing whole thesaurus if user want.
choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()

if choice == 'yes':
    for key, values in thesaurus.items():
        print("\n" + key.title() + " synonyms are:")
        for value in values:
            print("\t- " + value)

else:
    print("I hope you enjoyed the program. Thank you!")
    
"""
Learnings:
1. Dictionaries
2. Looping through dictionaries
3. Understanding of key and values of a dictionary
"""