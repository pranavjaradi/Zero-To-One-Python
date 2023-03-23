"""
Guess My Word App:
You are responsible for writing a program that plays a word guessing game with a user. Your
program will provide a category of words to the user and a string of dashes “-----” that represent
the length of the word. The user will guess the word and with each incorrect guess, your
program will reveal a letter at random, “-a---”. Upon guessing the word correctly, your program
will then inform the user how many guesses they took.
"""

import random

print("Welcome to the Guess My Word App.")

#Creating a dictionary for game.
game_dict = {
    'sports' : ['cricket', 'football', 'hockey', 'tennis', 'badminton', 'squash'],
    'colors' : ['black', 'white', 'brown', 'green', 'purple', 'yellow'],
    'fruits' : ['apple', 'orange', 'grapes', 'watermelon', 'blueberry', 'jackfruit'],
    'vegetables' : ['cucumber', 'pumpkin', 'potato', 'pepper', 'cabbage', 'radish'],
    'classes' : ['english', 'history', 'science', 'mathematics', 'art', 'health']
}

#List with all keys in games_dict
game_keys = [key for key in game_dict.keys()]

running = True
while running:
    #Randomly picking a category for game ie game_keys
    category_index = random.randint(0, len(game_keys)-1)
    game_category = game_keys[category_index]

    #Randomly picking a word for gameplay
    word_index = random.randint(0, len(game_dict[game_category])-1)
    game_word = game_dict[game_category][word_index]

    #Creating a list for game word with '-' for each word
    blank_word = ['-' for letter in game_word]

    #Asking user to guess word with hint of category and word length
    print("\nGuess a 7 letter word from the following category: " + game_category)
    for blank in blank_word:
        print(blank, end='')
    
    guess = ''
    guess_count = 0

    #Initialising a while loop for guessing
    while guess != game_word:
        guess = input("\nEnter your guess: ").lower()
        if guess != game_word:
            print("That is not correct. Let us reveal a letter to help you!")
            guess_count += 1
            
            #Replacing a '-' with one word in the game_word
            check = True
            while check:
                letter_index = random.randint(0, len(blank_word) - 1)
                if blank_word[letter_index] == '-':
                    blank_word[letter_index] = game_word[letter_index]
                    print(check)
                    check = False

            for blank in blank_word:
                print(blank, end='')
        else:
            guess_count +=1
            print("\nCorrect! You guessed the word in {} guesses.".format(guess_count))
    
    #asking user for choice to continue the play
    choice = input("\nWould you like to play again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for playing the game.")