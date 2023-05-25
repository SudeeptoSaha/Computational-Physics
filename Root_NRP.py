import math

# Define the function f
def f(x):
    return math.tanh(x) + x - x**3 - 1

# Define the derivative of the function f
def df(x):
    return 1 - 3*x**2 + 1/math.cosh(x)**2

# Define the Newton-Raphson method to find the root of f
def newton_raphson(x0, eps):
    x = x0
    while True:
        fx = f(x)
        dfx = df(x)
        x_next = x - fx / dfx
        if abs(x_next - x) < eps:
            return x_next
        x = x_next

# Get the user input for the lower and upper bounds of the root
a = float(input("Enter lower bound: "))
b = float(input("Enter upper bound: "))

# Use the midpoint of the bounds as the initial guess for the root
x0 = (a + b) / 2

# Set the tolerance for the Newton-Raphson method
eps = 0.001

# Find the root using the Newton-Raphson method
root = newton_raphson(x0, eps)

# Print the root of the function
print("The root of the function is: ", root)
