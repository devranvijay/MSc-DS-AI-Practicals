"""
Practical 06: Hypothesis Testing and ANOVA
Subject : 502 - Essential Technologies for Data Science
Aim     : To perform a one-sample t-test, a two-sample (independent)
          t-test, and a one-way ANOVA test, and interpret the
          resulting p-values against a chosen significance level.

Dependencies: numpy, scipy
Install with: pip install numpy scipy
"""

import numpy as np
from scipy import stats

SIGNIFICANCE_LEVEL = 0.05


def generate_sample_data(seed: int = 42) -> dict:
    """
    Generate reproducible synthetic exam-score samples for three
    teaching methods, used to demonstrate t-tests and ANOVA.
    """
    rng = np.random.default_rng(seed)
    return {
        "class_scores": rng.normal(loc=68, scale=8, size=40),
        "method_a": rng.normal(loc=70, scale=7, size=30),
        "method_b": rng.normal(loc=75, scale=7, size=30),
        "method_c": rng.normal(loc=65, scale=9, size=30),
    }


def one_sample_t_test(sample: np.ndarray, population_mean: float) -> None:
    """
    Test H0: sample mean == population_mean
         H1: sample mean != population_mean
    """
    print("\n--- ONE-SAMPLE T-TEST ---")
    print(f"H0: The class average equals {population_mean}")
    print(f"H1: The class average is different from {population_mean}")

    t_statistic, p_value = stats.ttest_1samp(sample, popmean=population_mean)
    print(f"Sample mean : {sample.mean():.2f}")
    print(f"t-statistic : {t_statistic:.4f}")
    print(f"p-value     : {p_value:.4f}")
    interpret_p_value(p_value)


def two_sample_t_test(sample_a: np.ndarray, sample_b: np.ndarray) -> None:
    """
    Test H0: mean(sample_a) == mean(sample_b)
         H1: mean(sample_a) != mean(sample_b)
    Uses Welch's t-test (does not assume equal variances).
    """
    print("\n--- TWO-SAMPLE (INDEPENDENT) T-TEST ---")
    print("H0: Method A and Method B produce the same average score")
    print("H1: Method A and Method B produce different average scores")

    t_statistic, p_value = stats.ttest_ind(sample_a, sample_b, equal_var=False)
    print(f"Mean (Method A) : {sample_a.mean():.2f}")
    print(f"Mean (Method B) : {sample_b.mean():.2f}")
    print(f"t-statistic     : {t_statistic:.4f}")
    print(f"p-value         : {p_value:.4f}")
    interpret_p_value(p_value)


def one_way_anova(*samples: np.ndarray, labels: list) -> None:
    """
    Test H0: all group means are equal
         H1: at least one group mean is different
    """
    print("\n--- ONE-WAY ANOVA ---")
    print(f"H0: The mean score is the same across {', '.join(labels)}")
    print("H1: At least one group has a different mean score")

    f_statistic, p_value = stats.f_oneway(*samples)
    for label, sample in zip(labels, samples):
        print(f"Mean ({label}) : {sample.mean():.2f}")
    print(f"F-statistic : {f_statistic:.4f}")
    print(f"p-value     : {p_value:.4f}")
    interpret_p_value(p_value)


def interpret_p_value(p_value: float) -> None:
    """Print a plain-English interpretation of a p-value against alpha = 0.05."""
    if p_value < SIGNIFICANCE_LEVEL:
        print(f"Conclusion  : p < {SIGNIFICANCE_LEVEL} -> Reject H0 "
              "(statistically significant difference).")
    else:
        print(f"Conclusion  : p >= {SIGNIFICANCE_LEVEL} -> Fail to reject H0 "
              "(no statistically significant difference).")


def main() -> None:
    """Entry point that drives the hypothesis testing and ANOVA demonstration."""
    print("=" * 60)
    print("PRACTICAL 06 : HYPOTHESIS TESTING AND ANOVA")
    print("=" * 60)

    data = generate_sample_data()

    one_sample_t_test(data["class_scores"], population_mean=65)
    two_sample_t_test(data["method_a"], data["method_b"])
    one_way_anova(
        data["method_a"], data["method_b"], data["method_c"],
        labels=["Method A", "Method B", "Method C"],
    )

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
