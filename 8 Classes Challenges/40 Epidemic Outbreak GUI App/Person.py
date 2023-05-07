#Person class for Epidemic outbreak GUI app.
import random

class Person():
    """Class for a individual Person in population.
    """
    def __init__(self):
        """Initialising attributes
        """
        self.is_infected = False #Initally person will be healthy.
        self.is_dead = False #Initially person will be alive.
        self.days_infected = 0 #Person days infected will be zero initially.
    
    def infect(self, simulation):
        """Infect a person if random number is less than infection_probability.

        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        if random.randint(0,100) < simulation.infection_probability:
            self.is_infected = True
    
    def heal(self):
        """Method fo healing the Person.
        """
        self.is_infected = False
        self.days_infected = 0
    
    def die(self):
        """
        Method for killing a Person
        """
        self.is_dead = True
    
    def update(self, simulation):
        """Updating a Person if they are alive.
        If they are infected then increase days infected count and then check if they should die or heal.

        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                if random.randint(0,100) < simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()