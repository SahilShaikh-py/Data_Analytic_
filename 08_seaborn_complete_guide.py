"""
=============================================================================
TOPIC 08: SEABORN (STATISTICAL DATA VISUALIZATION) MASTER GUIDE
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is Seaborn and Why is it Used?
   - Seaborn is a high-level statistical data visualization library built on top of Matplotlib.
   - It provides elegant default aesthetics, sophisticated color palettes, and built-in
     support for computing and plotting statistical aggregations.

2. Matplotlib vs Seaborn:
   - Matplotlib: Low-level granularity where every figure component is manually defined.
   - Seaborn: High-level abstraction that natively accepts Pandas DataFrames, enabling
     categorical subsetting with simple arguments like `hue`, `col`, and `style`.

3. Plot Categories Covered:
   - Distribution Plots: `histplot()`, `kdeplot()` (Kernel Density Estimation)
   - Categorical Plots: `countplot()`, `barplot()`, `boxplot()`, `violinplot()`
   - Relational Plots: `scatterplot()`, `lineplot()` with multi-attribute styling
   - Matrix Plots: `heatmap()` (Correlation matrix visualization)
   - Multi-plot Grids: `pairplot()` (Pairwise exploratory data analysis - EDA)
=============================================================================
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Apply modern Seaborn theme globally
sns.set_theme(style="whitegrid", palette="muted")

print("=" * 65)
print(">>> PREPARING SAMPLE DATASET FOR VISUALIZATION <<<")
print("=" * 65)

# Synthetic Tech & Analytics Industry Dataset
np.random.seed(42)
n_records = 150

roles = np.random.choice(["Data Analyst", "Data Scientist", "Cyber Analyst", "ML Engineer"], size=n_records)
gender = np.random.choice(["Male", "Female"], size=n_records, p=[0.55, 0.45])
experience_yrs = np.random.uniform(1, 12, size=n_records).round(1)

# Base salary scale conditioned on domain role and seniority
base_role_salary = {"Data Analyst": 45, "Cyber Analyst": 55, "Data Scientist": 70, "ML Engineer": 80}
salaries = [base_role_salary[r] + (exp * 6.0) + np.random.normal(0, 4) for r, exp in zip(roles, experience_yrs)]
performance_rating = np.random.choice([3, 4, 5], size=n_records, p=[0.25, 0.50, 0.25])
project_count = np.random.randint(2, 12, size=n_records)

df_tech = pd.DataFrame({
    "Role": roles,
    "Gender": gender,
    "Experience_Yrs": experience_yrs,
    "Salary_LPA": np.round(salaries, 2),
    "Performance_Rating": performance_rating,
    "Projects_Completed": project_count
})

print("• First 5 rows of created dataset:")
print(df_tech.head())


print("\n" + "=" * 65)
print(">>> PART 1: DISTRIBUTION PLOTS (HISTPLOT & KDEPLOT) <<<")
print("=" * 65)

# Histogram overlaid with Kernel Density Estimation (KDE)
plt.figure(figsize=(9, 5))
sns.histplot(
    data=df_tech,
    x="Salary_LPA",
    kde=True,
    hue="Gender",
    element="step",
    palette="magma"
)
plt.title("Salary Distribution with KDE by Gender", fontsize=14, fontweight="bold")
plt.xlabel("Salary (Lakhs Per Annum)", fontsize=12)
plt.ylabel("Count of Employees", fontsize=12)
plt.tight_layout()

plt.savefig("07_seaborn_dist_kde.png", dpi=150)
plt.close()
print("• [Saved] 07_seaborn_dist_kde.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 2: CATEGORICAL PLOTS (BAR, COUNT, BOX, VIOLIN) <<<")
print("=" * 65)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Categorical Explorations (Seaborn)", fontsize=16, fontweight="bold")

# 1. CountPlot: Frequency of employees per job role
sns.countplot(
    data=df_tech,
    x="Role",
    hue="Gender",
    ax=axes[0, 0],
    palette="Set2"
)
axes[0, 0].set_title("Employee Count per Role by Gender", fontweight="bold")
axes[0, 0].tick_params(axis="x", rotation=15)

# 2. BarPlot: Mean salary per role with confidence intervals
sns.barplot(
    data=df_tech,
    x="Role",
    y="Salary_LPA",
    hue="Gender",
    ax=axes[0, 1],
    palette="Blues_d"
)
axes[0, 1].set_title("Average Salary per Role", fontweight="bold")
axes[0, 1].tick_params(axis="x", rotation=15)

# 3. BoxPlot: Five-number summary and outlier detection (Min, Q1, Median, Q3, Max)
sns.boxplot(
    data=df_tech,
    x="Role",
    y="Salary_LPA",
    ax=axes[1, 0],
    palette="Pastel1"
)
axes[1, 0].set_title("Salary Spread & Outlier Detection (Boxplot)", fontweight="bold")
axes[1, 0].tick_params(axis="x", rotation=15)

# 4. ViolinPlot: Combines box plot with probability density spread
sns.violinplot(
    data=df_tech,
    x="Role",
    y="Experience_Yrs",
    hue="Gender",
    split=True,
    ax=axes[1, 1],
    palette="coolwarm"
)
axes[1, 1].set_title("Experience Distribution (Violin Plot)", fontweight="bold")
axes[1, 1].tick_params(axis="x", rotation=15)

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig("08_seaborn_categorical_plots.png", dpi=150)
plt.close()
print("• [Saved] 08_seaborn_categorical_plots.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 3: RELATIONAL PLOT (SCATTER WITH HUE, SIZE & STYLE) <<<")
print("=" * 65)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_tech,
    x="Experience_Yrs",
    y="Salary_LPA",
    hue="Role",
    style="Gender",
    size="Projects_Completed",
    sizes=(40, 200),
    palette="deep",
    alpha=0.85
)

plt.title("Experience vs Salary Multi-dimensional Analysis", fontsize=14, fontweight="bold")
plt.xlabel("Experience (Years)", fontsize=12)
plt.ylabel("Salary (LPA ₹)", fontsize=12)
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True)
plt.tight_layout()

plt.savefig("09_seaborn_relational_scatter.png", dpi=150)
plt.close()
print("• [Saved] 09_seaborn_relational_scatter.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 4: MATRIX PLOT - HEATMAP (CORRELATION MATRIX) <<<")
print("=" * 65)

# Calculate pairwise Pearson correlation between numeric features
numeric_cols = ["Experience_Yrs", "Salary_LPA", "Performance_Rating", "Projects_Completed"]
corr_matrix = df_tech[numeric_cols].corr()
print("• Correlation Matrix:")
print(corr_matrix.round(2))

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,          # Display numeric coefficients
    fmt=".2f",          # Two decimal precision
    cmap="coolwarm",    # Diverging color palette
    vmin=-1, vmax=1,    # Correlation range
    linewidths=1.5,
    cbar=True
)
plt.title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()

plt.savefig("10_seaborn_heatmap_correlation.png", dpi=150)
plt.close()
print("• [Saved] 10_seaborn_heatmap_correlation.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 5: PAIRPLOT (FULL EXPLORATORY DATA ANALYSIS) <<<")
print("=" * 65)

# Pairplot: Multi-panel grid showing distributions and bivariate pairwise relationships
pairplot_fig = sns.pairplot(
    data=df_tech[["Role", "Experience_Yrs", "Salary_LPA", "Projects_Completed"]],
    hue="Role",
    palette="Set1",
    diag_kind="kde",
    corner=False
)
pairplot_fig.fig.suptitle("Pairplot: Comprehensive Pairwise Feature Analysis", y=1.02, fontsize=14, fontweight="bold")
pairplot_fig.savefig("11_seaborn_pairplot_eda.png", dpi=150)
plt.close()
print("• [Saved] 11_seaborn_pairplot_eda.png generated successfully!")

print("\n" + "=" * 65)
print(">>> TOPIC 08 (SEABORN MASTER GUIDE) COMPLETED! <<<")
print("=" * 65)
