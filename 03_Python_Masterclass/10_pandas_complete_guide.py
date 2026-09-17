"""
=============================================================================
TOPIC 06: PANDAS (DATA MANIPULATION & ANALYSIS) MASTER GUIDE
=============================================================================
Author: Python Mastery Course
Level: Beginner to Advanced (Data Analytics & Data Science)

Conceptual Overview:
--------------------
1. What is Pandas?
   - Pandas is Python's leading library for loading, transforming, cleaning, 
     and analyzing tabular data (such as Excel spreadsheets, CSVs, and SQL tables).

2. Core Data Structures:
   - Series: A 1D labeled array capable of holding any data type (similar to a single column).
   - DataFrame: A 2D labeled tabular structure with rows and columns (similar to an Excel spreadsheet or SQL table).

3. Main Topics Covered in this Guide:
   [Data Analytics Core]
   - Creating Series & DataFrames from Python Dictionaries and Lists
   - Data Inspection (`head()`, `tail()`, `info()`, `describe()`, `shape`, `dtypes`)
   - Data Selection: `.loc[]` (label-based) vs `.iloc[]` (integer-position-based)
   - Conditional Filtering & Compound Queries
   - Adding, Renaming, and Transforming Columns
   - Handling Missing Data (`isna()`, `dropna()`, `fillna()`)
   - GroupBy & Multi-metric Aggregations
   - Relational Merging & Joining (`pd.merge`, `pd.concat`)
   
   [Data Science & Machine Learning Level]
   - Categorical Encoding (One-Hot `pd.get_dummies` & Ordinal Mapping)
   - Feature Scaling (Min-Max Normalization & Z-Score Standardization)
   - Outlier Detection & Handling (IQR Rule & `.clip()`)
   - Correlation Matrix & Feature Relationships (`df.corr()`)
   - Continuous Feature Discretization & Binning (`pd.cut` & `pd.qcut`)
   - Advanced `.apply()`, Lambda & DateTime Feature Engineering
   - Reshaping & Multidimensional Aggregation (`pivot_table`)
=============================================================================
"""

import pandas as pd
import numpy as np

# Display formatting settings for clean terminal output
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

print("=" * 65)
print(">>> PART 1: PANDAS SERIES & DATAFRAME CREATION <<<")
print("=" * 65)

# 1. Pandas Series (1D Labeled Array)
temperatures = pd.Series([32.5, 34.0, 29.8, 31.2], index=["Delhi", "Mumbai", "Bangalore", "Pune"], name="Temperature_C")
print("• Pandas Series (City Temperatures):")
print(temperatures)
print(f"  Max Temp: {temperatures.max()}°C in {temperatures.idxmax()}")

# 2. Pandas DataFrame (2D Tabular Data)
employees_raw = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Rahul Roy", "Pooja Hegde", "Amit Patel", "Sneha Rao", "Karan Johar", "Vikram Rathore", "Divya Sen"],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing", "IT", "Finance"],
    "Age": [26, 29, 35, 31, 42, 28, np.nan],  # Missing value
    "Salary": [65000, 52000, 95000, 80000, 72000, 68000, 84000],
    "Experience_Yrs": [3, 5, 11, 7, 15, 4, 9],
    "Performance_Score": [88, np.nan, 95, 82, 70, 91, 85]  # Missing value
}

df = pd.DataFrame(employees_raw)
print("\n• Created Employee DataFrame:")
print(df)


print("\n" + "=" * 65)
print(">>> PART 2: DATA INSPECTION & SUMMARY <<<")
print("=" * 65)

# head(n): Returns the first n rows (default 5)
print("• df.head(3) [Top 3 rows]:")
print(df.head(3))

# shape: Returns dimensions as (rows, columns)
print(f"\n• Dataset Shape (Rows, Columns): {df.shape}")

# dtypes: Returns the data type of each column
print("\n• Column Data Types:")
print(df.dtypes)

# describe(): Generates descriptive statistics for numerical columns
print("\n• Statistical Summary [df.describe()]:")
print(df.describe())


print("\n" + "=" * 65)
print(">>> PART 3: DATA SELECTION (.loc VS .iloc) <<<")
print("=" * 65)

# .iloc: Integer-location based selection (Row indices 0 to 2, Column indices 1, 2, 4)
print("• Using .iloc[0:3, [1, 2, 4]] (By integer index position):")
print(df.iloc[0:3, [1, 2, 4]])

# .loc: Label-based selection (Selecting specific column names)
print("\n• Using .loc[0:2, ['Name', 'Department', 'Salary']] (By column names):")
print(df.loc[0:2, ['Name', 'Department', 'Salary']])


print("\n" + "=" * 65)
print(">>> PART 4: FILTERING & CONDITIONAL QUERYING <<<")
print("=" * 65)

# Condition 1: Filter IT Department employees
it_employees = df[df["Department"] == "IT"]
print("• IT Department Employees:")
print(it_employees[["Emp_ID", "Name", "Salary"]])

