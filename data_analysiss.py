
import pandas as pd
import os

# ----------------------------------
# 1. LOAD THE CLEANED DATASET
# ----------------------------------

if os.path.exists("cleaned_bmi.csv"):
    df = pd.read_csv("cleaned_bmi.csv")
    print("Cleaned dataset loaded successfully!")

elif os.path.exists("bmi.csv"):
    df = pd.read_csv("bmi.csv")
    print("Original dataset loaded successfully!")

else:
    print("Error: Dataset not found!")
    raise SystemExit

# ----------------------------------
# 2. DISPLAY BASIC INFORMATION
# ----------------------------------

print("\n----- DATASET OVERVIEW -----")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

# ----------------------------------
# 3. STATISTICAL ANALYSIS
# ----------------------------------

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())

# ----------------------------------
# 4. BMI CALCULATION
# ----------------------------------

if "Height" in df.columns and "Weight" in df.columns:

    df["BMI"] = df["Weight"] / ((df["Height"] / 100) ** 2)

    print("\n----- BMI ANALYSIS -----")
    print("Average BMI:", round(df["BMI"].mean(), 2))
    print("Minimum BMI:", round(df["BMI"].min(), 2))
    print("Maximum BMI:", round(df["BMI"].max(), 2))

# ----------------------------------
# 5. GENDER-WISE ANALYSIS
# ----------------------------------

if "Gender" in df.columns:

    print("\n----- GENDER DISTRIBUTION -----")
    print(df["Gender"].value_counts())

    if "BMI" in df.columns:
        gender_analysis = df.groupby("Gender")["BMI"].agg(
            ["mean", "min", "max", "count"]
        )

        print("\nGender-wise BMI Analysis:")
        print(gender_analysis)

        gender_analysis.to_csv("gender_bmi_analysis.csv")

# ----------------------------------
# 6. INDEX DISTRIBUTION
# ----------------------------------

if "Index" in df.columns:

    print("\n----- INDEX DISTRIBUTION -----")
    print(df["Index"].value_counts().sort_index())

    index_analysis = df.groupby("Index").size().reset_index(
        name="Count"
    )

    index_analysis.to_csv("index_distribution.csv", index=False)

# ----------------------------------
# 7. CORRELATION ANALYSIS
# ----------------------------------

numeric_df = df.select_dtypes(include="number")

print("\n----- CORRELATION MATRIX -----")
print(numeric_df.corr())

# ----------------------------------
# 8. SAVE ANALYSED DATA
# ----------------------------------

df.to_csv("bmi_analysis_results.csv", index=False)

print("\nAnalysis completed successfully!")
print("Generated Files:")
print("1. bmi_analysis_results.csv")
print("2. gender_bmi_analysis.csv (if Gender is available)")
print("3. index_distribution.csv (if Index is available)")
