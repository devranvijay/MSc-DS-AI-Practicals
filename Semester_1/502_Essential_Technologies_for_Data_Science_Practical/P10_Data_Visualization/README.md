# Practical 10 — Data Visualization (Univariate / Bivariate / Multivariate)

**Subject:** 502 – Essential Technologies for Data Science
**File:** `data_visualization.py`

## Aim
To create univariate, bivariate, and multivariate visualizations of a
student-performance dataset, choosing the chart type appropriate to
the number of variables being analyzed.

## Theory
- **Univariate visualization** (one variable): histogram, boxplot —
  shows the distribution/spread of a single variable.
- **Bivariate visualization** (two variables): scatter plot, line plot
  — shows the relationship between two variables.
- **Multivariate visualization** (3+ variables): scatter plot with
  color/size/shape encoding additional dimensions — here, branch is
  encoded as color and attendance % as marker size.

## How to Run
```bash
pip install pandas numpy matplotlib
python data_visualization.py
```
Plots are saved to the `outputs/` folder as three PNG files.

## Viva Questions & Answers
1. **Q: When would you use a boxplot instead of a histogram for univariate data?**
   A: A boxplot summarizes quartiles/outliers compactly and is better
   for comparing distributions across categories side-by-side; a
   histogram better shows the full shape of a single distribution.
2. **Q: What chart types are common for bivariate numeric-numeric analysis?**
   A: Scatter plots (for relationship/correlation) and line plots
   (for trends over an ordered variable like time).
3. **Q: How can you visualize 3 or more dimensions on a 2D scatter plot?**
   A: Encode extra variables using color, marker size, marker shape,
   or facets (small multiples/subplots).
4. **Q: Why use `alpha` (transparency) in scatter plots?**
   A: To reveal overlapping points ("overplotting") in dense regions
   of the data.
5. **Q: What visualization would you choose to compare a numeric variable
   across 3 categorical groups?**
   A: Side-by-side boxplots or violin plots, one per category.

## Real-World Relevance
Choosing the right visualization for the number/type of variables
involved is central to effective exploratory data analysis (EDA) and
communicating insights to non-technical stakeholders.
