import math
import numpy as np
import matplotlib.pyplot as plt

# Define a function for uniform motion calculation
def jednoliko_gibanje(F,m,time,x_0=0,v_0=0,dt=0.1):
    # Arrays for kinematic variables
    t = []
    x = []
    v = []
    a = []

    # Inital values
    a.append(F/m)
    t.append(0.)
    v.append(v_0)
    x.append(x_0)

    # Loop over N steps and calculate kinematic variables to store
    for i in range(int(time/dt)):
        a.append(F/m)
        t.append(0.1*(i+1)) # Take time step of 0.1
        v.append(v[i] + a[i]*dt)
        x.append(x[i] + v[i]*dt)


    fig, (pl1, pl2, pl3) = plt.subplots(1, 3, figsize=(20,10))
    fig.suptitle('Jednoliko gibanje')

    # x-t plot
    pl1.plot(t,x)
    pl1.set_xlabel('t [s]')
    pl1.set_ylabel('x [m]')
    pl1.set_title('x-t graf')

    # v-t plot
    pl2.plot(t,v)
    pl2.set_xlabel('t [s]')
    pl2.set_ylabel('$v [\\frac{m}{s}]$')
    pl2.set_title('v-t graf')

    # a-t plot
    pl3.plot(t,a)
    pl3.set_xlabel('t [s]')
    pl3.set_ylabel('a [$\\frac{m}{s^2}$]')
    pl3.set_title('a-t graf')

    fig.savefig("gibanje.pdf")
    plt.show()

# Function for projectile motion
def kosi_hitac(v_0, theta, time, x_0=0, y_0=0, dt=0.1):
    g = -9.81 # acceleration due to gravity

    # Arrays for kinematic variables
    t, x, y, v_x, v_y, a_x, a_y = ([] for i in range(7))

    # Initial values
    a_x.append(0)
    a_y.append(g)
    t.append(0.)
    v_x.append(v_0*math.cos(math.radians(theta)))
    v_y.append(v_0*math.sin(math.radians(theta)))
    x.append(x_0)
    y.append(y_0)

    # Loop over 100 steps to calculate all the kinematic variables
    for i in range(int(time/dt)):
        a_x.append(0)
        a_y.append(g)
        t.append(dt*(i+1))
        v_x.append(v_x[i] + a_x[i]*dt)
        v_y.append(v_y[i] + a_y[i]*dt)
        x.append(x[i] + v_x[i]*dt)
        y.append(y[i] + v_y[i]*dt)


    fig, (pl1, pl2, pl3) = plt.subplots(1, 3, figsize=(20,10))
    fig.suptitle('Kosi hitac')

    # x-y plot
    pl1.plot(x,y)
    pl1.set_xlabel('x [m]')
    pl1.set_ylabel('y [m]')
    pl1.set_title('x-y graf')

    # x-t plot
    pl2.plot(t,x)
    pl2.set_xlabel('t [s]')
    pl2.set_ylabel('$x [m]$')
    pl2.set_title('x-t graf')

    # y-t plot
    pl3.plot(t,y)
    pl3.set_xlabel('t [s]')
    pl3.set_ylabel('y [m]')
    pl3.set_title('y-t graf')

    fig.savefig("kosi_hitac.pdf")
    plt.show()
