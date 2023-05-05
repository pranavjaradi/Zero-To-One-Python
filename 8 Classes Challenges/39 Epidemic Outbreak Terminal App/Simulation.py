#Simulation class for Epidemic outbreak terminal app

class Simulation():
    """
    Class for controlling the simulation and spread the disease
    """
    def __init__(self):
        """
        Initialising attributes from user inputs.
        """
        self.day_number = 1
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = int(input("--Enter the percentage (0-100) of the population to initially infect: "))/100
        self.infection_percent /= 100
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = int(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("--Enter the duration (in days) of the infection: "))
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = int(input("--Enter the mortality rate (0-100) of the infection: 35"))
        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("--Enter the number of days to simulate: 10"))