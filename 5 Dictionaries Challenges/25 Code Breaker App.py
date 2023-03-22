"""
Code Breaker App:
You are responsible for writing a program that will encode or decode a message based off the
letter distribution of a predetermined key text. Your program will determine a frequency analysis
for two texts and use these letter distributions to create a cipher to either encode or decode a
message based off user input. This program is an extension of the Frequency Analysis App.
"""


from collections import Counter

print("Welcome to the Frequency Analysis app.")

#list of letters to keep in string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#hardcoding key_phrase_1
key_phrase_1 = """
Absolutely! Being challenging doesn't essentially force goofiness, however.
It just keeps lazier minds neglectful on posters' questions.
Rarely, submissions tempt upvotes vaguely while xenially yielding zero!
"""

#taking strinng from user
#key_phrase_1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

#removing all non-alphabets
for letter in key_phrase_1:
    if letter not in letters:
        key_phrase_1 = key_phrase_1.replace(letter, '')

#Counting occurence of each letter and total letters
letter_count = Counter(key_phrase_1)
total_letters = len(key_phrase_1)

#Printing frequency of each letter
print("\nLetter\tOccurence\tPercentage")
for key, value in sorted(letter_count.items()):
    print(key + "\t" + str(value) + "\t\t" + str(round(value*100/total_letters, 2)) + "%")

#creating letters in highest to lowest order list
key_phrase_1_ordered_letters = []
for element in letter_count.most_common():
    key_phrase_1_ordered_letters.append(element[0])

#printing letters in highest to lowest order
for element in key_phrase_1_ordered_letters:
    print(element[0],end='')

#hardcoding key_phrase_2
key_phrase_2 = """
All Bright Chess Debutants Endowed For Greatness Have
Ineffable Jaunty Knowledgeable Lives Made Naturally Of
Perfect Quintessential Rock Solid True Unabated Values Worth
Xerographic Youthful Zeal.
"""
#taking strinng from user for second string
#key_phrase_2 = input("\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

#removing all non-alphabets
for letter in key_phrase_2:
    if letter not in letters:
        key_phrase_2 = key_phrase_2.replace(letter, '')

#Counting occurence of each letter and total letters
letter_count_2 = Counter(key_phrase_2)
total_letters_2 = len(key_phrase_2)

#Printing frequency of each letter
print("\nLetter\tOccurence\tPercentage")
for key, value in sorted(letter_count_2.items()):
    print(key + "\t" + str(value) + "\t\t" + str(round(value*100/total_letters_2, 2)) + "%")

#creating letters in highest to lowest order list
key_phrase_2_ordered_letters = []
for element in letter_count_2.most_common():
    key_phrase_2_ordered_letters.append(element[0])

#printing letters in highest to lowest order
for element in key_phrase_2_ordered_letters:
    print(element[0],end='')

#Taking user input for encode or decode choice
choice = input("\nWould you like to encode or decode a message: ").lower().strip()
user_phrase = input("What is the phrase: ").lower().strip()

#removing all non-alphabetic characters
for letter in user_phrase:
    if letter not in letters:
        user_phrase = user_phrase.replace(letter, '')

#encoding a message
if choice == "encode":
    encoded_message = []
    for letter in user_phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_message.append(letter)
    print("\nThe encoded message is: \n" + ''.join(encoded_message))

#decoding a message
elif choice == "decode":
    decoded_message = []
    for letter in user_phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_message.append(letter)
    print("\nThe decoded message is: \n" + ''.join(decoded_message))

else:
    print("\nPlease enter either encode or decode and try again!")