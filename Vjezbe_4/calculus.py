import numpy as np

def value(func, x):
    return func(x)

def derivative_at_point(func, x, epsilon = 0.01, method = 3):
    if method == 2:
        return (func(x+epsilon) - func(x))/epsilon
    elif method == 3:
        return (func(x+epsilon) - func(x-epsilon))/(2*epsilon)

def derviate_over_range(func, dn, up, epsilon = 0.01, method = 3):
    dfx = []
    x = []
    for x_i in np.arange(dn, up, epsilon):
        x.append(x_i)
        dfx.append(derivative_at_point(func,x_i,epsilon,method))
    return dfx,x

def integrate_up_dn(func, dn, up, Nstep):
    sum_up = 0.
    sum_dn = 0.
    dx = abs(up-dn)/Nstep
    for i in range(0, Nstep):
        sum_dn += func(i*dx)*dx
        sum_up += func((i+1)*dx)*dx
    return sum_dn,sum_up

def integrate(func, dn, up, Nstep):
    sum = 0.
    dx = abs(up-dn)/Nstep
    for i in range(0, Nstep):
        sum += func(i*dx) + func((i+1)*dx)
    return (sum*dx)/2
