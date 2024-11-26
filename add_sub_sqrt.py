import numpy as np  # Import NumPy as np

# Step 1: Create two NumPy arrays
array1 = np.array([4, 9, 16, 25])
array2 = np.array([2, 3, 4, 5])

print("Array 1:", array1)
print("Array 2:", array2)

# Step 2: Perform element-wise operations
add_result = np.add(array1, array2)  # Element-wise addition
sub_result = np.subtract(array1, array2)  # Element-wise subtraction
mul_result = np.multiply(array1, array2)  # Element-wise multiplication
div_result = np.divide(array1, array2)  # Element-wise division

print("\nElement-wise Addition:", add_result)
print("Element-wise Subtraction:", sub_result)
print("Element-wise Multiplication:", mul_result)
print("Element-wise Division:", div_result)

# Step 3: Universal functions
sqrt_result = np.sqrt(array1)  # Square root of elements
log_result = np.log(array1)  # Natural logarithm of elements
exp_result = np.exp(array2)  # Exponential of elements

print("\nSquare Root of Array 1:", sqrt_result)
print("Natural Logarithm of Array 1:", log_result)
print("Exponential of Array 2:", exp_result)
