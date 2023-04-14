"""
Pythonagachi Simulator App:
You will be responsible for writing a program that simulates the behavior of a retro 90's
Tamagachi toy. You program will allow a user to create their own creature, give it a name, and
care for it until it unfortunately parishes. Users will monitor the creatures hunger, boredom,
tiredness, and dirtiness and take actions to prevent any of the categories from getting to high. If
the categories get too high there will be unfortunate consequences.
"""
import random
class Creature():
    """
    Creature and its attributes
    """
    def __init__(self, name):
        """
        It will create a creature with given name and then set its different attributes
        Args:
            name (string): Name of creature
        """
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.dirtiness = 0
        self.tiredness = 0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True
    
    def eat(self):
        """
        Simulate eating for given creature and decrease hunger by 1 to 4 randomly and food by 1 unit
        """
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print("Yumm! {} ate a great meal.".format(self.name))
        else:
            print("{} has no food! Better forage for some.")
        
        if self.hunger < 0:
            self.hunger = 0
    
    def play(self):
        """
        Simulate a game where player will guess the number thought by creature and decrease boredom of creature.
        """
        num = random.randint(0,2)
        print("{} wants to play a game".format(self.name))
        print("{} is thinking of a number 0, 1, or 2.......".format(self.name))
        guess = int(input("Guess the number: "))
        if guess == num:
            print("You guessed it correctly.")
            self.boredom -= 3
        else:
            print("Your guess is incorrect :(")
            self.boredom -= 1
        
        if self.boredom < 0:
            self.boredom = 0
    
    def sleep(self):
        """
        Simulating creature sleeping. Sleeping will decrease boredom and tiredness of creature.
        """
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print("{} is currently sleeping.".format(self.name))
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0
    
    def awake(self):
        """
        Simulating waking up creature and setting is_sleeping accordingly
        """
        num = random.randint(0,2)
        if num == 0:
            print("{} just woke up.".format(self.name))
            self.is_sleeping = False
            self.boredom = 0
        else:
            #Creature did not woke up
            print("{} won't wake up.".format(self.name))
            self.sleep()
    
    def clean(self):
        """
        Simulating creature bath decreasing dirtiness to zero
        """
        self.dirtiness = 0
        print("Yay! {} took a bath".format(self.name))
    
    def forage(self):
        """
        Simulating creature hunting for food. Creature will find food between 0 to 4
        Food finding will make creature dirty
        """
        food_found = random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        print("{} found {} pieces of food".format(self.name, food_found))
    
    def show_values(self):
        """
        Method for printing all details of creature
        """
        print("Creature Name: {}".format(self.name))
        print("Hunger (0-10): {}".format(self.hunger))
        print("Boredom (0-10): {}".format(self.boredom))
        print("Tiredness (0-10): {}".format(self.tiredness))
        print("Dirtiness (0-10): {}".format(self.dirtiness))
        print("Food inventory: {} pieces".format(self.food))
        
        if self.is_sleeping:
            print("\nCurrent status: {}".format("Sleeping"))
        else:
            print("\nCurrent status: {}".format("Awake"))
    
    def increment_values(self,difficulty):
        """
        Increasing hunger and dirtiness of creature according to difficulty set by player initially.
        Args:
            difficulty (integer): User will set difficulty of game at start
        """
        self.hunger += random.randint(0,difficulty)
        self.dirtiness += random.randint(0,difficulty)
        if self.is_sleeping == False:
            self.boredom += random.randint(0,difficulty)
            self.tiredness += random.randint(0,difficulty)
    
    def kill(self):
        """
        Simulating creature death by hunger or dirtiness and sleep by boredom or tiredness.
        """
        if self.hunger >= 10:
            print("{} starved to death.".format(self.name))
            self.is_alive = False
        elif self.dirtiness >= 10:
            print("{} suffered from infection and died.".format(self.name))
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print("{} is bored and falling asleep.".format(self.name))
            self.is_sleeping = True
        elif self.tiredness >= 10:
            print("{} is sleepy and falling asleep".format(self.name))
            self.is_sleeping = True