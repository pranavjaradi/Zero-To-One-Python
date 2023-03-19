"""
Frequency Analysis App:
You are responsible for writing a program that will analyse the letter distribution of a given text.
Your program will take any text, remove all non-alpha characters, count the frequency of each
letter within the text, calculate the percentage of occurrence for each letter, and create a list of
letters ordered from highest occurrence to lowest occurrence. Your program will perform these
operations for two different bodies of text.
"""
from collections import Counter

print("Welcome to the Frequency Analysis app.")

#list of letters to keep in string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#taking strinng from user
key_phrase_1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

#removing all non-alphabets
for letter in key_phrase_1:
    if letter not in letters:
        key_phrase_1 = key_phrase_1.replace(letter, '')

#Counting occurence of each letter and total letters
letter_count = Counter(key_phrase_1)
total_letters = len(key_phrase_1)

#Printing frequency of each letter
print("Letter\tOccurence\tPercentage")
for key, value in sorted(letter_count.items()):
    print(key + "\t" + str(value) + "\t\t" + str(round(value*100/total_letters, 2)) + "%")

#printing letters in highest to lowest order

