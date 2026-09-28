# ------------------------------------------------------
# Practical No: 8
# Aim: To perform data wrangling operations (CSV/Excel) using pandas.
# ------------------------------------------------------

# Theory:
# Data wrangling is the process of cleaning and transforming raw data
# into a usable format. It includes handling missing values, removing
# duplicate rows, and converting data into the required type before
# analysis.

# Algorithm:
# 1. Start
# 2. Create a raw dataset with missing values and duplicate rows
# 3. Save it as a CSV file and read it back using pandas
# 4. Handle missing values using fillna()
# 5. Remove duplicate rows using drop_duplicates()
# 6. Save the cleaned data to a new CSV file and an Excel file
# 7. Stop

# Python Program:

import pandas as pd
import numpy as np

raw_dict = {
    "Name": ["Ravi", "Sneha", "Aman", "Aman", "Pooja"],
    "Marks": [85, np.nan, 78, 78, np.nan],
}

raw_data = pd.DataFrame(raw_dict)
raw_data.to_csv("raw_data.csv", index=False)

data = pd.read_csv("raw_data.csv")
print("Raw Data:")
print(data)
print("\nMissing values in each column:")
print(data.isnull().sum())

data["Marks"] = data["Marks"].fillna(data["Marks"].mean())
print("\nData after filling missing values:")
print(data)

data = data.drop_duplicates()
print("\nData after removing duplicates:")
print(data)

data.to_csv("cleaned_data.csv", index=False)
data.to_excel("cleaned_data.xlsx", index=False)
print("\nCleaned data saved as cleaned_data.csv and cleaned_data.xlsx")

# Sample Input / Output:
# Raw Data:
#     Name  Marks
# 0   Ravi   85.0
# 1  Sneha    NaN
# 2   Aman   78.0
# 3   Aman   78.0
# 4  Pooja    NaN
# Missing values in each column:
# Name     0
# Marks    2
# Data after removing duplicates:
#     Name  Marks
# 0   Ravi   85.0
# 1  Sneha   80.33
# 2   Aman   78.0
# 4  Pooja   80.33

# Result:
# The program to perform data wrangling on a dataset was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What is data wrangling?
# 2. Which function is used to check missing values in a DataFrame?
# 3. How can missing values be filled in pandas?
# 4. Which function removes duplicate rows in pandas?
# 5. Name two file formats pandas can read and write.
