# Import required libraries
import pandas as pd
# Import dataset
df = pd.read_csv("student_performance.csv")
# View dataset
print("First 5 Records:")
print(df.head())
# Shape, dimension and column names
print("\nShape of dataset     :", df.shape)
print("Dimension of dataset :", df.ndim)
print("Column names         :", df.columns.tolist())
# Select data using column number (iloc)
print("\nSelect rows 0-2 and columns 0-2 using iloc:")
print(df.iloc[0:3, 0:3])
# Select data using column names
print("\nSelect columns using names:")
print(df[["Name", "Marks"]].head())
# Simple conditional selection
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80][["Name", "Marks"]])
# Compound conditional selection
print("\nScience students with Attendance >= 90:")
science_90 = df[(df["Department"] == "Science") & (df["Attendance"] >= 90)]
print(science_90[["Name", "Department", "Attendance"]])
print("\nStudents from Arts OR Marks < 60:")
arts_or_low = df[(df["Department"] == "Arts") | (df["Marks"] < 60)]
print(arts_or_low[["Name", "Department", "Marks"]])
# Update and modify dataset
df.loc[df["Name"] == "Anil", "Marks"] = 58          # update a value
# add new column
df["Result"] = df["Marks"].apply(lambda m: "Pass" if m >= 60 else "Fail")
df = df.rename(columns={"Study_Hours": "Hours"})    # rename column
df = df.drop(columns=["Age"])                       # drop column
print("\nModified Dataset:")
print(df.head(8))
print("\nNew Shape:", df.shape)
