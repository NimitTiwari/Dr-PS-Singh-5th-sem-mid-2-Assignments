# Python program using matplotlib and NumPy to perform translation, rotation, and scaling on a 2D polygon (triangle, in this case).

import numpy as np
import matplotlib.pyplot as plt

# Original 2D object: triangle
triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])  # Closed triangle

def translate(points, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    return apply_transform(points, T)

def rotate(points, angle_deg):
    angle_rad = np.radians(angle_deg)
    R = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                  [np.sin(angle_rad),  np.cos(angle_rad), 0],
                  [0, 0, 1]])
    return apply_transform(points, R)

def scale(points, sx, sy):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    return apply_transform(points, S)

def apply_transform(points, matrix):
    # Convert to homogeneous coordinates
    ones = np.ones((points.shape[0], 1))
    homogenous_points = np.hstack([points, ones])
    transformed = homogenous_points @ matrix.T
    return transformed[:, :2]

def plot_shapes(original, translated, rotated, scaled):
    plt.figure(figsize=(10, 6))
    plt.plot(*original.T, label='Original', marker='o')
    plt.plot(*translated.T, label='Translated', marker='o')
    plt.plot(*rotated.T, label='Rotated', marker='o')
    plt.plot(*scaled.T, label='Scaled', marker='o')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.title("2D Transformations: Translation, Rotation, Scaling")
    plt.show()

# Apply transformations
translated = translate(triangle, tx=2, ty=1)
rotated = rotate(triangle, angle_deg=45)
scaled = scale(triangle, sx=2, sy=0.5)

# Plot all
plot_shapes(triangle, translated, rotated, scaled)
