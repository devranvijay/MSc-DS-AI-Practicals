# Practical 06 — Hypothesis Testing & ANOVA

**Subject:** 502 – Essential Technologies for Data Science
**File:** `hypothesis_testing_anova.py`

## Aim
To perform a one-sample t-test, an independent two-sample t-test, and
a one-way ANOVA, and interpret the resulting p-values.

## Theory
Hypothesis testing evaluates whether an observed effect in a sample is
likely to reflect a real effect in the population, or whether it could
plausibly be due to random chance.
- **Null hypothesis (H0)**: assumes no effect / no difference.
- **Alternative hypothesis (H1)**: assumes an effect / a difference exists.
- **p-value**: the probability of observing data this extreme if H0
  were true. If `p < 0.05` (the chosen significance level, α), H0 is
  rejected.
- **One-sample t-test**: compares a sample mean to a known/hypothesized value.
- **Two-sample t-test**: compares the means of two independent groups.
- **One-way ANOVA**: extends the t-test to three or more groups,
  testing whether *at least one* group mean differs.

## How to Run
```bash
pip install numpy scipy
python hypothesis_testing_anova.py
```

## Viva Questions & Answers
1. **Q: What is a Type I error vs a Type II error?**
   A: Type I (false positive) = rejecting a true H0; Type II (false
   negative) = failing to reject a false H0.
2. **Q: Why use ANOVA instead of running multiple t-tests for 3+ groups?**
   A: Running multiple t-tests inflates the overall Type I error rate
   (multiple comparisons problem); ANOVA tests all groups in one go
   while controlling the error rate.
3. **Q: What does a significant ANOVA result (p < 0.05) actually tell you?**
   A: That at least one group's mean differs from the others — it does
   NOT say which pair(s) differ (a post-hoc test like Tukey's HSD is
   needed for that).
4. **Q: Why does the script use Welch's t-test instead of the standard t-test?**
   A: Welch's t-test does not assume the two groups have equal
   variances, making it more robust for real-world unequal-variance data.
5. **Q: What is the significance level (α) and why is 0.05 common?**
   A: α is the threshold probability for rejecting H0; 0.05 (5%) is a
   widely-used convention balancing sensitivity and false-positive risk.

## Real-World Relevance
Hypothesis testing and ANOVA are used in A/B testing (e.g. comparing
two website designs), clinical trials, and quality-control comparisons
across multiple production batches.
