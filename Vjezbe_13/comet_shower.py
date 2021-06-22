import universe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun","yellow", 1.989e30,0.696*1e9, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury","orange", 3.3e24, 2.439*1e6, np.array((0.,0.466 * au)), np.array((-47362.,0.)))
venus = universe.Planet("Venus","red", 4.8685e24, 6.051*1e6, np.array((0.723 * au,0.)), np.array((0.,35020.)))
earth = universe.Planet("Earth","blue", 5.9742e24, 6.371*1e6, np.array((-1.*au,0.)), np.array((0.,-29783.)))
mars = universe.Planet("Mars", "brown", 6.417e23, 3.389*1e6, np.array((0.,-1.666 * au)), np.array((24007.,0.)))

planets = [sun,mercury,venus,earth,mars]

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)

ss.comet_shower(100)

fig, axs = plt.subplots(1, 5, figsize=(30, 10))

for p, ax in zip(planets,axs):
    ax.hist(p.distance_to_comet, bins = 5)
    ax.set_title(p.name)
    ax.set_xlabel('distance (a.u.)')
    ax.set_ylabel('Number of comets')

fig.savefig('comets_histo.pdf')
#plt.show()
