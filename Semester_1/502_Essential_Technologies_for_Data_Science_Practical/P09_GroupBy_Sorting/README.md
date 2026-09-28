# Practical 09 — Group By & Sorting

**Subject:** 502 – Essential Technologies for Data Science
**File:** `groupby_sorting.py`

## Aim
To demonstrate pandas' `groupby()` aggregation (single and multi-level)
and multiple sorting techniques (`sort_values`, `nlargest`) on a
regional sales dataset.

## Theory
`groupby()` implements the **split-apply-combine** pattern: the data
is split into groups based on one or more keys, an aggregation
function is applied to each group independently, and the results are
combined into a single output. Sorting (`sort_values`) reorders rows
by one or more columns, while `nlargest`/`nsmallest` efficiently
extract the top/bottom-N rows without a full sort.

## How to Run
```bash
pip install pandas numpy
python groupby_sorting.py
```

## Viva Questions & Answers
1. **Q: What does "split-apply-combine" mean in the context of groupby?**
   A: Split: partition data by group keys. Apply: run an aggregation
   (sum, mean, count, etc.) on each group. Combine: merge results back
   into one DataFrame/Series.
2. **Q: How do you group by more than one column?**
   A: Pass a list: `dataframe.groupby(["region", "product"])`.
3. **Q: What is the difference between `.agg()` with a dict vs named
   aggregation (`agg(new_col=("col", "func"))`)?**
   A: Named aggregation lets you rename the output columns directly
   during aggregation, avoiding a separate `rename()` step.
4. **Q: How is `nlargest(n, column)` different from sorting and slicing?**
   A: `nlargest` uses a partial-sort algorithm and is more efficient
   for large datasets than a full `sort_values().head(n)`.
5. **Q: How do you sort by multiple columns with different sort orders?**
   A: `dataframe.sort_values(by=[col1, col2], ascending=[True, False])`.

## Real-World Relevance
`groupby` and sorting are used constantly in business reporting — e.g.
computing "total revenue by region" or "top 5 best-selling products"
from raw transaction logs.
