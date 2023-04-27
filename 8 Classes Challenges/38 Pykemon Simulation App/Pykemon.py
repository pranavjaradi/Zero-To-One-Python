import random

class Pykemon():
    """Parent class from which Fire, Water and Grass classes will inherit
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