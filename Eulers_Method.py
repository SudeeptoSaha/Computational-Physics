import matplotlib.pyplot as plt

# Define initial conditions and time step
x, v, h = 1, 0, 0.01

# Initialize arrays to store solution values
t, x_vals, v_vals = [0], [x], [v]

# Calculate solutions using Euler method
for i in range(10000):
    x, v = x + h * v, v - h * x
    t.append(t[-1] + h)
    x_vals.append(x)
    v_vals.append(v)

# Plot graphs
plt.subplot(131)
plt.plot(t, x_vals)
plt.xlabel('t')
plt.ylabel('x')
plt.title('x Vs t')

plt.subplot(132)
plt.plot(x_vals, v_vals)
plt.xlabel('x')
plt.ylabel('v')
plt.title('x Vs v')

plt.subplot(133)
plt.plot(t, v_vals)
plt.xlabel('t')
plt.ylabel('v')
plt.title('v Vs t')

plt.tight_layout()
plt.show()
