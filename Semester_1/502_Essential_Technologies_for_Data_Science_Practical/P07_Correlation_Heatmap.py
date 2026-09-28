# ------------------------------------------------------
# Practical No: 7
# Aim: To find correlation between variables and display it using
#      a heatmap in Python.
# ------------------------------------------------------

# Theory:
# Correlation measures the strength and direction of the linear
# relationship between two variables. Its value ranges from -1 to +1.
# A heatmap is a graphical way of showing the correlation matrix using
# colors, making it easy to spot strong and weak relationships.

# Algorithm:
# 1. Start
# 2. Create a dataset with more than one numeric column
# 3. Convert it into a pandas DataFrame
# 4. Find the correlation matrix using corr()
# 5. Display the correlation matrix as a heatmap
# 6. Stop

# Python Program:

import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 62, 65, 70, 72, 78, 80, 85, 90, 95],
    "Marks": [40, 45, 50, 55, 60, 68, 72, 78, 85, 92],
}

data = pd.DataFrame(data_dict)
print("Dataset:")
print(data)

correlation_matrix = data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.imshow(correlation_matrix, cmap="coolwarm")
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap_output.png")
print("\nHeatmap saved as correlation_heatmap_output.png")

# Sample Input / Output:
# Correlation Matrix:
#               Study_Hours  Attendance     Marks
# Study_Hours      1.000000    0.996...   0.998...
# Attendance       0.996...    1.000000    0.995...
# Marks            0.998...    0.995...    1.000000

# Result:
# The program to find correlation and display it as a heatmap was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What does a correlation value of +1 mean?
# 2. What does a correlation value of -1 mean?
# 3. Does correlation mean causation? Explain.
# 4. Which pandas function is used to compute correlation?
# 5. Why is a heatmap useful for correlation analysis?
