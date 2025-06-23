import pandas as pd

# Step 1: Load the dataset
print("Loading employee data...")
df = pd.read_csv('employee_data.csv')
print("\nInitial Data:")
print(df)

# Step 2: Handle missing values
print("\nHandling missing values...")
# Fill missing 'Age' with the average age (ignoring missing values)
avg_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(round(avg_age))
# Fill missing 'Salary' with the average salary (ignoring missing values)
avg_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(round(avg_salary))
print("\nData after filling missing values:")
print(df)

# Step 3: Standardize department names
print("\nStandardizing department names...")
department_map = {
    'HR': 'HR',
    'Human Resources': 'HR',
    'H.R.': 'HR',
    'hr': 'HR',
    'Finance': 'Finance',
    'IT': 'IT'
}
df['Department'] = df['Department'].map(department_map)
print("\nData after standardizing department names:")
print(df)

# Step 4: Remove duplicate records based on 'ID'
print("\nRemoving duplicate records based on 'ID'...")
df = df.drop_duplicates(subset=['ID'], keep='first')
print("\nCleaned Data:")
print(df)

# Step 5: Save the cleaned data to a new CSV file
output_file = 'cleaned_employee_data.csv'
print(f"\nAttempting to save cleaned data to {output_file} ...")
try:
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
except Exception as e:
    print(f"Error saving file: {e}")

print("Hello, world!") 