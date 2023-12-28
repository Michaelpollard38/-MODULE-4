import matplotlib.pyplot as plt
import numpy as np

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def choose_direction(self):
        direction = np.random.choice([1, -1])
        distance = np.random.choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.choose_direction()
            y_step = self.choose_direction()

            # Avoiding steps that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculating new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Creating a RandomWalk instance
rw = RandomWalk()
rw.fill_walk()

# Plotting the Random Walk
plt.figure(figsize=(10, 6))
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

# Emphasizing the starting and ending points
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Styling the Walk
plt.title('Random Walk', fontsize=18)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.show()

# Generating Multiple Random Walks
plt.figure(figsize=(10, 6))

for _ in range(5):  # Generating 5 random walks
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)

plt.title('Multiple Random Walks', fontsize=18)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.show()
