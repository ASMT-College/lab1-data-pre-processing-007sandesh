import pandas as pd

# Step 1: Load the dataset
input_file = 'discretization/sales_data.csv'
df = pd.read_csv(input_file)
print("Initial Data (first 5 rows):\n", df.head())

# Step 2: Discretize the 'Sales' column into 4 equal-width bins
bins = 4
df['Sales_Binned'] = pd.cut(df['Sales'], bins=bins, labels=[f'Bin_{i+1}' for i in range(bins)])

print("\nData with Discretized Sales (first 5 rows):\n", df.head())

# Step 3: Save the discretized data to a new CSV file
output_file = 'discretization/discretized_sales_data.csv'
df.to_csv(output_file, index=False)
print(f"\nDiscretization complete! Discretized data saved to {output_file}") 