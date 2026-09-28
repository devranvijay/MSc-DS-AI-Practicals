"""
Practical 09: Group By and Sorting
Subject : 502 - Essential Technologies for Data Science
Aim     : To demonstrate pandas' groupby aggregation capabilities and
          multiple sorting techniques on a retail sales dataset.

Dependencies: pandas, numpy
Install with: pip install pandas numpy
"""

import os

import numpy as np
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "regional_sales.csv")


def generate_dataset_if_missing(path: str, seed: int = 42) -> None:
    """Create a reproducible synthetic regional-sales dataset if missing."""
    if os.path.exists(path):
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    rng = np.random.default_rng(seed)

    regions = ["North", "South", "East", "West"]
    products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

    records = []
    for _ in range(60):
        records.append({
            "region": rng.choice(regions),
            "product": rng.choice(products),
            "units_sold": int(rng.integers(1, 25)),
            "revenue": round(float(rng.uniform(500, 60000)), 2),
        })

    pd.DataFrame(records).to_csv(path, index=False)


def total_revenue_by_region(dataframe: pd.DataFrame) -> pd.Series:
    """Group by region and compute total revenue, sorted descending."""
    return dataframe.groupby("region")["revenue"].sum().sort_values(ascending=False)


def average_units_by_product(dataframe: pd.DataFrame) -> pd.Series:
    """Group by product and compute the average units sold."""
    return dataframe.groupby("product")["units_sold"].mean().sort_values(ascending=False)


def multi_level_aggregation(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Group by both region and product simultaneously, computing multiple
    aggregate statistics (sum, mean, count) in a single operation.
    """
    return dataframe.groupby(["region", "product"]).agg(
        total_revenue=("revenue", "sum"),
        average_units=("units_sold", "mean"),
        num_orders=("revenue", "count"),
    ).round(2)


def sort_multi_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Sort the dataset by region (ascending) then revenue (descending)."""
    return dataframe.sort_values(by=["region", "revenue"], ascending=[True, False])


def top_n_transactions(dataframe: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return the top-N highest revenue transactions using nlargest."""
    return dataframe.nlargest(n, "revenue")


def main() -> None:
    """Entry point that drives the groupby and sorting demonstration."""
    print("=" * 60)
    print("PRACTICAL 09 : GROUP BY AND SORTING")
    print("=" * 60)

    generate_dataset_if_missing(DATA_PATH)
    dataframe = pd.read_csv(DATA_PATH)
    print(f"\nDataset preview ({len(dataframe)} rows):\n{dataframe.head()}")

    print("\n--- Total revenue by region (sorted descending) ---")
    print(total_revenue_by_region(dataframe))

    print("\n--- Average units sold by product (sorted descending) ---")
    print(average_units_by_product(dataframe))

    print("\n--- Multi-level aggregation: region x product ---")
    print(multi_level_aggregation(dataframe))

    print("\n--- Sorted by region (asc), then revenue (desc) [first 10 rows] ---")
    print(sort_multi_column(dataframe).head(10))

    print("\n--- Top 5 highest-revenue transactions ---")
    print(top_n_transactions(dataframe))

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
