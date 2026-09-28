"""
Practical 10: Data Visualization (Univariate, Bivariate, Multivariate)
Subject : 502 - Essential Technologies for Data Science
Aim     : To create univariate, bivariate, and multivariate
          visualizations of a dataset using matplotlib, choosing the
          appropriate chart type for each type of analysis.

Dependencies: pandas, numpy, matplotlib
Install with: pip install pandas numpy matplotlib
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def generate_dataset(seed: int = 42, num_records: int = 150) -> pd.DataFrame:
    """Generate a reproducible synthetic student-performance dataset."""
    rng = np.random.default_rng(seed)

    study_hours = rng.uniform(1, 10, num_records).round(1)
    branch = rng.choice(["Data Science", "AI", "Statistics"], size=num_records)
    attendance_pct = np.clip(60 + study_hours * 3 + rng.normal(0, 5, num_records), 40, 100).round(1)
    final_score = np.clip(
        30 + study_hours * 5 + attendance_pct * 0.2 + rng.normal(0, 6, num_records), 0, 100
    ).round(1)

    return pd.DataFrame({
        "branch": branch,
        "study_hours": study_hours,
        "attendance_pct": attendance_pct,
        "final_score": final_score,
    })


def univariate_visualization(dataframe: pd.DataFrame, output_dir: str) -> str:
    """Create a univariate plot: histogram of final_score."""
    figure, axis = plt.subplots(figsize=(6, 4.5))
    axis.hist(dataframe["final_score"], bins=15, color="#4C72B0", edgecolor="white")
    axis.set_title("Univariate: Distribution of Final Score")
    axis.set_xlabel("Final Score")
    axis.set_ylabel("Frequency")
    figure.tight_layout()

    path = os.path.join(output_dir, "01_univariate_histogram.png")
    figure.savefig(path, dpi=120)
    plt.close(figure)
    return path


def bivariate_visualization(dataframe: pd.DataFrame, output_dir: str) -> str:
    """Create a bivariate plot: scatter plot of study_hours vs final_score."""
    figure, axis = plt.subplots(figsize=(6, 4.5))
    axis.scatter(dataframe["study_hours"], dataframe["final_score"],
                 color="#DD8452", alpha=0.7, edgecolor="black", linewidth=0.3)
    axis.set_title("Bivariate: Study Hours vs Final Score")
    axis.set_xlabel("Study Hours")
    axis.set_ylabel("Final Score")
    figure.tight_layout()

    path = os.path.join(output_dir, "02_bivariate_scatter.png")
    figure.savefig(path, dpi=120)
    plt.close(figure)
    return path


def multivariate_visualization(dataframe: pd.DataFrame, output_dir: str) -> str:
    """
    Create a multivariate plot: scatter of study_hours vs final_score,
    color-coded by branch and sized by attendance_pct.
    """
    figure, axis = plt.subplots(figsize=(7, 5))
    branches = dataframe["branch"].unique()
    colors = plt.cm.viridis(np.linspace(0, 0.85, len(branches)))

    for branch_name, color in zip(branches, colors):
        subset = dataframe[dataframe["branch"] == branch_name]
        axis.scatter(
            subset["study_hours"], subset["final_score"],
            s=subset["attendance_pct"], color=color, alpha=0.7,
            edgecolor="black", linewidth=0.3, label=branch_name,
        )

    axis.set_title("Multivariate: Study Hours vs Score\n(color = branch, size = attendance %)")
    axis.set_xlabel("Study Hours")
    axis.set_ylabel("Final Score")
    axis.legend(title="Branch")
    figure.tight_layout()

    path = os.path.join(output_dir, "03_multivariate_scatter.png")
    figure.savefig(path, dpi=120)
    plt.close(figure)
    return path


def main() -> None:
    """Entry point that drives the visualization demonstration."""
    print("=" * 60)
    print("PRACTICAL 10 : DATA VISUALIZATION (UNI / BI / MULTIVARIATE)")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dataframe = generate_dataset()
    print(f"\nDataset preview:\n{dataframe.head()}")

    uni_path = univariate_visualization(dataframe, OUTPUT_DIR)
    bi_path = bivariate_visualization(dataframe, OUTPUT_DIR)
    multi_path = multivariate_visualization(dataframe, OUTPUT_DIR)

    print(f"\nUnivariate plot saved to   : {uni_path}")
    print(f"Bivariate plot saved to    : {bi_path}")
    print(f"Multivariate plot saved to : {multi_path}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
