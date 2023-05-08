"""
Epidemic Outbreak GUI App:
You will be responsible for writing a program that simulates the spread of an infectious disease
throughout a population similar to the previous program. Using classes, you will model an
individual person's and an entire population's attributes and behaviors. Your program will allow
users to set various initial conditions in regards to the infection such as population size, infection
rate, mortality rate, and infection duration. The program will then simulate the interaction of
people within a population and spread the disease. Each iteration of spreading the disease will
result in a summary displaying statistics of the population. This time however, rather than storing
the population in a list and checking if the person to the left or right of the current person is
infected, we will store the population in a two dimensional list using nested for loops. This will
allow us to check for infections both to the left and right and above and below. This added
feature will help allow the program to create a Graphical User Interface or GUI (goo-e) to
visually show the spread of the infection. Rather than representing the spread of the infection
using O, I, and X in the terminal, each person in the population will be represented by a color
square in a GUI; green being healthy, yellow being infected, and red being dead.
"""
from Population import *
from Simulation import *
import tkinter
import time

#Program functions
def graphics(simulation, population, canvas):
    """
    It will create a square window of size 600(if window size need to be change, we need to change this) and draw NxN squares in it.
    Each square will represent a person of size 600//grid_size. x & y will be starting poition of square. 
    Args:
        simulation (instance): Object of Simulation class
        population (instance): Object of Population class
        canvas (instance): Object of tkinter
    """
    square_dimension = 600 // simulation.grid_size #Using floor division for rounded value.
    for i in range(simulation.grid_size):
        y = i * square_dimension
        for j in range(simulation.grid_size):
            x = j*square_dimension
            if population.population[i][j].is_dead:
                canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='red')
            else:
                if population.population[i][j].is_infected:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='green')

#Main Code
#Creating a simulation object
sim = Simulation()

#Setting window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#Creating a window for simulation and giving a title.
sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")

#Creating a canvas for our simulation. We will draw square representing person in the window.
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
sim_canvas.pack(side=tkinter.LEFT)

#Creating population object and starting initial infection
pop = Population(sim)
pop.initial_infection(sim)
pop.display_statistics(sim)
input("Press enter to begin simulation.")

for i in range(1, sim.sim_days):
    if pop.population_check():
        #If at least one person is alive then only running the simulation.
        pop.spread_infection(sim)
        pop.update(sim)
        pop.display_statistics(sim)
        graphics(sim, pop, sim_canvas)
        sim_canvas.update()
        time.sleep(1)
        if i != sim.sim_days - 1:
            sim_canvas.delete('all')
    else:
        #If no person in population is alive then breaking the loop
        print("\nAll person died after {} days.".format(sim.day_number))
        break