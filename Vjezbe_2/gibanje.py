import numpy as np
import matplotlib.pyplot as plt


F = 10 # force in Newton
m = 0.1 # mass in kg
dt = 0.1 #time step

# Define arrays to store kinematic variables
t = []
x = []
v = []
a = []

# Inital values
a.append(F/m)
t.append(0.)
v.append(0.)
x.append(0.)

# Loop over 100 steps and calculate kinematic variables to store
for i in range(100):
    a.append(F/m)
    t.append(0.1*(i+1)) # Take time step of 0.1
    v.append(v[i] + a[i]*dt)
    x.append(x[i] + v[i]*dt)


fig, (pl1, pl2, pl3) = plt.subplots(1, 3, figsize=(20,10))
fig.suptitle('Jednoliko ubrzano gibanje')

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

fig.savefig("figure_1.pdf")
plt.show()
