import math
import numpy as np
import random

class Planet:
    def __init__(self, name, color, m, radius, r, v):
        self.name = name
        self.color = color
        self.m    = m
        self.radius = radius
        self.r    = r
        self.v    = v
        self.a    = np.array((0.,0.))
        self.x = []
        self.y = []
        self.da = []
        self.distance = []

        self.comet_hit = 0
        self.closest_distance = 14.96e11
        self.distance_to_comet = []

        self.x.append(r[0])
        self.y.append(r[1])

class Universe:
    G = 6.67408e-11
    day = 60*60*24
    au = 1.496e11
    year = 365.242*day

    def __init__(self, dt=0.1):
        self.planets = []
        self.comets = []
        self.dt = dt * self.day
        self.t = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def add_comet(self):
        mass, radius, x, y, vx, vy = self.__random_m_r_v()
        print(mass, radius, x, y, vx, vy)
        comet = Planet("comet", "black", mass*1e13, radius*1e3, np.array((x*self.au,y*self.au)), np.array((vx*1e4,vy*1e4)))
        self.planets.append(comet)

    def remove_comet(self):
        self.comets.append(self.planets[-1])
        del self.planets[-1]

    def evolve(self, time, method = 'euler'):
        self.t.append(0)
        steps = int(time/self.dt)
        i=1
        while i < steps:
            self.__move(i)
            i += 1

    def evolve_comet(self, method = 'euler'):
        self.t.append(0)
        i = 0
        while np.linalg.norm(self.planets[-1].r) < 6*self.au:
            self.__move(i)
            i += 1

    def comet_shower(self, N_comets, method = 'euler'):
        i=0
        total_time_passed = 0.
        while i < N_comets:
            self.add_comet()
            self.evolve_comet()
            self.remove_comet()
            for p in self.planets:
                p.distance_to_comet.append(p.closest_distance/self.au)
                p.closest_distance = 10*self.au
            i += 1
            total_time_passed += self.t[-1]/self.year
            print(total_time_passed)

    def __random_m_r_v(self):
        mass = random.uniform(1., 9.9)
        radius = random.uniform(0.1, 0.5)

        case = random.randint(1, 4)

        if(case == 1):
            x = 4
            y = random.uniform(-4.,4.)
            vx = random.uniform(-4.,-1.)
            if(y>0):
                vy = random.uniform(-4.,-1.)
            else:
                vy = random.uniform(1.,4.)

        elif(case == 2):
            y = 4
            x = random.uniform(-4.,4.)
            vy = random.uniform(-4.,-1.)
            if(x>0):
                vx = random.uniform(-4.,-1.)
            else:
                vx = random.uniform(1.,4.)

        elif(case == 3):
            x = -4
            y = random.uniform(-4.,4.)
            vx = random.uniform(1.,4.)
            if(y>0):
                vy = random.uniform(-4.,-1.)
            else:
                vy = random.uniform(1.,4.)
        else:
            y = -4
            x = random.uniform(-4.,4.)
            vy = random.uniform(1.,4.)
            if(x>0):
                vx = random.uniform(-4.,-1.)
            else:
                vx = random.uniform(1.,4.)

        return mass, radius, x, y, vx, vy

    def __total_mass(self):
        M = 0
        for p in self.planets:
            M += p.m
        return M

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        #print(self.t[i-1] + self.dt)

        # Calculate distances between all planets
        for p1 in self.planets:
            p1.da.clear()
            p1.distance.clear()
            for p2 in self.planets:
                if (p1 == p2):
                    p1.da.append(np.array((0.,0.)))
                    p1.distance.append(4*self.au)
                else:
                    p1.da.append((-1*self.G*p2.m*(p1.r - p2.r))/(np.linalg.norm(p1.r - p2.r))**3)
                    p1.distance.append(np.linalg.norm(p1.r - p2.r))

            if(p1.distance[-1] < p1.closest_distance):
                p1.closest_distance = p1.distance[-1]

            if(p1.distance[-1] < 1.1*(p1.radius + self.planets[-1].radius)):
                p1.comet_hit +=1
                self.planets[-1].r[0] = 6.*self.au
                self.planets[-1].r[1] = 6.*self.au
                p1.closest_distance = 0.0
                print("Comet hit {0}!".format(p1.name))

            # Move plantes
            p1.a *= 0
            for da in p1.da:
                p1.a += da

            #print(p1.name,p1.a)
            p1.v += p1.a*self.dt
            p1.r += p1.v*self.dt

            #print(p1.name, p1.r)
            p1.x.append(p1.r[0])
            p1.y.append(p1.r[1])
