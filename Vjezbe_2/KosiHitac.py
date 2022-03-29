import math
import numpy as np
import matplotlib.pyplot as plt


v_0 = 100 # initial speed in m/s
theta = 45 # initial angle in degrees
g = -9.81 # acceleration due to gravity
dt = 0.1 #time step

# Prepare arrays to store kinematic variables
t, x, y, v_x, v_y, a_x, a_y = ([] for i in range(7))

# Initial values
a_x.append(0)
a_y.append(g)
t.append(0.)
v_x.append(v_0*math.cos(math.radians(theta)))
v_y.append(v_0*math.sin(math.radians(theta)))
x.append(0.)
y.append(0.)

# Loop over 100 steps to calculate all the kinematic variables
for i in range(100):
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
