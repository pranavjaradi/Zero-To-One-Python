import random

class Pykemon():
    """Parent class from which Fire, Water and Grass classes will inherit."""
    def __init__(self, name, element, health, speed):
        """Pykemon attributes Initialisation

        Args:
            name (string): Name of pykemon
            element (string): One from Fire, Water, Grass
            health (int): health of pykemon. Initially max health and current health will be same. Max health will be used for healing.
            speed (int): Speed of pykemon
        """
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True
    
    def light_attack(self, enemy):
        """It will do a minimal but guaranteed damage.
        This light attack will have a different name, depending on the
        elemental type of the pokemon. However, all light attacks will appear in a list
        called moves, which is an attribute of a specific Pykemon, at index 0.

        Args:
            enemy (string): Enemy which was attacked
        """
        damage = random.randint(15,25)
        print("Pykemon {} used {}.".format(self.name, self.moves[0])) #moves is list (will initialise in child class) for each pykemon = [light, heavy, restore, special]
        print("It did a damage of {}".format(damage))
        enemy.current_health -= damage
    
    def heavy_attack(self, enemy):
        """
        The heavy attack has the potential to deal massive damage to the enemy
        Pykemon but it could also deal no damage at all; it is risky. This heavy attack will
        have a different name, depending on the element type of the pokemon.
        However, all heavy attacks will appear in a list called moves, which is an attribute
        of a specific Pykemon at index 1.

        Args:
            enemy (object): Enemy pykemon object created using same class Pykemon.
        """
        damage = random.randint(0,50)
        print("Pykemon {} used {}.".format(self.name, self.moves[1])) #moves is list (will initialise in child class) for each pykemon = [light, heavy, restore, special]
        if damage < 10:
            print("The attack missed!!!!")
        else:
            print("It did a damage of {}".format(damage))
            enemy.current_health -= damage
    
    def restore(self):
        """
        The restore move doesn't deal any damage at all but instead restores a small
        portion of health to the Pykemon calling the move. This restore move will have a
        different name, depending on the element type of the pokemon. However, all
        restore moves will appear in a list called moves, which is an attribute of a specific
        Pykemon at index 2.
        """
        heal = random.randint(15, 25)
        print("Pykemon {} used {}.".format(self.name, self.moves[2]))
        print("It healed {} health points.".format(heal))
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health
    
    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print("Pykemon {} has fainted!".format(self.name))
            input("Please Enter to continue.")
    
    def show_stats(self):
        print("\nName: {}".format(self.name))
        print("Element Type: {}".format(self.element))
        print("Health: {}/{}".format(self.current_health, self.max_health))
        print("Speed: {}".format(self.speed))

class Fire(Pykemon):
    """
    Creating Fire type pykemon using parent classs Pykemon
    Args:
        Pykemon (class): Parent class
    """
    def __init__(self, name, element, health, speed):
        """
        Initialising Fire child class from Pykemon.
        """
        super().__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast'] #List in order of Light, heavy, restore and special attack for all fire pykemon
    
    def special_attack(self, enemy):
        """
        The special attack deals massive damage to grass type Pykemon,
        normal damage to fire type Pykemon, and minimal damage to water type Pykemon.
        All special attacks will appear in a list called moves,
        which is an attribute of a specific Pykemon at index 3.
        Args:
            enemy (object): Object of class Pykemon.
        """
        print("Pykemon {} used {}.".format(self.name, self.moves[3]))
        if enemy.element == 'GRASS':
            print("The move was super effective.")
            damage = random.randint(35, 50)
        elif enemy.element == 'WATER':
            print("The move was not very effective.")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)
        print("It did a damage of {}".format(damage))
        enemy.current_health -= damage
    
    def move_info(self):
        """
        Print the details of all 4 moves including move name and damge dealt done by them.
        """
        print("\n{} Moves:".format(self.name))
        print("--{}--".format(self.moves[0])) #Light attack move
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print("\n--{}--".format(self.moves[1])) #Heavy attack move
        print("\tA risky attack...")
        print("\tCould deal up to 50 damage points or as little as 0 damage points.")
        print("\n--{}--".format(self.moves[2])) #Restore move
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("\n--{}--".format(self.moves[3])) #Special attack move
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")

class Water(Pykemon):
    """Child class of Pykemon for water type

    Args:
        Pykemon (class): Parent class
    """
    def __init__(self, name, element, health, speed):
        """
        Initialising the water type pykemon
        """
        super().__init__(name, element, health, speed)
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon'] #List in order of Light, heavy, restore and special attack for all Water pykemon
    
    def special_attack(self, enemy):
        """The special attack deals massive damage to fire type Pykemon,
        normal damage to Grass type Pykemon, and minimal damage to water type Pykemon.
        This special attack will have a different name, depending on the element type of the pokemon.
        However, all special attacks will appear in a list called moves,
        which is an attribute of a specific Pykemon at index 3.
        Args:
            enemy (object): Object of class Pykemon.
        """
        print("Pykemon {} used {}.".format(self.name, self.moves[3]))
        if enemy.element == 'FIRE':
            print("The move was super effective.")
            damage = random.randint(35, 50)
        elif enemy.element == 'GRASS':
            print("The move was not very effective.")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)
        print("It did a damage of {}".format(damage))
        enemy.current_health -= damage
    
    def move_info(self):
        """
        Print the details of all 4 moves including move name and damge dealt done by them.
        """
        print("\n{} Moves:".format(self.name))
        print("--{}--".format(self.moves[0])) #Light attack move
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print("\n--{}--".format(self.moves[1])) #Heavy attack move
        print("\tA risky attack...")
        print("\tCould deal up to 50 damage points or as little as 0 damage points.")
        print("\n--{}--".format(self.moves[2])) #Restore move
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("\n--{}--".format(self.moves[3])) #Special attack move
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")

