import numpy as np
import charged_particle as cp
import matplotlib.pyplot as plt

# Magnetic and electric field
B = np.array((0,0,1))
E = np.array((0,0,0))

# Electron and positron
q_ele = -1
q_pos = +1
m_ele = 1
m_pos = 1
v_ele = np.array((0.1,0.1,0.1))
v_pos = np.array((0.1,0.1,0.1))

ele = cp.ChargedParticle(q_ele,m_ele,v_ele,E,B,0.01)
poz = cp.ChargedParticle(q_pos,m_pos,v_pos,E,B,0.01)

x_ele, y_ele, z_ele = ele.calculate_trajectory(20,'rk')
x_poz, y_poz, z_poz = poz.calculate_trajectory(20,'rk')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(x_ele, y_ele, z_ele, 'blue')
ax.plot3D(x_poz, y_poz, z_poz, 'red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("ele_poz.png")

# Euler and Runge-Kutta
q_e = -1
q_rk = -1
m_e = 1
m_rk = 1
v_e = np.array((0.1,0.1,0.1))
v_rk = np.array((0.1,0.1,0.1))

e = cp.ChargedParticle(q_e,m_e,v_e,E,B,0.01)
rk = cp.ChargedParticle(q_rk,m_rk,v_rk,E,B,0.01)

x_e, y_e, z_e = e.calculate_trajectory(20,'euler')
x_rk, y_rk, z_rk = rk.calculate_trajectory(20,'rk')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(x_e, y_e, z_e, 'blue')
ax.plot3D(x_rk, y_rk, z_rk, 'b--')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("ele_euler_rk.png")

plt.show()
