import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def mesh_ranges(x_line, y_line):
    return np.meshgrid(x_line, y_line)


def line_tension(x_line, y_line, w, unit):
    weight_units = {'N': 1, 'lbs': 4.44822}
    x, y = mesh_ranges(x_line, y_line)
    a_1 = np.arctan(y / x)
    a_2 = np.arctan(y / (x_line.min() + x_line.max() - x))
    return (w * weight_units[unit]) / (np.sin(a_1) + (np.cos(a_1) / np.cos(a_2)) * np.sin(a_2))


def arr_indices_of_maximum(arr):
    return np.unravel_index(arr.argmax(), arr.shape)


def arr_indices_of_minimum(arr):
    return np.unravel_index(arr.argmin(), arr.shape)


def max_cords(x, y, z):
    maximum = arr_indices_of_maximum(z)
    return x[maximum], y[maximum], z[maximum]


def min_cords(x, y, z):
    minimum = arr_indices_of_minimum(z)
    return x[minimum], y[minimum], z[minimum]


mass_of_head = 0.3  # kg
w = mass_of_head * 9.81  # N



x_range = np.linspace(1, 250, num=500)  # cm
y_range = np.linspace(20, , num=500)  # cm

T1 = line_tension(x_range, y_range, w, 'lbs')
T2 = line_tension(x_range.max() - x_range, y_range, w, 'lbs')

print(max_cords(*mesh_ranges(x_range, y_range), T1))
print((x_range.max()**2 + y_range.max()**2)**(1/2))

fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.contour3D(*mesh_ranges(x_range, y_range), T1, 500)
ax.set_xlabel('x length of line 1 (cm)')
ax.set_ylabel('y length of line 1 (cm)')
ax.set_zlabel('tension in line 1 (lbs)')
#
# fig = plt.figure(2)
# ax = plt.axes(projection='3d')
# ax.contour3D(*mesh_ranges(x_range, y_range), T2, 1000)
# ax.set_xlabel('x length of line 2 (cm)')
# ax.set_ylabel('y length of line 2 (cm)')
# ax.set_zlabel('tension in line 2 (lbs)')
