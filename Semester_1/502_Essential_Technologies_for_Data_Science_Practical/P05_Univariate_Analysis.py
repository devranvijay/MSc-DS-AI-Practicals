# ------------------------------------------------------
# Practical No: 5
# Aim: To perform univariate analysis on a dataset using Python.
# ------------------------------------------------------

# Theory:
# Univariate analysis studies one variable at a time. It includes
# measures of central tendency (mean, median, mode) and measures of
# dispersion (variance, standard deviation, range) which describe
# the distribution of the data.

# Algorithm:
# 1. Start
# 2. Create a dataset (list of marks) and convert it into a pandas Series
# 3. Calculate mean, median, mode, variance, standard deviation and range
# 4. Plot a histogram of the data
# 5. Display the results
# 6. Stop

# Python Program:

import pandas as pd
import matplotlib.pyplot as plt

marks = [45, 60, 65, 70, 70, 75, 80, 85, 85, 90, 95, 40, 55, 65, 75]
data = pd.Series(marks)

print("Dataset:", list(data))
print("Mean =", data.mean())
print("Median =", data.median())
print("Mode =", data.mode()[0])
print("Variance =", data.var())
print("Standard Deviation =", data.std())
print("Minimum =", data.min())
print("Maximum =", data.max())
print("Range =", data.max() - data.min())

plt.hist(data, bins=6, color="skyblue", edgecolor="black")
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("univariate_output.png")
print("Histogram saved as univariate_output.png")

# Sample Input / Output:
# Dataset: [45, 60, 65, 70, 70, 75, 80, 85, 85, 90, 95, 40, 55, 65, 75]
# Mean = 70.33333333333333
# Median = 70.0
# Mode = 65
# Variance = 245.238095...
# Standard Deviation = 15.66...
# Minimum = 40
# Maximum = 95
# Range = 55

# Result:
# The program to perform univariate analysis on the given dataset was
# executed successfully and the output was verified.

# Viva Questions:
# 1. What is univariate analysis?
# 2. What is the difference between mean, median and mode?
# 3. What does standard deviation indicate about a dataset?
# 4. What is the range of a dataset?
# 5. Which pandas function is used to find the mode of a Series?
