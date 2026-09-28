# Practical 07 — Correlation + Heatmap

**Subject:** 502 – Essential Technologies for Data Science
**File:** `correlation_heatmap.py`

## Aim
To compute the Pearson correlation coefficient between numeric
variables and visualize the correlation matrix as an annotated heatmap.

## Theory
The **Pearson correlation coefficient (r)** measures the strength and
direction of the *linear* relationship between two continuous
variables, ranging from -1 (perfect negative) to +1 (perfect
positive), with 0 meaning no linear relationship. A correlation matrix
arranges pairwise `r` values for every combination of variables in a
dataset, and a heatmap uses color intensity to make patterns easy to
spot at a glance.

## How to Run
```bash
pip install pandas numpy matplotlib
python correlation_heatmap.py
```
Output heatmap is saved to `outputs/correlation_heatmap.png`.

## Viva Questions & Answers
1. **Q: Does correlation imply causation?**
   A: No. A strong correlation only shows association, not that one
   variable causes the other — a confounding variable may be responsible.
2. **Q: What does a correlation of -0.8 mean?**
   A: A strong negative linear relationship — as one variable
   increases, the other tends to decrease significantly.
3. **Q: What is a limitation of Pearson correlation?**
   A: It only captures *linear* relationships; a strong non-linear
   relationship (e.g. U-shaped) can show a near-zero Pearson correlation.
4. **Q: How would you handle multicollinearity detected via a heatmap?**
   A: Drop or combine one of the highly correlated features, or apply
   dimensionality reduction (e.g. PCA), since multicollinearity can
   destabilize linear models.
5. **Q: What's the difference between Pearson and Spearman correlation?**
   A: Pearson measures linear relationships on raw values; Spearman
   measures monotonic relationships using ranked data, making it more
   robust to outliers and non-linearity.

## Real-World Relevance
Correlation heatmaps are a standard first step in feature selection
and exploratory data analysis (EDA), helping identify redundant
features before model building.
