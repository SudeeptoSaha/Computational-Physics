import numpy as np
import matplotlib.pyplot as plt

V = 2.0  # velocity of the wave
Dt = 0.005  # Delta t
Dx = 0.01  # Delta x, must be consistent with Courant condition
eps = V * Dt / Dx
Lamda = 5.0

# Time steps should be such that L*Dx > V*Dt * T on top of the Courant condition

L = 400
T = 25


def phi0(i):
    # initial condition
    wave = np.exp(-((i - 30) / Lamda) ** 2)
    return wave


def phi1(phi, i):
    # use the Lax algorithm to get the very first update
    xi = 0.5 * (phi[i+1] + phi[i-1]) - eps * 0.5 * (phi[i + 1] - phi[i - 1])
    return xi


def Lax(phi, k):
    if k == 0 or k == (L - 1):
        return 0.
    else:
        return phi1(phi, k)


# Initializing the configuration
# First Dirichlet at the initial point
phi = np.zeros(L)
phi[0] = 0

# Put in the profile in between
for k in range(1, L - 1):
    phi[k] = phi0(k)

# Dirichlet at the other point
phi[L - 1] = 0



# Use Lax algorithm to get the data at the first update
# with Dirichlet at the end points
for t in range(1, T):
    phi_new = np.zeros(L)
    for k in range(L):
        phi_new[k] = Lax(phi, k)

    for j in range(L):
        phi[j] = phi_new[j]

# Plot the initial and final wave configurations
plt.plot(np.arange(L), phi0(np.arange(L)), label="Initial wave configuration")
plt.plot(np.arange(L), phi, label="Final wave configuration")
plt.xlabel("Position")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
