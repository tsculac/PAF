import math
import numpy as np

class Planet:
    def __init__(self, name, m, r, v):
        self.name = name
        self.m    = m
        self.r    = r # set position vector to initial position
        self.v    = v # set velocity vector to initial velocity
        self.a    = np.array((0.,0.)) # set acceleration vector to 0

        # Helper array to calculate distance between all objects needed to calculate the force
        self.dr = []

        # Remember position coordinates for plotting purposes
        self.x = []
        self.y = []

        self.x.append(r[0])
        self.y.append(r[1])

class Universe:
    # Define constants
    G = 6.67408e-11
    day = 60*60*24

    def __init__(self, dt=0.1):
        self.planets = [] # prepare array to store all planets in
        self.dt = dt * self.day # step size
        self.t = [] # we will save elapsed time of the simulation in case it is needed

    def add_planet(self, planet):
        self.planets.append(planet)

    def evolve(self, time, method = 'euler'):
        self.t.append(0)
        steps = int(time/self.dt) # calculate the number of steps of the simulation
        i=1
        while i < steps:
            self.__move() # move all planets
            i += 1

    def __move(self):
        self.t.append(self.t[-1] + self.dt) # Save time

        # Calculate distances between all planets
        for p1 in self.planets: # we are calculating distace of p1 with respect to all other planets in the Universe
            p1.dr.clear() # clear all distances from the prvious calculation
            for p2 in self.planets: # we have to loop over all other planets (p2) in the Universe
                if (p1 == p2): # If the loop over other planets ends up on the planet p1 just put 0 as a force contribution
                    p1.dr.append(np.array((0.,0.)))
                else: # Otherwise calculate the distance between the planets accoding to Newton gravity law and include mass and gravitational constant
                    p1.dr.append((-1*self.G*p2.m*(p1.r - p2.r))/(np.linalg.norm(p1.r - p2.r))**3)

            # Move planets
            p1.a *= 0 # Clear acceleration from previous calculations
            for dr in p1.dr:
                p1.a += dr # Sum contributions from all planets to the total acceleration

            # Update velocity and position using Eulers method
            p1.v += p1.a*self.dt
            p1.r += p1.v*self.dt

            # Save x,y coordinates
            p1.x.append(p1.r[0])
            p1.y.append(p1.r[1])
