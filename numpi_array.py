# Step 1: Install NumPy (This is for reference; run this in your terminal or notebook if not installed)
# !pip install numpy

# Step 2: Import NumPy
import numpy as np

# Step 3: Create arrays using lists
list_array = np.array([1, 2, 3, 4, 5])
print("Array from List:")
print(list_array)
print(f"Attributes: Shape: {list_array.shape}, Size: {list_array.size}, DataType: {list_array.dtype}\n")

# Step 4: Create arrays using built-in functions

# Array of zeros
zeros_array = np.zeros((2, 3))
print("Array of Zeros:")
print(zeros_array)
print(f"Attributes: Shape: {zeros_array.shape}, Size: {zeros_array.size}, DataType: {zeros_array.dtype}\n")

# Array of ones
ones_array = np.ones((3, 2), dtype=int)
print("Array of Ones:")
print(ones_array)
print(f"Attributes: Shape: {ones_array.shape}, Size: {ones_array.size}, DataType: {ones_array.dtype}\n")

# Array with a range of values
range_array = np.arange(10, 20, 2)
print("Array with Range:")
print(range_array)
print(f"Attributes: Shape: {range_array.shape}, Size: {range_array.size}, DataType: {range_array.dtype}\n")

# Array with evenly spaced values
linspace_array = np.linspace(0, 1, 5)
print("Array with Linspace:")
print(linspace_array)
print(f"Attributes: Shape: {linspace_array.shape}, Size: {linspace_array.size}, DataType: {linspace_array.dtype}\n")

# Identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:")
print(identity_matrix)
print(f"Attributes: Shape: {identity_matrix.shape}, Size: {identity_matrix.size}, DataType: {identity_matrix.dtype}\n")
