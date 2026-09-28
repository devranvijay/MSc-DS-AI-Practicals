"""
Practical 08: Data Wrangling (CSV / Excel)
Subject : 502 - Essential Technologies for Data Science
Aim     : To perform data wrangling on a raw, messy dataset - handling
          missing values, duplicate rows, inconsistent formatting, and
          incorrect data types - and export the cleaned result to both
          CSV and Excel formats.

Dependencies: pandas, numpy, openpyxl (for Excel export)
Install with: pip install pandas numpy openpyxl
"""

import os

import numpy as np
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RAW_CSV_PATH = os.path.join(DATA_DIR, "raw_sales_data.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def generate_messy_dataset_if_missing(path: str) -> None:
    """Create a deliberately messy synthetic sales dataset for wrangling practice."""
    if os.path.exists(path):
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    raw_records = pd.DataFrame({
        "order_id": [101, 102, 103, 104, 104, 105, 106, 107, 108, 109],
        "product": [" Laptop", "mouse", "Keyboard ", "Monitor", "Monitor",
                    "laptop", None, "Webcam", "Mouse ", "MONITOR"],
        "quantity": [1, 2, 1, np.nan, np.nan, 1, 3, 2, np.nan, 1],
        "unit_price": [55000, 450, 900, 12000, 12000, 54500, 300, 1500, 460, 12500],
        "order_date": ["2026-01-05", "2026-01-06", "2026-01-06", "2026-01-07",
                       "2026-01-07", "2026-01-08", "2026-01-08", "2026-01-09",
                       "2026-01-10", "2026-01-10"],
    })
    raw_records.to_csv(path, index=False)


def load_raw_data(path: str) -> pd.DataFrame:
    """Load the raw CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def clean_text_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Strip whitespace and normalize casing (title case) in the given text columns."""
    cleaned = dataframe.copy()
    for column in columns:
        cleaned[column] = cleaned[column].astype(str).str.strip().str.title()
        cleaned[column] = cleaned[column].replace("Nan", np.nan)
    return cleaned


def handle_missing_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values with column-appropriate strategies:
    - 'quantity': fill with the column median (numeric, likely to have outliers).
    - 'product'  : drop rows where the product name itself is missing.
    """
    cleaned = dataframe.copy()
    median_quantity = cleaned["quantity"].median()
    cleaned["quantity"] = cleaned["quantity"].fillna(median_quantity)
    cleaned = cleaned.dropna(subset=["product"])
    return cleaned


def remove_duplicate_rows(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Remove fully duplicated rows based on order_id, keeping the first occurrence."""
    return dataframe.drop_duplicates(subset=["order_id"], keep="first")


def fix_data_types(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Convert columns to their correct data types (int, float, datetime)."""
    cleaned = dataframe.copy()
    cleaned["quantity"] = cleaned["quantity"].astype(int)
    cleaned["unit_price"] = cleaned["unit_price"].astype(float)
    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"])
    return cleaned


def add_derived_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Add a 'total_amount' column computed from quantity and unit_price."""
    cleaned = dataframe.copy()
    cleaned["total_amount"] = cleaned["quantity"] * cleaned["unit_price"]
    return cleaned


def export_cleaned_data(dataframe: pd.DataFrame, output_dir: str) -> tuple:
    """Export the cleaned DataFrame to both CSV and Excel formats."""
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "cleaned_sales_data.csv")
    excel_path = os.path.join(output_dir, "cleaned_sales_data.xlsx")

    dataframe.to_csv(csv_path, index=False)
    try:
        dataframe.to_excel(excel_path, index=False, sheet_name="CleanedSales")
    except ImportError:
        excel_path = "(skipped - install 'openpyxl' to enable Excel export)"

    return csv_path, excel_path


def main() -> None:
    """Entry point that drives the data-wrangling pipeline."""
    print("=" * 60)
    print("PRACTICAL 08 : DATA WRANGLING (CSV / EXCEL)")
    print("=" * 60)

    generate_messy_dataset_if_missing(RAW_CSV_PATH)
    raw_dataframe = load_raw_data(RAW_CSV_PATH)

    print(f"\nRaw dataset ({len(raw_dataframe)} rows):\n{raw_dataframe}")
    print(f"\nMissing values per column:\n{raw_dataframe.isnull().sum()}")

    dataframe = clean_text_columns(raw_dataframe, columns=["product"])
    dataframe = handle_missing_values(dataframe)
    dataframe = remove_duplicate_rows(dataframe)
    dataframe = fix_data_types(dataframe)
    dataframe = add_derived_column(dataframe)

    print(f"\nCleaned dataset ({len(dataframe)} rows):\n{dataframe}")
    print(f"\nData types after cleaning:\n{dataframe.dtypes}")

    csv_path, excel_path = export_cleaned_data(dataframe, OUTPUT_DIR)
    print(f"\nCleaned CSV exported to  : {csv_path}")
    print(f"Cleaned Excel exported to: {excel_path}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
