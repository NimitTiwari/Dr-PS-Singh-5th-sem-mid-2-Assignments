# Python program that animates a 2D car moving across the screen using translation transformations.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 30)
ax.set_aspect('equal')
ax.set_title("2D Car Animation")

# Create car components
car_body = patches.Rectangle((0, 5), 20, 10, color='blue')
wheel1 = patches.Circle((5, 5), 2, color='black')
wheel2 = patches.Circle((15, 5), 2, color='black')

# Add to plot
ax.add_patch(car_body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Animation function
def animate(frame):
    dx = frame  # translation in x-direction
    car_body.set_xy((dx, 5))
    wheel1.center = (dx + 5, 5)
    wheel2.center = (dx + 15, 5)
    return car_body, wheel1, wheel2

# Create animation
ani = FuncAnimation(fig, animate, frames=range(0, 80), interval=100, blit=True)

plt.show()
