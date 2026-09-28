"""
Practical 05: Univariate Analysis
Subject : 502 - Essential Technologies for Data Science
Aim     : To perform univariate (single-variable) statistical analysis
          on a dataset - computing measures of central tendency,
          dispersion, and shape, and visualizing the distribution.

Dependencies: pandas, numpy, matplotlib
Install with: pip install pandas numpy matplotlib
"""

import os

import matplotlib
matplotlib.use("Agg")  # Allows the script to run on machines with no display.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "student_scores.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def generate_dataset_if_missing(path: str, num_records: int = 200) -> None:
    """
    Create a small, reproducible synthetic 'student marks' dataset if it
    does not already exist on disk, so the script can run independently.
    """
    if os.path.exists(path):
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    rng = np.random.default_rng(seed=42)

    marks = rng.normal(loc=65, scale=12, size=num_records)
    marks = np.clip(marks, 0, 100).round(2)

    dataframe = pd.DataFrame({
        "student_id": range(1, num_records + 1),
        "marks": marks,
    })
    dataframe.to_csv(path, index=False)


def compute_central_tendency(series: pd.Series) -> dict:
    """Compute mean, median, and mode of a numeric pandas Series."""
    return {
        "Mean": series.mean(),
        "Median": series.median(),
        "Mode": series.mode().iloc[0],
    }


def compute_dispersion(series: pd.Series) -> dict:
    """Compute range, variance, standard deviation, and IQR of a Series."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    return {
        "Range": series.max() - series.min(),
        "Variance": series.var(),
        "Standard Deviation": series.std(),
        "25th Percentile (Q1)": q1,
        "75th Percentile (Q3)": q3,
        "Interquartile Range (IQR)": q3 - q1,
    }


def compute_shape_statistics(series: pd.Series) -> dict:
    """Compute skewness and kurtosis to describe the shape of the distribution."""
    return {
        "Skewness": series.skew(),
        "Kurtosis": series.kurtosis(),
    }


def plot_distribution(series: pd.Series, output_dir: str) -> str:
    """Save a histogram-with-KDE-style plot and a boxplot for the given Series."""
    os.makedirs(output_dir, exist_ok=True)
    figure, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    axes[0].hist(series, bins=15, color="#4C72B0", edgecolor="white")
    axes[0].set_title("Histogram of Marks")
    axes[0].set_xlabel("Marks")
    axes[0].set_ylabel("Frequency")

    axes[1].boxplot(series, vert=True, patch_artist=True,
                     boxprops=dict(facecolor="#DD8452"))
    axes[1].set_title("Boxplot of Marks")
    axes[1].set_ylabel("Marks")

    figure.suptitle("Univariate Analysis: Distribution of Student Marks")
    figure.tight_layout()

    output_path = os.path.join(output_dir, "univariate_distribution.png")
    figure.savefig(output_path, dpi=120)
    plt.close(figure)
    return output_path


def print_section(title: str, statistics: dict) -> None:
    """Pretty-print a dictionary of statistics under a section heading."""
    print(f"\n{title}")
    print("-" * len(title))
    for label, value in statistics.items():
        if isinstance(value, float):
            print(f"{label:<28}: {value:.3f}")
        else:
            print(f"{label:<28}: {value}")


def main() -> None:
    """Entry point that drives the univariate analysis demonstration."""
    print("=" * 60)
    print("PRACTICAL 05 : UNIVARIATE ANALYSIS")
    print("=" * 60)

    generate_dataset_if_missing(DATA_PATH)
    dataframe = pd.read_csv(DATA_PATH)
    marks = dataframe["marks"]

    print(f"\nDataset loaded from: {DATA_PATH}")
    print(f"Number of records  : {len(dataframe)}")
    print(f"\nFirst 5 records:\n{dataframe.head()}")

    print_section("Measures of Central Tendency", compute_central_tendency(marks))
    print_section("Measures of Dispersion", compute_dispersion(marks))
    print_section("Measures of Shape", compute_shape_statistics(marks))

    saved_path = plot_distribution(marks, OUTPUT_DIR)
    print(f"\nDistribution plot saved to: {saved_path}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
