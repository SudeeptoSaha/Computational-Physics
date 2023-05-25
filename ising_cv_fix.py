import numpy as np
import matplotlib.pyplot as plt

L = 256  # Number of lattice

def my_rand(I):
    return np.random.rand()

# Periodicity operation for the lattice sites 
def prev(x):
    # To find the previous lattice site using periodicity
    if x == 0:
        return L - 1
    else:
        return x - 1

def next(x):
    # To find the next lattice site using periodicity
    if x == L - 1:
        return 0
    else:
        return x + 1

Sweeps = 1300  # The number of updates

initT, finalT, steps = 0.000001, 4.0, 50  # Temperature parameters
Ignore = 100  # The number of sweeps between measuring

Dt = (finalT - initT) / steps

record = np.zeros((steps+1, 3))  # To store temperature, magnetization, and energy

for k in range(steps+1):
    Sum = 0.0
    E_sum = 0.0
    E_squared_sum = 0.0
    T = initT + k*Dt
    
    # Let make all the spins pointing up
    spin = np.ones(L)

    # Keep on flipping the spins at sites sequentially and use Metropolis algorithm to update the flips
    for n in range(1, Sweeps+1):
        for j in range(L):  # sweeping now along the row
            # find the sum of the spins of the neighbors
            sum = spin[prev(j)] + spin[next(j)]

            # calculate the "energy" associated with these bonds
            ex = spin[j] * sum

            # The Boltzmann probability of flipping the spin at site (i)
            prob = np.exp(-2.0 * ex / T)

            # Metropolis says to flip the flip if the Boltzmann probability of
            # flipping is larger than a random number between 0 and 1, else not.
            x = my_rand(j)
            if prob > x:
                spin[j] = -spin[j]
        
        # Calculate the energy of the system
        E = -np.sum(spin[i] * spin[next(i)] for i in range(L))
        
        # Do not record all the updates for averaging as we need measurements to be uncorrelated
        if n > Ignore:
            # Next measure the magnetization over the lattice which is the sum of the spins on the lattice sites
            spinsum = np.abs(np.sum(spin))
            Sum += spinsum
            E_sum += E
            E_squared_sum += E*E

    E_average = E_sum / (Sweeps - Ignore)
    E_squared_Average= E_squared_sum / (Sweeps - Ignore)
    record[k, 0] = T
    beta= 1/T
    Cv = ((beta)**2) * ((E_squared_sum)**2 - (E_average)**2)
    record[k, 1] = Cv
    


plt.plot(record[:, 0], record[:, 1], 'ro')
plt.xlabel('Temperature')
plt.ylabel('Specific heat')
plt.show()
