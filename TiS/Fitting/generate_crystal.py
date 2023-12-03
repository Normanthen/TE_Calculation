import numpy as np
import sys

args = sys.argv

def generate_points(first: np.ndarray, last: np.ndarray, n: int) -> np.ndarray:
    """
    Generates n points between first and last point.
    """
    return np.linspace(first, last, n) 

if (len(args) == 2):
    filename = args[1]
    use_file_weight = True

elif (len(args) == 3):
    filename = args[1]
    npoints = int(args[2])
    use_file_weight = False
else: 
    filename = input("Enter the filename: ")


array_of_crystal_b = np.loadtxt(filename)

n_array = np.shape(array_of_crystal_b)[0]
if use_file_weight:
    sum_of_weight = int(np.sum(array_of_crystal_b[:, 3]))
else:
    sum_of_weight = npoints * n_array

print(sum_of_weight)

for i in range(n_array - 1):
    if (use_file_weight): weight = int(array_of_crystal_b[i, 3])
    else: weight = npoints
    points = generate_points(array_of_crystal_b[i, :3], array_of_crystal_b[i+1, :3], weight)

    for i in range(len(points)):
        print(f"{points[i, 0]:.16f} {points[i, 1]:.16f} {points[i, 2]:.16f} 1")