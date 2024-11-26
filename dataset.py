import pandas as pd

# Step 1: Load the CSV file
file_name = input("Enter the CSV file name (with extension): ")  # Example: 'data.csv'
df = pd.read_csv(file_name)

# Step 2: Display the first few rows
print("\nFirst Few Rows of the DataFrame:")
print(df.head())

# Step 3: Display information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Step 4: Display basic statistics of the DataFrame
print("\nBasic Statistics of the DataFrame:")
print(df.describe())

# Step 5: Modify the DataFrame (e.g., add a new column)
df['New_Column'] = range(1, len(df) + 1)
print("\nModified DataFrame:")
print(df.head())

# Step 6: Save the modified DataFrame to a new CSV file
output_file = input("Enter the name for the output CSV file (with extension): ")  # Example: 'output.csv'
df.to_csv(output_file, index=False)
print(f"\nModified DataFrame saved to {output_file}")
