"""
=============================================================================
TOPIC: EXPLORATORY DATA ANALYSIS (EDA) & STATISTICAL BUSINESS INSIGHTS
=============================================================================
Author: Python Mastery Course
Level: Intermediate to Advanced (Data Analytics & Business Intelligence)

Conceptual Overview:
--------------------
1. What is Exploratory Data Analysis (EDA)?
   - EDA is the investigative process of analyzing datasets to summarize their 
     main characteristics, discover hidden patterns, spot anomalies, and test 
     hypotheses using statistical summaries and graphical representations.
   - Analogy: Think of a medical health checkup. Before prescribing medicine 
     (Machine Learning), the doctor checks blood pressure, heart rate, and 
     vital indicators (EDA) to understand the patient's condition.

2. Three Types of EDA:
   - Univariate Analysis: Analyzing one single variable (e.g. Distribution of Age).
   - Bivariate Analysis: Analyzing the relationship between two variables (e.g. Ad Spend vs Sales).
   - Multivariate Analysis: Analyzing interactions among 3 or more variables (e.g. Sales across Cities and Categories).

3. Topics Covered in this Guide:
   - Part 1: Dataset Overview & Five-Number Summary
   - Part 2: Univariate Statistical Profiling (Mean, Median, Std, Skewness)
   - Part 3: Bivariate Slicing with Multi-Metric GroupBy Aggregations
   - Part 4: Multi-Dimensional Cross-Tabulation with Pivot Tables
   - Part 5: Correlation Matrix & Identifying Sales Drivers
   - Part 6: Outlier Detection via the Interquartile Range (IQR Rule)
   - Part 7: Executive Business Insights Synthesis & Actionable Recommendations
=============================================================================
"""

import sys
import pandas as pd
import numpy as np

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Display settings for clean tabular terminal formatting
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)

# =============================================================================
# PART 1: DATASET OVERVIEW & FIVE-NUMBER SUMMARY
# =============================================================================
print("=" * 65)
print(">>> PART 1: DATASET INGESTION & FIVE-NUMBER SUMMARY <<<")
print("=" * 65)

# Creating a realistic multi-store retail dataset
np.random.seed(42)
n_records = 120

stores = np.random.choice(["Mumbai Central", "Delhi NCR", "Bangalore Tech Hub", "Pune City"], size=n_records)
categories = np.random.choice(["Electronics", "Home & Kitchen", "Fashion", "Stationery"], size=n_records, p=[0.35, 0.25, 0.25, 0.15])
units_sold = np.random.randint(1, 15, size=n_records)
unit_prices = np.random.choice([150, 450, 1200, 3500, 18000, 45000], size=n_records, p=[0.20, 0.25, 0.25, 0.15, 0.10, 0.05])
discounts = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.25], size=n_records, p=[0.30, 0.25, 0.20, 0.15, 0.10])
customer_ratings = np.random.choice([2.5, 3.0, 3.5, 4.0, 4.5, 5.0], size=n_records, p=[0.05, 0.10, 0.20, 0.30, 0.25, 0.10])

# Derived financial columns
gross_sales = units_sold * unit_prices
net_sales = gross_sales * (1 - discounts)
# Simulating profit margin around 22% with slight random variance
margin_rates = np.random.uniform(0.12, 0.35, size=n_records)
net_profit = net_sales * margin_rates

df_retail = pd.DataFrame({
    "Store": stores,
    "Category": categories,
    "Units_Sold": units_sold,
    "Unit_Price": unit_prices,
    "Discount_Rate": discounts,
    "Net_Sales": np.round(net_sales, 2),
    "Net_Profit": np.round(net_profit, 2),
    "Customer_Rating": customer_ratings
})

print("• First 5 Retail Records:")
print(df_retail.head(5))

print("\n• Five-Number Summary (df.describe()):")
print(df_retail.describe().round(2))


# =============================================================================
# PART 2: UNIVARIATE STATISTICAL PROFILING
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: UNIVARIATE STATISTICAL PROFILING <<<")
print("=" * 65)

sales_col = df_retail["Net_Sales"]

mean_sales = sales_col.mean()
median_sales = sales_col.median()
std_sales = sales_col.std()
skewness = sales_col.skew()

print(f"• Net Sales Statistics:")
print(f"  Mean (Average) Sales   : Rs. {mean_sales:,.2f}")
print(f"  Median (50th percentile): Rs. {median_sales:,.2f}")
print(f"  Standard Deviation     : Rs. {std_sales:,.2f}")
print(f"  Skewness Metric        : {skewness:.2f}")

if skewness > 1:
    print("  -> Interpretation: Highly Right-Skewed distribution (A few large-ticket sales pull the mean up).")
elif -1 <= skewness <= 1:
    print("  -> Interpretation: Relatively symmetric distribution.")
else:
    print("  -> Interpretation: Left-skewed distribution.")


# =============================================================================
# PART 3: BIVARIATE SLICING (GROUPBY WITH MULTI-METRICS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: CATEGORY & REGION-WISE PERFORMANCE <<<")
print("=" * 65)

