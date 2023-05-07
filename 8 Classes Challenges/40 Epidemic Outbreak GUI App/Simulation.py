import math

class Simulation():
    """
    Class for controlling the simulation and spread the disease accordingly.
    """
    def __init__(self):
        """
        Initialising the attributes required for simulation after taking from the user
        """
        self.day_number = 1 #Starting day will be day 1
        
        #We need a perfect square for population size for visual purpose.
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        root = math.sqrt(self.population_size)
        """
        The int function will round the decimal value. If we add
        .5 to the root, unless it is a perfect square, it will always be rounded up
        and the condition will hold.
        """
        if int(root + 0.5)**2 != self.population_size:
            #If population size is not a perfect square then making it a perfect square by rounding it.
            root = round(root, 0)
            self.grid_size = int(root) #Setting the grid size
            self.population_size = self.grid_size ** 2 #updating the population size
            print("Rounding population size to {} for visual purposes.".format(self.population_size)) #Informing user about updated population
        else:
            #Else population is a perfect square number
            self.grid_size = int(math.sqrt(self.population_size))
        
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = int(input("--Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_percent /= 100
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = int(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("--Enter the duration (in days) of the infection: "))
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = int(input("--Enter the mortality rate (0-100) of the infection: "))
        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("--Enter the number of days to simulate: "))