# Condition 2: Compound condition (Salary > 70000 AND Experience >= 5)
senior_high_earners = df[(df["Salary"] > 70000) & (df["Experience_Yrs"] >= 5)]
print("\n• High Earners (Salary > 70k AND Exp >= 5 Yrs):")
print(senior_high_earners[["Name", "Department", "Salary", "Experience_Yrs"]])


print("\n" + "=" * 65)
print(">>> PART 5: COLUMN OPERATIONS & FEATURE CREATION <<<")
print("=" * 65)

# Creating a new feature column (Annual Bonus = 10% of Salary)
df["Bonus"] = df["Salary"] * 0.10

# Total Compensation = Base Salary + Bonus
df["Total_Compensation"] = df["Salary"] + df["Bonus"]

# Renaming existing column
df.rename(columns={"Name": "Employee_Name"}, inplace=True)
print("• DataFrame after adding Bonus and Total Compensation:")
print(df[["Employee_Name", "Department", "Salary", "Bonus", "Total_Compensation"]])


print("\n" + "=" * 65)
print(">>> PART 6: HANDLING MISSING VALUES (CLEANING) <<<")
print("=" * 65)

# Check missing value counts per column
print("• Missing Values Count per column:")
print(df.isna().sum())

# Impute missing Age with the median age
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Impute missing Performance Score with the mean score
mean_score = round(df["Performance_Score"].mean(), 1)
df["Performance_Score"] = df["Performance_Score"].fillna(mean_score)

print(f"\n• After Imputing Missing Values (Age filled with {median_age}, Score filled with {mean_score}):")
print(df[["Employee_Name", "Age", "Performance_Score"]])


print("\n" + "=" * 65)
print(">>> PART 7: GROUPBY & AGGREGATIONS <<<")
print("=" * 65)

# Department-wise Average Salary, Total Count, and Max Salary
dept_summary = df.groupby("Department").agg(
    Total_Employees=("Emp_ID", "count"),
    Avg_Salary=("Salary", "mean"),
    Max_Salary=("Salary", "max"),
    Avg_Exp=("Experience_Yrs", "mean")
).round(2)

print("• Department-wise Summary Report:")
print(dept_summary)


print("\n" + "=" * 65)
print(">>> PART 8: MERGING & CONCATENATION <<<")
print("=" * 65)

# Project Allocation Table
projects_data = {
    "Emp_ID": [101, 102, 103, 104, 108],
    "Project_Name": ["Project Alpha (AI)", "HR Portal", "Cloud Migration", "FinTech App", "Cyber Defense"]
}
df_projects = pd.DataFrame(projects_data)

# Inner Merge: Matches records present in both tables
merged_inner = pd.merge(df, df_projects, on="Emp_ID", how="inner")
print("• Merged Table (Employee + Assigned Project):")
print(merged_inner[["Emp_ID", "Employee_Name", "Department", "Project_Name"]])

# Left Merge: Retains all employees, matching projects where available
merged_left = pd.merge(df, df_projects, on="Emp_ID", how="left")
print("\n• Left Merge (All Employees with/without Assigned Project):")
print(merged_left[["Emp_ID", "Employee_Name", "Project_Name"]])

# =============================================================================
# DATA SCIENCE & MACHINE LEARNING LEVEL PANDAS CONCEPTS
# =============================================================================

print("\n" + "=" * 65)
print(">>> PART 9: CATEGORICAL ENCODING (ONE-HOT & ORDINAL MAPPING) <<<")
print("=" * 65)

# 1. One-Hot Encoding (pd.get_dummies) for Machine Learning Algorithms
# ML algorithms text/strings nahi samajhte; nominal data ko 0 aur 1 binary columns me convert karte hain.
encoded_df = pd.get_dummies(df, columns=["Department"], prefix="Dept", drop_first=True, dtype=int)
print("• One-Hot Encoded DataFrame (drop_first=True to avoid Dummy Variable Trap):")
print(encoded_df[["Employee_Name", "Dept_HR", "Dept_IT", "Dept_Marketing"]].head(4))

# 2. Ordinal Encoding / Mapping (Categorical order ko numeric hierarchy me convert karna)
performance_map = {"Needs Improvement": 1, "Average": 2, "Good": 3, "Star Performer": 4}
df["Performance_Band"] = pd.cut(
    df["Performance_Score"], 
    bins=[0, 75, 85, 92, 100], 
    labels=["Needs Improvement", "Average", "Good", "Star Performer"]
)
df["Performance_Encoded"] = df["Performance_Band"].map(performance_map)
print("\n• Ordinal Feature Mapping:")
print(df[["Employee_Name", "Performance_Score", "Performance_Band", "Performance_Encoded"]].head(4))


print("\n" + "=" * 65)
print(">>> PART 10: FEATURE SCALING & NORMALIZATION (FROM SCRATCH) <<<")
print("=" * 65)

# 1. Min-Max Normalization: Values ko 0 se 1 ke fixed range me scale karta hai
# Formula: (X - X_min) / (X_max - X_min)
salary_min = df["Salary"].min()
salary_max = df["Salary"].max()
df["Salary_MinMax_Scaled"] = ((df["Salary"] - salary_min) / (salary_max - salary_min)).round(4)

