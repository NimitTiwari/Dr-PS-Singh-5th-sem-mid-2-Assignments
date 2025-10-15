# Python program that animates a bouncing ball using 2D geometric transformations—specifically translation and reflection to simulate bounce.


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.set_aspect('equal')
ax.set_title("2D Bouncing Ball Animation")

# Create the ball
ball = patches.Circle((10, 10), radius=3, color='red')
ax.add_patch(ball)

# Initial parameters
x, y = 10, 10
vx, vy = 1.5, 2.0  # velocity in x and y
gravity = -0.2
bounce_damping = 0.8

def animate(frame):
    global x, y, vx, vy

    # Update position
    x += vx
    y += vy
    vy += gravity  # gravity effect

    # Bounce off floor
    if y <= 3:
        y = 3
        vy = -vy * bounce_damping

    # Bounce off walls
    if x <= 3 or x >= 97:
        vx = -vx

    ball.center = (x, y)
    return ball,

# Run animation
ani = FuncAnimation(fig, animate, frames=300, interval=30, blit=True)
plt.show()
