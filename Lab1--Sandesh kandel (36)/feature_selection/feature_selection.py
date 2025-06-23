import pandas as pd

# Step 1: Load the dataset
input_file = 'feature_selection/medical_data.csv'
df = pd.read_csv(input_file)
print("Initial Data (first 5 rows):\n", df.head())

# Step 2: Select the top 2 features most correlated with the target
# Assume the last column is the target
feature_cols = df.columns[:-1]
target_col = df.columns[-1]
correlations = df[feature_cols].corrwith(df[target_col]).abs()
top_features = correlations.sort_values(ascending=False).head(2).index.tolist()

print(f"\nTop 2 features most correlated with target ('{target_col}'):", top_features)

# Step 3: Save the selected features and target to a new CSV file
selected_df = df[top_features + [target_col]]
output_file = 'feature_selection/selected_features.csv'
selected_df.to_csv(output_file, index=False)
print(f"\nFeature selection complete! Selected features saved to {output_file}") 