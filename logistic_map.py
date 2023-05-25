import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x, iterations=100):
    for n in range(iterations):
        x = r * x * (1 - x)
    return x

R = np.linspace(1, 3.7, num=10000)
X = []
Y = []

for r in R:
    X.append(r)
    x = np.random.uniform(0, 1)
    y = logistic_map(r, x)
    Y.append(y)

plt.plot(X,Y, ls='',marker=',')
plt.show()

    
