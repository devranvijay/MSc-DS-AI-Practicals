# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
# Import dataset
df = pd.read_csv("student_data.csv")
# Display first 5 records
print("First 5 Records:")
print(df.head())
# Display information about dataset
print("\nDataset Information:")
print(df.info())
# Select numeric columns
numeric_columns = df.select_dtypes(include='number').columns
print("\nNumeric Columns:")
print(numeric_columns)
# Univariate analysis
for column in numeric_columns:
    print("\n-----------------------------------")
    print("Analysis of:", column)
    print("-----------------------------------")
    # Descriptive statistics
    print(df[column].describe())
    # Mean, Median and Mode
    print("Mean   :", df[column].mean())
    print("Median :", df[column].median())
    print("Mode   :", df[column].mode()[0])
    # Histogram
    plt.figure(figsize=(6, 4))
    plt.hist(df[column], bins=10, edgecolor='black')
    plt.title("Histogram of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
    # Box plot
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[column].dropna())
    plt.title("Box Plot of " + column)
    plt.ylabel(column)
    plt.show()
