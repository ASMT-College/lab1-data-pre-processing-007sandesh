import pandas as pd

# Step 1: Load the dataset
input_file = 'binning/customer_ages.csv'
df = pd.read_csv(input_file)
print("Initial Data (first 5 rows):\n", df.head())

# Step 2: Apply binning to the 'Age' column
# We'll create 3 bins: Young, Middle, Old
bins = [0, 30, 50, 100]
labels = ['Young', 'Middle', 'Old']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

print("\nData with Age Groups (first 5 rows):\n", df.head())

# Step 3: Save the binned data to a new CSV file
output_file = 'binning/binned_customer_ages.csv'
df.to_csv(output_file, index=False)
print(f"\nBinning complete! Binned data saved to {output_file}") 