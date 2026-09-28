# Practical 05 — Univariate Analysis

**Subject:** 502 – Essential Technologies for Data Science
**File:** `univariate_analysis.py`

## Aim
To perform univariate statistical analysis on a numeric variable —
measures of central tendency, dispersion, and shape — and visualize
its distribution using a histogram and a boxplot.

## Theory
Univariate analysis studies **one variable at a time**.
- **Central tendency**: mean, median, mode — describe the "center" of
  the data.
- **Dispersion**: range, variance, standard deviation, IQR — describe
  how spread out the data is.
- **Shape**: skewness (asymmetry) and kurtosis (tailedness/peakedness)
  — describe the distribution's form relative to a normal curve.

## Dataset
The script auto-generates a reproducible synthetic dataset of 200
student marks (`data/student_scores.csv`) on first run using a fixed
random seed, so it works out-of-the-box without any external file.

## How to Run
```bash
pip install pandas numpy matplotlib
python univariate_analysis.py
```
Output plot is saved to `outputs/univariate_distribution.png`.

## Viva Questions & Answers
1. **Q: What is the difference between variance and standard deviation?**
   A: Variance is the average squared deviation from the mean;
   standard deviation is its square root, expressed in the same unit
   as the original data (making it easier to interpret).
2. **Q: What does positive skewness indicate?**
   A: The distribution has a longer tail on the right side (a few
   unusually high values pull the mean above the median).
3. **Q: Why is the median preferred over the mean for skewed data?**
   A: The median is robust to outliers/skew, whereas the mean is
   pulled toward extreme values.
4. **Q: What is the Interquartile Range (IQR) used for?**
   A: It measures the spread of the middle 50% of the data and is used
   to detect outliers (values beyond Q1 - 1.5*IQR or Q3 + 1.5*IQR).
5. **Q: What does kurtosis tell us?**
   A: It measures the "tailedness" of a distribution — high kurtosis
   means more extreme outliers than a normal distribution.

## Real-World Relevance
Univariate analysis is always the first step of exploratory data
analysis (EDA) — it flags data-quality issues (outliers, skew) before
any modeling begins.
