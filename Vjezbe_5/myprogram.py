import harmonic_oscillator as ho
import numpy as np
import matplotlib.pyplot as plt
import math

h1 = ho.HarmonicOscillator()
h1.init(0.1,10,0.3,0,0.001)
h1.oscillate(2)
h1.plot_trajectory()



fig= plt.figure(figsize=(20,10))
# Plot numerical solutions
t1 = []
x1 = []
t1, x1 = h1.get_x()
plt.scatter(t1,x1,s=0.5,label='dt=0.001')

t2 = []
x2 = []
h1.reset()
h1.init(0.1,10,0.3,0,0.01)
h1.oscillate(2)
t2, x2 = h1.get_x()
plt.scatter(t2,x2,s=5,label='dt=0.01')

t3 = []
x3 = []
h1.reset()
h1.init(0.1,10,0.3,0,0.05)
h1.oscillate(2)
t3, x3 = h1.get_x()
plt.scatter(t3,x3,s=20,label='dt=0.05')

# Plot analytical solution
t_a = np.arange(0,2,0.001)
omega = np.sqrt(10/0.1)
phi = np.pi/2
x_a = 0.3*np.sin(omega*t_a+phi)
plt.plot(t_a,x_a,c='red',label='analytical')

plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('Harmonic oscillator')
plt.legend(loc="lower right")

fig.savefig("comparison.pdf")
