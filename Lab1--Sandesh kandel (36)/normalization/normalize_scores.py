import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the dataset
input_file = 'normalization/student_scores.csv'
df = pd.read_csv(input_file)
print("Initial Data (first 5 rows):\n", df.head())

# Step 2: Apply Min-Max normalization to the score columns
score_columns = ['Math', 'Science', 'English']
scaler = MinMaxScaler()
normalized_values = scaler.fit_transform(df[score_columns])

# Create a new DataFrame for normalized scores
normalized_df = pd.DataFrame(normalized_values, columns=[col + '_Normalized' for col in score_columns])

# Step 3: Combine original and normalized scores side by side
result_df = pd.concat([df, normalized_df], axis=1)

print("\nOriginal and Normalized Scores (first 5 rows):\n", result_df.head())

# Step 4: Save the combined DataFrame to a new CSV file
output_file = 'normalization/normalized_student_scores.csv'
result_df.to_csv(output_file, index=False)
print(f"\nNormalization complete! Combined data saved to {output_file}") 