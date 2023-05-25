import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set the number of points to use in the Monte Carlo method
num_points = 1000

# Initialize variable to keep track of the number of points inside the volume
inside_volume = 0

# Generate random points and check if they are inside the volume
for i in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1-x)
    z = random.uniform(0, 1-x-y)
    if x + y + z <= 1:
        inside_volume += 1

# Calculate the value of the volume using the Monte Carlo method
volume_approx = inside_volume / num_points

# Print the result
print("Approximate value of the volume:", volume_approx)

# Plot and shade the volume generated
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
x, y = np.linspace(0, 1, 20), np.linspace(0, 1, 20)
X, Y = np.meshgrid(x, y)
Z = 1 - X - Y
ax.plot_surface(X, Y, Z, alpha=0.2, color='#4169e1')
for i in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1-x)
    z = random.uniform(0, 1-x-y)
    if x + y + z <= 1:
        ax.scatter(x, y, z, color='#4169e1', alpha=0.2)
    else:
        ax.scatter(x, y, z, color='#ff4500', alpha=0.2)
plt.show()
