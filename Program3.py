import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot a simple line graph
plt.plot(x, y, label='Sine Function')

# Changing label type and line thickness
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')
plt.legend()
plt.grid(True)
plt.show()

# Using built-in styles
plt.style.use('seaborn-darkgrid')

# Plotting and styling individual points with scatter()
plt.scatter(x, y, color='red', marker='o', label='Data Points')

# Plotting a series of points with scatter()
x_series = np.random.rand(50)
y_series = np.random.rand(50)
plt.scatter(x_series, y_series, color='blue', marker='x', label='Random Data')

# Calculating data automatically
x_auto = np.linspace(0, 10, 20)
y_auto = x_auto**2
plt.scatter(x_auto, y_auto, color='green', marker='s', label='Automatic Data')

# Defining custom colors
plt.scatter(x, y, color='#FF5733', marker='^', label='Custom Color')

# Using a colormap
colors = np.arange(len(x))
plt.scatter(x, y, c=colors, cmap='viridis', marker='D', label='Colormap')

# Saving plots automatically
plt.savefig('output_plot.png', dpi=300)

# Show all plots
plt.legend()
plt.show()


import random

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)
