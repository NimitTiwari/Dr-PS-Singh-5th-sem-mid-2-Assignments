# Python program that draws a polygon using the Bresenham Line Drawing Algorithm. You define the polygon by its vertices, and the program connects each pair of consecutive vertices to form the edges.

import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x, y = x1, y1

    if dy <= dx:
        err = 2 * dy - dx
        for _ in range(dx + 1):
            points.append((x, y))
            if err >= 0:
                y += sy
                err -= 2 * dx
            x += sx
            err += 2 * dy
    else:
        err = 2 * dx - dy
        for _ in range(dy + 1):
            points.append((x, y))
            if err >= 0:
                x += sx
                err -= 2 * dy
            y += sy
            err += 2 * dx

    return points

def draw_polygon(vertices):
    polygon_points = []
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to first vertex
        edge_points = bresenham_line(x1, y1, x2, y2)
        polygon_points.extend(edge_points)

    return polygon_points

def plot_polygon(points):
    x_vals, y_vals = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, marker='o', color='purple')
    plt.title("Polygon Drawing using Bresenham Algorithm")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Example polygon: pentagon
polygon_vertices = [(5, 2), (8, 4), (7, 8), (3, 8), (2, 4)]

polygon_points = draw_polygon(polygon_vertices)
plot_polygon(polygon_points)