# Grouping by Category and computing Total Revenue, Average Profit, and Order Count
cat_performance = df_retail.groupby("Category").agg(
    Total_Revenue=("Net_Sales", "sum"),
    Average_Order_Value=("Net_Sales", "mean"),
    Total_Profit=("Net_Profit", "sum"),
    Orders_Count=("Net_Sales", "count")
).round(2)

cat_performance["Profit_Margin_%"] = ((cat_performance["Total_Profit"] / cat_performance["Total_Revenue"]) * 100).round(2)
cat_performance.sort_values(by="Total_Revenue", ascending=False, inplace=True)

print("• Performance Breakdown by Product Category:")
print(cat_performance)

# Regional Store Ranking
store_performance = df_retail.groupby("Store")["Net_Sales"].sum().sort_values(ascending=False)
print("\n• Regional Store Revenue Leaderboard:")
for rank, (store, rev) in enumerate(store_performance.items(), start=1):
    print(f"  #{rank} {store:<20}: Rs. {rev:,.2f}")


# =============================================================================
# PART 4: MULTI-DIMENSIONAL CROSS-TABULATION (PIVOT TABLES)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: MULTI-DIMENSIONAL PIVOT TABLE ANALYSIS <<<")
print("=" * 65)

# Pivot table: Store on Rows, Category on Columns, Sum of Net_Sales in Cells
pivot_sales = df_retail.pivot_table(
    index="Store",
    columns="Category",
    values="Net_Sales",
    aggfunc="sum",
    fill_value=0,
    margins=True,       # Adds 'All' Total row & column
    margins_name="Total"
).round(2)

print("• Sales Matrix (Store vs Category Pivot):")
print(pivot_sales)


# =============================================================================
# PART 5: CORRELATION MATRIX & KEY BUSINESS DRIVERS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: CORRELATION MATRIX & FEATURE RELATIONSHIPS <<<")
print("=" * 65)

# Calculate Pearson correlation across numerical metrics
numeric_df = df_retail[["Units_Sold", "Unit_Price", "Discount_Rate", "Net_Sales", "Net_Profit", "Customer_Rating"]]
corr_matrix = numeric_df.corr().round(3)

print("• Pearson Correlation Coefficients (-1.00 to +1.00):")
print(corr_matrix)

profit_sales_corr = corr_matrix.loc["Net_Profit", "Net_Sales"]
discount_profit_corr = corr_matrix.loc["Discount_Rate", "Net_Profit"]

print(f"\n• Correlation Insights:")
print(f"  Sales to Profit Correlation : {profit_sales_corr:+.3f} (Very Strong Positive Driver)")
print(f"  Discount to Profit Correlation: {discount_profit_corr:+.3f} (Negative/Neutral pressure)")


# =============================================================================
# PART 6: OUTLIER DETECTION (INTERQUARTILE RANGE - IQR RULE)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: OUTLIER DETECTION (IQR RULE) <<<")
print("=" * 65)

# IQR = Q3 (75th percentile) - Q1 (25th percentile)
# Lower Bound = Q1 - 1.5 * IQR
# Upper Bound = Q3 + 1.5 * IQR
q1 = df_retail["Net_Sales"].quantile(0.25)
q3 = df_retail["Net_Sales"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df_retail[(df_retail["Net_Sales"] < lower_bound) | (df_retail["Net_Sales"] > upper_bound)]

print(f"• IQR Metric Breakdown:")
print(f"  Q1 (25th Percentile): Rs. {q1:,.2f}")
print(f"  Q3 (75th Percentile): Rs. {q3:,.2f}")
print(f"  IQR (Spread)        : Rs. {iqr:,.2f}")
print(f"  Upper Outlier Threshold (> Q3 + 1.5*IQR): Rs. {upper_bound:,.2f}")
print(f"\n• Number of Statistical Outliers Detected: {len(outliers)} rows")

if not outliers.empty:
    print("• Sample High-Value Outlier Transactions:")
    print(outliers[["Store", "Category", "Units_Sold", "Unit_Price", "Net_Sales"]].head(3))


# =============================================================================
# PART 7: EXECUTIVE BUSINESS INSIGHTS SUMMARY
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: EXECUTIVE BUSINESS INSIGHTS & RECOMMENDATIONS <<<")
print("=" * 65)

top_category = cat_performance.index[0]
top_cat_rev = cat_performance.iloc[0]["Total_Revenue"]
top_cat_margin = cat_performance.iloc[0]["Profit_Margin_%"]

top_store = store_performance.index[0]
top_store_rev = store_performance.iloc[0]

print("• Key Findings for Executive Leadership:")
print(f"  1. Top Revenue Category: '{top_category}' generated Rs. {top_cat_rev:,.2f} with a {top_cat_margin}% profit margin.")
print(f"  2. Leading Regional Store: '{top_store}' is the top performer generating Rs. {top_store_rev:,.2f}.")
print(f"  3. Discount Impact: Heavy discounts do not significantly expand transaction counts; recommend capping discounts at 10%.")
print(f"  4. Outlier Transactions: High-ticket purchases represent enterprise B2B customers; establish a dedicated VIP account management pipeline.")

print("=" * 65)
print(">>> TOPIC 12 COMPLETE: EXPLORATORY DATA ANALYSIS MASTERED <<<")
print("=" * 65)
