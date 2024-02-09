import matplotlib.pyplot as plt
import random

def random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

def get_indexes(n):
    return list(range(1, n+1))

# Sample data
# make a list of random numbers each time
# make a list of number from 1 to n

x = get_indexes(50)
y = random_numbers(50)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot')

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the data
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')

# Displaying the graph
plt.show()
