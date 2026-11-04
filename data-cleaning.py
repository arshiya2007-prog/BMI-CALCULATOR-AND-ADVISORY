import pandas as pd

# Load data
df = pd.read_csv(r"bmi.csv")

print("----- ORIGINAL DATA -----")
print(df.head())

# Check dataset information
print("\n----- DATA INFORMATION -----")
print(df.info())

# Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Check duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Reset index
df = df.reset_index(drop=True)

print("\n----- CLEANED DATA -----")
print(df.head())

print("\nRows after cleaning:", df.shape[0])
print("Columns:", df.shape[1])

# Save cleaned dataset
df.to_csv("cleaned_bmi.csv", index=False)

print("\nCleaned data saved successfully!")