class Grass(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Vine Whip', 'Wrap', 'Grow', 'Leaf Blade']
    
    def special_attack(self, enemy):
        """
        The special attack deals massive damage to water type Pykemon, normal
        damage to Fire type Pykemon, and minimal damage to grass type Pykemon.
        All special attacks will appear in a list called moves,
        which is an attribute of a specific Pykemon at index 3.
        Args:
            enemy (object): Object of class Pykemon.
        """
        print("Pykemon {} used {}.".format(self.name, self.moves[3]))
        if enemy.element == 'WATER':
            print("The move was super effective.")
            damage = random.randint(35, 50)
        elif enemy.element == 'FIRE':
            print("The move was not very effective.")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)
        print("It did a damage of {}".format(damage))
        enemy.current_health -= damage
    
    def move_info(self):
        """
        Print the details of all 4 moves including move name and damge dealt done by them.
        """
        print("\n{} Moves:".format(self.name))
        print("--{}--".format(self.moves[0])) #Light attack move
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print("\n--{}--".format(self.moves[1])) #Heavy attack move
        print("\tA risky attack...")
        print("\tCould deal up to 50 damage points or as little as 0 damage points.")
        print("\n--{}--".format(self.moves[2])) #Restore move
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("\n--{}--".format(self.moves[3])) #Special attack move
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")

class Game():
    """
    It will have methods required for gameplay.
    """
    def __init__(self):
        """Initialisng the Game class which will have initially the pykemon types, names, and battle won.
        """
        self.pykemon_elements = ['FIRE', 'WATER', 'GRASS']
        self.pykemon_names = ['Chewdie', 'Spatol', 'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot', 'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        self.battles_won = 0 #Initially no battles won
    
    def create_pykemon(self):
        """Creats a pykemon randomly.
        Returns:
            object: A Pykemon object with all attributes viz. name, element, health, speed.
        """
        health = random.randint(70,100)
        speed = random.randint(1,10)
        element = random.choice(self.pykemon_elements)
        name = random.choice(self.pykemon_names)
        #Creating pykemon in accordance with element.
        if element == 'FIRE':
            pykemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pykemon = Water(name, element, health, speed)
        else:
            pykemon = Grass(name, element, health, speed)
        
        return pykemon
    
    def choose_pykemon(self):
        """User will presented with three random pykemon to choose from of each element type.
        The user will play with this choosen pykemon.
        Returns:
            object: Pykemon object from which user will play the game
        """
        starters = [] #List will hold 3 pykemon
        while len(starters) < 3:
            pykemon = self.create_pykemon()
            valid_pykemon = True
            for starter in starters:
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False
            if valid_pykemon:
                starters.append(pykemon)
        
        for starter in starters:
            #Displaying stats and info of pykemons to user
            starter.show_stats()
            starter.move_info()
        print("\nProfessor Eramo presents you with three Pykemon:")
        print("(1) - {}".format(starters[0].name))
        print("(2) - {}".format(starters[1].name))
        print("(3) - {}".format(starters[2].name))
        choice = int(input("Which Pykemon would you like to choose: "))
        pykemon = starters[choice-1]
        return pykemon
    
    def get_attack(self, pykemon):
        """Getting move from user which they want pykemon to perform

        Args:
            pykemon (object): Pykemon class object

        Returns:
            int: Choice of move viz. light attack, heavy attack, restore, and special attack.
        """
        print("\nWhat would you like to do....")
        print("(1) - {}".format(pykemon.moves[0]))
        print("(2) - {}".format(pykemon.moves[1]))
        print("(3) - {}".format(pykemon.moves[2]))
        print("(4) - {}".format(pykemon.moves[3]))
        choice = int(input("Please enter your move choice: "))
        print("\n----------------------------------------")
        return choice
    
    def player_attack(self, move, player, computer):
        """
        Player pykemon will attack based on get_attack return value and then
        checks if computer is fainted after player move or not.
        Args:
            move (int): return value of get_attack method
            player (object): Player's pykemon
            computer (object): enemy pykemon handled by computer
        """
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)
        computer.faint()
    
    def computer_attack(self, player, computer):
        """
        Computer pykemon will attack based a random move value and then
        checks if player is fainted after computer move or not.
        Args:
            player (object): Player's pykemon
            computer (object): Enemy pykemon handled by computer
        """
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        player.faint()
    
    def battle(self, player, computer):
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)