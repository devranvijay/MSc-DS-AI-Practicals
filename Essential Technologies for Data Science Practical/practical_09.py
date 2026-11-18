# Import required libraries
import pandas as pd
# Import dataset
df = pd.read_csv("student_performance.csv")
# Group by single column
print("Average Marks by Department:")
print(df.groupby("Department")["Marks"].mean().round(2))
# Count of students in each group
print("\nNumber of Students by Department:")
print(df.groupby("Department")["Name"].count())
# Multiple summary statistics using agg()
print("\nSummary of Marks by Department:")
print(df.groupby("Department")["Marks"]
      .agg(["count", "mean", "min", "max"]).round(2))
# Group by multiple columns
print("\nAverage Marks by Department and Gender:")
print(df.groupby(["Department", "Gender"])["Marks"].mean().round(2))
# Sorting in ascending order
print("\nSorted by Marks (Ascending):")
print(df.sort_values(by="Marks")[["Name", "Department", "Marks"]].head())
# Sorting in descending order
print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False)
      [["Name", "Department", "Marks"]].head())
# Sorting by multiple columns
print("\nSorted by Department (A-Z) and Marks (High-Low):")
print(df.sort_values(by=["Department", "Marks"], ascending=[True, False])
      [["Name", "Department", "Marks"]])
# Top 3 students using nlargest()
print("\nTop 3 Students:")
print(df.nlargest(3, "Marks")[["Name", "Marks"]])
