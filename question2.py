# Python implementation of the DDA (Digital Differential Analyzer) line drawing algorithm using matplotlib for visualization.

import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))  # Number of steps = max(dx, dy)

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

def plot_line(points):
    x_vals, y_vals = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, marker='o', color='blue')
    plt.title("DDA Line Drawing")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Example usage
x_start, y_start = 2, 3
x_end, y_end = 15, 10

line_points = dda_line(x_start, y_start, x_end, y_end)
plot_line(line_points)
