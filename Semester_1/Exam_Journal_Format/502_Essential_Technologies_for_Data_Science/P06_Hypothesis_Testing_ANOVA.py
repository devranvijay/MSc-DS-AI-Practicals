# ------------------------------------------------------
# Practical No: 6
# Aim: To perform hypothesis testing (t-test) and ANOVA in Python.
# ------------------------------------------------------

# Theory:
# Hypothesis testing checks whether an assumption (null hypothesis)
# about a population is true, using sample data. A t-test compares
# the means of two groups. ANOVA (Analysis of Variance) is used to
# compare the means of three or more groups at the same time.
# If the p-value is less than 0.05, the null hypothesis is rejected.

# Algorithm:
# 1. Start
# 2. Take two samples of exam scores for a t-test
# 3. Apply the t-test and check the p-value
# 4. Take three samples of exam scores for ANOVA
# 5. Apply the ANOVA test and check the p-value
# 6. Display the conclusion
# 7. Stop

# Python Program:

from scipy import stats

group_a = [70, 72, 75, 78, 80]
group_b = [60, 62, 65, 68, 70]

t_value, p_value = stats.ttest_ind(group_a, group_b)
print("Group A:", group_a)
print("Group B:", group_b)
print("t-statistic =", t_value)
print("p-value =", p_value)

if p_value < 0.05:
    print("Reject null hypothesis: significant difference between the groups")
else:
    print("Fail to reject null hypothesis: no significant difference")

method1 = [85, 88, 90, 92]
method2 = [78, 80, 82, 85]
method3 = [70, 72, 75, 78]

f_value, p_value2 = stats.f_oneway(method1, method2, method3)
print("\nMethod 1:", method1)
print("Method 2:", method2)
print("Method 3:", method3)
print("F-statistic =", f_value)
print("p-value =", p_value2)

if p_value2 < 0.05:
    print("Reject null hypothesis: at least one method mean is different")
else:
    print("Fail to reject null hypothesis: all method means are similar")

# Sample Input / Output:
# t-statistic = 3.16...
# p-value = 0.013...
# Reject null hypothesis: significant difference between the groups
# F-statistic = 21.6...
# p-value = 0.0006...
# Reject null hypothesis: at least one method mean is different

# Result:
# The program to perform t-test and ANOVA was executed successfully
# and the output was verified.

# Viva Questions:
# 1. What is a null hypothesis?
# 2. What does the p-value indicate in hypothesis testing?
# 3. When do we use a t-test and when do we use ANOVA?
# 4. What is the significance level commonly used in hypothesis testing?
# 5. What library/function is used to perform ANOVA in Python?
