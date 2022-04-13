import matplotlib.pyplot as plt
import calculus as calc
import numpy as np

def f(x):
    return 5*x**3 -2*x**2 + 2*x -3

print(calc.value(f,0))
print(calc.derivative_at_point(f,0))


fig= plt.figure(figsize=(20,10))

# Plot analytical solution
x_a = np.linspace(-2,2,100)
y_a = 15*x_a**2-4*x_a+2
plt.plot(x_a, y_a, '-r', label='analitical derivative')

# Plot numerical solutions
fx, x = calc.derviate_over_range(f,-2,2,0.1,method=2)
plt.scatter(x,fx,s=5)

x.clear()
fx.clear()
fx, x = calc.derviate_over_range(f,-2,2,0.01,method=2)
plt.scatter(x,fx,s=5)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Numerical derivation')

fig.savefig("derivative_2ndOrder.pdf")

plt.show()
