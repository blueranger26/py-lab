import array

# Creating an array using the array module
student_array = array.array('i', [4, 54, 43])
print("Original Array:", student_array)

# Accessing elements (same for both array and list)
print("Element at index 0 in Array:", student_array[0])

# Updating elements (same for both array and list)
student_array[0] = 5
print("Updated Array:", student_array)

# List Example
student_list = [4, 54, 43]
print("\nOriginal List:", student_list)

# Accessing elements in list (same as array)
print("Element at index 0 in List:", student_list[0])

# Updating elements (same for both array and list)
student_list[0] = 5
print("Updated List:", student_list)

# Inserting an element
student_array.insert(2, 6)  # Works with arrays
print("\nArray after insert:", student_array)

# Appending an element (works for both array and list)
student_array.append(10)
print("Array after append:", student_array)

student_list.append(10)
print("\nList after append:", student_list)

# Sorting the array (Requires conversion to list for sorting)
sorted_array = sorted(student_array)  # sorted() creates a new list
print("Sorted Array (created new list):", sorted_array)

# Sorting the list (works directly with list)
student_list.sort()  # In-place sort for list
print("Sorted List:", student_list)

# Reversing the array using slicing
reversed_array = student_array[::-1]  # Slicing creates a new reversed array
print("\nReversed Array using slicing:", reversed_array)

# Reversing the list (in-place reverse)
student_list.reverse()  # In-place reverse for list
print("Reversed List:", student_list)

# Copying the array (array.copy() is used)
copied_array = student_array.copy()  # In-place copy
print("\nCopied Array:", copied_array)

# Copying the list (list.copy() is used)
copied_list = student_list.copy()  # In-place copy for lists
print("Copied List:", copied_list)

# Popping an element (works for both array and list)
popped_value_array = student_array.pop(2)
print("\nPopped Value from Array:", popped_value_array)
print("Array after popping:", student_array)

popped_value_list = student_list.pop(2)
print("Popped Value from List:", popped_value_list)
print("List after popping:", student_list)

# Removing an element (works for both array and list)
student_array.remove(54)
print("\nArray after removing 54:", student_array)

student_list.remove(54)
print("List after removing 54:", student_list)

# Searching for a value (works for both array and list)
search_value = 10
if search_value in student_array:
    print(f"\nValue {search_value} found in Array")
else:
    print(f"Value {search_value} not found in Array")

if search_value in student_list:
    print(f"Value {search_value} found in List")
else:
    print(f"Value {search_value} not found in List")

# Comparing performance of array vs list (simple comparison without time module)
print("\nArray vs List function comparison:")

# List specific function: extend
# The array module does not have extend()
student_list.extend([100, 200, 300])  # Adds elements to the list
print("List after extend:", student_list)

# Array specific function: buffer_info()
# The list does not have buffer_info()
print("\nArray Buffer Info:", student_array.buffer_info())

# List specific function: count (to count occurrences)
print("Count of 10 in List:", student_list.count(10))

# Array specific function: itemsize (size of one element)
print("Item size of Array:", student_array.itemsize)
