import math
import matplotlib.pyplot as plt

class HarmonicOscillator:

    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []

    def init(self, m, k, x0, v0, dt=0.001):
        self.k = k
        self.m = m
        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-(self.k/self.m)*x0)
        self.dt = dt

        self.name = "HarmonicOscillator_" + str(m) + "_" + str(k)

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.v.clear()
        self.a.clear()

    def get_x(self):
        return self.t, self.x

    def get_v(self):
        return self.t, self.v

    def get_a(self):
        return self.t, self.a

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a.append(-(self.k/self.m)*self.x[i-1])
        self.v.append(self.v[i-1] + self.a[i]*self.dt)
        self.x.append(self.x[i-1] + self.v[i]*self.dt)


    def oscillate(self, time):
        Nstep = int(time/self.dt)
        for i in range (1,Nstep):
            self.__move(i)

    def plot_trajectory(self):
        fig, (pl1, pl2, pl3) = plt.subplots(1, 3, figsize=(20,10))
        fig.suptitle('Harmonic oscillator')

        # x-t graf
        pl1.scatter(self.t,self.x,s=0.5)
        pl1.set_xlabel('t [s]')
        pl1.set_ylabel('x [m]')
        pl1.set_title('x-t graf')

        # v-t graf
        pl2.scatter(self.t,self.v,s=0.5)
        pl2.set_xlabel('t [s]')
        pl2.set_ylabel('$v [\\frac{m}{s}]$')
        pl2.set_title('v-t graf')

        # a-t graf
        pl3.scatter(self.t,self.a,s=0.5)
        pl3.set_xlabel('t [s]')
        pl3.set_ylabel('a [$\\frac{m}{s^2}$]')
        pl3.set_title('a-t graf')

        fig.savefig(self.name + ".pdf")
