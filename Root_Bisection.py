import math

def f(x):
    return math.tanh(x) + x - x**3 - 1

a = float(input("Enter the lower range: "))
b = float(input("Enter the upper range: "))

# Check if the product of the function values at the two endpoints is positive
if f(a) * f(b) >= 0:
    print("Invalid input")
else:
    # Set the tolerance level to 0.001
    tol = 0.001
    # Set the maximum number of iterations to 1000
    max_iter = 1000
    # Initialize the iteration counter to 0
    i = 0
    # Start the bisection loop
    while abs(f(a) - f(b)) >= tol and i < max_iter:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    # Print the root of the equation
    print("The root of the equation is: ", c)
