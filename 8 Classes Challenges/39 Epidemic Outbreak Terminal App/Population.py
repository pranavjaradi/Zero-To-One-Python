#Population class for Epidemic outbreak terminal app
from Person import *
import random

class Population():
    """
    Class of whole population containing Person objects.
    """
    def __init__(self, simulation):
        """Initialising attributes.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        self.population = []
        for i in range(simulation.population_size):
            person = Person()
            self.population.append(person)
    
    def initial_infection(self, simulation):
        """
        Method for initially affecting population based on infection percent.
        It will infect n number of Person object. Then shuffle the population containing Person objects.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        infected_count = int(round(simulation.infection_percent * simulation.population_size, 0))
        for i in range(infected_count):
            self.population[i].is_infected = True 
            self.population[i].days_infected = 1
        random.shuffle(self.population)
    
    def spread_infection(self, simulation):
        """Method to infect a person. A will only be infected if its adjacent person are infected and is alive.
        For first and last person only single person will be adjacent to it, for other two person will be adjacent.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        for i in range(len(self.population)):
            if not self.population[i].is_dead:
                if i == 0 and self.population[i+1].is_infected == True:
                    self.population[i].infect(simulation)
                elif i < len(self.population) - 1:
                    if self.population[i+1].is_infected == True or self.population[i-1].is_infected == True:
                        self.population[i].infect(simulation)
                elif i == len(self.population) - 1:
                    if self.population[i-1].is_infected == True:
                        self.population[i].infect(simulation)
    
    def update(self, simulation):
        """Method will update the day and Person (using Person class update method)
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        simulation.day_number += 1
        for person in self.population:
            person.update(simulation)
    
    def display_statistics(self, simulation):
        """Display the statistics of population after each day.
        It will calculate the percentage of infected people and dead people.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        total_infected_count = 0
        total_death_count = 0
        for i in range(len(self.population)):
            if self.population[i].is_infected:
                total_infected_count += 1
                if self.population[i].is_dead:
                    total_death_count += 1
        
        infected_percent = round((total_infected_count * 100) / simulation.population_size, 4)
        death_percent = round((total_death_count * 100) / simulation.population_size, 4)
        
        print("\n-----Day # {}-----".format(simulation.day_number))
        print("Percentage of Population Infected: {}%".format(infected_percent))
        print("Percentage of Population Dead: {}%".format(death_percent))
        print("Total People Infected: {} / {}".format(total_infected_count, simulation.population_size))
        print("Total Deaths: {} / {}".format(total_death_count, simulation.population_size))
    
    def graphics(self):
        """
        Method for printing status of each person in population.
        'O' for healthy, 'I' for infected and 'X' for Dead Person.
        Example: O-O-I-X-I-O-X-X
        """
        status = []
        for person in self.population:
            if person.is_dead:
                char = 'X'
            else:
                if person.is_infected:
                    char = 'I'
                else:
                    char = 'O'
            status.append(char)
        
        print('-'.join(state for state in status))
    
    def population_check(self):
        """Method to check if all person in population are dead
        Returns:
            Boolean : Return False when all person are dead.
        """
        i = 0
        alive_staus = True
        for person in self.population:
            if not person.is_dead:
                i += 1
        
        if i == 0:
            alive_staus =  False
        
        return alive_staus