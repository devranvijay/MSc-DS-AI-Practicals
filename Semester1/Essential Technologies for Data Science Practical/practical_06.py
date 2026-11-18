# Import required libraries
import pandas as pd
from scipy import stats
# Import dataset
df = pd.read_csv("student_performance.csv")
print("First 5 Records:")
print(df.head())
alpha = 0.05
# 1. One Sample t-test
# H0: Mean marks of students = 70
# H1: Mean marks of students != 70
print("\n----- One Sample t-test -----")
t_stat, p_value = stats.ttest_1samp(df["Marks"], 70)
print("Sample Mean :", round(df["Marks"].mean(), 2))
print("t-statistic :", round(t_stat, 4))
print("p-value     :", round(p_value, 4))
if p_value < alpha:
    print("Result: Reject H0 - Mean marks differ from 70")
else:
    print("Result: Fail to reject H0 - Mean marks are equal to 70")
# 2. Independent Two Sample t-test
# H0: Mean marks of Male = Mean marks of Female
# H1: Mean marks of Male != Mean marks of Female
print("\n----- Independent Two Sample t-test -----")
male = df[df["Gender"] == "Male"]["Marks"]
female = df[df["Gender"] == "Female"]["Marks"]
print("Mean Marks (Male)   :", round(male.mean(), 2))
print("Mean Marks (Female) :", round(female.mean(), 2))
t_stat, p_value = stats.ttest_ind(male, female)
print("t-statistic :", round(t_stat, 4))
print("p-value     :", round(p_value, 4))
if p_value < alpha:
    print("Result: Reject H0 - Significant difference between Male and Female")
else:
    print("Result: Fail to reject H0 - No significant difference "
          "between Male and Female")
# 3. One-Way ANOVA
# H0: Mean marks of all departments are equal
# H1: At least one department mean is different
print("\n----- One-Way ANOVA -----")
print(df.groupby("Department")["Marks"].mean().round(2))
science = df[df["Department"] == "Science"]["Marks"]
commerce = df[df["Department"] == "Commerce"]["Marks"]
arts = df[df["Department"] == "Arts"]["Marks"]
f_stat, p_value = stats.f_oneway(science, commerce, arts)
print("F-statistic :", round(f_stat, 4))
print("p-value     :", round(p_value, 4))
if p_value < alpha:
    print("Result: Reject H0 - At least one department mean is different")
else:
    print("Result: Fail to reject H0 - All department means are equal")
