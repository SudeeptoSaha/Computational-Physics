import numpy as np
import random
K = 1.0    
beta = 1.0 

def calculate_energy(x):
    return 0.5 * K * x**2
#Define initial state
x_i = random.uniform(0,1)
E_i = calculate_energy(x_i)

#Define final state
sigma = 1.0   
final = lambda x: np.random.normal(x, sigma)

n_steps = 10000
reject=0

for i in range(n_steps):
    # Generate a final state
    x_f = final(x_i)
    E_f = calculate_energy(x_f)
    
    # Calculate the relative probability of picking the final state over the current state
    X = np.exp(-beta * (E_f - E_i))
    
    # Accept or reject the final state
    if E_f < E_i:
        reject +=1
    else:
        r = np.random.uniform()
        if X > r:
            reject +=1
accept= (n_steps-reject)

accept_ratio= (n_steps-reject)/n_steps   

print("Total Accept:",accept)
print("Accept_Ratio:",accept_ratio)
