import numpy as np  # Import NumPy as np

# Step 1: Create a NumPy array
original_array = np.arange(1, 13)  # Creates an array with values from 1 to 12
print("Original Array:")
print(original_array)

# Step 2: Reshape the array into different dimensions
reshaped_array = np.reshape(original_array, (3, 4))  # Reshape into 3 rows and 4 columns
print("\nReshaped Array (3x4):")
print(reshaped_array)

# Step 3: Transpose of the reshaped array
transposed_array = np.transpose(reshaped_array)  # Transpose rows and columns
print("\nTransposed Array (4x3):")
print(transposed_array)

# Step 4: Swap axes of the reshaped array
# Swap axes 0 and 1
swapped_axes_array = np.swapaxes(reshaped_array, 0, 1)
print("\nArray After Swapping Axes (Rows become columns):")
print(swapped_axes_array)

# Step 5: Reshape into a 2x2x3 array and swap axes
reshaped_3d = np.reshape(original_array, (2, 2, 3))  # Reshape into a 3D array
print("\nReshaped 3D Array (2x2x3):")
print(reshaped_3d)

# Swap axes 1 and 2 in the 3D array
swapped_3d_axes = np.swapaxes(reshaped_3d, 1, 2)
print("\n3D Array After Swapping Axes (Axes 1 and 2):")
print(swapped_3d_axes)
