"""
Epidemic Outbreak Terminal App:
You will be responsible for writing a program that simulates the spread of an infectious disease
throughout a population. Using classes, you will model an individual person's and an entire
population's attributes and behaviors. Your program will allow users to set various initial
conditions in regards to the infection such as population size, infection rate, mortality rate, and
infection duration. The program will then simulate the interaction of people within a population
and spread the disease. Each iteration of spreading the disease will result in a summary
displaying statistics of the population.
"""

#Importing all classes
from Population import *
from Simulation import *

#Creating Simulation and Population object
simulation = Simulation()
population = Population(simulation)

#Starting infection and displaying it
population.initial_infection(simulation)
population.display_statistics(simulation)
population.graphics()
input("Press enter to begin the simulation")


for i in range(1, simulation.sim_days):
    if population.population_check():
        #If at least one person is alive then only running the simulation.
        population.spread_infection(simulation)
        population.update(simulation)
        population.display_statistics(simulation)
        population.graphics()
        if i != simulation.sim_days - 1:
            input("Press enter to advance to the next day.")
    else:
        #If no person in population is alive then breaking the loop
        print("\nAll person died after {} days.".format(simulation.day_number))
        break