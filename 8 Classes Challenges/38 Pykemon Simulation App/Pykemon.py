import random

class Pykemon():
    """
    Parent class from which Fire, Water and Grass classes will inherit
    """
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
        super.__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast'] #List in order of Light, heavy, restore and special attack for all fire pykemon
    
    def special_attack(self, enemy):
        """
        The special attack deals massive damage to grass type Pykemon,
        normal damage to fire type Pykemon, and minimal damage to water type Pykemon.
        This special attack will have a different name, depending on the element type
        of the pokemon. However, all special attacks will appear in a list called moves,
        which is an attribute of a specific Pykemon at index 3.
        Args:
            enemy (object): Object of class Pykemon.
        """
        
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