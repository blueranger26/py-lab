import pandas as pd

# Step 1: Create a dictionary of lists
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [23, 30, 25, 35, 29],
    "Salary": [50000, 60000, 55000, 65000, 62000],
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}

# Step 2: Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Step 3: Display the first few rows
print("\nFirst Few Rows of the DataFrame:")
print(df.head())

# Step 4: Display the last few rows
print("\nLast Few Rows of the DataFrame:")
print(df.tail())

# Step 5: Display information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Step 6: Display basic statistics of the DataFrame
print("\nBasic Statistics of the DataFrame:")
print(df.describe())

# Step 7: Display the entire DataFrame
print("\nFull DataFrame:")
print(df)
