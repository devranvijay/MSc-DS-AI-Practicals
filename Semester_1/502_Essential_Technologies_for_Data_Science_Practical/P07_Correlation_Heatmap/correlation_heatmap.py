"""
Practical 07: Correlation Analysis and Heatmap Visualization
Subject : 502 - Essential Technologies for Data Science
Aim     : To compute the Pearson correlation coefficient between
          numeric variables in a dataset and visualize the correlation
          matrix as a heatmap.

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
    """
    Generate a reproducible synthetic dataset of student attributes with
    a deliberately built-in correlation structure:
    study_hours -> influences attendance_pct and final_score.
    """
    rng = np.random.default_rng(seed)

    study_hours = rng.uniform(1, 10, num_records)
    attendance_pct = np.clip(60 + study_hours * 3 + rng.normal(0, 5, num_records), 40, 100)
    sleep_hours = np.clip(9 - 0.3 * study_hours + rng.normal(0, 1, num_records), 3, 10)
    final_score = np.clip(
        30 + study_hours * 5 + attendance_pct * 0.2 + rng.normal(0, 6, num_records), 0, 100
    )

    return pd.DataFrame({
        "study_hours": study_hours.round(1),
        "attendance_pct": attendance_pct.round(1),
        "sleep_hours": sleep_hours.round(1),
        "final_score": final_score.round(1),
    })


def compute_correlation_matrix(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Compute the Pearson correlation matrix for all numeric columns."""
    return dataframe.corr(method="pearson")


def describe_strongest_relationships(correlation_matrix: pd.DataFrame) -> None:
    """Print the strongest positive and negative correlations (excluding self-correlation)."""
    correlations = correlation_matrix.where(
        ~np.eye(len(correlation_matrix), dtype=bool)
    ).stack()

    strongest_positive = correlations.idxmax()
    strongest_negative = correlations.idxmin()

    print(f"\nStrongest positive correlation : {strongest_positive} "
          f"= {correlations[strongest_positive]:.3f}")
    print(f"Strongest negative correlation : {strongest_negative} "
          f"= {correlations[strongest_negative]:.3f}")


def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, output_dir: str) -> str:
    """Save the correlation matrix as an annotated heatmap image."""
    os.makedirs(output_dir, exist_ok=True)

    figure, axis = plt.subplots(figsize=(6.5, 5.5))
    heatmap_image = axis.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)

    axis.set_xticks(range(len(correlation_matrix.columns)))
    axis.set_yticks(range(len(correlation_matrix.columns)))
    axis.set_xticklabels(correlation_matrix.columns, rotation=45, ha="right")
    axis.set_yticklabels(correlation_matrix.columns)

    for row in range(len(correlation_matrix)):
        for col in range(len(correlation_matrix)):
            axis.text(col, row, f"{correlation_matrix.iloc[row, col]:.2f}",
                       ha="center", va="center", color="black", fontsize=9)

    axis.set_title("Correlation Heatmap")
    figure.colorbar(heatmap_image, ax=axis, label="Pearson correlation coefficient")
    figure.tight_layout()

    output_path = os.path.join(output_dir, "correlation_heatmap.png")
    figure.savefig(output_path, dpi=120)
    plt.close(figure)
    return output_path


def main() -> None:
    """Entry point that drives the correlation and heatmap demonstration."""
    print("=" * 60)
    print("PRACTICAL 07 : CORRELATION ANALYSIS AND HEATMAP")
    print("=" * 60)

    dataframe = generate_dataset()
    print(f"\nDataset preview:\n{dataframe.head()}")

    correlation_matrix = compute_correlation_matrix(dataframe)
    print(f"\nCorrelation matrix:\n{correlation_matrix.round(3)}")

    describe_strongest_relationships(correlation_matrix)

    saved_path = plot_correlation_heatmap(correlation_matrix, OUTPUT_DIR)
    print(f"\nHeatmap saved to: {saved_path}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
