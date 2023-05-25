import numpy as np
from scipy.optimize import root_scalar

# Define the system of ODEs
def ode_system(x, y):
    dydx = np.zeros_like(y)
    dydx[0] = y[1]
    dydx[1] = -y[0]*(1-y[0]**2)
    return dydx

# Define the Runge-Kutta method (4th order)
def rk4(f, x0, x1, y0, h):
    n = int((x1 - x0)/h)
    x = x0 + np.arange(n + 1)*h
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + h/2, y[i] + k1/2)
        k3 = h*f(x[i] + h/2, y[i] + k2/2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    return x, y

# Define the residual function to find root for y1(10) = 0
def residual(y2_guess):
    # Initial conditions
    x0 = 0
    y0 = [0, y2_guess]
    # Solve the ODE system using a Runge-Kutta method
    x, y = rk4(ode_system, x0, 10, y0, h=0.01)
    # Return the residual
    return y[-1, 0]-1

# Guess an initial value for y2(0)
y2_guess = 0.1

# Use the root-finding algorithm to adjust y2(0) until y1(10) = 0
sol = root_scalar(residual, bracket=[0.1, 1.0], method='brentq')

# Retrieve the final solution
y2_final = sol.root
x_final = 10
y_final = [0, y2_final]

# Solve the ODE system using a Runge-Kutta method
x, y = rk4(ode_system, 0, x_final, y_final, h=0.01)

# Plot the solution
import matplotlib.pyplot as plt
plt.plot(x, y[:, 0])
plt.xlabel('x')
plt.ylabel('φ(x)')
plt.show()
