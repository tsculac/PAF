import universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
earth = universe.Planet("Earth", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(earth)

ss.evolve(3.0*year)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=5.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")

plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.savefig("sun_earth.pdf")
plt.show()
