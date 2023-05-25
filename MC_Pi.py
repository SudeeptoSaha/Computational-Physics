import random
import math
import matplotlib.pyplot as plt

# Set the number of points to use in the Monte Carlo method
num_points = 100000

# Initialize variables to keep track of the number of points inside and outside the circle
inside_circle = 0
outside_circle = 0

# Generate random points and check if they are inside the circle
for i in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    if distance <= 1:
        inside_circle += 1
    else:
        outside_circle += 1

# Calculate the value of pi using the Monte Carlo method
pi_approx = 4 * (inside_circle / num_points)

# Print the result
print("Approximate value of pi:", pi_approx)


