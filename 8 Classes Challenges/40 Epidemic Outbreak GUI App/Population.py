"""Population class for Epidemic outbreak GUI app"""
from Person import *
import random

class Population():
    """
    Class of whole population containing Person objects.
    """
    def __init__(self, simulation):
        """Initialising attributes.
        Population will be a two dimensional list. It will have N number of list representing rows of grid.
        Each Row will have N Person objects, Thus making NxN Grid.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        self.population = [] #List containg Person objects collectively called as Population.
        for i in range(simulation.grid_size):
            row = []
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)
    
    def initial_infection(self, simulation):
        """
        Method for initially affecting population based on infection percent.
        It will pick a 'y' person in 'x' row randomly. Then infect that person if not already infected.
        Args:
            simulation (instance): A simulation object of Simulation class instance.
        """
        infected_count = int(round(simulation.infection_percent * simulation.population_size, 0))
        infections = 0
        while infections < infected_count:
            x = random.randint(0, simulation.grid_size - 1)
            y = random.randint(0, simulation.grid_size - 1)
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1
    
    def spread_infection(self, simulation):
        """Method to infect a person. A will only be infected if one of its adjacent person are infected and is alive.
        Adjacent person can be above, below, left, right to the person.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if not self.population[i][j].is_dead:
                    if i == 0:
                        #i will be 0 for top row which means there are is no row above it
                        if j == 0:
                            #j will be 0 for first person, which means no person is to the left of it.
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            #j will be equal to grid_size-1 for last person in a row, no person will be right to it.
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i][j-1].is_infected:
                                self.population[i][j].infect(simulation)
                    
                    elif i == simulation.grid_size - 1:
                        #i will be equal to grid_size-1 for last row, no row will be below it.
                        if j == 0:
                            #This is first person in row, no person to left.
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            #j will be equal to grid_size-1 for last person in a row, no person will be right to it.
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i][j-1].is_infected:
                                self.population[i][j].infect(simulation)
                    
                    else:
                        #for rows excluding top and bottom rows.
                        if j == 0:
                            #This is first person in row, no person to left.
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            #j will be equal to grid_size-1 for last person in a row, no person will be right to it.
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        """Method will update the day and Person (using Person class update method)
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        simulation.day_number += 1
        for row in self.population:
            for person in row:
                person.update(simulation)
    
    def display_statistics(self, simulation):
        """Display the statistics of population after each day.
        It will calculate the percentage of infected people and dead people.
        Args:
            simulation (instance): A simulation instance of Simulation class object.
        """
        total_infected_count = 0
        total_death_count = 0
        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count += 1
                    if person.is_dead:
                        total_death_count += 1
        
        infected_percent = round((total_infected_count * 100) / simulation.population_size, 4)
        death_percent = round((total_death_count * 100) / simulation.population_size, 4)
        
        print("\n-----Day # {}-----".format(simulation.day_number))
        print("Percentage of Population Infected: {}%".format(infected_percent))
        print("Percentage of Population Dead: {}%".format(death_percent))
        print("Total People Infected: {} / {}".format(total_infected_count, simulation.population_size))
        print("Total Deaths: {} / {}".format(total_death_count, simulation.population_size))
    
    def population_check(self):
        """Method to check if all person in population are dead.
        Returns:
            Boolean : Return False when all person are dead.
        """
        i = 0
        alive_staus = True
        for row in self.population:
            for person in row:
                if not person.is_dead:
                    i += 1
        
        if i == 0:
            alive_staus =  False
        
        return alive_staus