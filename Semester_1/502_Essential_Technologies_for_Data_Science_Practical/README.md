# 502 — Essential Technologies for Data Science Practical

**Semester:** I | **University:** University of Mumbai (UoM) | **Practicals:** 10

This subject builds the Python and statistical foundations required
for data science: core language mechanics (operators, loops, data
structures) followed by the standard exploratory-data-analysis (EDA)
toolkit (univariate analysis, hypothesis testing, correlation,
data wrangling, aggregation, and visualization).

## Practicals in this Subject

| # | Practical | Core Libraries |
|---|-----------|-----------------|
| 1 | Arithmetic operations in Python | standard library |
| 2 | Relational & logical operators | standard library |
| 3 | For & while loops | standard library |
| 4 | Lists, Sets, Dictionary | standard library |
| 5 | Univariate analysis | pandas, numpy, matplotlib |
| 6 | Hypothesis testing & ANOVA | numpy, scipy |
| 7 | Correlation + Heatmap | pandas, numpy, matplotlib |
| 8 | Data wrangling (CSV/Excel) | pandas, numpy, openpyxl |
| 9 | Group By & Sorting | pandas, numpy |
| 10 | Data visualization (Uni/Bi/Multi) | pandas, numpy, matplotlib |

## Learning Progression

Practicals 1-4 establish Python fundamentals (syntax, control flow,
core data structures) — the building blocks every later script relies
on. Practicals 5-10 apply those fundamentals to the standard data
science workflow: understanding a single variable (5), testing
statistical hypotheses (6), understanding relationships between
variables (7), cleaning raw data (8), aggregating and ranking it (9),
and finally visualizing it at every level of complexity (10).

## How to Run Any Practical

```bash
cd P05_Univariate_Analysis
python univariate_analysis.py
```

Each script is fully self-contained — where a dataset is needed, it is
generated automatically on first run with a fixed random seed for
reproducibility, and any plots/exports are written to that practical's
own `outputs/` folder.

See the repository root `README.md` for the full index and setup
instructions, and each practical's own `README.md` for its aim,
theory, sample output, and viva questions.
