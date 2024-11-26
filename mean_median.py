import numpy as np

# Step 1: Create a NumPy array
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original Array:")
print(data)

# Step 2: Calculate basic statistical metrics
mean_value = np.mean(data)  # Calculate mean
median_value = np.median(data)  # Calculate median
std_deviation = np.std(data)  # Calculate standard deviation
variance_value = np.var(data)  # Calculate variance

print("\nBasic Statistical Metrics:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Variance: {variance_value}")

# Step 3: Compute percentiles
percentile_25 = np.percentile(data, 25)  # 25th percentile
percentile_50 = np.percentile(data, 50)  # 50th percentile (median)
percentile_75 = np.percentile(data, 75)  # 75th percentile

print("\nPercentiles:")
print(f"25th Percentile: {percentile_25}")
print(f"50th Percentile (Median): {percentile_50}")
print(f"75th Percentile: {percentile_75}")

# Step 4: Compute correlation coefficients
# Create another array to compare
data2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
correlation_matrix = np.corrcoef(data, data2)

print("\nCorrelation Coefficients:")
print("Correlation Matrix:")
print(correlation_matrix)
print(f"Correlation Coefficient between data and data2: {correlation_matrix[0, 1]}")
