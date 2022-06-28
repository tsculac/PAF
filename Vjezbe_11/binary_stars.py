import universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

komet = universe.Planet("komet", 1e10, np.array((1.*au,0.001*au)), np.array((-10000,0.)))
earth = universe.Planet("Earth", 5.9742e24, np.array((0.,0.)), np.array((0.,0.)))

ss = universe.Universe()
ss.add_planet(komet)
ss.add_planet(earth)

ss.evolve(0.50*year)

fig= plt.figure(figsize=(10,10))
plt.plot(komet.x,komet.y,label=komet.name,color="black", linewidth=1.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")

plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.savefig("sun_earth.pdf")
