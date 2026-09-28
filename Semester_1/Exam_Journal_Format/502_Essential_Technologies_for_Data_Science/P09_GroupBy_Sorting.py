# ------------------------------------------------------
# Practical No: 9
# Aim: To perform Group By and sorting operations using pandas.
# ------------------------------------------------------

# Theory:
# The groupby() function is used to split data into groups based on
# some criteria, and then apply a function like sum or mean to each
# group. The sort_values() function is used to arrange data in
# ascending or descending order based on one or more columns.

# Algorithm:
# 1. Start
# 2. Create a dataset containing region, product and sales columns
# 3. Group the data by region and find the total sales
# 4. Sort the original data by sales in descending order
# 5. Display the results
# 6. Stop

# Python Program:

import pandas as pd

sales_dict = {
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Product": ["Pen", "Pen", "Book", "Pen", "Book", "Book"],
    "Sales": [200, 150, 300, 250, 400, 100],
}

data = pd.DataFrame(sales_dict)
print("Dataset:")
print(data)

grouped_data = data.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:")
print(grouped_data)

sorted_data = data.sort_values(by="Sales", ascending=False)
print("\nData sorted by Sales (descending):")
print(sorted_data)

# Sample Input / Output:
# Total Sales by Region:
# Region
# East     350
# North    500
# South    550
# Data sorted by Sales (descending):
#    Region Product  Sales
# 4   South    Book    400
# 2   North    Book    300

# Result:
# The program to perform Group By and sorting operations was executed
# successfully and the output was verified.

# Viva Questions:
# 1. What is the purpose of the groupby() function?
# 2. How do you sort a DataFrame in descending order?
# 3. Can you group data by more than one column? How?
# 4. What is the split-apply-combine strategy?
# 5. Which function is used to sort values in pandas?
