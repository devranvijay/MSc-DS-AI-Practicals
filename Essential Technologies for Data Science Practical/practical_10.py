# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import dataset
df = pd.read_csv("student_performance.csv")
# 1. Univariate Analysis (one variable)
plt.figure(figsize=(13, 4.4))
plt.subplot(1, 2, 1)
plt.hist(df["Marks"], bins=5, edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.subplot(1, 2, 2)
df["Department"].value_counts().plot(kind='bar', rot=0,
    color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Count of Students by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
# 2. Bivariate Analysis (two variables)
plt.figure(figsize=(13, 4.4))
plt.subplot(1, 2, 1)
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study_Hours")
plt.ylabel("Marks")
plt.subplot(1, 2, 2)
sns.boxplot(x="Department", y="Marks", data=df)
plt.title("Marks by Department")
plt.show()
# 3. Multivariate Analysis (more than two variables)
plt.figure(figsize=(13, 4.4))
plt.subplot(1, 2, 1)
sns.scatterplot(x="Study_Hours", y="Marks", hue="Department",
                size="Attendance", data=df)
plt.title("Study Hours vs Marks by Department and Attendance")
plt.subplot(1, 2, 2)
df.groupby(["Department", "Gender"])["Marks"].mean().unstack() \
    .plot(kind='bar', ax=plt.gca(), rot=0)
plt.title("Average Marks by Department and Gender")
plt.ylabel("Average Marks")
plt.show()
