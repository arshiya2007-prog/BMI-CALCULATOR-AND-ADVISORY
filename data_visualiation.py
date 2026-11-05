import pandas as pd
import plotly.express as px


# Read the CSV file
df = pd.read_csv(r"C:\Users\athek\Desktop\DAV\cleaned_bmi.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df["Index"].value_counts().sort_index())

# BMI category mapping
bmi_categories = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obesity",
    5: "Extreme Obesity"
}

df["BMI Category"] = df["Index"].map(bmi_categories)

# BAR GRAPH: Number of people in each BMI category
bmi_count = (
    df["BMI Category"]
    .value_counts()
    .reset_index()
)
bmi_count.columns = ["BMI Category", "Count"]

fig = px.bar(
    bmi_count,
    x="BMI Category",
    y="Count",
    title="Number of People in Each BMI Category",
    labels={"Count": "Number of People"},
    text="Count"
)
fig.show()


# HISTOGRAM: Weight distribution
fig = px.histogram(
    df,
    x="Weight",
    title="Distribution of Weight",
    nbins=30,
    labels={"Weight": "Weight (kg)"}
)
fig.show()


# PIE CHART: Gender distribution
gender_count = df["Gender"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]

fig = px.pie(
    gender_count,
    names="Gender",
    values="Count",
    title="Gender Distribution",
    hole=0.3
)
fig.show()


# SCATTER PLOT: Height vs Weight
fig = px.scatter(
    df,
    x="Height",
    y="Weight",
    color="BMI Category",
    hover_data=["Gender", "Index"],
    title="Height vs Weight by BMI Category",
    labels={
        "Height": "Height (cm)",
        "Weight": "Weight (kg)"
    }
)
fig.show()


# HEATMAP: Correlation between numerical columns
corr = df[["Height", "Weight", "Index"]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap of BMI Dataset",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1
)
fig.show()


# GROUPED BAR GRAPH: BMI category by gender
gender_bmi = (
    df.groupby(["BMI Category", "Gender"])
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    gender_bmi,
    x="BMI Category",
    y="Count",
    color="Gender",
    barmode="group",
    title="BMI Categories by Gender"
)
fig.show()


# BOX PLOT: Weight distribution by gender
fig = px.box(
    df,
    x="Gender",
    y="Weight",
    color="Gender",
    title="Weight Distribution by Gender",
    labels={"Weight": "Weight (kg)"}
)
fig.show()


# HISTOGRAM: Height distribution
fig = px.histogram(
    df,
    x="Height",
    title="Distribution of Height",
    nbins=30,
    labels={"Height": "Height (cm)"}
)
fig.show()


# BAR GRAPH: Average weight by gender
avg_weight = (
    df.groupby("Gender")["Weight"]
    .mean()
    .reset_index()
)

fig = px.bar(
    avg_weight,
    x="Gender",
    y="Weight",
    title="Average Weight by Gender",
    labels={"Weight": "Average Weight (kg)"},
    text_auto=".2f"
)
fig.show()


# VIOLIN PLOT: Weight distribution by BMI category
fig = px.violin(
    df,
    x="BMI Category",
    y="Weight",
    color="BMI Category",
    box=True,
    points="outliers",
    title="Weight Distribution by BMI Category"
)
fig.show()
