#Importing all classes
from Population import *
from Simulation import *

simulation = Simulation()
population = Population(simulation)

population.initial_infection(simulation)
population.display_statistics(simulation)
population.graphics()
input("Press enter to begin the simulation")


for i in range(1, simulation.sim_days):
    if population.population_check():
        population.spread_infection(simulation)
        population.update(simulation)
        population.display_statistics(simulation)
        population.graphics()
        if i != simulation.sim_days - 1:
            input("Press enter to advance to the next day.")
    else:
        print("\nAll person died after {} days.".format(simulation.day_number))
        break