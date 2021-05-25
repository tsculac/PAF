import numpy as np

class BungeeJumping:
    g = -9.81
    air_density = 1.225

    def __init__(self):
        self.t = []
        self.y = []
        self.v = []
        self.a = []

        self.Ek = []
        self.Ep = []
        self.Eel = []
        self.Euk = []


    def init(self, h, mass, l0, k, drag, area, dt=0.001):
        self.t.append(0)
        self.y.append(h)
        self.v.append(0)
        self.a.append(self.g)
        self.dt = dt

        self.m = mass
        self.h = h
        self.l0 = l0
        self.k = k
        self.Cd = drag
        self.A = area

        self.__update_energy(h, 0)

    def __a(self, y,v,t):
        #print(y,v,t)
        if(y + self.l0 > self.h):
            dx = 0.
        else:
            dx = (y+self.l0)-self.h
        return self.g -self.k*dx/self.m -1*np.sign(v)*((self.air_density*self.Cd*self.A)/(2*self.m))*v**2

    def __update_energy(self, y, v):
        Ek = 0.5*self.m*v**2
        Ep = np.abs(self.m*self.g*y)
        if(y + self.l0 > self.h):
            dx = 0.
        else:
            dx = (y+self.l0)-self.h
        Eel = 0.5*self.k*dx**2
        self.Ek.append(Ek)
        self.Ep.append(Ep)
        self.Eel.append(Eel)
        self.Euk.append(Ek+Ep+Eel)

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)

        k1v = (self.__a(self.y[i-1], self.v[i-1], self.t[i-1]))*self.dt
        k1y = self.v[i-1] * self.dt

        k2v = (self.__a(self.y[i-1]+k1y/2, self.v[i-1]+k1v/2, self.t[i-1]+self.dt/2))*self.dt
        k2y = (self.v[i-1]+k1v/2) * self.dt

        k3v = (self.__a(self.y[i-1]+k2y/2, self.v[i-1]+k2v/2, self.t[i-1]+self.dt/2))*self.dt
        k3y = (self.v[i-1]+k2v/2) * self.dt

        k4v = self.__a(self.y[i-1]+k3y/2, self.v[i-1]+k3v/2, self.t[i-1]+self.dt/2)*self.dt
        k4y = (self.v[i-1]+k3v/2) * self.dt

        self.v.append(self.v[i-1] + (k1v + 2*k2v + 2*k3v + k4v)/6)
        self.y.append(self.y[i-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)

        self.__update_energy(self.y[i], self.v[i])

    def evolve(self, time = 20):
        i=0
        while self.t[i] < time and self.y[i]>0 :
            self.__move(i)
            i += 1
        return self.t, self.y

    def get_energy(self):
        return self.Ek, self.Ep, self.Eel, self.Euk