# 2. Z-score Standardization: Mean ko 0 aur Standard Deviation ko 1 banata hai
# Formula: (X - Mean) / Std
salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
df["Salary_Z_Score"] = ((df["Salary"] - salary_mean) / salary_std).round(4)

print("• Feature Scaling Comparison (Raw vs MinMax Scaled vs Z-Score):")
print(df[["Employee_Name", "Salary", "Salary_MinMax_Scaled", "Salary_Z_Score"]].head(4))


print("\n" + "=" * 65)
print(">>> PART 11: OUTLIER DETECTION & CLIPPING (IQR METHOD) <<<")
print("=" * 65)

# IQR (Interquartile Range) Method: Outliers detect karne ka standard statistical tarika
# IQR = Q3 (75th Percentile) - Q1 (25th Percentile)
q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr
print(f"• Salary Thresholds: Q1={q1}, Q3={q3}, IQR={iqr}")
print(f"  Lower Bound: {lower_limit}, Upper Bound: {upper_limit}")

outliers = df[(df["Salary"] < lower_limit) | (df["Salary"] > upper_limit)]
print(f"  Outliers Count: {len(outliers)}")

# Outlier Treatment: Capping / Clipping using .clip()
df["Salary_Clipped"] = df["Salary"].clip(lower=lower_limit, upper=upper_limit)
print("• Salary after Clipping extreme values:")
print(df[["Employee_Name", "Salary", "Salary_Clipped"]].head(4))


print("\n" + "=" * 65)
print(">>> PART 12: CORRELATION MATRIX & FEATURE RELATIONSHIPS <<<")
print("=" * 65)

# Numerical columns ke pairwise Pearson correlation coefficients (-1 se +1)
# ML me multicollinearity check karne aur target variable ke strong predictors find karne ke liye
numeric_cols = ["Age", "Salary", "Experience_Yrs", "Performance_Score"]
corr_matrix = df[numeric_cols].corr().round(3)
print("• Pearson Correlation Matrix:")
print(corr_matrix)


print("\n" + "=" * 65)
print(">>> PART 13: DISCRETIZATION & BINNING (pd.cut & pd.qcut) <<<")
print("=" * 65)

# Continuous variables ko categorical groups me bucket karna
# pd.cut: Equal-width custom intervals
df["Exp_Category"] = pd.cut(
    df["Experience_Yrs"],
    bins=[0, 4, 8, 20],
    labels=["Junior (0-4)", "Mid-Level (5-8)", "Senior (9+)"]
)

# pd.qcut: Quantile-based (equal frequency bucket distribution)
df["Salary_Tier"] = pd.qcut(df["Salary"], q=3, labels=["Tier 1 (Entry)", "Tier 2 (Mid)", "Tier 3 (High)"])

print("• Continuous Feature Binning:")
print(df[["Employee_Name", "Experience_Yrs", "Exp_Category", "Salary", "Salary_Tier"]].head(5))


print("\n" + "=" * 65)
print(">>> PART 14: ADVANCED APPLY, LAMBDA & DATETIME FEATURE EXTRACTION <<<")
print("=" * 65)

# 1. Custom Row-wise logic with .apply() and lambda
df["Bonus_Eligibility"] = df.apply(
    lambda row: "High Bonus" if row["Performance_Score"] >= 88 and row["Experience_Yrs"] >= 5 else "Standard Bonus",
    axis=1
)

# 2. DateTime Engineering: Timestamps se ML features extract karna
sample_dates = pd.date_range(start="2021-01-15", periods=len(df), freq="120D")
df["Joining_Date"] = sample_dates
df["Join_Year"] = df["Joining_Date"].dt.year
df["Join_Month"] = df["Joining_Date"].dt.month_name()
df["Join_Quarter"] = df["Joining_Date"].dt.quarter
df["Join_DayOfWeek"] = df["Joining_Date"].dt.day_name()
df["Is_Weekend_Join"] = df["Joining_Date"].dt.dayofweek.isin([5, 6])

print("• Extracted DateTime Features for ML:")
print(df[["Employee_Name", "Joining_Date", "Join_Year", "Join_Month", "Join_DayOfWeek", "Bonus_Eligibility"]].head(4))


print("\n" + "=" * 65)
print(">>> PART 15: RESHAPING DATA (PIVOT TABLES FOR FEATURE AGGREGATION) <<<")
print("=" * 65)

# Pivot Table: Multi-dimensional feature aggregation
pivot_salary_exp = df.pivot_table(
    values="Salary",
    index="Exp_Category",
    columns="Department",
    aggfunc="mean",
    fill_value=0,
    observed=False
).round(2)

print("• Pivot Table: Mean Salary by Experience Category & Department:")
print(pivot_salary_exp)

print("\n" + "=" * 65)
print(">>> TOPIC 06 (PANDAS MASTER GUIDE) COMPLETED! <<<")
print("=" * 65)

