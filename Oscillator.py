import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return np.array([y[1], -y[0]])

def euler_method(f, t0, y0, tf, N):
    h = (tf - t0) / N
    t = np.linspace(t0, tf, N+1)
    y = np.zeros((N+1, 2))
    y[0, :] = y0
    for i in range(1, N+1):
        y[i, :] = y[i-1, :] + h * f(t[i-1], y[i-1, :])
    return t, y

# Set the initial conditions and parameters for the simulation
t0 = 0
y0 = np.array([1.0, 0.0])
tf = 50
N = 1000
t, y = euler_method(f, t0, y0, tf, N)

plt.plot(t, y[:, 0])
plt.xlabel("Time(t)")
plt.ylabel("Amplitude")
plt.title("Harmonic oscillation using the Euler method")
plt.show()
