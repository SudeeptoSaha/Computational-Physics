import numpy as np
import matplotlib.pyplot as plt

# define lattice size
L = 40

# define function to get indices of neighboring sites
def get_neighbors(i, j):
    up = i-1 if i > 0 else L-1
    down = i+1 if i < L-1 else 0
    left = j-1 if j > 0 else L-1
    right = j+1 if j < L-1 else 0
    return [(up, j), (down, j), (i, left), (i, right)]

# set number of sweeps and temperature range
sweeps = 13000
inT, finT = 0.0, 4.0
steps = 50
Dt = (finT - inT) / steps

# initialize the temperature list and results list
T_list = np.linspace(inT, finT, steps+1)
result_list = []

# loop over temperatures
for T in T_list:
    # initialize the lattice to all spin up
    spin = np.ones((L, L), dtype=int)
    
    # loop over sweeps
    result = 0
    for n in range(1, sweeps):
        # loop over all sites in random order
        site_list = np.random.permutation(L*L)
        for q in site_list:
            i, j = divmod(q, L)
            spin_ptr = spin[i, j]
            neighbors = np.array(get_neighbors(i, j))
            sum = np.sum(spin[neighbors[:,0], neighbors[:,1]])
            ex = spin_ptr * sum
            prob = np.exp(-2.0 * ex / T)
            if np.random.random() < prob:
                spin[i, j] = -spin[i, j]
        
        # only calculate results after some initial number of sweeps
        if n > 2000:
            result += np.abs(np.sum(spin))
    
    # calculate and append the average result for this temperature
    result_list.append(result / (sweeps - 2000))

# plot the results
plt.plot(T_list, result_list, 'bo-')
plt.xlabel('Temperature')
plt.ylabel('Average Magnetization')
plt.show()
