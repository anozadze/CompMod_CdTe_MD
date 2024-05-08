import os
import numpy as np
import matplotlib as plt
import pandas as pd

path_to_file = "/Users/noamfisher/Desktop/Comp_MSMS/Project/Annealing/log_anneal.lammps"
data = np.genfromtxt(path_to_file, usecols=[0, 1, 2, 3, 4, 5, 6], skip_header=4, skip_footer=41)
time=[x[1] for x in data]
temperature=[x[2] for x in data]
energy=[(x[3]/500.0) for x in data]
pressure=[x[5] for x in data]
volume=[(x[6]/500.0) for x in data]

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from the file
data = np.genfromtxt('log_anneal.lammps', usecols=[0, 1, 2, 3, 4, 5, 6], skip_header=4, skip_footer=41)

time = [x[1] for x in data]
temperature = [x[2] for x in data]
energy = [(x[3] / 500.0) for x in data]
pressure = [x[5] for x in data]
volume = [(x[6] / 500.0) for x in data]

# Perform linear regression
coefficients = np.polyfit(temperature, volume, 1)
polynomial = np.poly1d(coefficients)
equation = f"y = {coefficients[0]:.4f}x + {coefficients[1]:.4f}"  # Format the equation string

# Create a new X data for smooth line
x_new = np.linspace(min(temperature), max(temperature), 100)
y_new = polynomial(x_new)

# Plot the data and the best-fit line
plt.scatter(temperature, volume)
plt.plot(x_new, y_new, color='red', label=equation)
plt.xlabel('Temperature')
plt.ylabel('Volume per atom ($\AA^{3}$')
plt.title('Best Linear Fit for Volume vs. Temperature')
plt.legend()
plt.show()

def calculate_rmse(coefficients, x, y):
    poly = np.poly1d(coefficients)
    y_poly = poly(x)
    rmse = np.sqrt(np.mean((y - y_poly) ** 2))
    return rmse

# Try different polynomial degrees and find the best fit
best_degree = 0
best_rmse = float('inf')
best_coefficients = None

for degree in range(1, 6):  # Try degrees from 1 to n-1
    coefficients = np.polyfit(temperature, volume, degree)
    rmse = calculate_rmse(coefficients, temperature, volume)
    if rmse < best_rmse:
        best_degree = degree
        best_rmse = rmse
        best_coefficients = coefficients

print(f"Best polynomial degree: {best_degree}")
print(f"Best RMSE: {best_rmse:.4f}")

# Create the best-fit polynomial equation string
best_polynomial = np.poly1d(best_coefficients)
equation_terms = [f"{coeff:.4f}x^{deg}" for deg, coeff in enumerate(best_coefficients[::-1])]
best_equation = "y = " + " + ".join(equation_terms)
print(f"Best-fit equation: {best_equation}")

# Plot the data and the best-fit line
x_new = np.linspace(min(temperature), max(temperature), 100)
y_new = best_polynomial(x_new)

plt.scatter(temperature, volume)
plt.plot(x_new, y_new, color='red', label=best_equation)
plt.xlabel('Temperature')
plt.ylabel('Volume')
plt.title('Best Polynomial Fit for Volume vs. Temperature')
plt.legend()
plt.show()
