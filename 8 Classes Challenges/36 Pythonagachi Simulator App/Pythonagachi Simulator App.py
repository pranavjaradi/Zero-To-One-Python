"""
Pythonagachi Simulator App:
You will be responsible for writing a program that simulates the behavior of a retro 90's
Tamagachi toy. You program will allow a user to create their own creature, give it a name, and
care for it until it unfortunately parishes. Users will monitor the creatures hunger, boredom,
tiredness, and dirtiness and take actions to prevent any of the categories from getting to high. If
the categories get too high there will be unfortunate consequences.
"""

from creature import Creature


def show_menu(creature):
    """Function to show menu to user
    Giving only one option to awake the creature if creature is sleeping
    If creature is awake, giving player full menu

    Args:
        creature (object): creature/tomogachi created using class Creature

    Returns:
        string: It is choice of user based on menu
    """
    if creature.is_sleeping:
        choice = input("Enter 6 to awake the creature: ")
        choice = "6"
    else:
        print("Enter 1 to eat.")
        print("Enter 2 to play.")
        print("Enter 3 to sleep.")
        print("Enter 4 to take a bath.")
        print("Enter 5 to forage for food.")
        choice = input("Enter a choice (1-5): ")
    
    return choice

def call_action(creature, choice):
    """Function for calling method from class for selected creature

    Args:
        creature (object): creature created using class Creature
        choice (string): It is choice of user based on menu
    """
    if choice == "1":
        creature.eat()
    elif choice == "2":
        creature.play()
    elif choice == "3":
        creature.sleep()
    elif choice == "4":
        creature.clean()
    elif choice == "5":
        creature.forage()
    elif choice == "6":
        creature.awake()
    else:
        print("You have entered an invalid choice")

#Main Code
print("Welcome to the Pythonagachi Simulator App")
difficulty = int(input("Please choose a difficulty level (1-5): ")) #Difficulty will be used in gameplay increasing hunger, dirtiness, boredom, and tiredness
if difficulty > 5:
    #setting difficulty to 5 if user enter value more than 5
    difficulty = 5
elif difficulty < 1:
    #setting difficulty to 1 if user enter value less than 1
    difficulty = 1

is_active = True

while is_active:
    #Taking user input for name of creature and creating Creature object using it
    name = input("What name would you like to give your pet Pythonogachi: ")
    creature = Creature(name)

    rounds = 1
    while creature.is_alive:
        #Playing till creature is alive
        print("------------------------------------------")
        print("Round #{}\n".format(rounds))
        creature.show_values()
        choice = show_menu(creature)
        call_action(creature, choice)
        
        #Printing round summary
        print("Round #{} Summary:\n".format(rounds))
        creature.show_values()
        input("\nPress (enter) to continue....")
        
        #Increment values and check for death
        creature.increment_values(difficulty)
        creature.kill()
        
        #round is over
        rounds += 1

    #Creature is died game over
    print("R. I. P.")
    print("\n{} survived a total of {} rounds.".format(creature.name, rounds))
    play_more = input("Would you like to play again (y/n): ").lower()
    
    #Asking user to play again
    if play_more != "y":
        print("Thank you for playing Pythonagachi!")
        is_active = False