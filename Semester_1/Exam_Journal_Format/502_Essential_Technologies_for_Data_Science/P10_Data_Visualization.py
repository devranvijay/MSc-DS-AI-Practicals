# ------------------------------------------------------
# Practical No: 10
# Aim: To perform univariate, bivariate and multivariate data
#      visualization using Python.
# ------------------------------------------------------

# Theory:
# Univariate visualization shows the distribution of a single
# variable (example: histogram). Bivariate visualization shows the
# relationship between two variables (example: scatter plot).
# Multivariate visualization shows the relationship between three or
# more variables at once, often using color or size as an extra
# dimension.

# Algorithm:
# 1. Start
# 2. Create a dataset with study hours, attendance and marks
# 3. Draw a histogram for univariate analysis of marks
# 4. Draw a scatter plot for bivariate analysis of study hours vs marks
# 5. Draw a multivariate scatter plot using color for a third variable
# 6. Stop

# Python Program:

import matplotlib.pyplot as plt

data_dict = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 62, 65, 70, 72, 78, 80, 85, 90, 95],
    "Marks": [40, 45, 50, 55, 60, 68, 72, 78, 85, 92],
}

plt.figure()
plt.hist(data_dict["Marks"], bins=5, color="orange", edgecolor="black")
plt.title("Univariate: Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("univariate_plot.png")

plt.figure()
plt.scatter(data_dict["Study_Hours"], data_dict["Marks"], color="blue")
plt.title("Bivariate: Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("bivariate_plot.png")

plt.figure()
plt.scatter(data_dict["Study_Hours"], data_dict["Marks"], c=data_dict["Attendance"], cmap="viridis")
plt.title("Multivariate: Study Hours vs Marks (color = Attendance)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.colorbar(label="Attendance")
plt.savefig("multivariate_plot.png")

print("All three plots (univariate, bivariate, multivariate) saved successfully.")

# Sample Input / Output:
# All three plots (univariate, bivariate, multivariate) saved successfully.
# (Three PNG image files are created showing the respective plots.)

# Result:
# The program to perform univariate, bivariate and multivariate
# visualization was executed successfully and the output was verified.

# Viva Questions:
# 1. What is the difference between univariate and bivariate analysis?
# 2. Which type of plot is best suited for showing a single variable's
#    distribution?
# 3. Which plot is used to show the relationship between two variables?
# 4. How can a third variable be represented in a 2D scatter plot?
# 5. Name the Python library used for plotting in this program.
