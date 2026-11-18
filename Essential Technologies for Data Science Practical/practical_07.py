# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import dataset
df = pd.read_csv("student_performance.csv")
# Select numeric columns
numeric_df = df.select_dtypes(include='number')
print("Numeric Columns:")
print(numeric_df.columns.tolist())
# Pearson correlation matrix
corr_matrix = numeric_df.corr(method='pearson')
print("\nCorrelation Matrix:")
print(corr_matrix.round(2))
# Correlation of each column with Marks
print("\nCorrelation with Marks:")
print(corr_matrix["Marks"].sort_values(ascending=False).round(2))
# Heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
