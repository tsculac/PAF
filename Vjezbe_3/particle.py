import math
import matplotlib.pyplot as plt

class Particle:
    g = -9.81

    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.a_x = []
        self.a_y = []

    def set_initial_conditions(self, v, theta, x_0, y_0, dt=0.001):
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.v_x.append(v*math.cos(math.radians(theta)))
        self.v_y.append(v*math.sin(math.radians(theta)))
        self.a_x.append(0)
        self.a_y.append(self.g)
        self.dt = dt
        self.v = v
        self.theta = theta

        self.name = "kosi_hitac_" + str(v) + "_" + str(theta)

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.y.clear()
        self.v_x.clear()
        self.v_y.clear()
        self.a_x.clear()
        self.a_y.clear()

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a_x.append(0)
        self.a_y.append(self.g)
        self.v_x.append(self.v_x[-1] + self.a_x[-1]*self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1]*self.dt)
        self.x.append(self.x[-1] + self.v_x[-1]*self.dt)
        self.y.append(self.y[-1] + self.v_y[-1]*self.dt)
        #print("i={0}, x={1}, y={2}, vx={3}, vy={4}, ax={5}, ay={6}, t={7}".format(i, self.x[i], self.y[i],self.v_x[i], self.v_y[i],self.a_x[i], self.a_y[i], self.t[i]))


    def range(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def analitical_range(self):
        return (self.v**2 / abs(self.g))*math.sin(2*math.radians(self.theta))

    def plot_trajectory(self):
        fig= plt.figure(figsize=(20,10))

        # x-y graf
        plt.plot(self.x,self.y)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('x-y graf')

        fig.savefig(self.name + ".pdf")
        plt.show()
