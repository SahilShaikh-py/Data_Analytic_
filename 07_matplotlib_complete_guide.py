"""
=============================================================================
TOPIC 07: MATPLOTLIB (DATA VISUALIZATION) COMPLETE MASTER GUIDE
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is Matplotlib?
   - Matplotlib is the foundational 2D plotting and data visualization library in Python.
   - Its `pyplot` submodule (aliased as `plt`) provides an intuitive, MATLAB-like plotting interface.

2. Core Chart Types Covered:
   - Line Plot: For visualizing trends and time-series series (e.g., stock performance, monthly sales).
   - Bar Chart: For comparing discrete categorical metrics (Vertical & Horizontal).
   - Scatter Plot: For identifying relationships, clusters, and correlations between two continuous variables.
   - Histogram: For inspecting probability distributions and data spread.
   - Pie Chart: For representing proportions and percentage distributions of a whole.
   - Subplots: For laying out multi-chart dashboards on a unified canvas (`plt.subplot`).

3. Visual Styling & Customizations:
   - Axis Labels (`xlabel`, `ylabel`), Chart Title (`title`), Legend (`legend`), Grid lines (`grid`).
   - Colors, Data Markers, Line Styles, Figure Dimensions (`plt.figure(figsize=(w, h))`).
   - Image Export: `plt.savefig("chart.png")` to export publication-quality graphics.
=============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

print("=" * 65)
print(">>> PART 1: LINE PLOT (MONTHLY SALES TREND) <<<")
print("=" * 65)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_2023 = [45, 52, 58, 65, 70, 75, 82, 88, 85, 92, 98, 110]
sales_2024 = [50, 58, 63, 72, 80, 89, 95, 102, 99, 108, 115, 130]

# 1. Initialize figure dimensions
plt.figure(figsize=(10, 5))

# 2. Line plotting with customized styling, markers, and line weights
plt.plot(months, sales_2023, label="Sales 2023", color="#1f77b4", marker="o", linestyle="--", linewidth=2)
plt.plot(months, sales_2024, label="Sales 2024", color="#ff7f0e", marker="s", linestyle="-", linewidth=2.5)

# 3. Titles, Axis Labels, Legend, and Gridlines
plt.title("Monthly Company Sales Comparison (2023 vs 2024)", fontsize=14, fontweight="bold", pad=12)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (in Lakhs ₹)", fontsize=12)
plt.legend(loc="upper left", frameon=True)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

# Save chart to high-resolution PNG
plt.savefig("01_line_plot_sales.png", dpi=150)
plt.close()
print("• [Saved] 01_line_plot_sales.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 2: BAR CHART (DEPARTMENT SALARY COMPARISON) <<<")
print("=" * 65)

departments = ["IT", "Data Science", "Cyber Security", "Finance", "HR", "Marketing"]
avg_salaries = [85, 95, 90, 72, 55, 60]  # In Thousands
bar_colors = ["#2b5c8f", "#17a2b8", "#28a745", "#ffc107", "#dc3545", "#6f42c1"]

plt.figure(figsize=(9, 5))
bars = plt.bar(departments, avg_salaries, color=bar_colors, edgecolor="black", width=0.6)

# Direct data labeling above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"₹{yval}k", ha="center", va="bottom", fontweight="bold")

plt.title("Average Salary by Department (2024)", fontsize=14, fontweight="bold")
plt.xlabel("Department", fontsize=12)
plt.ylabel("Avg Salary (₹ in Thousands)", fontsize=12)
plt.ylim(0, 110)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("02_bar_chart_departments.png", dpi=150)
plt.close()
print("• [Saved] 02_bar_chart_departments.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 3: SCATTER PLOT & HISTOGRAM <<<")
print("=" * 65)

# 1. Scatter Plot (Experience vs Salary)
np.random.seed(42)
experience = np.random.uniform(1, 15, 60)
salary = 30 + (experience * 6.5) + np.random.normal(0, 5, 60)  # Linear correlation with gaussian noise

plt.figure(figsize=(8, 5))
plt.scatter(experience, salary, color="#e63946", alpha=0.8, edgecolors="black", s=60, label="Employees")

# Trend line (Linear Regression Best Fit)
m, c = np.polyfit(experience, salary, 1)
plt.plot(experience, m*experience + c, color="darkblue", linewidth=2, label="Trend Line")

plt.title("Experience vs Salary Correlation", fontsize=14, fontweight="bold")
plt.xlabel("Years of Experience", fontsize=12)
plt.ylabel("Salary (in Lakhs ₹)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("03_scatter_plot_correlation.png", dpi=150)
plt.close()
print("• [Saved] 03_scatter_plot_correlation.png generated successfully!")

# 2. Histogram (Exam Scores Distribution)
exam_scores = np.random.normal(loc=72, scale=12, size=200) # Normal distribution

plt.figure(figsize=(8, 5))
plt.hist(exam_scores, bins=15, color="#457b9d", edgecolor="black", alpha=0.8)
plt.axvline(np.mean(exam_scores), color="red", linestyle="dashed", linewidth=2, label=f"Mean: {np.mean(exam_scores):.1f}")

plt.title("Distribution of Student Exam Scores", fontsize=14, fontweight="bold")
plt.xlabel("Marks Scored (out of 100)", fontsize=12)
plt.ylabel("Number of Students (Frequency)", fontsize=12)
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()

plt.savefig("04_histogram_scores.png", dpi=150)
plt.close()
print("• [Saved] 04_histogram_scores.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 4: PIE CHART (MARKET SHARE) <<<")
print("=" * 65)

languages = ["Python", "JavaScript", "Java", "C++", "Go/Rust", "Others"]
usage_shares = [38, 25, 15, 10, 8, 4]
explode = (0.1, 0, 0, 0, 0, 0)  # Explode the Python slice for visual emphasis
colors_pie = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]

plt.figure(figsize=(7, 7))
plt.pie(
    usage_shares,
    explode=explode,
    labels=languages,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors_pie,
    shadow=True,
    wedgeprops={"edgecolor": "black", "linewidth": 1}
)
plt.title("Programming Languages Popularity in Data Science", fontsize=14, fontweight="bold")
plt.tight_layout()

plt.savefig("05_pie_chart_languages.png", dpi=150)
plt.close()
print("• [Saved] 05_pie_chart_languages.png generated successfully!")


print("\n" + "=" * 65)
print(">>> PART 5: SUBPLOTS (2x2 DASHBOARD GRID) <<<")
print("=" * 65)

# Creating a 2x2 multi-panel visualization layout
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 9))
fig.suptitle("Data Analytics Master Dashboard (Matplotlib Subplots)", fontsize=16, fontweight="bold")

# Subplot 1: Line Plot (Top-Left)
axes[0, 0].plot(months[:6], sales_2024[:6], marker="o", color="navy")
axes[0, 0].set_title("H1 Sales Growth", fontweight="bold")
axes[0, 0].grid(True, linestyle=":")

# Subplot 2: Bar Plot (Top-Right)
axes[0, 1].bar(departments[:4], avg_salaries[:4], color=["teal", "coral", "forestgreen", "gold"])
axes[0, 1].set_title("Top 4 Dept Salaries", fontweight="bold")
axes[0, 1].grid(axis="y", linestyle=":")

# Subplot 3: Scatter Plot (Bottom-Left)
axes[1, 0].scatter(experience[:30], salary[:30], color="purple", alpha=0.7)
axes[1, 0].set_title("Experience vs Pay (Sample)", fontweight="bold")
axes[1, 0].grid(True, linestyle=":")

# Subplot 4: Histogram (Bottom-Right)
axes[1, 1].hist(exam_scores, bins=10, color="orange", edgecolor="black")
axes[1, 1].set_title("Score Distribution", fontweight="bold")
axes[1, 1].grid(axis="y", linestyle=":")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("06_subplots_dashboard.png", dpi=150)
plt.close()
print("• [Saved] 06_subplots_dashboard.png generated successfully!")

print("\n" + "=" * 65)
print(">>> TOPIC 07 (MATPLOTLIB MASTER GUIDE) COMPLETED! <<<")
print("=" * 65)
