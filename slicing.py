import numpy as np

# Step 1: Create a 2D NumPy array
array = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print("Original Array:")
print(array)

# Step 2: Access specific elements
print("\nAccessing Specific Elements:")
print("Element at row 0, column 1:", array[0, 1])  # Access element in the first row, second column
print("Element at row 2, column 2:", array[2, 2])  # Access element in the third row, third column

# Step 3: Access specific rows and columns
print("\nAccessing Rows and Columns:")
print("First Row:", array[0])  # Access the first row
print("Second Column:", array[:, 1])  # Access the second column

# Step 4: Slicing to extract subarrays
print("\nSlicing Operations:")
print("Top-left 2x2 subarray:")
print(array[0:2, 0:2])  # Extract a 2x2 subarray from the top-left corner
print("Last row, all columns:")
print(array[2, :])  # Extract the last row

# Step 5: Boolean indexing
print("\nBoolean Indexing:")
bool_condition = array > 50  # Create a Boolean mask
print("Boolean Mask (elements > 50):")
print(bool_condition)
print("Elements > 50:")
print(array[bool_condition])  # Apply the mask to extract elements

# Step 6: Fancy indexing
print("\nFancy Indexing:")
rows = [0, 2]  # Specify rows to extract
columns = [1, 2]  # Specify columns to extract
print("Selected elements from rows [0, 2] and columns [1, 2]:")
print(array[rows, columns])  # Extract specific elements based on row and column indices

# Step 7: Modify elements using fancy indexing
array[[0, 1], [0, 2]] = 99  # Modify elements at (0, 0) and (1, 2)
print("\nArray After Modification:")
print(array)
