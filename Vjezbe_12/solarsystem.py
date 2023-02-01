import universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun","yellow", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury","orange", 3.3e24, np.array((0.,0.466 * au)), np.array((-47362.,0.)))
venus = universe.Planet("Venus","red", 4.8685e24, np.array((0.723 * au,0.)), np.array((0.,35020.)))
earth = universe.Planet("Earth","blue", 5.9742e24, np.array((-1.*au,0.)), np.array((0.,-29783.)))
mars = universe.Planet("Mars", "brown", 6.417e23, np.array((0.,-1.666 * au)), np.array((24007.,0.)))

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)

ss.evolve(10.*year)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.name,color=sun.color, linewidth=5.0)

plt.plot(mercury.x,mercury.y,label=mercury.name,color=mercury.color)
plt.plot(mercury.x[-1], mercury.y[-1], 'o', color=mercury.color)

plt.plot(venus.x,venus.y,label=venus.name,color=venus.color)
plt.plot(venus.x[-1], venus.y[-1], 'o', color=venus.color)

plt.plot(earth.x,earth.y,label=earth.name,color=earth.color)
plt.plot(earth.x[-1], earth.y[-1], 'o', color=earth.color)

plt.plot(mars.x,mars.y,label=mars.name,color=mars.color)
plt.plot(mars.x[-1], mars.y[-1], 'o', color=mars.color)


plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.savefig("solar_system.pdf")
plt.axis('equal')
plt.show()
