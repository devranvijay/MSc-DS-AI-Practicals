# Practical 08 — Data Wrangling (CSV / Excel)

**Subject:** 502 – Essential Technologies for Data Science
**File:** `data_wrangling.py`

## Aim
To clean a deliberately messy raw dataset — handling missing values,
duplicate rows, inconsistent text formatting, and incorrect data
types — then export the cleaned result to both CSV and Excel.

## Theory
Data wrangling (data cleaning/munging) transforms raw, messy data into
an analysis-ready format. Typical steps include: standardizing text
casing/whitespace, imputing or dropping missing values, removing
duplicate records, correcting data types (strings to numbers/dates),
and deriving new columns. Real-world data is rarely clean, so this
step consumes a large share of any practical data-science workflow.

## How to Run
```bash
pip install pandas numpy openpyxl
python data_wrangling.py
```
Cleaned files are written to `outputs/cleaned_sales_data.csv` and
`outputs/cleaned_sales_data.xlsx`.

## Viva Questions & Answers
1. **Q: What is the difference between dropping and imputing missing values?**
   A: Dropping removes rows/columns with missing data (safe when
   missingness is rare); imputing fills gaps with a statistic (mean,
   median, mode) or model-based estimate, preserving sample size.
2. **Q: Why use median instead of mean to fill missing `quantity` values?**
   A: The median is robust to outliers/skew, so it doesn't get
   distorted by a few unusually large order quantities.
3. **Q: How do you detect and remove duplicate rows in pandas?**
   A: `dataframe.duplicated()` flags duplicates; `dataframe.drop_duplicates()`
   removes them, optionally restricted to specific columns via `subset=`.
4. **Q: Why is standardizing text casing important before analysis?**
   A: Because `"Laptop"`, `"laptop"`, and `"LAPTOP "` would otherwise
   be treated as three different categories during grouping/counting.
5. **Q: What library is required for pandas to write `.xlsx` files?**
   A: `openpyxl` (for `.xlsx`) — pandas delegates Excel I/O to it.

## Real-World Relevance
Data wrangling is the single most time-consuming stage of any
real-world data-science project — clean input data is a prerequisite
for trustworthy analysis and modeling.
